class Animals:
    name = ""
    sound = ""

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animals):
    name = "Dog"
    sound = "ruff, ruff"


class Cat(Animals):
    name = "Cat"
    sound = "miaow"


tom = Cat()
print(tom.speak())

spike = Dog()
print(spike.speak())
