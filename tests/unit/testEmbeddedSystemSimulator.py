"""
Unit Tests for EmbeddedSystemSimulator

Author: Louis H
Date: 2024-08-04

This module contains unit tests for the EmbeddedSystemSimulator class, including tests for
sending and receiving data.

Modules:
    - pytest: Provides the testing framework.
    - scripts.embeddedSystem: Imports the EmbeddedSystemSimulator class to be tested.

Tests:
    - test_send_data: Verifies that the data sent is one of the expected values.
    - test_receive_data: Verifies that the response received is one of the expected values.
    - test_invalid_send_data: Verifies that the data sent is not an invalid value.
    - test_invalid_receive_data: Verifies that the response received is not an invalid value.
"""

import pytest
from scripts.embeddedSystem import EmbeddedSystemSimulator

@pytest.fixture
def simulator():
    """
    Fixture that provides an instance of EmbeddedSystemSimulator.

    Returns:
        EmbeddedSystemSimulator: An instance of EmbeddedSystemSimulator.
    """
    return EmbeddedSystemSimulator()

def test_send_data(simulator):
    """
    Tests the send_data method of EmbeddedSystemSimulator.

    Args:
        simulator: The EmbeddedSystemSimulator instance provided by the fixture.
    """
    data = simulator.send_data()
    assert data in ['Data1', 'Data2', 'Data3']

def test_receive_data(simulator):
    """
    Tests the receive_data method of EmbeddedSystemSimulator.

    Args:
        simulator: The EmbeddedSystemSimulator instance provided by the fixture.
    """
    response = simulator.receive_data()
    assert response in ['Acknowledge', 'Error', 'Timeout']

def test_invalid_send_data(simulator):
    """
    Tests the send_data method of EmbeddedSystemSimulator for invalid data.

    Args:
        simulator: The EmbeddedSystemSimulator instance provided by the fixture.
    """
    data = simulator.send_data()
    assert data == 'Invalid Data', "Test failed intentionally: data is not 'Invalid Data'"

def test_invalid_receive_data(simulator):
    """
    Tests the receive_data method of EmbeddedSystemSimulator for invalid responses.

    Args:
        simulator: The EmbeddedSystemSimulator instance provided by the fixture.
    """
    response = simulator.receive_data()
    assert response == 'Invalid Response', "Test failed intentionally: response is not 'Invalid Response'"
