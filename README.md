# OriginAiDemo

## Overview
This repository contains a comprehensive and production-ready automation framework designed to showcase WiFi Sensing capabilities inspired by Origin Wireless. Built using Python, PyTest, Behave, and Allure, the framework ensures thorough test coverage and reporting. It includes scripts for simulating WiFi signal disruptions and embedded system interactions, along with automated test cases and continuous integration setup.

## Key Features

### WiFi Signal and Embedded System Simulation
- Simulates various WiFi signal scenarios, movements, and breathing patterns.
- Simulates data transmission and reception in an embedded system.

### Automated Testing with PyTest and Behave
- Unit and integration tests for comprehensive coverage.
- Uses PyTest for unit testing.
- Uses Behave for behavior-driven development (BDD) and integration tests.

### Continuous Integration with GitHub Actions
- Automated test execution on code commits.
- CI/CD pipeline for seamless integration and deployment.

### Detailed Reporting with Allure
- Generates informative and customizable test reports.
- Provides easy-to-understand and shareable test results.

### Well-Organized Code Structure
- Clear separation of test cases, configurations, and utilities.

## Technologies Used
- **WiFi Simulation**: Custom Python scripts
- **Embedded System Simulation**: Custom Python scripts
- **Unit Testing**: PyTest
- **Integration Testing**: Behave
- **Continuous Integration**: GitHub Actions
- **Reporting**: Allure
- **Version Control**: Git

## Getting Started

### Prerequisites
- Python 3.x
- pip
- Git

### Clone the Repository
```bash
git clone git@github.com:lhorqqueb/OriginAiDemo.git
cd OriginAiDemo

git clone git@github.com:lhorqqueb/OriginAiDemo.git
cd OriginAiDemo
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Unit Tests
```bash
behave tests/integration/features
```

### Run Automated Tests
```bash
./scripts/runTests.sh
```

### View Test Reports
To generate and view the allure report, run: 
```bash
allure serve ./allure-results
```
