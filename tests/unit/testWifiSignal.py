"""
Unit Test for WiFiSimulator Signal Simulation

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the WiFiSimulator class, specifically testing the 
signal strength simulation functionality.

Modules:
    - pytest: Provides the testing framework.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.

Tests:
    - test_signal: Verifies that the simulated signal strength is one of the expected values.
"""

import pytest
from scripts.wifiSimulation import WiFiSimulator

@pytest.fixture
def simulator():
    """
    Fixture that provides an instance of WiFiSimulator.

    Returns:
        WiFiSimulator: An instance of WiFiSimulator.
    """
    return WiFiSimulator()

def test_signal(simulator):
    """
    Tests the simulate_signal method of WiFiSimulator.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    signal = simulator.simulate_signal()
    assert signal in ['Strong', 'Weak', 'No Signal']
