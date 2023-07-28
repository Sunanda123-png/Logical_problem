"""Inheritance and multilevel inheritance"""

class Person:
    def worker(self):
        print("worker is working")
class Employee(Person):
    def sector(self):
        print("It sector is growing")
class Programmer(Employee):
    def coder(self):
        print("coder maintaining the code")

p = Programmer()
p.worker()
p.sector()
p.coder()