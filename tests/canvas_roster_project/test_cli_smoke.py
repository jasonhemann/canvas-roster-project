import subprocess
import sys


def test_make_photoroster_module_help():
    proc = subprocess.run(
        [sys.executable, "-m", "canvas_roster_project.make_photoroster", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "Generate a photo roster for a Canvas course." in proc.stdout


def test_package_entrypoint_help():
    proc = subprocess.run(
        [sys.executable, "-m", "canvas_roster_project", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "Generate a photo roster for a Canvas course." in proc.stdout
