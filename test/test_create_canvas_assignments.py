import pytest
from src.create_canvas_assignments import load_yaml, internalize_structure, check_existing_groups

def test_load_yaml_valid(mocker):
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data="assignment_groups: []"))
    data = load_yaml("dummy_path.yaml")
    assert data == {"assignment_groups": []}

def test_load_yaml_file_not_found(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(ValueError, match="File not found"):
        load_yaml("nonexistent.yaml")

def test_internalize_structure():
    raw_data = {
        "assignment_groups": [
            {"name": "Test Group", "due_date": "2024-09-01 23:59", "questions": [
                {"name": "Test Question", "points": 10}
            ]}
        ]
    }
    internalized_data = internalize_structure(raw_data)
    expected_data = [{
        "name": "HW1: Test Group",
        "questions": [
            {"name": "1: Test Question", "points": 10, "due_date": "2024-09-01T23:59:00"}
        ]
    }]
    assert internalized_data == expected_data
