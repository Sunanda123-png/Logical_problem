"""Create an identical list from the first list using list comprehension."""


def identical_list(arr):
    result = [element for element in l]
    return result


l= [2,3,4,5,6]
print(identical_list(l))
