"""Given two arrays of positive integers, add their elements into a new array. The solution should add both arrays,
 one by one starting from the 0'th index, and split the sum into individual digits if it is a 2–digit number.

Input : [23, 5, 2, 7, 87], [4, 67, 2, 8]
Output: [2, 7, 7, 2, 4, 1, 5, 8, 7]

Input : [], [4, 67, 2, 8]
Output: [4, 6, 7, 2, 8]"""

from itertools import zip_longest


def two_array(lst1, lst2):
    result = [x + y for x, y in zip_longest(lst1, lst2, fillvalue=0)]
    return [int(num) for i in result for num in str(i)]



lst1 = [23, 5, 2, 7, 87]
lst2 = [4, 67, 2, 8]
print(two_array(lst1, lst2))
