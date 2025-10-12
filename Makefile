include ./colors.mk

.ONESHELL:
SHELL = /bin/bash
PYTHON = python3.12
BUILD_DIR = src playground

# Python Virtual Environment
.PHONY: venv
venv:
	@echo -e "$(COLOR_GREEN)Creating virtual environment with uv...$(END_COLOR)"
	uv sync
	@echo -e "$(COLOR_GREEN)Virtual environment created and dependencies installed$(END_COLOR)"

.PHONY: style
style:
	@echo -e "$(COLOR_GREEN)Running code style checks with ruff...$(END_COLOR)"
	@echo -e "$(COLOR_GREEN)Running ruff format...$(END_COLOR)"
	uv run ruff format ${BUILD_DIR}
	@echo -e "$(COLOR_GREEN)Running ruff check...$(END_COLOR)"
	uv run ruff check --fix ${BUILD_DIR}
