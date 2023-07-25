"""Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981"""


def rearrange(num):
    num_str = str(num)
    min_value = int(''.join(sorted(num_str)))
    max_value = int(''.join(sorted(num_str, reverse=True)))
    difference = max_value - min_value
    return difference

num = 972882
print(rearrange(num))