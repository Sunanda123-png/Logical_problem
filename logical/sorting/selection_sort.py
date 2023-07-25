"""Write a program for selection sort"""
"""In selection sort we have to find smallest value and swap the elemnt to 0th index for ascending order"""


def selection_sort(arr):
    for index in range(len(arr)):
        min_val = min(arr[index:])
        min_ind = arr.index(min_val)
        arr[index], arr[min_ind] = arr[min_ind], arr[index]
    return arr

if __name__ == "__main__":
    print(__name__)
    arr = [56, 27, 13, 1, 87, 23]
    print(selection_sort(arr))
