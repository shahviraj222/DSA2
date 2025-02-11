class Car:
    def __init__(self,brand,model):
      self.__brand = brand
      self.__model = model
      self.name = "viraj"
    def display(self):
        print(f"Brand:{self.__brand}\tModel:{self.__model}",end="\t")

class ElectricCar (Car):
   def __init__(self, brand, model,size):
      super().__init__(brand, model)
      self.__batterySize = size

   def display(self):
      super().display()
      print("Battery Size:",self.__batterySize)   


mynewcar = ElectricCar("BMW","X1",5000)

mynewcar.display()
                       