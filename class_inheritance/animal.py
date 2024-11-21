class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print(f"This is {self.name} and it is a {self.species}")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def describe(self):
        print(f"This is {self.name}, a {self.breed} {self.species}")


class Cat(Animal):
    def __init__(self, name, species, favourite_toy):
        super().__init__(name, species)
        self.favourite_toy = favourite_toy

    def describe(self):
        print(
            f"This is {self.name}, a {self.species} that loves playing with {self.favourite_toy}"
        )


unknown_animal = Animal(name="Unknown", species="Unknown")
unknown_animal.describe()

dog = Dog(name="Buddy", species="Dog", breed="Golden Retriever")
dog.describe()

cat = Cat(name="Whiskers", species="Cat", favourite_toy="Yarn")
cat.describe()
