"""count the space in string"""


def count_space(str):
    result = [element for element in str if element == ' ']
    return len(result)


str = "India is my Country"
print(count_space(str))
