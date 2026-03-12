# Canvas Roster Project

Canvas Roster Project generates a class photo roster PDF using student photos fetched from Canvas.

## Quick start

```sh
make sync
source .venv/bin/activate
uv run python -m canvas_roster_project.make_photoroster <COURSE_ID>
```

The resulting PDF is saved as `photo_roster_<COURSE_ID>.pdf`.

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

## Notes

- Canvas domain is configured to `https://setonhall.instructure.com`.
- Avoid hardcoding API keys in source files.
