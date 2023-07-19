"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Input: nums = [2,2,1]
Output: 1


Input: nums = [4,1,2,1,2]
Output: 4"""


def find_single(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num


arr = [2, 2, 1, 3, 3]
print(find_single(arr))


