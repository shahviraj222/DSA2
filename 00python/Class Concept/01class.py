class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


my_car = Car("BMW","X1")        
print(my_car.brand,my_car.model)

my_new_car = Car("TATA","CURVEV")        
print(my_new_car.brand,my_new_car.model)


a =  213.23423423
print(f"{a:.2f}")