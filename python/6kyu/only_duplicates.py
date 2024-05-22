#DESCRIPTION
'''Given a string, remove any characters that are unique from the string.

Example:

input: "abccdefee"

output: "cceee"'''

#MY SOLUTION
def only_duplicates(st):
    answer = list(st)
    final = ""
    for letter in answer:
        if answer.count(letter) > 1:
            final += letter
        else:
            pass
    return final