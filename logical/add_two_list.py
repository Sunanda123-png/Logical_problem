"""Add two list
"""
from itertools import zip_longest

def add_two_list(lst1, lst2):
    result = [x+y for x in zip_longest]
    lst = []
    min_length = min(len(lst1), len(lst2))
    for i in range(min_length):
        lst.append(lst1[i]+ lst2[i])
    if len(lst1) > len(lst2):
        lst.extend(lst1[min_length:])
    else:
        lst.extend(lst2[min_length:])
    return lst
    # for i in range(len(lst1)):
    #     lst.append(lst1[i]+lst2[i])
    # return lst


lst1 = [4, 5, 6, 34]
lst2 = [1, 2, 3]
print(add_two_list(lst1,lst2))