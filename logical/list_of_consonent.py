"""Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled
while eating yuky yams”"""


def consonent(str):
    s = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    result = [element for element in str if element not in s]
    return result


str ="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print(consonent(str))