"""
Unit Test for WiFiSimulator Movement Simulation

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the WiFiSimulator class, specifically testing the 
movement simulation functionality.

Modules:
    - pytest: Provides the testing framework.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.

Tests:
    - test_movement: Verifies that the simulated movement is one of the expected values.
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

def test_movement(simulator):
    """
    Tests the simulate_movement method of WiFiSimulator.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    movement = simulator.simulate_movement()
    assert movement in ['None', 'Walking', 'Running', 'Falling']
