"""
Create a function that takes a string and returns a string ordered by the length of the words. From shortest to longest
 word. If there are words with the same amount of letters, order them alphabetically.

Examples
sort_by_length("Hello my friend") ➞ "my Hello friend"

sort_by_length("Have a wonderful day") ➞ "a day Have wonderful"

sort_by_length("My son loves pineapples") ➞ "My son loves pineapples"
"""


def sort_word(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=lambda word: (len(word), word))
    return ' '.join(sorted_words)


print(sort_word("have a nice day"))
