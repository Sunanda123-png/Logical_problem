"""2.Given a name, return the letter with the highest index in alphabetical order,
 with its corresponding index, in the form of a string. You are prohibited to use max() nor is 
 reassigning a value to the alphabet list allowed.
Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
 "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"
alphabet_index(alphabet, "Oscar") ➞ "19s"""


def list_problem(alphabet, name):
    highest_letter = ''
    highest_index = -1
    for element in name:
        if element in alphabet:
            ind = alphabet.index(element)
            if ind > highest_index:
                highest_index = ind
                highest_letter = element

    return highest_index+1, highest_letter


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(list_problem(alphabet, "andrey"))
