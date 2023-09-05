"""Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would
look like (index, value), (index, value)"""


def get_index_and_value(arr):
    result = [(index, value) for index, value in enumerate(arr)]
    # result = {index: value for index, value in enumerate(arr)}
    return result


l = ["hi", 4, 8.99, "apple", ('t', 'b', 'n')]
print(get_index_and_value(l))
