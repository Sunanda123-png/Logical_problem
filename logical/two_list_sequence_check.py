"""The goal is to test if a consecutive sequence is formed. A consecutive sequence is defined as sequence of
incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of vectors as
shown.

[3 5 1 -5 ]=> [3+4 5+3 1+8 15-5] = [7 8 9 10] => true
[4 3 8 15]
Also important is that the vectors can be of different sizes, where excess numbers in the longer one will be paired with 0s from the other one.

[2 2 2 ] => [2+5 2+6 2+7 10+0] = [ 7 8 9 10] => true
[5 6 7 10]
Notes
Each array has at least two elements."""


def sequence(lst1, lst2):
    sum_num = [num1 + num2 for num1, num2 in zip(lst1, lst2)]
    for i in range(1, len(sum_num)):
        if abs(sum_num[i] - sum_num[i - 1]) != 1:
            return False
    return True


lst1 = [3, 5, 1, -10]
lst2 = [4, 3, 8, 15]
print(sequence(lst1, lst2))
