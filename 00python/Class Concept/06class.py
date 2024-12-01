# accessing the class varible without specifiying the object of the class
class Car:
    total_call = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_call+=1


my_car = Car("Tata","Ev")

my_new_car = Car("BMW","X1")

print("Accessing the variable without calling the object of the class:",Car.total_call)
