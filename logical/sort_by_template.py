"""Elavarasu A8:12 AM
The function is given two strings t - template, s - to be sorted. Sort the characters in s such that if the character
 is present in t then it is sorted according to the order in t and other characters are sorted alphabetically after the
  ones found in t.

Examples
custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"

custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"

custom_sort("", "abcdefzyx") ➞ "abcdefxyz"

custom_sort("", "") ➞ ""
Notes
The characters in t and s are all lower-case.
tff-nrsd-edp"""


def template_sort(t, s):
    sorted_s = sorted(s, key=lambda char: (t.index(char) if char in t else len(t), char))
    return ''.join(sorted_s)


print(template_sort("edc", "abcdefzyx"))
