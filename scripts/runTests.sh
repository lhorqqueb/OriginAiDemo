#!/bin/bash

echo "Setting up test environment..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip

echo "Installing dependencies..."
pip3 install pytest behave pytest-reportportal

echo "Running unit tests with PyTest..."
pytest --reportportal -c reportportalConfig.py tests/unit/ > logs/unitTestResults.log

echo "Running integration tests with Behave..."
behave tests/integration/features/ > logs/integrationTestResults.log

echo "Test execution complete. Check logs for details."
