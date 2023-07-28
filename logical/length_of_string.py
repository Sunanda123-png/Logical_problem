"""Run–length encoding (RLE) is a simple form of lossless data compression that runs on sequences with the
 same value occurring many consecutive times. It encodes the sequence to store only a single value and its count.

Input: 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
Output: '12W1B12W3B24W1B14W'
Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and so on."""


def string_count(text):
    s = ""
    current_latter = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_latter:
            count += 1
        else:
            s += str(count) + current_latter
            count = 1
            current_latter = text[i]
    s += str(count) + current_latter

    return s


w = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(string_count(w))
