"""Write a Python program to remove a key from a dictionary."""


def remove_key(dic, k):
    if k in dic:
        del dic[k]
    return dic

dic = {'a':2, 'b':5, 'c':8}
print(remove_key(dic, 'b'))