"""Given a list of people objects, create a function that sorts the list by an attribute name.
The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

firstname
lastname
age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40"""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


def people_sort(people, attribute):
    if not people:
        return []

    def get_attribute(person):
        return getattr(person, attribute)

    sorted_people = sorted(people, key=get_attribute)
    sorted_attribute_values = [get_attribute(person) for person in sorted_people]
    return sorted_attribute_values


p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

print(people_sort([p1, p2, p3], "firstname"))
print(people_sort([p1, p2, p3], "lastname"))
print(people_sort([p1, p2, p3], "age"))
