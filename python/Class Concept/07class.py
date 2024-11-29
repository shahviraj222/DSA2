# Static Methode = Can not accessable in Instance 
class Car:
    __total_call = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.__total_call += 1 

    def display(self):
        print(self.__brand)
    # here the staticmethode don't take ""self"" we don't required (wiring)  
    @staticmethod
    def get_total_call():
        return Car.__total_call


my_car = Car("Tata","EV")



my_car.__brand = "BMW"     #here new varible is creted for this object 
print(my_car.__brand )     
print(my_car.display())    #The older is saved and we get two entry [ Tata  None ]

print(Car.get_total_call())

