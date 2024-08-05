# WiFi Simulation Feature File
# 
# Author: Louis H
# Date: 2024-08-04
#
# This feature file describes the scenarios for simulating WiFi signals, movement, and breathing patterns using the WiFiSimulator.
# It includes scenarios for simulating valid and invalid values for each parameter.
#
# Feature: Describes the high-level behavior of the WiFi simulation.
# Scenario: Defines specific situations and expected outcomes for the simulation.
# Given: Sets up the initial context of the scenario.
# When: Specifies the action to perform.
# Then: Specifies the expected outcome of the action.

Feature: WiFi Simulation

  Scenario: Simulate strong WiFi signal
    Given the WiFi simulator is running
    When I simulate a WiFi signal
    Then the signal should be one of "Strong", "Weak", "No Signal"

  Scenario: Simulate invalid WiFi signal (NEG)
    Given the WiFi simulator is running
    When I simulate a WiFi signal
    Then the signal should not be "invalid signal"

  Scenario: Simulate walking movement
    Given the WiFi simulator is running
    When I simulate movement
    Then the movement should be one of "None", "Walking", "Running", "Falling"

  Scenario: Simulate invalid movement (NEG)
    Given the WiFi simulator is running
    When I simulate movement
    Then the movement should not be "Flying"

  Scenario: Simulate normal breathing pattern
    Given the WiFi simulator is running
    When I simulate breathing
    Then the breathing pattern should be one of "Normal", "Fast", "Slow"

  Scenario: Simulate invalid breathing pattern (NEG)
    Given the WiFi simulator is running
    When I simulate breathing
    Then the breathing pattern should not be "Holding Breath"
