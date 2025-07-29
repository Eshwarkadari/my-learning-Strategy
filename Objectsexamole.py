
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute
        self.year = year    # Instance attribute

    def display_info(self): # Instance method
        print(f"Car: {self.year} {self.make} {self.model}")

    def age(self, current_year): # Instance method
        return current_year - self.year

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing attributes
print(car1.make)  # Output: Toyota
print(car2.year)  # Output: 2022

# Calling methods
car1.display_info() # Output: Car: 2020 Toyota Camry
car2.display_info() # Output: Car: 2022 Honda Civic

print(f"Car1 is {car1.age(2025)} years old.") # Output: Car1 is 5 years old.
'''

class Dog:
    species = "Canis familiaris" # Class attribute

    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed # Instance attribute

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

print(dog1.species) # Output: Canis familiaris
print(dog2.species) # Output: Canis familiaris
print(Dog.species)
print(dog1.bark())
print(dog2.bark())
