# WiFi Sensing Simulation Feature File
# 
# Author: Louis H
# Date: 2024-08-04
#
# This feature file describes the scenarios for simulating WiFi signal and interactions 
# using the WiFiSimulator. It includes scenarios for simulating WiFi signals, movement, 
# and breathing patterns.
#
# Feature: Describes the high-level behavior of the WiFi simulator.
# Scenario: Defines specific situations and expected outcomes for the simulation.
# Given: Sets up the initial context of the scenario.
# When: Specifies the action to perform.
# Then: Specifies the expected outcome of the action.

Feature: WiFi Sensing Simulation

  Scenario: Simulate WiFi signal and interactions
    Given the WiFi simulator is running
    When I simulate a WiFi signal
    Then the signal should be one of "Strong", "Weak", "No Signal"
    When I simulate movement
    Then the movement should be one of "None", "Walking", "Running", "Falling"
    When I simulate breathing
    Then the breathing pattern should be one of "Normal", "Fast", "Slow"
