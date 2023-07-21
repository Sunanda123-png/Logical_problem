"""size of tuple in bytes"""
import sys


def tup_size(tup):
    result = sys.getsizeof(tup)
    return result


tup = (1, 'hello', 3.14, [1, 2, 3])
print(tup_size(tup))
