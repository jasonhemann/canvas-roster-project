.PHONY: sync format lint lint-fix typecheck test smoke coverage check check-env clean

UV ?= uv
PYTHON_VERSION ?= 3.13

sync:
	$(UV) sync --python $(PYTHON_VERSION) --group dev --group test

format:
	$(UV) run --python $(PYTHON_VERSION) ruff format src tests

lint:
	$(UV) run --python $(PYTHON_VERSION) ruff check src tests

lint-fix:
	$(UV) run --python $(PYTHON_VERSION) ruff check src tests --fix

typecheck:
	$(UV) run --python $(PYTHON_VERSION) basedpyright

test:
	$(UV) run --python $(PYTHON_VERSION) pytest -q

smoke:
	$(UV) run --python $(PYTHON_VERSION) python -m canvas_roster_project --help >/dev/null
	$(UV) run --python $(PYTHON_VERSION) python -m canvas_roster_project.make_photoroster --help >/dev/null

coverage:
	@echo "Coverage target (warn-only in wave 1): 80%"
	-$(UV) run --python $(PYTHON_VERSION) pytest --cov=src/canvas_roster_project --cov-report=term-missing -q

check: lint typecheck test smoke

check-env:
	@echo "Python:" && $(UV) run --python $(PYTHON_VERSION) python -V
	@echo "Interpreter Path:" && $(UV) run --python $(PYTHON_VERSION) python -c "import sys; print(sys.executable)"
	@echo "Virtualenv Prefix:" && $(UV) run --python $(PYTHON_VERSION) python -c "import sys; print(sys.prefix)"

clean:
	rm -rf .venv __pycache__ */__pycache__ .pytest_cache .ruff_cache dist build *.egg-info
