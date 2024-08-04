from behave import given, when, then
from scripts.wifiSimulation import WiFiSimulator

@given('the WiFi simulator is running')
def step_impl(context):
    context.simulator = WiFiSimulator()

@when('I simulate a WiFi signal')
def step_impl(context):
    context.signal = context.simulator.simulate_signal()

@then('the signal should be one of "Strong", "Weak", "No Signal"')
def step_impl(context):
    assert context.signal in ['Strong', 'Weak', 'No Signal']

@when('I simulate movement')
def step_impl(context):
    context.movement = context.simulator.simulate_movement()

@then('the movement should be one of "None", "Walking", "Running", "Falling"')
def step_impl(context):
    assert context.movement in ['None', 'Walking', 'Running', 'Falling']

@when('I simulate breathing')
def step_impl(context):
    context.breathing = context.simulator.simulate_breathing()

@then('the breathing pattern should be one of "Normal", "Fast", "Slow"')
def step_impl(context):
    assert context.breathing in ['Normal', 'Fast', 'Slow']
