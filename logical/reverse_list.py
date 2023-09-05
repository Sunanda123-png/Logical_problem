"""Write a program for reversing list using for loop"""


def reverse_list(arr):
    # l = []
    # for element in range(len(arr)-1, -1, -1):
    #     l.append(arr[element])
    l = arr[::-1]
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


"""reverse a string from midle
input - jaikrishna
output  -  rkiajishna"""


def reverse_from_middle(txt):
    s = ''
    length = len(txt)
    mid = length//2
    first_half = txt[:mid]
    rever = first_half[::-1]
    second_half = txt[mid:]
    result = rever + second_half
    return  result

str = "jaikrishna"
print(reverse_from_middle(str))

