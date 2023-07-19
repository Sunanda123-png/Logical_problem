"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]"""


def sum_with_target(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            sum = num[i] + num[j]
            if sum == target:
                return [i, j]


numbers = [2, 7, 11, 15]
target = 9
print(sum_with_target(numbers, target))
