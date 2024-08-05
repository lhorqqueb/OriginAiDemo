#!/bin/bash

echo "======================== Running tests and generating Allure report... ========================"

# Ensure dependencies are installed
pip install pytest allure-pytest behave

# Set PYTHONPATH
export PYTHONPATH=$(pwd)

# Run PyTest with Allure
pytest --alluredir=allure-results tests/unit/*

# Run Behave tests with Allure formatter
ALLURE_BEHAVE_FORMATTER=allure_behave.formatter:AllureFormatter behave -f $ALLURE_BEHAVE_FORMATTER -o allure-results tests/integration/features/

# Generate and Serve Allure Report
allure serve allure-results

# Add a newline and delete __pycache__, .pytest_cache, and allure-results directories
echo ""
echo "======================== Cleaning up Cache directories... ========================"
find . -type d -name "__pycache__" -exec rm -rf {} \;
find . -type d -name ".pytest_cache" -exec rm -rf {} \;
find . -type d -name "allure-results" -exec rm -rf {} \;
echo ""

echo "============================ Cleanup complete. ============================"
