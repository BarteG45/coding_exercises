#DESCRIPTION
'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''

#MY SOLUTION
def remove_exclamation_marks(s):
    exc = "!"
    answer = ""
    for char in s:
        if char not in exc:
            answer += char
    return answer