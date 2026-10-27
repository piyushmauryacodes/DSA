class Animals:
    pass

class Pets:
    pass

class Dog(Animals, Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")



a=Dog()
a.bark()
