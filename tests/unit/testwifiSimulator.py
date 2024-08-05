"""
Unit Tests for WiFiSimulator

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the WiFiSimulator class, including tests for
signal strength, movement, and breathing pattern simulations.

Modules:
    - pytest: Provides the testing framework.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.

Tests:
    - test_signal: Verifies that the simulated signal strength is one of the expected values.
    - test_movement: Verifies that the simulated movement is one of the expected values.
    - test_breathing: Verifies that the simulated breathing pattern is one of the expected values.
    - test_invalid_signal: Verifies that the simulated signal strength is not an invalid value.
    - test_invalid_movement: Verifies that the simulated movement is not an invalid value.
    - test_invalid_breathing: Verifies that the simulated breathing pattern is not an invalid value.
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

def test_movement(simulator):
    """
    Tests the simulate_movement method of WiFiSimulator.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    movement = simulator.simulate_movement()
    assert movement in ['None', 'Walking', 'Running', 'Falling']

def test_breathing(simulator):
    """
    Tests the simulate_breathing method of WiFiSimulator.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    breathing = simulator.simulate_breathing()
    assert breathing in ['Normal', 'Fast', 'Slow']

def test_invalid_signal(simulator):
    """
    Tests the simulate_signal method of WiFiSimulator for invalid signals.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    signal = simulator.simulate_signal()
    assert signal == 'Invalid Signal', "Test failed intentionally: signal is not 'Invalid Signal'"

def test_invalid_movement(simulator):
    """
    Tests the simulate_movement method of WiFiSimulator for invalid movement.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    movement = simulator.simulate_movement()
    assert movement == 'Flying', "Test failed intentionally: movement is not 'Flying'"

def test_invalid_breathing(simulator):
    """
    Tests the simulate_breathing method of WiFiSimulator for invalid breathing patterns.

    Args:
        simulator: The WiFiSimulator instance provided by the fixture.
    """
    breathing = simulator.simulate_breathing()
    assert breathing == 'Holding Breath', "Test failed intentionally: breathing is not 'Holding Breath'"
