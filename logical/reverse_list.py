"""Write a program for reversing list using for loop"""


def reverse_list(arr):
    l = []
    for element in range(len(arr)-1, -1, -1):
        l.append(arr[element])
    return l


arr = [2, 4, 6, 8, 10]
print(reverse_list(arr))


def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def reverse_list(arr):
    result = [arr[x] for x in range(len(arr) - 1, -1, -1)]
    return result



arr = [2, 4, 6, 8, 10]
print(reverse_list(arr))
