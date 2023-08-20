"""Given a string containing unique letters, return a sorted string with the letters that don't appear in the string.

Examples:
get_missing_letters("abcdefgpqrstuvwxyz") ➞ "hijklmno"

get_missing_letters("zyxwvutsrq") ➞ "abcdefghijklmnop"

get_missing_letters("abc") ➞ "defghijklmnopqrstuvwxyz"

get_missing_letters("abcdefghijklmnopqrstuvwxyz") ➞ ""

Notes:

The combination of both strings should be 26 elements long, including all the letters in the alphabet.
Letters will all be in lowercase."""


import string
def missing_character(n):
    # lst = []
    a = list(string.ascii_lowercase)
    #
    # print(a)
    # for i in a:
    #     if i not in n:
    #         lst.append(i)
    return "".join([i for i in a if i not in n])

n = "abcdefgpqrstuvwxyz"
print(missing_character(n))

