import pytest
from scripts.wifiSimulation import WiFiSimulator

@pytest.fixture
def simulator():
    return WiFiSimulator()

def test_signal(simulator):
    signal = simulator.simulate_signal()
    assert signal in ['Strong', 'Weak', 'No Signal']
