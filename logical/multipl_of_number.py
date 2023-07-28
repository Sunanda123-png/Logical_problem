"""Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
Notes
Notice that num is also included in the returned list."""


def multiple(num, length):
    # lst = []
    # for element in range(1,length+1):
    #     result = element*num
    #     lst.append(result)
    # return lst
    return [element*num for element in range(1, length+1)]

print(multiple(7, 5))