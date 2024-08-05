"""
Behavior-Driven Development (BDD) Steps for WiFi Signal, Embedded System, Environmental, and Combined Simulators

Author: Louis H
Date: 2024-08-04

This module defines the steps for testing the WiFiSimulator, EmbeddedSystemSimulator, EnvironmentalSimulator, 
and CombinedSimulator using Behave, a BDD framework. It includes scenarios for simulating WiFi signals, movement, 
breathing patterns, sending/receiving data in the embedded system, and evaluating WiFi performance based on 
combined factors.

Modules:
    - behave: Provides the BDD framework for defining given/when/then steps.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.
    - scripts.embeddedSystem: Imports the EmbeddedSystemSimulator class to be tested.
    - scripts.environmentalSimulation: Imports the EnvironmentalSimulator class to be tested.
    - scripts.combinedSimulation: Imports the CombinedSimulator class to be tested.

Steps:
    - given: Initializes the simulators.
    - when: Defines actions for simulating signals, movement, breathing, sending/receiving data, temperature, humidity, and performance evaluation.
    - then: Verifies the expected outcomes of the actions.
"""

from behave import given, when, then
from scripts.wifiSimulation import WiFiSimulator
from scripts.embeddedSystem import EmbeddedSystemSimulator
from scripts.environmentalSimulation import EnvironmentalSimulator
from scripts.combinedSimulation import CombinedSimulator

# WiFi Simulator Steps
@given('the WiFi simulator is running')
def step_impl(context):
    """
    Initializes the WiFi simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = WiFiSimulator()

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

# Embedded System Simulator Steps
@given('the embedded system simulator is running')
def step_impl(context):
    """
    Initializes the embedded system simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = EmbeddedSystemSimulator()

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

# Environmental Simulator Steps
@given('the environmental simulator is running')
def step_impl(context):
    """
    Initializes the environmental simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = EnvironmentalSimulator()

@when('I simulate temperature')
def step_impl(context):
    """
    Simulates temperature and stores the result in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.temperature = context.simulator.simulate_temperature()

@then('the temperature should be between -10 and 40')
def step_impl(context):
    """
    Verifies that the simulated temperature is within the expected range.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert -10 <= context.temperature <= 40

@then('the temperature should not be between -10 and 40')
def step_impl(context):
    """
    Verifies that the simulated temperature is not within the expected range.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.temperature < -10 or context.temperature > 40, "Test failed intentionally: temperature is within the valid range"

@when('I simulate humidity')
def step_impl(context):
    """
    Simulates humidity and stores the result in the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.humidity = context.simulator.simulate_humidity()

@then('the humidity should be between 0 and 100')
def step_impl(context):
    """
    Verifies that the simulated humidity is within the expected range.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert 0 <= context.humidity <= 100

@then('the humidity should not be between 0 and 100')
def step_impl(context):
    """
    Verifies that the simulated humidity is not within the expected range.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.humidity < 0 or context.humidity > 100, "Test failed intentionally: humidity is within the valid range"

# Combined Simulator Steps
@given('the combined simulator is running')
def step_impl(context):
    """
    Initializes the combined simulator and assigns it to the context.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.simulator = CombinedSimulator()

@when('I evaluate performance')
def step_impl(context):
    """
    Evaluates the WiFi performance based on combined environmental and embedded system factors.

    Args:
        context: Behave context object for sharing data between steps.
    """
    context.performance = context.simulator.evaluate_performance()

@then('the WiFi performance should be "Excellent"')
def step_impl(context):
    """
    Verifies that the WiFi performance is evaluated as "Excellent".

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.performance == 'Excellent'

@then('the WiFi performance should be "Ideal"')
def step_impl(context):
    """
    Verifies that the WiFi performance is evaluated as "Ideal".

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.performance == 'Ideal'

@then('the WiFi performance should be "Optimized"')
def step_impl(context):
    """
    Verifies that the WiFi performance is evaluated as "Optimized".

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.performance == 'Optimized'

@then('the WiFi performance should not be "Poor"')
def step_impl(context):
    """
    Verifies that the WiFi performance is not evaluated as "Poor" and intentionally fails the test if it is.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.performance != 'Poor', "Test failed intentionally: performance is Poor"

@then('the WiFi performance should not be "Normal"')
def step_impl(context):
    """
    Verifies that the WiFi performance is not evaluated as "Normal" and intentionally fails the test if it is.

    Args:
        context: Behave context object for sharing data between steps.
    """
    assert context.performance != 'Normal', "Test failed intentionally: performance is Normal"
