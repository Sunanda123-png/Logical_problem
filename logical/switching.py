"""
[1,2,3,4,5,6,7,8] then output [ 3,4,1,2,7,8,5,6]
"""


def switching(lst):
    new_list = []
    for i in range(0, len(lst), 4):
        new_list.extend(lst[i + 2:i + 4])
        new_list.extend(lst[i:i + 2])
    return new_list


input_list = [1,8, 30, 4, 45, 6, 7, 8,9]
new_lst = switching(input_list)
print(new_lst)


