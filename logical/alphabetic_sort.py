"""
Create a function which takes every letter in every word, and puts it in alphabetical order. Note how the original word
 lengths must stay the same.

Examples
true_alphabetic("hello world") ➞ "dehll loorw"

true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"

true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"
Notes
All sentences will be in lowercase.
No punctuation or numbers will be included in the Tests."""


def alpha_sort(sentence):
    words = sentence.split()
    print(words)
    sorted_words = []
    output_str = sentence.replace(" ", "")
    print(output_str)
    sorted_sen = "".join(sorted(output_str))
    for word in words:
        len_word = len(word)
        print(len_word)
        separate_word = sorted_sen[len_word:]
        sorted_words.append(separate_word)
    return sorted_words




    # word_count = len(sentence.split())
    # print(word_count)
    # output_str = sentence.replace(" ", "")
    # sorted_str = ''.join(sorted(output_str))

    # half_length = len(sorted_str) // word_count
    # word1 = sorted_str[:half_length]
    # word2 = sorted_str[half_length:]

    # sorted_words.append(word1)
    # sorted_words.append(word2)
    # parts = [sorted_str[i:i + word_count] for i in range(0, len(sorted_str), word_count)]

    # result = ' '.join(parts)

    # return result

    # for word in words:
    #     word_length = len(word)

    #
    #     sorted_word = ''.join(sorted(word))
    #     print(sorted_word)
    #     sorted_words.append(sorted_word)
    #
    # result = ' '.join(sorted_words)
    # return result

sentence = "edabit is awesome"
print(alpha_sort(sentence))
