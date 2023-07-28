"""Write a program for method overridding"""

class A:
    def display(self):
        print("This is class based A method")

class B(A):
    def display(self):
        print("this is calss based B method")

b = B()
b.display()