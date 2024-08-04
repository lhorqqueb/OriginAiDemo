import random
import time

class EmbeddedSystemSimulator:
    def __init__(self):
        self.responses = ['Acknowledge', 'Error', 'Timeout']

    def send_data(self):
        data = random.choice(['Data1', 'Data2', 'Data3'])
        print(f"Sending data: {data}")
        return data

    def receive_data(self):
        response = random.choice(self.responses)
        print(f"Received response: {response}")
        return response

    def run(self):
        while True:
            self.send_data()
            time.sleep(5)
            self.receive_data()
            time.sleep(5)

if __name__ == "__main__":
    simulator = EmbeddedSystemSimulator()
    simulator.run()
