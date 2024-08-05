# Combined Simulation Feature File
# 
# Author: Louis H
# Date: 2024-08-04
#
# This feature file describes the scenarios for evaluating WiFi performance based on combined environmental
# and embedded system factors using the CombinedSimulator.
# It includes scenarios for determining WiFi performance levels (Excellent, Ideal, Optimized, Poor).
#
# Feature: Describes the high-level behavior of the combined simulation.
# Scenario: Defines specific situations and expected outcomes for the simulation.
# Given: Sets up the initial context of the scenario.
# When: Specifies the action to perform.
# Then: Specifies the expected outcome of the action.

Feature: Combined Simulation

  Scenario: Evaluate WiFi performance as Excellent
    Given the combined simulator is running
    When I evaluate performance
    Then the WiFi performance should be "Excellent"

  Scenario: Evaluate WiFi performance as Optimized
    Given the combined simulator is running
    When I evaluate performance
    Then the WiFi performance should be "Optimized"

  Scenario: Evaluate WiFi performance as Poor
    Given the combined simulator is running
    When I evaluate performance
    Then the WiFi performance should be "Poor"

  Scenario: Evaluate WiFi performance as Normal
    Given the combined simulator is running
    When I evaluate performance
    Then the WiFi performance should be "Normal"
