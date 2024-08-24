from typing import List, Dict, Optional, Callable, Union
import os
import yaml
import sys
import argparse
from canvasapi import Canvas
from datetime import datetime
from dateutil import parser as date_parser

# Canvas API URL and API key
DOMAIN = "https://yourinstitution.instructure.com"
API_KEY = os.environ.get("CANVAS_API_KEY", "NONE")

# Ensure the API key is provided
if API_KEY == "NONE":
    raise EnvironmentError("CANVAS_API_KEY environment variable is not set.")

# Define type aliases for clarity
RawAssignmentGroupData = Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]
InternalizedQuestionData = Dict[str, Union[str, int]]
InternalizedAssignmentGroupData = Dict[str, Union[str, List[InternalizedQuestionData]]]

# Function to load and validate the YAML file
def load_yaml(file_path: str) -> Dict[str, List[RawAssignmentGroupData]]:
    try:
        with open(file_path, 'r') as file:
            data: Dict[str, List[RawAssignmentGroupData]] = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

# Function to internalize and validate the structure
def internalize_structure(data: Dict[str, List[RawAssignmentGroupData]]) -> List[InternalizedAssignmentGroupData]:
    internalized_data: List[InternalizedAssignmentGroupData] = []

    for i, group in enumerate(data.get('assignment_groups', []), start=1):
        raw_group_name: str = group['name']
        group_name: str = f"HW{i}: {raw_group_name}"
        default_due_date_str: Optional[str] = group.get('due_date')

        internalized_group: InternalizedAssignmentGroupData = {'name': group_name, 'questions': []}

        for j, question in enumerate(group.get('questions', []), start=1):
            raw_question_name: str = question['name']
            question_name: str = f"{i}: {raw_question_name}"
            points: int = question.get('points', 0)
            question_due_date_str: Optional[str] = question.get('due_date', default_due_date_str)

            if not question_due_date_str:
                raise ValueError(f"No due date specified for '{question_name}' in '{group_name}'.")

            question_due_date: datetime = date_parser.parse(question_due_date_str)

            internalized_question: InternalizedQuestionData = {
                'name': question_name,
                'points': points,
                'due_date': question_due_date.isoformat()
            }

            internalized_group['questions'].append(internalized_question)

        internalized_data.append(internalized_group)

    return internalized_data

# Function to print the internalized structure for user validation
def print_structure(internalized_data: List[InternalizedAssignmentGroupData]) -> None:
    print("Validated structure:")
    for group in internalized_data:
        print(f"Assignment Group: {group['name']}")
        for question in group['questions']:
            print(f"  - {question['name']} (Points: {question['points']}, Due: {question['due_date']})")

# Function to confirm input with a callback for 'no' response
def confirm_input(prompt: str, on_no: Callable[[], None]) -> bool:
    response: str = input(prompt).strip().lower()
    if response == 'yes':
        return True
    else:
        on_no()
        return False

# Function to handle 'no' response
def handle_no_response() -> None:
    print("Operation canceled by user.")
    sys.exit(0)

# Function to check if assignment groups already exist
def check_existing_groups(canvas_course, internalized_data: List[InternalizedAssignmentGroupData]) -> bool:
    existing_groups = {group.name for group in canvas_course.get_assignment_groups()}
    for group in internalized_data:
        if group['name'] in existing_groups:
            raise ValueError(f"Error: Assignment group '{group['name']}' already exists.")
    return True

# Function to create assignments in Canvas
def create_assignments(canvas_course, internalized_data: List[InternalizedAssignmentGroupData]) -> None:
    for group in internalized_data:
        group_name: str = group['name']

        # Create the assignment group
        assignment_group = canvas_course.create_assignment_group(name=group_name)
        print(f"Created assignment group '{group_name}'.")

        # Loop through the questions and create the assignments
        for question in group['questions']:
            question_name: str = question['name']
            points: int = question['points']
            due_date_str: str = question['due_date']
            due_date: datetime = date_parser.parse(due_date_str)

            assignment = canvas_course.create_assignment({
                'name': question_name,
                'points_possible': points,
                'due_at': due_date.isoformat(),
                'assignment_group_id': assignment_group.id,
                'published': False
            })

            print(f"  Created assignment '{question_name}' with {points} points and due date {due_date}.")

# Main function
def main(course_id: int, file_path: str) -> None:
    # Load and validate the structure
    try:
        raw_data: Dict[str, List[RawAssignmentGroupData]] = load_yaml(file_path)
    except ValueError as e:
        print(f"Error loading YAML file: {e}")
        return

    try:
        internalized_data: List[InternalizedAssignmentGroupData] = internalize_structure(raw_data)
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    # Print the internalized structure for validation
    print_structure(internalized_data)

    # Confirm input and proceed if 'yes'
    if confirm_input("Proceed with creating the assignments? (yes/no): ", handle_no_response):
        canvas: Canvas = Canvas(DOMAIN, API_KEY)

        # Find the course with the given course_id
        try:
            course = canvas.get_course(course_id)
        except Exception as e:
            print(f"Error accessing course ID {course_id}: {e}")
            return

        # Check if any assignment groups already exist
        try:
            check_existing_groups(course, internalized_data)
        except ValueError as e:
            print(f"Aborting operation: {e}")
            return

        # Create assignments and assignment groups
        try:
            create_assignments(course, internalized_data)
            print("Finished creating assignment groups and assignments.")
        except Exception as e:
            print(f"An error occurred while creating assignments: {e}")

# Run the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Canvas assignments from a YAML file.")
    parser.add_argument("course_id", type=int, help="The ID of the Canvas course.")
    parser.add_argument("file_path", type=str, help="The path to the YAML file containing assignment data.")

    args = parser.parse_args()

    main(args.course_id, args.file_path)
