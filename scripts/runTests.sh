#!/bin/bash

echo ====================" Running tests and generating Allure report... ===================="

# Ensure dependencies are installed
pip install pytest allure-pytest

# Set PYTHONPATH
export PYTHONPATH=$(pwd)

# Run PyTest with Allure
pytest --alluredir=allure-results tests/unit/*

# Generate and Serve Allure Report
allure serve allure-results

# Add a newline and delete __pycache__ and .pytest_cache directories
echo ""
echo "====================== Cleaning up Cache directories... "======================
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name ".pytest_cache" -exec rm -rf {} +
echo ""

echo "============================ Cleanup complete. "============================
