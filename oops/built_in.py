"""builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module, displays the documentation of
the abs() function and finds the absolute value of -155."""

import builtins


class Built:

    def __init__(self):
        self.value = -115

    def find_value(self):
        return builtins.abs(self.value)
        # print(builtins.abs(-155))


obj = Built()
print(obj.find_value())
