"""Write a Python program to sum all the items in a dictionary."""

def sum_item(dic):
    sum = 0
    for key, val in dic.items():
        sum += val
    return sum

dic = {'a':2, 'b':5, 'c':8}
print(sum_item(dic))