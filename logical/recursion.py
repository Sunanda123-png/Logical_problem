"""Write a program for factorial numbers and input as per user wish"""


def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)

n= 10
print(fact(n))