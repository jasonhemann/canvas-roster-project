# **Canvas API Project**

This tool generates a **class photo roster PDF** using student photos from **Canvas**.

## **Prerequisites**

1. **Python** `>=3.13`
2. **Canvas API Token** (See [Canvas API Documentation](https://canvasapi.readthedocs.io/))
3. **PDM** for managing dependencies

## **Installation & Setup**

First, activate the virtual environment:

```sh
eval $(pdm venv activate in-project)
```
To deactivate later, run:
```sh
deactivate
```

Install dependencies:

```sh
pdm install
```

## **Usage**

### **Generate a Photo Roster PDF**
Run the script using:
```sh
python -m canvas_api_project.make_photoroster --course <COURSE_ID> --output photo_roster.pdf
```

- Replace `<COURSE_ID>` with the Canvas Course ID.
- The generated PDF will be saved as **photo_roster.pdf**.

### **Create Assignments in Canvas**
To create assignments in a Canvas course:

```sh
python -m canvas_api_project.create_canvas_assignments --course <COURSE_ID> --config assignments.yaml
```

- **`assignments.yaml`** defines the assignments to be created.

## **Testing & Code Quality**

### **Run Tests**
To run all tests:
```sh
pdm run pytest
```
To check code coverage:
```sh
pdm run pytest --cov=canvas_api_project
```

### **Linting & Formatting**
Run all linting and formatting checks:
```sh
pdm run pre-commit run --all-files
```

This will:
- Check formatting with `black` and `isort`
- Lint code with `flake8`
- Run type checks with `mypy`

## **Development**

### **Adding Dependencies**
To add a runtime dependency:
```sh
pdm add <package>
```
To add a development dependency:
```sh
pdm add -d <package>
```

### **Useful Commands**
List dependencies:
```sh
pdm list --tree
```

Uninstall a package:
```sh
pdm remove <package>
```

## **Canvas API Documentation & Resources**
- **[Getting Started with Canvas API](https://community.canvaslms.com/t5/Canvas-Developers-Group/Canvas-APIs-Getting-started-the-practical-ins-and-outs-gotchas/ba-p/263685)**
- **[Live API on Test Environment](https://setonhall.test.instructure.com/doc/api/live)**
- **[Canvas API Python Library](https://canvasapi.readthedocs.io/)** (Makes API interaction much easier!)

