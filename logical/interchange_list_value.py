"""Interchange the first value and last value in list"""

def interchange(arr):
    size = len(arr)
    temp = arr[0]
    arr[0] = arr[size-1]
    arr[size-1] = temp
    return arr



arr = [10, 20, 30, 40]
print(interchange(arr))

