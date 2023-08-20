"""
A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing.
Create a function that takes a list of numbers and returns the length of the longest consecutive-run.
To illustrate:

longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
Examples
longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# Longest consecutive-run: [1, 2, 3].

longest_run([5, 4, 2, 1]) ➞ 2
# Longest consecutive-run: [5, 4] and [2, 1].

longest_run([3, 5, 7, 10, 15]) ➞ 1
"""


def consequtive_run(num):
    current_length = 1
    long_run = 1
    for i in range(1, len(num)):
        if num[i] == num[i - 1] + 1 or num[i] == num[i - 1] - 1:
            current_length += 1
            long_run = max(long_run, current_length)
        else:
            current_length = 1
    return long_run


num = [5, 4, 2, 1]
print(consequtive_run(num))


