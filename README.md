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
uv run python -m canvas_roster_project.make_photoroster <COURSE_ID>
```
(Or alternatively, if you are in an activated venv)

```sh
python -m canvas_roster_project.make_photoroster <COURSE_ID>
```

The resulting PDF will be saved as `photo_roster_<COURSE_ID>.pdf`.

---

## Installation and Setup

This section covers the prerequisites, API token setup, and environment configuration.

### Prerequisites

Before using this project, ensure you have:

1. **A Canvas API Token** – See [Generating and Configuring Your Canvas API Token](#generating-and-configuring-your-canvas-api-token) for details.
2. **Python 3.9 or higher** – Required for installing and running `uv`.
3. **uv** – Used for managing project dependencies and versions. Installation instructions are available on the [uv website](https://docs.astral.sh/uv/).

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

1. **Create and Activate the Virtual Environment:**
   ```sh
   uv sync --group dev
   source .venv/bin/activate
   ```
2. **Install Dependencies:**
   ```sh
   uv sync --group dev
   ```
3. **Execute Script:**
   ```sh
   python src/canvas_roster_project.make_photoroster.py <COURSE_ID>
   ```
Replace `<COURSE_ID>` with the actual Canvas Course ID. The PDF output will be saved as `photo_roster<COURSE_ID>.pdf`.
4. **Deactivate the Virtual Environment:**
   ```sh
   deactivate
   ```

#### Windows (PowerShell)

1. **Activate the Virtual Environment:**

   In your PowerShell prompt, run:
   ```powershell
   PS1> .\.venv\Scripts\Activate.ps1
   ```
   > **Note:** The `PS1>` is the prompt indicator and should not be typed as part of the command.
2. **Install Dependencies:**
   ```powershell
   PS1> uv sync --group dev
   ```
3. **Execute Script:**
   ```sh
   PS1> python src/canvas_roster_project.make_photoroster.py <COURSE_ID>
   ```
Replace `<COURSE_ID>` with the actual Canvas Course ID. The PDF output will be saved as `photo_roster<COURSE_ID>.pdf`.
4. **Deactivate the Virtual Environment:**
   ```powershell
   PS1> deactivate
   ```

---

## Development Notes

We use `uv` for dependency and version management. The following commands assume a Unix-like environment unless otherwise noted.

### Managing Dependencies

- **Add a runtime dependency:**
  ```sh
  uv add <package>
  ```
- **Add a development dependency:**
  ```sh
  uv add --group dev <package>
  ```
- **List installed dependencies:**
  ```sh
  uv tree
  ```
- **Remove a dependency:**
  ```sh
  uv remove <package>
  ```

### Testing and Code Quality

- **Run Tests:**
  ```sh
  uv run pytest
  ```
- **Check Code Coverage:**
  ```sh
  uv run pytest --cov=canvas_roster_project
  ```
- **Linting and Formatting:**
  Run all checks with:
  ```sh
  uv run pre-commit run --all-files
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



