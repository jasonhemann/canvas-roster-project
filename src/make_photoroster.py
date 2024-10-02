import os
import requests
import shutil
import argparse
from canvasapi import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PilImage
import tempfile

# Function to download an image
def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
        return filename
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

# Function to create the PDF photo roster
def create_photo_roster(students, pdf_file_path):
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Table header
    data = [["Photo", "Name", "Email"]]

    for student in students:
        # Handle missing avatar
        if student['avatar_url']:
            image_path = os.path.join(temp_image_dir, f"{student['id']}_avatar.jpg")
            if download_image(student['avatar_url'], image_path):
                try:
                    with PilImage.open(image_path) as img:
                        img.thumbnail((100, 100))
                        if img.mode == 'RGBA':
                            img = img.convert('RGB')  # Convert RGBA to RGB to handle JPEG format
                        img.save(image_path)
                    image = Image(image_path, width=50, height=50)
                except Exception as e:
                    print(f"Error handling image: {e}")
                    image = "No Photo"
            else:
                image = "No Photo"
        else:
            image = "No Photo"

        data.append([image, student['name'], student['email'] or "No Email"])

    # Create the table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)

# Create a temporary directory for images
temp_image_dir = tempfile.mkdtemp()

# Argument parser for taking the course ID as input
parser = argparse.ArgumentParser(description='Generate a photo roster for a Canvas course.')
parser.add_argument('course_id', type=int, help='The course ID for the Canvas course')
args = parser.parse_args()

# Canvas API setup
DOMAIN = "https://setonhall.instructure.com"
API_KEY = os.environ.get("CANVAS_API_KEY", "NONE")

canvas = Canvas(DOMAIN, API_KEY)
course = canvas.get_course(args.course_id)

try:
    # Fetch students and their data (handle pagination)
    users = course.get_users()

    students = []
    for user in users:
        profile = user.get_profile()
        students.append({
            'id': user.id,
            'name': user.name,
            'email': profile.get('primary_email', None),
            'avatar_url': profile.get('avatar_url', None)
        })

    # Create the PDF roster
    create_photo_roster(students, f"photo_roster_{args.course_id}.pdf")

finally:
    # Clean up temp images
    shutil.rmtree(temp_image_dir)
