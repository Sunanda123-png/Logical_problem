"""Sample program for multiple inheritance"""


class LandAnimal:
    def printing(self):
        print("This is land based animal")


class WaterAnimal:
    def display(self):
        print("This is water based animal")


class Frog(LandAnimal, WaterAnimal):
    #
    pass

f = Frog()
f.display()
f.printing()

