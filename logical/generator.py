"""Write a function for getting even number limit will be passing by user"""


def even_number(limit):
    num = 0
    while num <= limit:
        yield num
        num +=2

limit= 20
generator = even_number(limit)
for i in generator:
    print(i)