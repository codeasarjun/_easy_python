
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} with a {self.battery_capacity}-kWh battery"

my_electric_car = ElectricCar("Tesla", "Model S", 100)

print(my_electric_car.display_info())
