"""Generate a PDF photo roster for a Canvas course."""

from __future__ import annotations

import argparse
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

import requests
from canvasapi import Canvas
from PIL import Image as PilImage
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate, Table, TableStyle

CANVAS_DOMAIN = "https://setonhall.instructure.com"


@dataclass(frozen=True)
class CliArgs:
    """CLI arguments for roster generation."""

    course_id: int


@dataclass(frozen=True)
class Student:
    """Minimal student profile used for PDF rendering."""

    student_id: int
    name: str
    email: str | None
    avatar_url: str | None


class _CanvasUser(Protocol):
    id: int
    name: str

    def get_profile(self) -> dict[str, object]: ...


class _CanvasCourse(Protocol):
    def get_users(self) -> list[_CanvasUser]: ...


class _CanvasClient(Protocol):
    def get_course(self, course_id: int) -> object: ...


def parse_args(argv: list[str] | None = None) -> CliArgs:
    """Parse CLI arguments for roster generation."""
    parser = argparse.ArgumentParser(description="Generate a photo roster for a Canvas course.")
    _ = parser.add_argument(
        "course_id",
        type=int,
        help="The course ID for the Canvas course",
    )
    args = parser.parse_args(argv)
    return CliArgs(course_id=cast(int, args.course_id))


def get_canvas_client() -> Canvas:
    """Create a Canvas client using ``CANVAS_API_KEY`` from environment."""
    api_key = os.environ.get("CANVAS_API_KEY", "NONE")
    return Canvas(CANVAS_DOMAIN, api_key)


def fetch_students(canvas: object, course_id: int) -> list[Student]:
    """Fetch course users from Canvas and map to student records."""
    client = cast(_CanvasClient, canvas)
    course = cast(_CanvasCourse, client.get_course(course_id))
    students: list[Student] = []

    for user in course.get_users():
        profile = user.get_profile()
        email_obj = profile.get("primary_email")
        avatar_obj = profile.get("avatar_url")
        email = str(email_obj) if isinstance(email_obj, str) else None
        avatar = str(avatar_obj) if isinstance(avatar_obj, str) else None

        students.append(
            Student(
                student_id=int(user.id),
                name=str(user.name),
                email=email,
                avatar_url=avatar,
            )
        )

    return students


def download_image(url: str, filename: Path) -> bool:
    """Download image to ``filename`` and return success status."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"Error downloading image: {exc}")
        return False

    _ = filename.write_bytes(response.content)
    return True


def _photo_cell(student: Student, temp_image_dir: Path) -> object:
    """Return a reportlab cell value for the student photo."""
    if student.avatar_url is None:
        return "No Photo"

    image_path = temp_image_dir / f"{student.student_id}_avatar.jpg"
    if not download_image(student.avatar_url, image_path):
        return "No Photo"

    try:
        with PilImage.open(image_path) as image:
            image.thumbnail((100, 100))
            if image.mode == "RGBA":
                image = image.convert("RGB")
            image.save(image_path)
    except OSError as exc:
        print(f"Error handling image: {exc}")
        return "No Photo"

    return Image(str(image_path), width=50, height=50)


def create_photo_roster(
    students: list[Student],
    pdf_file_path: Path,
    temp_image_dir: Path,
) -> None:
    """Create the photo-roster PDF for the provided students."""
    document = SimpleDocTemplate(str(pdf_file_path), pagesize=letter)
    table_rows: list[list[object]] = [["Photo", "Name", "Email"]]

    for student in students:
        table_rows.append(
            [
                _photo_cell(student, temp_image_dir),
                student.name,
                student.email or "No Email",
            ]
        )

    table = Table(table_rows)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    document.build([table])


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for generating roster PDFs."""
    args = parse_args(argv)

    temp_image_dir = Path(tempfile.mkdtemp())
    try:
        students = fetch_students(get_canvas_client(), args.course_id)
        output_pdf = Path(f"photo_roster_{args.course_id}.pdf")
        create_photo_roster(students, output_pdf, temp_image_dir)
    finally:
        shutil.rmtree(temp_image_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
