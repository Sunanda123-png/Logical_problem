class Dog:
    def sound(self):
        print("bow bow")
class Cat:
    def sound(self):
        print("Meo Meo")
def makesound(animaltype):
    animaltype.sound()

c = Cat()
d= Dog()
makesound(c)
makesound(d)