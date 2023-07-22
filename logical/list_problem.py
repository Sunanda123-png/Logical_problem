"""Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst
 can be found in biglst, and in the same order.

Examples:

[4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an
ordered sublist of [3, 2, 1, 2, 3].
Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.

Examples
is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False

is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
Notes
Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst."""


def order_list(list_a, list_b):
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            return False
        return True
    
list_a = [5, 4, 3, 2, 1]
list_b = [1, 2, 3, 4, 5]
print(order_list(list_a,list_b))