#EX. 1 DESCRIPTION
'''Match Email Addresses:
Write a Python program that validates if a given string is a valid email address using regular expressions. Prompt the user to enter an email address and check if it matches the standard email format. Print "Valid email address" if it's valid, otherwise print "Invalid email address."'''

#EX. 1 SOLUTION
import re
email = input("Give your email here: ")

pattern= r"^[a-z0-9][\w.+]*@[a-z]+(\.[a-z]{1,4})+$"

valid_email = re.search(pattern, email)

if valid_email:
        print('Valid email address. \n')
else:
        print('Invalid email address.\n')

#EX. 2 DESCRIPTION
'''Match Phone Numbers:
Write a Python program that validates if a given string is a valid phone number using regular expressions. Prompt the user to enter a phone number and check if it matches any standard phone number format. Print "Valid phone number" if it's valid, otherwise print "Invalid phone number."'''

#EX. 2 SOLUTION
import re 
text = input()

pattern=r"^(\+[0-9]{2,3})([0-9]{9})$"

if re.search(pattern, text):
        print('Valid phone number. \n')
else:
        print('Invalid phone number.\n')

#EX. 3 DESCRIPTION
'''Match Dates:
Write a Python program that validates if a given string is a valid date in the format MM/DD/YYYY using regular expressions. Prompt the user to enter a date and check if it matches the specified format. Print "Valid date" if it's valid, otherwise print "Invalid date."'''

#EX. 3 SOLUTION
import re
text = input()

pattern=r"(0?[1-9]|1[0-2])([0-2][1-9]|[12]0|3|01])"

if re.search(pattern, text):
        print('Valid date. \n')
else:
        print('Invalid date.\n')