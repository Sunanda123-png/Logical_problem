"""Given a positive number, check if it is a perfect square without using any built-in library function. A perfect square is a number that is the square of an integer.

Input: n = 25
Output: true
Explanation: 25 is a perfect square since it can be written as 5×5.


Input: n = 20
Output: false
Explanation: 20 is not the product of an integer with itself."""


def perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    if root * root == num:
        return True
    return False


num = int(input("Enter the number to check the perfect Square:- "))
print(perfect_square(num))
