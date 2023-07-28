"""Given a text and a pattern, return the index of the first occurrence of pattern in text and return -1 if pattern is not part of text.

Input: text = 'ABCABAABCABAC', pattern = 'ABAA'
Output: 3
Explanation: The pattern occurs only once in the text, starting from index 3.

Input: text = 'ABCABAABCABAC', pattern = 'CAB'
Output: 2
Explanation: The pattern occurs twice in the text, starting from index 2 and 8. The solution should return the index of the first occurrence, i.e., 2."""



def pattern(text, patter):
    if patter not in text:
        return -1
    ind = text.find(patter)
    return ind

text = 'ABCABAABCABAC'
patter = 'CAB'
print(pattern(text, patter))