"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Input: n = 2
Output: false"""


def sum_of_squares(n):
    sum_squares = 0
    while n > 0:
        digit = n % 10
        sum_squares += digit * digit
        n //= 10
    return sum_squares

def is_happy(n):
    v = set()
    while n not in v and n != 1:
        v.add(n)
        n = sum_of_squares(n)
    return n == 1


print(is_happy(19))
print(is_happy(2))