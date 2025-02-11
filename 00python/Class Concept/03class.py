# Inheritence
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Company Name:{self.brand} \nModel Name:{self.model}")


class ElectricCar (Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def display(self):
        super().display()
        print(f"BatterySize:{self.battery_size}")  


my_electri_car = ElectricCar("BMW","EVS1","5000")        

my_electri_car.display()