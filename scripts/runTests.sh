#!/bin/bash

echo "Setting up test environment..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip allure

echo "Installing dependencies..."
pip3 install -r requirements.txt
pip3 install allure-pytest

echo "Running unit tests with PyTest..."
pytest --alluredir=./allure-results tests/unit/

echo "Running integration tests with Behave..."
behave -f allure_behave.formatter:AllureFormatter -o ./allure-results tests/integration/features/

echo "Generating Allure Report..."
allure serve ./allure-results
