#EX. 1 DESCRIPTION
'''Match a Specific Word:
Write a Python program that uses regular expressions to determine if a specific word exists in a given string. Prompt the user to enter a string and then check if the word "hello" is present in it. Print "Match found!" if the word is found, otherwise print "No match found." '''

#EX. 1 SOLUTION
import re
text = input()

patterns=[ r'hello']

for pattern in patterns:
    print(f"Searching for {pattern} in: {text}")

    if re.search(pattern,  text):
        print('Match was found. \n')
    else:
        print('No match was found.\n')

#EX. 2 DESCRIPTION
'''Match Digits:
Write a Python program that uses regular expressions to find and print all the digits in a given string. Prompt the user to enter a string, then print all the digits found in the input string.'''

#EX. 2 SOLUTION
import re
text = input("Provide text: ")

pattern= r"\d+"

digits = re.findall(pattern,text)

print(f"All digits here: {digits}")