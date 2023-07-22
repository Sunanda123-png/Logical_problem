"""Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even,
 and the word 'odd' if the number is odd.  Result would look like ['odd','odd', 'even']"""


def even_odd():
    result = ['even' if element % 2 == 0 else 'odd' for element in range(20)]
    return result


print(even_odd())
