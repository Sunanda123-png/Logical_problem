# """1. Write a Python program to create a set."""
# s = {1, 2, 3, 4, 5}
# j = {4, 5, 6, 7, 8}
# l = {3, 4, 5}
# # result = s.union(j)
# # result=j.difference(s)
# result = l.issubset(s)
# result = l.f
#
# print(result)
#
# """Write a Python program to create a shallow copy of sets."""
#
# import copy
#
# s = {1, 2, 3, 4, 89}
# sh = copy.copy(s)
# sh.remove(4)
# print(sh)
#
# """remove duplicate and which number you have removed"""
# def remove_duplicate(arr):
#     count_dict = {}
#     li = []
#     highest_count = 0
#     highest_element = []
#     for element in arr:
#         if element in count_dict:
#             count_dict[element] += 1
#         else:
#             count_dict[element] = 1
#             li.append(element)
#     for num, count in count_dict.items():
#         if count>1 and count> highest_count:
#             highest_element.append(num)
#     return highest_element, li
#
# arr = [1,2,2,3,6,6,4,9,9]
# print(remove_duplicate(arr))


"""Write python program to find the maximum and minimum values in a set without inbuilt function"""


def max_min(s):
    max_val = None
    min_val = None
    for element in s:
        if max_val is None and min_val is None:
            max_val = element
            min_val = element
        else:
            if element > max_val:
                max_val = element
            if element < min_val:
                min_val = element
    return max_val, min_val
s = {2,5,7,45,56}
print(max_min(s))
