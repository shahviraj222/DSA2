class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Company Name:{self.brand} \nModel Name:{self.model}\n")

my_car = Car("BMW","X1")        
my_car.display()

my_new_car = Car("TATA","CURVEV")        
my_new_car.display()
