# Environmental Simulation Feature File
# 
# Author: Louis H
# Date: 2024-08-04
#
# This feature file describes the scenarios for simulating environmental data using the EnvironmentalSimulator.
# It includes scenarios for simulating valid and invalid values for temperature and humidity.
#
# Feature: Describes the high-level behavior of the environmental simulation.
# Scenario: Defines specific situations and expected outcomes for the simulation.
# Given: Sets up the initial context of the scenario.
# When: Specifies the action to perform.
# Then: Specifies the expected outcome of the action.

Feature: Environmental Simulation

  Scenario: Simulate valid temperature
    Given the environmental simulator is running
    When I simulate temperature
    Then the temperature should be between -10 and 40

  Scenario: Simulate invalid temperature (NEG)
    Given the environmental simulator is running
    When I simulate temperature
    Then the temperature should not be between -10 and 40

  Scenario: Simulate valid humidity
    Given the environmental simulator is running
    When I simulate humidity
    Then the humidity should be between 0 and 100

  Scenario: Simulate invalid humidity (NEG)
    Given the environmental simulator is running
    When I simulate humidity
    Then the humidity should not be between 0 and 100
