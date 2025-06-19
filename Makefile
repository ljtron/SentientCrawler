# .PHONY: activate
.ONESHELL:
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
# SHELL := /bin/bash

createEnvironment:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)
	@echo "Virtual environment created at $(VENV)"
	$(PIP) install --upgrade pip
#$(PIP) install -r requirements.txt

activate:	
	@echo "To activate the virtual environment, run:" 
	@echo "source $(VENV)/bin/activate"


freeze:	
	$(PIP) freeze > requirements.txt

download:
	$(PIP) install -r requirements.txt

pushReady:
	$(freeze)	deactivate	git add

# yourTarget: 
# 	 $(PIP) -h

# $(eval SHELL:=/bin/bash)
	
# echo "here shell is $$0"

# hellomake: hellomake.c hellofunc.c
#      gcc -o hellomake hellomake.c hellofunc.c -I.