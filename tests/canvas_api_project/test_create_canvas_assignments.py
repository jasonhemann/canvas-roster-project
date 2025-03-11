from unittest.mock import MagicMock, patch

import pytest

from canvas_roster_project.create_canvas_assignments import (
    check_existing_groups,
    confirm_input,
    create_assignments,
    handle_no_response,
    internalize_structure,
    load_yaml,
    print_structure,
)


def test_print_structure(mocker):
    internalized_data = [
        {
            "name": "HW1: Test Group",
            "questions": [
                {
                    "name": "1: Test Question",
                    "points": 10,
                    "due_date": "2024-09-01T23:59:00",
                }
            ],
        }
    ]
    mock_print = mocker.patch("builtins.print")
    print_structure(internalized_data)
    mock_print.assert_any_call("Assignment Group: HW1: Test Group")
    mock_print.assert_any_call(
        "  - 1: Test Question (Points: 10, Due: 2024-09-01T23:59:00)"
    )


def test_confirm_input_yes(mocker):
    mock_input = mocker.patch("builtins.input", return_value="yes")
    on_no_mock = mocker.Mock()
    result = confirm_input("Proceed?", on_no_mock)
    assert result is True
    on_no_mock.assert_not_called()


def test_confirm_input_no(mocker):
    mock_input = mocker.patch("builtins.input", return_value="no")
    on_no_mock = mocker.Mock()
    result = confirm_input("Proceed?", on_no_mock)
    assert result is False
    on_no_mock.assert_called_once()


def test_handle_no_response(mocker):
    mock_exit = mocker.patch("sys.exit")
    handle_no_response()
    mock_exit.assert_called_once_with(0)


def test_check_existing_groups(mocker):
    mock_course = MagicMock()
    mock_group = MagicMock()
    mock_group.name = "HW1: Test Group"
    mock_course.get_assignment_groups.return_value = [mock_group]
    internalized_data = [{"name": "HW1: Test Group", "questions": []}]
    with pytest.raises(ValueError, match="already exists"):
        check_existing_groups(mock_course, internalized_data)


def test_create_assignments(mocker):
    mock_course = MagicMock()
    internalized_data = [
        {
            "name": "HW1: Test Group",
            "questions": [
                {
                    "name": "1: Test Question",
                    "points": 10,
                    "due_date": "2024-09-01T23:59:00",
                }
            ],
        }
    ]
    create_assignments(mock_course, internalized_data)
    mock_course.create_assignment_group.assert_called_once_with(name="HW1: Test Group")
    mock_course.create_assignment.assert_called_once_with(
        {
            "name": "1: Test Question",
            "points_possible": 10,
            "due_at": "2024-09-01T23:59:00",
            "assignment_group_id": mock_course.create_assignment_group.return_value.id,
            "published": False,
        }
    )


def test_load_yaml_valid(mocker):
    mock_open = mocker.patch(
        "builtins.open", mocker.mock_open(read_data="assignment_groups: []")
    )
    data = load_yaml("dummy_path.yaml")
    assert data == {"assignment_groups": []}


def test_load_yaml_file_not_found(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(ValueError, match="File not found"):
        load_yaml("nonexistent.yaml")


def test_internalize_structure():
    raw_data = {
        "assignment_groups": [
            {
                "name": "Test Group",
                "due_date": "2024-09-01 23:59",
                "questions": [{"name": "Test Question", "points": 10}],
            }
        ]
    }
    internalized_data = internalize_structure(raw_data)
    expected_data = [
        {
            "name": "HW1: Test Group",
            "questions": [
                {
                    "name": "1: Test Question",
                    "points": 10,
                    "due_date": "2024-09-01T23:59:00",
                }
            ],
        }
    ]
    assert internalized_data == expected_data
