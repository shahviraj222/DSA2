# Property Decorator
class Car:
    def __init__(self,brand,model):
        self.__brand = brand               
        self.__model = model

    def display(self):
        print(f"Company Name:{self.__brand} \nModel Name:{self.__model}\n")

    def get_brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = Car("Tata","Curv")

print(my_car.model)