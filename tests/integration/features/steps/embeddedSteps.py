from behave import given, when, then
from scripts.embeddedSystem import EmbeddedSystemSimulator

@given('the embedded system simulator is running')
def step_impl(context):
    context.simulator = EmbeddedSystemSimulator()

@when('I send data from the embedded system')
def step_impl(context):
    context.data_sent = context.simulator.send_data()

@then('the data sent should be one of "Data1", "Data2", "Data3"')
def step_impl(context):
    assert context.data_sent in ['Data1', 'Data2', 'Data3']

@when('I receive data on the embedded system')
def step_impl(context):
    context.data_received = context.simulator.receive_data()

@then('the response should be one of "Acknowledge", "Error", "Timeout"')
def step_impl(context):
    assert context.data_received in ['Acknowledge', 'Error', 'Timeout']
