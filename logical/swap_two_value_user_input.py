"""Swap Two value as per user input in list"""


def swap_value(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


arr = [10, 5, 8, 3, 0, 2]
pos1 = int(input("Enter the  fast chosen position:- "))
pos2 = int(input("Enter the  second chosen position:- "))
print(swap_value(arr, pos1, pos2))
