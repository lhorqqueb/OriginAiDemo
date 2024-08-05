"""
Environmental Simulation

Author: Louis H
Date: 2024-08-04

This module simulates environmental data such as temperature and humidity.
The simulator generates random values for these parameters and prints them to the console.

Modules:
    - random: Provides functions for generating random data.
    - time: Provides time-related functions, used here for delays between simulations.

Classes:
    - EnvironmentalSimulator: A class that simulates temperature and humidity.
"""

import random
import time

class EnvironmentalSimulator:
    """
    A simulator for environmental data such as temperature and humidity.

    Attributes:
        temperatures (list): A list of possible temperature values.
        humidities (list): A list of possible humidity values.
    """

    def __init__(self):
        """
        Initializes the EnvironmentalSimulator with predefined temperatures and humidities.
        """
        self.temperatures = list(range(-10, 41))  # Temperatures from -10 to 40 degrees Celsius
        self.humidities = list(range(0, 101))  # Humidities from 0% to 100%

    def simulate_temperature(self):
        """
        Simulates temperature.

        Returns:
            int: The simulated temperature.
        """
        return random.choice(self.temperatures)

    def simulate_humidity(self):
        """
        Simulates humidity.

        Returns:
            int: The simulated humidity.
        """
        return random.choice(self.humidities)

    def run(self):
        """
        Continuously simulates temperature and humidity with a delay between each simulation.
        """
        while True:
            temperature = self.simulate_temperature()
            humidity = self.simulate_humidity()
            print(f"Simulated temperature: {temperature}°C, Humidity: {humidity}%")
            time.sleep(2)

if __name__ == "__main__":
    # Instantiate and run the environmental simulator
    simulator = EnvironmentalSimulator()
    simulator.run()
