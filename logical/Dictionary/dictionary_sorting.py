"""Write a Python script to sort (ascending and descending) a dictionary by value"""

import operator


def sorting_dictionary(dic):
    s = dict(sorted(dic.items(), key=operator.itemgetter(1)))
    r = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
    return s


dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorting_dictionary(dic))
