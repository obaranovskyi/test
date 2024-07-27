class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    def __init__(self, name, age, mammal_type):
        super().__init__(name, age)
        # new updates
        self.mammal_type = mammal_type

    def run(self):
        print(f"{self.name} is running.")

class Bird(Animal):
    def __init__(self, name, age, bird_type):
        super().__init__(name, age)
        # some new updates
        self.bird_type = bird_type

    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def __init__(self, name, age, fish_type):
        super().__init__(name, age)
        # and even more updates
        self.fish_type = fish_type

    def swim(self):
        print(f"{self.name} is swimming.")

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def show_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Age: {animal.age}")

if __name__ == "__main__":
    zoo = Zoo()

    elephant = Mammal("Elephant", 10, "Herbivore")
    eagle = Bird("Eagle", 5, "Carnivore")
    shark = Fish("Shark", 15, "Carnivore")

    zoo.add_animal(elephant)
    zoo.add_animal(eagle)
    zoo.add_animal(shark)

    zoo.show_animals()

    elephant.run()
    eagle.fly()
    shark.swim()

    zoo.remove_animal(eagle)

    zoo.show_animals()
