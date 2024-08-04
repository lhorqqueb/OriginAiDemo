import random
import time

class WiFiSimulator:
    def __init__(self):
        self.signals = ['Strong', 'Weak', 'No Signal']
        self.movements = ['None', 'Walking', 'Running', 'Falling']
        self.breathing_patterns = ['Normal', 'Fast', 'Slow']

    def simulate_signal(self):
        return random.choice(self.signals)

    def simulate_movement(self):
        return random.choice(self.movements)

    def simulate_breathing(self):
        return random.choice(self.breathing_patterns)

    def run(self):
        while True:
            signal = self.simulate_signal()
            movement = self.simulate_movement()
            breathing = self.simulate_breathing()
            print(f"Detected signal: {signal}, Movement: {movement}, Breathing: {breathing}")
            time.sleep(2)

if __name__ == "__main__":
    simulator = WiFiSimulator()
    simulator.run()
