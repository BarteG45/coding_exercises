#DESCRIPTION
'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

#MY SOLUTION
def find_short(s):
    words_len = []
    for word in s.split():
        words_len.append(len(word))
    return min(words_len)