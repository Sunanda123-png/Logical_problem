"""Replacing string latter with another latter in list"""

# def replaceing(arr):
#     result = [element.replace('G', 'o').replace('o', 'G')for element in arr]
#     return result
#
#
# arr = ['Good', 'Morning', 'Guwahati']
# print(replaceing(arr))


"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"""


def reverse_vowel(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l = []
    j = []
    result = []
    for element in s:
        if element in vowels:
            l.append(element)
        else:
            j.append(element)
    l.reverse()
    for x, y in zip(j, l):
        result.append(x)
        result.append(y)
    output = ''.join(result)
    return output




s = "leetcode"
print(reverse_vowel(s))
