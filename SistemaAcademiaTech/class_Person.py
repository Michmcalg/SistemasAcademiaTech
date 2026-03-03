#Class variables, Inheritance, Multiple inheritance, super(), Polymorphism

from abc import abstractmethod


class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod 
    def Introduction(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        


class online_acess():
    pass

