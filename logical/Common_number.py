"""Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5"""


def common_number(l1, l2):
    result = [element for element in l1 if element in l2]
    return result


l1 = [1, 2, 3, 4]
l2 = [2, 3, 4, 5]
print(common_number(l1,l2))