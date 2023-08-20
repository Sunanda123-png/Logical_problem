# def max_num(lst):
#     max_tuple = max(lst, key=lambda x: x[1])
#     max_key, max_value = max_tuple
#     return max_key, max_value
#
#
# lst = [("a", 4), ("b", 6), ("c", 10)]
# print(max_num(lst))


def max_val(lst):
    tuple_sum = lambda x: sum(x)
    print(tuple_sum)
    max_val = max(lst, key=tuple_sum)
    return max_val


lst = [(1, 2), (3, 4), (5, 6)]
print(max_val(lst))
