"""
Unit Test for WiFiSimulator Breathing Simulation

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the WiFiSimulator class, specifically testing the 
breathing pattern simulation functionality.

Modules:
    - pytest: Provides the testing framework.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.

Tests:
    - test_breathing: Verifies that the simulated breathing pattern is one of the expected values.
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

def test_breathing(simulator):
    """
    Tests the simulate_breathing method of WiFiSimulator.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    breathing = simulator.simulate_breathing()
    assert breathing in ['Normal', 'Fast', 'Slow']
