# Makefile for Artemis City

# Variables
PYTHON = python3

# Targets
.PHONY: install test run-cli run-simulation

install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt

test:
	@echo "Running tests..."
	$(PYTHON) -m unittest discover -s tests

run-cli:
	@echo "Running the Agentic Codex CLI..."
	$(PYTHON) interface/codex_cli.py

run-simulation:
	@echo "Running the Mail Delivery Simulation..."
	$(PYTHON) sandbox_city/networked_scripts/mail_delivery_sim.py