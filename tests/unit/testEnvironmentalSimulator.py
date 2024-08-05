"""
Unit Tests for EnvironmentalSimulator

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the EnvironmentalSimulator class, including tests for
temperature and humidity simulations.

Modules:
    - pytest: Provides the testing framework.
    - scripts.environmentalSimulation: Imports the EnvironmentalSimulator class to be tested.

Tests:
    - test_temperature: Verifies that the simulated temperature is within the expected range.
    - test_humidity: Verifies that the simulated humidity is within the expected range.
    - test_invalid_temperature: Verifies that the simulated temperature is not an invalid value.
    - test_invalid_humidity: Verifies that the simulated humidity is not an invalid value.
"""

import pytest
from scripts.environmentalSimulation import EnvironmentalSimulator

@pytest.fixture
def simulator():
    """
    Fixture that provides an instance of EnvironmentalSimulator.

    Returns:
        EnvironmentalSimulator: An instance of EnvironmentalSimulator.
    """
    return EnvironmentalSimulator()

def test_temperature(simulator):
    """
    Tests the simulate_temperature method of EnvironmentalSimulator.

    Args:
        simulator: The EnvironmentalSimulator instance provided by the fixture.
    """
    temperature = simulator.simulate_temperature()
    assert -10 <= temperature <= 40

def test_humidity(simulator):
    """
    Tests the simulate_humidity method of EnvironmentalSimulator.

    Args:
        simulator: The EnvironmentalSimulator instance provided by the fixture.
    """
    humidity = simulator.simulate_humidity()
    assert 0 <= humidity <= 100

def test_invalid_temperature(simulator):
    """
    Tests the simulate_temperature method of EnvironmentalSimulator for invalid temperatures.

    Args:
        simulator: The EnvironmentalSimulator instance provided by the fixture.
    """
    temperature = simulator.simulate_temperature()
    assert temperature < -10 or temperature > 40, "Test failed intentionally: temperature is within the valid range"

def test_invalid_humidity(simulator):
    """
    Tests the simulate_humidity method of EnvironmentalSimulator for invalid humidities.

    Args:
        simulator: The EnvironmentalSimulator instance provided by the fixture.
    """
    humidity = simulator.simulate_humidity()
    assert humidity < 0 or humidity > 100, "Test failed intentionally: humidity is within the valid range"
