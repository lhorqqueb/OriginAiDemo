# Embedded System Simulation Feature File
# 
# Author: Louis H
# Date: 2024-08-04
#
# This feature file describes the scenarios for sending and receiving data using the EmbeddedSystemSimulator.
# It includes scenarios for simulating valid data transmission and reception.
#
# Feature: Describes the high-level behavior of the embedded system simulation.
# Scenario: Defines specific situations and expected outcomes for the simulation.
# Given: Sets up the initial context of the scenario.
# When: Specifies the action to perform.
# Then: Specifies the expected outcome of the action.

Feature: Embedded System Simulation

  Scenario: Send and receive valid data
    Given the embedded system simulator is running
    When I send data from the embedded system
    Then the data sent should be one of "Data1", "Data2", "Data3"
    When I receive data on the embedded system
    Then the response should be one of "Acknowledge", "Error", "Timeout"

  Scenario: Send invalid data (NEG)
    Given the embedded system simulator is running
    When I send data from the embedded system
    Then the data sent should not be "Invalid Data"

  Scenario: Receive invalid response (NEG)
    Given the embedded system simulator is running
    When I receive data on the embedded system
    Then the response should not be "Invalid Response"
