"""Given an array nums of size n, return the majority element.
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""


def major_duplicate(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    highest_duplicate = None
    highest_count = 0

    for num, count in count_dict.items():
        if count > 1 and count > highest_count:
            highest_duplicate = num
            highest_count = count
    return highest_duplicate


arr = [2, 2, 1, 1, 1, 2, 2]
print(major_duplicate(arr))
