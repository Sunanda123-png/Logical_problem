class FootbalPlayer:
    def __init__(self,name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is {self.age}year"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} is {self.weight}kg"


player = FootbalPlayer("David Jones", 25, 175, 75)
print(player.get_age())
print(player.get_height())
print(player.get_weight())