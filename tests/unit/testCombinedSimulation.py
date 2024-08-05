import pytest
from scripts.combinedSimulation import CombinedSimulator

@pytest.fixture
def simulator():
    """
    Fixture to create an instance of CombinedSimulator.
    
    Returns:
        CombinedSimulator: An instance of CombinedSimulator.
    """
    return CombinedSimulator()

def test_evaluate_performance(simulator):
    """
    Tests the evaluate_performance method of CombinedSimulator for various scenarios.

    Ensures the performance is either 'Optimized' or 'Excellent', otherwise the test fails.

    Args:
        simulator (CombinedSimulator): The CombinedSimulator instance provided by the fixture.
    """
    performance = simulator.evaluate_performance()
    print(f"Evaluated Performance: {performance}")
    assert performance in ['Optimized', 'Excellent'], f"Test failed: Performance is {performance}"
