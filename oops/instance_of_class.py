"""Write a Python program to create an instance of a specified class and display the namespace of the said instance."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Person("Ram", 20)
print(obj.__dict__)