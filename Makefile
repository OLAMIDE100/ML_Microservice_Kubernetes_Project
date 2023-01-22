## The Makefile includes instructions on environment setup and lint tests
# Create and activate a virtual environment
# Install dependencies in requirements.txt
# Dockerfile should pass hadolint
# app.py should pass pylint
# (Optional) Build a simple integration test


setup:
	python -m venv .devops_env



install: setup
	pip install -r docker/requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	hadolint docker/Dockerfile
	pylint --disable=R,C,W1203,W1202 docker/app.py

all: install lint test
