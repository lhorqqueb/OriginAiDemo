"""
Unit Tests for CombinedSimulator

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the CombinedSimulator class, including tests for
evaluating WiFi performance based on combined environmental and embedded system factors.

Modules:
    - pytest: Provides the testing framework.
    - scripts.combinedSimulation: Imports the CombinedSimulator class to be tested.

Tests:
    - test_evaluate_performance: Verifies the WiFi performance evaluation based on different scenarios.
"""

import pytest
from scripts.combinedSimulation import CombinedSimulator

@pytest.fixture
def simulator():
    """
    Fixture that provides an instance of CombinedSimulator.

    Returns:
        CombinedSimulator: An instance of CombinedSimulator.
    """
    return CombinedSimulator()

def test_evaluate_performance(simulator):
    """
    Tests the evaluate_performance method of CombinedSimulator for various scenarios.

    Args:
        simulator: The CombinedSimulator instance provided by the fixture.
    """
    performance = simulator.evaluate_performance()
    assert performance in ['Excellent', 'Ideal', 'Optimized', 'Poor']
