# Canvas Roster Project

Canvas Roster Project generates a **class photo roster PDF** using student photos fetched from Canvas.

## Table of Contents

- [Quick Start](#quick-start)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Generating and Configuring Your Canvas API Token](#generating-and-configuring-your-canvas-api-token)
  - [Virtual Environment Setup](#virtual-environment-setup)
- [Usage](#usage)
- [Development Notes](#development-notes)
- [Canvas API Documentation and Resources](#canvas-api-documentation-and-resources)

---

## Quick Start

Generate a photo roster PDF by running the following command, replacing `<COURSE_ID>` with your Canvas course identifier:

```sh
python -m canvas_roster_project.make_photoroster <COURSE_ID>
```

The resulting PDF will be saved as `photo_roster<COURSE_ID>.pdf`.

---

## Installation and Setup

This section covers the prerequisites, API token setup, and environment configuration.

### Prerequisites

Before using this project, ensure you have:

1. **A Canvas API Token** – See [Generating and Configuring Your Canvas API Token](#generating-and-configuring-your-canvas-api-token) for details.
2. **Python 3.9 or higher** – Required for installing and running `pdm`.
3. **pdm** – Used for managing project dependencies and versions. Installation instructions are available on the [pdm website](https://pdm-project.org/en/latest/#installation).

### Generating and Configuring Your Canvas API Token

1. **Generate Your API Token:**

   Follow the [walk-through video](https://www.youtube.com/watch?v=cZ5cn8stjM0#t=0m30s) to generate your Canvas API token. Once generated, securely copy your token.

2. **Make the API Token Available:**

   Set the token as an environment variable:

   - **Unix-like Systems (Linux/macOS):**
     ```sh
     export CANVAS_API_KEY=your_token_here
     ```
   - **Windows (PowerShell):**
     ```powershell
     $env:CANVAS_API_KEY = "your_token_here"
     ```

   > **Security Note:** Avoid hardcoding your API token in your source code or committing it to version control. For better security, consider using an environment file.

3. **Verify the Configuration:**

   - **Unix-like Systems:**
     ```sh
     echo $CANVAS_API_KEY
     ```
   - **Windows (PowerShell):**
     ```powershell
     echo $env:CANVAS_API_KEY
     ```

### Virtual Environment Setup

Follow the instructions below based on your operating system.

#### Unix-like Systems (Linux/macOS)

1. **Activate the Virtual Environment:**
   ```sh
   eval $(pdm venv activate in-project)
   ```
2. **Install Dependencies:**
   ```sh
   pdm install
   ```
3. **Deactivate the Virtual Environment:**
   ```sh
   deactivate
   ```

#### Windows (PowerShell)

1. **Activate the Virtual Environment:**

   In your PowerShell prompt, run:
   ```powershell
   PS1> Invoke-Expression (pdm venv activate for-test)
   ```
   > **Note:** The `PS1>` is the prompt indicator and should not be typed as part of the command.
2. **Install Dependencies:**
   ```powershell
   pdm install
   ```
3. **Deactivate the Virtual Environment:**
   ```powershell
   deactivate
   ```

---

## Usage

After setting up the environment, generate the photo roster PDF with:

```sh
python -m canvas_roster_project.make_photoroster <COURSE_ID>
```

Replace `<COURSE_ID>` with the actual Canvas Course ID. The PDF output will be saved as `photo_roster<COURSE_ID>.pdf`.

---

## Development Notes

We use `pdm` for dependency and version management. The following commands assume a Unix-like environment unless otherwise noted.

### Managing Dependencies

- **Add a runtime dependency:**
  ```sh
  pdm add <package>
  ```
- **Add a development dependency:**
  ```sh
  pdm add -d <package>
  ```
- **List installed dependencies:**
  ```sh
  pdm list --tree
  ```
- **Remove a dependency:**
  ```sh
  pdm remove <package>
  ```

### Testing and Code Quality

- **Run Tests:**
  ```sh
  pdm run pytest
  ```
- **Check Code Coverage:**
  ```sh
  pdm run pytest --cov=canvas_roster_project
  ```
- **Linting and Formatting:**
  Run all checks with:
  ```sh
  pdm run pre-commit run --all-files
  ```
  This command:
  - Formats code with `black` and `isort`
  - Lints code with `flake8`
  - Runs type checks with `mypy`

---

## Canvas API Documentation and Resources

- **[Getting Started with Canvas API](https://community.canvaslms.com/t5/Canvas-Developers-Group/Canvas-APIs-Getting-started-the-practical-ins-and-outs-gotchas/ba-p/263685)**
- **[Live API on Test Environment](https://setonhall.test.instructure.com/doc/api/live)**
- **[Canvas API Python Library](https://canvasapi.readthedocs.io/)** -- Simplifies API interactions



