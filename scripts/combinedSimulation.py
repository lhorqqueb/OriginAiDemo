import random
import time
from scripts.wifiSimulation import WiFiSimulator
from scripts.embeddedSystem import EmbeddedSystemSimulator
from scripts.environmentalSimulation import EnvironmentalSimulator

class CombinedSimulator:
    """
    CombinedSimulator evaluates WiFi performance based on the combination of environmental factors, 
    embedded system responses, and simulated WiFi signal strength.

    Attributes:
        wifi_simulator (WiFiSimulator): An instance of WiFiSimulator to simulate WiFi signals and movement.
        embedded_simulator (EmbeddedSystemSimulator): An instance of EmbeddedSystemSimulator to simulate 
                                                     sending and receiving data.
        environmental_simulator (EnvironmentalSimulator): An instance of EnvironmentalSimulator to simulate 
                                                         environmental factors like temperature and humidity.
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
        Evaluates the WiFi performance based on combined environmental and embedded system factors.

        Simulates temperature, humidity, embedded system responses, WiFi signal strength, and movement, then
        evaluates the performance as 'Excellent', 'Ideal', 'Optimized', or 'Poor' based on predefined thresholds.

        Returns:
            str: The evaluated WiFi performance level ('Excellent', 'Ideal', 'Optimized', 'Poor').
        """
        temperature = self.environmental_simulator.simulate_temperature()
        humidity = self.environmental_simulator.simulate_humidity()
        embedded_response = self.embedded_simulator.receive_data()
        signal = self.wifi_simulator.simulate_signal()
        movement = self.wifi_simulator.simulate_movement()

        print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Embedded Response: {embedded_response}, WiFi Signal: {signal}, Movement: {movement}")

        if signal == 'Strong' and 20 <= temperature <= 30 and 30 <= humidity <= 60 and embedded_response == 'Acknowledge' and movement == 'None':
            return 'Excellent'
        elif signal in ['Strong', 'Weak'] and 10 <= temperature <= 35 and 20 <= humidity <= 70 and embedded_response in ['Acknowledge', 'Timeout'] and movement in ['None', 'Walking']:
            return 'Ideal'
        elif signal in ['Strong', 'Weak'] and -10 <= temperature <= 40 and 0 <= humidity <= 100 and movement in ['None', 'Walking', 'Running']:
            return 'Optimized'
        else:
            return 'Poor'

    def run(self):
        """
        Continuously evaluates and prints WiFi performance at regular intervals.
        
        Runs an infinite loop that calls the evaluate_performance method every 2 seconds and prints the performance level.
        """
        while True:
            performance = self.evaluate_performance()
            print(f"WiFi Performance: {performance}")
            time.sleep(2)

if __name__ == "__main__":
    # Instantiate and run the CombinedSimulator
    simulator = CombinedSimulator()
    simulator.run()
