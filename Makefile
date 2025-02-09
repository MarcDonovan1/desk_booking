
VENV_DIR = venv

test:
	python3 -m unittest discover tests

coverage:
	coverage run -m unittest discover tests
	coverage report -m --skip-covered

format:
	black .
# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)

# Install dependencies
install: venv
	$(VENV_DIR)/bin/pip install -r requirements.txt

run-venv:
	source $(VENV_DIR)/bin/activate

# Clean virtual environment
clean:
	rm -rf $(VENV_DIR)