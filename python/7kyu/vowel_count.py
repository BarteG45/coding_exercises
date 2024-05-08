#DESCRIPTION
'''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''

#MY SOLUTION
def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    v_count = []
    for char in sentence:
        if char in vowels:
            v_count += char
    return len(v_count)