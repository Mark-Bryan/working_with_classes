# class Person:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# class Critter:
#     """A base class for all critter properties"""
#     count = 0
#     def __init__(self, chat) :
#         self.sound = chat
#         Critter.count += 1

#     def talk(self):
#         return self.sound

class Bird:
    """A class to define bird properties"""
    count = 0
    def __init__(self, chat) :
        self.sound = chat
        Bird.count += 1

    def talk(self):
        return self.sound

        
        