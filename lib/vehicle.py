# vehicle.py

class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"  # Default go method for a generic vehicle

    def fill_up_tank(self):
        return "filling up!"  # Method to simulate refueling the vehicle
