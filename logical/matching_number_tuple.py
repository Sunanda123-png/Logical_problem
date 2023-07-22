"""Produce a list of tuples consisting of only the matching numbers in these lists
 list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)"""


def matching_number(list_a, list_b):
    result = [(a, b) for a in list_a for b in list_b if a == b]
    return result


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
print(matching_number(list_a, list_b))


