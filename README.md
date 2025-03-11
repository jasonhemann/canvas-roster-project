# **Canvas API Project**

This tool generates a **class photo roster PDF** using student photos from **Canvas**.

## **Usage**

### **Generate a Photo Roster PDF**
Run the script using:
```sh
python -m canvas_api_project.make_photoroster <COURSE_ID>
```

- Replace `<COURSE_ID>` with the Canvas Course ID.
- The generated PDF will be saved as **photo_roster<COURSE_ID>.pdf**.

## **Prerequisites**

1. **Python** `>=3.13`
2. **Canvas API Token** (see [Generating a Canvas API token](#generating-a-canvas-api-token))
3. **PDM** for managing dependencies

### **Generating a Canvas API token**

To generate your own API token from within your account, complete the steps in this [walk-through video](https://www.youtube.com/watch?v=cZ5cn8stjM0#t=0m30s) to create the token. Make sure to save it.

For more about the API and what it offers, see the [resources section](#canvas-api-documentation-and-resources) below.

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

## **Development**

We use `pdm` for version and dependency management.

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

### **Testing & Code Quality**

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

## **Canvas API Documentation and Resources**
- **[Getting Started with Canvas API](https://community.canvaslms.com/t5/Canvas-Developers-Group/Canvas-APIs-Getting-started-the-practical-ins-and-outs-gotchas/ba-p/263685)**
- **[Live API on Test Environment](https://setonhall.test.instructure.com/doc/api/live)**
- **[Canvas API Python Library](https://canvasapi.readthedocs.io/)** (Makes API interaction much easier!)

