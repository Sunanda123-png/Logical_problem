"""Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3,
 which will be initialised with the attributes name and age, return a sentence in the following format:

{other_person} is {older than / younger than / the same age as} me.

Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2) ➞ "Joel is older than me."

p2.compare_age(p1) ➞ "Samuel is younger than me."

p1.compare_age(p3) ➞ "Lily is the same age as me."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age > other_person.age:
            return f'{other_person.name} is younger than me'
        elif self.age < other_person.age:
            return f'{other_person.name} is older than me'
        else:
            return f'{other_person.name} is same as me'


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))
print(p1.compare_age(p3))