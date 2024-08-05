"""
Embedded System Simulator

Author: Louis H
Date: 2024-08-04

This module simulates an embedded system that sends and receives data. The simulator continuously sends data and
receives responses, mimicking the behavior of a real embedded system.

Usage:
    Run this script directly to start the simulation.

Example:
    python embedded_system_simulator.py

Modules:
    - random: Provides functions for generating random data.
    - time: Provides time-related functions, used here for delays between send/receive actions.

Classes:
    - EmbeddedSystemSimulator: A class that simulates sending and receiving data in an embedded system.
"""

import random
import time

class EmbeddedSystemSimulator:
    """
    A simulator for an embedded system that sends and receives data.

    Attributes:
        responses (list): A list of possible responses from the embedded system.
    """

    def __init__(self):
        """
        Initializes the EmbeddedSystemSimulator with predefined responses.
        """
        self.responses = ['Acknowledge', 'Error', 'Timeout']

    def send_data(self):
        """
        Simulates sending data from the embedded system.

        Returns:
            str: The data sent.
        """
        data = random.choice(['Data1', 'Data2', 'Data3'])
        print(f"Sending data: {data}")
        return data

    def receive_data(self):
        """
        Simulates receiving a response from the embedded system.

        Returns:
            str: The response received.
        """
        response = random.choice(self.responses)
        print(f"Received response: {response}")
        return response

    def run(self):
        """
        Continuously sends and receives data with a delay between each action.
        """
        while True:
            self.send_data()
            time.sleep(5)
            self.receive_data()
            time.sleep(5)

if __name__ == "__main__":
    # Instantiate and run the embedded system simulator
    simulator = EmbeddedSystemSimulator()
    simulator.run()
