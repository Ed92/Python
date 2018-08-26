class Dog():
    
    def __init__(self, breed, age, height, weight):
        self.breed = breed
        self.age = age
        self.height = height
        self.weight = weight

my_dog = Dog("Bulldog", 12, 123, 70)

print(my_dog.breed)
print(my_dog.age)
print(my_dog.height)
