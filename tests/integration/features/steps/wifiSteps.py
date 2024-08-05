"""
Behavior-Driven Development (BDD) Steps for WiFi Signal Simulator

Author: Louis H
Date: 2024-08-04

This module defines the steps for testing the WiFiSimulator using Behave, a BDD framework.
It includes scenarios for simulating WiFi signals, movement, and breathing patterns.

Modules:
    - behave: Provides the BDD framework for defining given/when/then steps.
    - scripts.wifiSimulation: Imports the WiFiSimulator class to be tested.

Steps:
    - given: Initializes the WiFi simulator.
    - when: Defines actions for simulating signals, movement, and breathing.
    - then: Verifies the expected outcomes of the actions.
"""

from behave import given, when, then
from scripts.wifiSimulation import WiFiSimulator

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
