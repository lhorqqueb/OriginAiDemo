import pytest
from scripts.wifiSimulation import WiFiSimulator

@pytest.fixture
def simulator():
    return WiFiSimulator()

def test_breathing(simulator):
    breathing = simulator.simulate_breathing()
    assert breathing in ['Normal', 'Fast', 'Slow']
