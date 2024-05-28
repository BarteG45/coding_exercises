#EX. 1 DESCRIPTION
'''Count Vowels:
Write a Python function that counts the number of vowels (a, e, i, o, u) in a given string using regular expressions. Prompt the user to enter a string and then print the count of vowels in that string.'''

#EX. 1 SOLUTION
import re
def vowel_count(patterns, phrase):
    vowels = []
    for pattern in patterns:
        vowels += (re.findall(pattern, phrase))
    print (f"The number of vowels in a given string is: {len(vowels)}")

#EX. 2 DESCRIPTION
'''Validate Credit Card Numbers:
Write a Python function that validates if a given string is a valid credit card number using regular expressions. Prompt the user to enter a credit card number and check if it matches any standard credit card number format. Print "Valid credit card number" if it's valid, otherwise print "Invalid credit card number."'''

#EX. 2 SOLUTION
text = input()

pattern=r"[0-9]{12,19}"

if re.search(pattern, text):
        print('Valid credit card number. \n')
else:
        print('Invalid credit card number.\n')