VENV=venv
VENV_SCRIPTS=$(VENV)/Scripts
PYTHON=$(VENV_SCRIPTS)/python
PYTEST=$(VENV_SCRIPTS)/pytest

.PHONY: build
build:
	$(PYTHON) -m build

.PHONY: clean
clean:
	rm -rf dist

.PHONY: dev-setup
dev-setup: venv dev-requirements

.PHONY: venv
venv:
	python -m venv $(VENV)

.PHONY: dev-requirements
dev-requirements: dev-requirements.txt
	$(PYTHON) -m pip install -r dev-requirements.txt

.PHONY: test
test:
	$(PYTEST)

.PHONY: upload-pypi
upload-pypi:
	$(PYTHON) -m twine upload --verbose dist/*