Feature: WiFi Sensing Simulation

  Scenario: Simulate WiFi signal and interactions
    Given the WiFi simulator is running
    When I simulate a WiFi signal
    Then the signal should be one of "Strong", "Weak", "No Signal"
    When I simulate movement
    Then the movement should be one of "None", "Walking", "Running", "Falling"
    When I simulate breathing
    Then the breathing pattern should be one of "Normal", "Fast", "Slow"
