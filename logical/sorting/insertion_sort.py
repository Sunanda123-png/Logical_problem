"""Write a program for insertion sort"""
"""The insertion sort like we divided list into two part 0th index sort and rest is unsorted. taking element from
unsorted part and compare with sort which is 0th position on first iteration and swap"""

def insertion_sort(arr):
    for element in range(1, len(arr)):
        current_element = arr[element]
        while current_element < arr[element - 1] and element > 0:
            arr[element] = arr[element-1]
            element = element-1
        arr[element] = current_element
    return arr



arr = [31, 2, 22, 56, 1, 7]
print(insertion_sort(arr))
