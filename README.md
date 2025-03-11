# **Canvas Roster Project**

This tool generates a **class photo roster PDF** using student photos from **Canvas**.

## **Quick-start Guide**

### **Generate a Photo Roster PDF**
Run the script using:
```sh
python -m canvas_api_project.make_photoroster <COURSE_ID>
```

- Replace `<COURSE_ID>` with the Canvas Course ID.
- The generated PDF will be saved as **photo_roster<COURSE_ID>.pdf**.

## **Installation, Setup, and Usage**

This section guides the walk through of setting up prerequisites and installing and using this software itself.

### **Prerequisites**

To use this software you must obtain/install the following:

1. A **Canvas API Token** (see [Generating a Canvas API token](#generating-and-configuring-your-canvas-api-token))
2. **Python** `>=3.9` for installing `pdm`
3. [`pdm`](https://pdm-project.org/en/latest/#installation) for managing versions and dependencies

We walk through this first step in detail.

### **Generating and Configuring Your Canvas API Token**

1. **Generate Your API Token:**
   Follow the [walk-through video](https://www.youtube.com/watch?v=cZ5cn8stjM0#t=0m30s) to generate your Canvas API token. Once generated, copy your token securely.

2. **Make the API Token Available:**

   One way to accomplish this is to set in the terminal session:

   - **Unix-like Systems (Linux/macOS):**
     ```sh
     export CANVAS_API_KEY=your_token_here
     ```

   - **Windows (PowerShell):**
     ```powershell
     $env:CANVAS_API_KEY = "your_token_here"
     ```

   > **Security Note:** Better practice is to store the key in an environment file. Ensure that you do not hardcode this key in your source code or commit it to version control.

3. **Verify the Configuration:**
   You can verify that the environment variable is set by running:

   - **Unix-like Systems:**
     ```sh
     echo $CANVAS_API_KEY
     ```
   - **Windows (PowerShell):**
     ```powershell
     echo $env:CANVAS_API_KEY
     ```

## **Usage**

Follow the instructions below based on your operating system.

### Unix-like Systems (Linux/macOS)

1. **Activate the Virtual Environment:**

   Run the following command in your terminal:

   ```sh
   eval $(pdm venv activate in-project)
   ```

2. **Install Dependencies:**

   Once the virtual environment is active, install the dependencies:

   ```sh
   pdm install
   ```

3. **Deactivate the Virtual Environment:**

   When you’re finished, exit the virtual environment by running:

   ```sh
   deactivate
   ```

### Windows (PowerShell)

1. **Activate the Virtual Environment:**

   In your PowerShell prompt, use the following command (including the prompt text as shown):

   ```powershell
   PS1> Invoke-Expression (pdm venv activate for-test)
   ```

2. **Install Dependencies:**

   After activation, install the dependencies:

   ```powershell
   pdm install
   ```

3. **Deactivate the Virtual Environment:**

   When finished, deactivate the environment by running:

   ```powershell
   deactivate
   ```

> **Note:** The `PS1>` shown in the Windows command is the prompt indicator; you should not type it as part of the command.

### **Generate a Photo Roster PDF**

Once inside the project, you can run the script using:
```sh
python -m canvas_api_project.make_photoroster <COURSE_ID>
```

- Replace `<COURSE_ID>` with the Canvas Course ID.
- The generated PDF will be saved as **photo_roster<COURSE_ID>.pdf**.

## **Development Notes**

We use `pdm` for all version and dependency management. The following instructions are written assuming a Unix-like environment.

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

