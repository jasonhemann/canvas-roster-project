# Canvas Roster Project

Canvas Roster Project generates a class photo roster PDF using student photos fetched from Canvas.

## Quick start

```sh
make sync
source .venv/bin/activate
uv run python -m canvas_roster_project.make_photoroster <COURSE_ID>
```

The resulting PDF is saved as `photo_roster_<COURSE_ID>.pdf`.

You can also use the installed console script from the project environment:

```sh
uv run canvas-roster <COURSE_ID>
```

## API token setup

Set your Canvas API token as `CANVAS_API_KEY`:

```sh
export CANVAS_API_KEY="your_token_here"
```

## Quality checks

```sh
make check
```

Individual commands:

```sh
make format
make lint
make lint-fix
make typecheck
make test
make smoke
make coverage
```

Coverage is currently warn-only in this wave.

## Build Standalone Executable

Create a standalone executable with PyInstaller:

```sh
make build
```

The executable is created at `./dist/canvas-roster`. It can run directly on the
same OS and architecture without setting up `uv`, a virtual environment, or
project dependencies:

```sh
./dist/canvas-roster <COURSE_ID>
```

To install the executable to your user-local bin directory:

```sh
make install
```

By default this copies it to `$HOME/.local/bin/canvas-roster`. Make sure
`$HOME/.local/bin` is on your `PATH`.

For a machine-wide install, choose `/usr/local/bin` explicitly:

```sh
make install INSTALL_DIR=/usr/local/bin
```

## Notes

- Canvas domain is configured to `https://setonhall.instructure.com`.
- Avoid hardcoding API keys in source files.
