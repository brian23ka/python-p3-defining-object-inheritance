# car.py

from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number, model="Generic Model"):
        # Initialize the parent class with the wheel_size and wheel_number attributes
        super().__init__(wheel_size, wheel_number)
        self.model = model  # Specific attribute for the Car class

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"  # Overridden go method for the car
