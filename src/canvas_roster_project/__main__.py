"""Module entrypoint for `python -m canvas_roster_project`."""

from __future__ import annotations

from .make_photoroster import main

if __name__ == "__main__":
    raise SystemExit(main())
