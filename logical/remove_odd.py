"""Given a list of numbers, remove all odd numbers from the list"""


def remove_odd(arr):
    result = [element for element in arr if element % 2 == 0]
    return result


arr = [1, 2, 3, 4, 5, 6, 7]
print(remove_odd(arr))
