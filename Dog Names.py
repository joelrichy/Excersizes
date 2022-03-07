class Dog():
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age
        print(name)

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self):
        self.age = age


dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(17)
dog2.change_age(9)

print(dog1.print_details(dog1))
print(dog2.print_details(dog2))