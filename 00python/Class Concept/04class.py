# Encapuslation  = capsulating the data for the outer world only available for the member of function

# using __ before any variable name 
class Car:
    def __init__(self,brand,model):
        self.__brand = brand               #this is the example of the encapsulation
        self.model = model
    def display(self):
        print(f"Company Name:{self.__brand} \nModel Name:{self.model}\n")

    def get_brand(self):
        return self.__brand

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_electri_car = ElectricCar("BMW","EVS1","5000")        

# print(my_electri_car.__brand)            #not able to access but accessable by the instance of the same class
print(my_electri_car.battery_size)
print(my_electri_car.get_brand())