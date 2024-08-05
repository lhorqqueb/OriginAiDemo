"""
WiFi Signal and Activity Simulator

Author: Louis H
Date: 2024-08-04

This module simulates various aspects of WiFi sensing technology, including signal strength, movement, and breathing patterns.
The simulator continuously generates random values for these parameters and prints them to the console.

Usage:
    Run this script directly to start the simulation.


Modules:
    - random: Provides functions for generating random data.
    - time: Provides time-related functions, used here for delays between simulations.

Classes:
    - WiFiSimulator: A class that simulates WiFi signal strength, movement, and breathing patterns.
"""

import random
import time

class WiFiSimulator:
    """
    A simulator for WiFi signal strength, movement, and breathing patterns.

    Attributes:
        signals (list): A list of possible WiFi signal strengths.
        movements (list): A list of possible movement types.
        breathing_patterns (list): A list of possible breathing patterns.
    """

    def __init__(self):
        """
        Initializes the WiFiSimulator with predefined signal strengths, movements, and breathing patterns.
        """
        self.signals = ['Strong', 'Weak', 'No Signal']
        self.movements = ['None', 'Walking', 'Running', 'Falling']
        self.breathing_patterns = ['Normal', 'Fast', 'Slow']

    def simulate_signal(self):
        """
        Simulates WiFi signal strength.

        Returns:
            str: The simulated signal strength.
        """
        return random.choice(self.signals)

    def simulate_movement(self):
        """
        Simulates movement.

        Returns:
            str: The simulated movement.
        """
        return random.choice(self.movements)

    def simulate_breathing(self):
        """
        Simulates breathing patterns.

        Returns:
            str: The simulated breathing pattern.
        """
        return random.choice(self.breathing_patterns)

    def run(self):
        """
        Continuously simulates WiFi signal strength, movement, and breathing patterns with a delay between each simulation.
        """
        while True:
            signal = self.simulate_signal()
            movement = self.simulate_movement()
            breathing = self.simulate_breathing()
            print(f"Detected signal: {signal}, Movement: {movement}, Breathing: {breathing}")
            time.sleep(2)

if __name__ == "__main__":
    # Instantiate and run the WiFi simulator
    simulator = WiFiSimulator()
    simulator.run()
