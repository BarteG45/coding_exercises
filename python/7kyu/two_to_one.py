#DESCRIPTION:
#Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

#Examples:
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

#MY SOLUTION
def longest(a1, a2):
    outcome = ""
    for char in a1:
        if char in outcome:
            pass
        else:
            outcome += char
    for char in a2:
        if char in outcome:
            pass
        else:
            outcome += char
    new_list = []
    for item in outcome:
        new_list.append(item)
    result = sorted(new_list)
    proba = ""
    for item in result:
        proba += item
    return proba