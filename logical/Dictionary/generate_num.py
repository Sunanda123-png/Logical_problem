"""Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x). Sample Dictionary ( n = 5)"""


def generate_dic(n):
    dic = {}
    for x in range(1,n+1):
        dic[x] = x*x
    return dic
print(generate_dic(6))