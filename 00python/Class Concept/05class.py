# Polymorphism  = in hindi one who can take multiple form

class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Use the same function to get sounds from different types of animals
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
