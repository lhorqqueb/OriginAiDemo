"""
Behavior-Driven Development (BDD) Steps for Embedded System Simulator

Author: Louis H
Date: 2024-08-04

This module defines the steps for testing the EmbeddedSystemSimulator using Behave, a BDD framework.
It includes scenarios for sending and receiving data in the embedded system.

Modules:
    - behave: Provides the BDD framework for defining given/when/then steps.
    - scripts.embeddedSystem: Imports the EmbeddedSystemSimulator class to be tested.

Steps:
    - given: Initializes the embedded system simulator.
    - when: Defines actions for sending and receiving data.
    - then: Verifies the expected outcomes of the actions.
"""

from behave import given, when, then
from scripts.embeddedSystem import EmbeddedSystemSimulator

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
