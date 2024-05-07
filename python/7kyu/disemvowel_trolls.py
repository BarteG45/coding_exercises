#DESCRIPTION
'''Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.'''

#MY SOLUTION
def disemvowel(string_):
    removed_vowels = ""
    for letter in string_:
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u" and letter != "A" and letter != "O" and letter != "U" and letter != "I" and letter != "E":
            removed_vowels += letter
    return removed_vowels