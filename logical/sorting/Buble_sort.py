"""Write program for buble sort"""


def buble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [2, 56, 27, 15, 7]
print(buble_sort(arr))
