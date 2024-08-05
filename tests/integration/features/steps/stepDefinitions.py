"""
Behavior-Driven Development (BDD) Steps for WiFi Signal and Embedded System Simulators

Author: Louis H
Date: 2024-08-04

This module defines the steps for testing the WiFiSimulator and EmbeddedSystemSimulator using Behave, a BDD framework.
It includes scenarios for simulating WiFi signals, movement, breathing patterns, and sending/receiving data in the embedded system.

Modules:
    - behave: Provides the BDD framework for defining given/when/then steps.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.
    - scripts.embeddedSystem: Imports the EmbeddedSystemSimulator class to be tested.

Steps:
    - given: Initializes the simulators.
    - when: Defines actions for simulating signals, movement, breathing, and sending/receiving data.
    - then: Verifies the expected outcomes of the actions.
"""

from behave import given, when, then
from scripts.wifiSimulation import WiFiSimulator
from scripts.embeddedSystem import EmbeddedSystemSimulator

@given('the WiFi simulator is running')
def step_impl(context):
    """
    Initializes the WiFi simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = WiFiSimulator()

@given('the embedded system simulator is running')
def step_impl(context):
    """
    Initializes the embedded system simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = EmbeddedSystemSimulator()

@when('I simulate a WiFi signal')
def step_impl(context):
    """
    Simulates a WiFi signal and stores the result in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.signal = context.simulator.simulate_signal()

@then('the signal should be one of "Strong", "Weak", "No Signal"')
def step_impl(context):
    """
    Verifies that the simulated WiFi signal is one of the expected values.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.signal in ['Strong', 'Weak', 'No Signal']

@then('the signal should not be "invalid signal"')
def step_impl(context):
    """
    Verifies that the simulated WiFi signal is not an invalid value.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.signal != 'invalid signal'

@when('I simulate movement')
def step_impl(context):
    """
    Simulates movement and stores the result in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.movement = context.simulator.simulate_movement()

@then('the movement should be one of "None", "Walking", "Running", "Falling"')
def step_impl(context):
    """
    Verifies that the simulated movement is one of the expected values.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.movement in ['None', 'Walking', 'Running', 'Falling']

@then('the movement should not be "Flying"')
def step_impl(context):
    """
    Verifies that the simulated movement is not an invalid value.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.movement != 'Flying'

@when('I simulate breathing')
def step_impl(context):
    """
    Simulates breathing patterns and stores the result in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.breathing = context.simulator.simulate_breathing()

@then('the breathing pattern should be one of "Normal", "Fast", "Slow"')
def step_impl(context):
    """
    Verifies that the simulated breathing pattern is one of the expected values.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.breathing in ['Normal', 'Fast', 'Slow']

@then('the breathing pattern should not be "Holding Breath"')
def step_impl(context):
    """
    Verifies that the simulated breathing pattern is not an invalid value.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.breathing != 'Holding Breath'

@when('I send data from the embedded system')
def step_impl(context):
    """
    Simulates sending data from the embedded system and stores the data sent in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.data_sent = context.simulator.send_data()

@then('the data sent should be one of "Data1", "Data2", "Data3"')
def step_impl(context):
    """
    Verifies that the data sent is one of the expected values.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.data_sent in ['Data1', 'Data2', 'Data3']

@then('the data sent should not be "Invalid Data"')
def step_impl(context):
    """
    Verifies that the data sent is not an invalid value.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.data_sent != 'Invalid Data'

@when('I receive data on the embedded system')
def step_impl(context):
    """
    Simulates receiving data on the embedded system and stores the response in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.data_received = context.simulator.receive_data()

@then('the response should be one of "Acknowledge", "Error", "Timeout"')
def step_impl(context):
    """
    Verifies that the response received is one of the expected values.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.data_received in ['Acknowledge', 'Error', 'Timeout']

@then('the response should not be "Invalid Response"')
def step_impl(context):
    """
    Verifies that the response received is not an invalid value.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.data_received != 'Invalid Response'
