import pytest
from scripts.wifiSimulation import WiFiSimulator

@pytest.fixture
def simulator():
    return WiFiSimulator()

def test_movement(simulator):
    movement = simulator.simulate_movement()
    assert movement in ['None', 'Walking', 'Running', 'Falling']
