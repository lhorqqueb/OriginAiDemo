"""
Combined Simulation for WiFi, Embedded System, and Environmental Data

Author: Louis H
Date: 2024-08-04

This module simulates the combined effect of environmental and embedded system factors on WiFi performance.
It generates random values for temperature, humidity, and embedded system responses, then evaluates WiFi performance.

Modules:
    - random: Provides functions for generating random data.
    - time: Provides time-related functions, used here for delays between simulations.
    - WiFiSimulator: Imports the WiFiSimulator class to simulate WiFi signals.
    - EmbeddedSystemSimulator: Imports the EmbeddedSystemSimulator class to simulate embedded system interactions.
    - EnvironmentalSimulator: Imports the EnvironmentalSimulator class to simulate temperature and humidity.
"""

import random
import time
from scripts.wifiSimulation import WiFiSimulator
from scripts.embeddedSystem import EmbeddedSystemSimulator
from scripts.environmentalSimulation import EnvironmentalSimulator

class CombinedSimulator:
    """
    A simulator that evaluates WiFi performance based on environmental and embedded system factors.

    Attributes:
        wifi_simulator (WiFiSimulator): An instance of WiFiSimulator.
        embedded_simulator (EmbeddedSystemSimulator): An instance of EmbeddedSystemSimulator.
        environmental_simulator (EnvironmentalSimulator): An instance of EnvironmentalSimulator.
    """

    def __init__(self):
        """
        Initializes the CombinedSimulator with instances of WiFiSimulator, EmbeddedSystemSimulator, and EnvironmentalSimulator.
        """
        self.wifi_simulator = WiFiSimulator()
        self.embedded_simulator = EmbeddedSystemSimulator()
        self.environmental_simulator = EnvironmentalSimulator()

    def evaluate_performance(self):
        """
        Evaluates WiFi performance based on combined factors of temperature, humidity, and embedded system response.

        Returns:
            str: The evaluated WiFi performance level (Excellent, Ideal, Optimized, Poor).
        """
        temperature = self.environmental_simulator.simulate_temperature()
        humidity = self.environmental_simulator.simulate_humidity()
        embedded_response = self.embedded_simulator.receive_data()
        signal = self.wifi_simulator.simulate_signal()

        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Embedded Response: {embedded_response}, WiFi Signal: {signal}")

        if signal == 'Strong' and 20 <= temperature <= 30 and 30 <= humidity <= 60 and embedded_response == 'Acknowledge':
            return 'Excellent'
        elif signal in ['Strong', 'Weak'] and 10 <= temperature <= 35 and 20 <= humidity <= 70 and embedded_response in ['Acknowledge', 'Timeout']:
            return 'Ideal'
        elif signal in ['Strong', 'Weak'] and -10 <= temperature <= 40 and 0 <= humidity <= 100:
            return 'Optimized'
        else:
            return 'Poor'

    def run(self):
        """
        Continuously evaluates WiFi performance with random delays between simulations.
        """
        while True:
            performance = self.evaluate_performance()
            print(f"WiFi Performance: {performance}")
            time.sleep(2)

if __name__ == "__main__":
    # Instantiate and run the combined simulator
    simulator = CombinedSimulator()
    simulator.run()
