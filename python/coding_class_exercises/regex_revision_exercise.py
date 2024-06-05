#DESCRIPTION
'''
Write a regular expression pattern to find all words starting with the letter "a" in the string "An apple a day keeps the doctor away".

Use re.search to check if the string contains the word "doctor".

Use re.findall to find all words starting with the letter "a".

Use re.sub to replace the word "doctor" with "physician".
'''

#MY SOLUTION
import re
text = "An apple a day keeps the doctor away"
pattern= r"\b[Aa]\w*"

if re.search((r"\bdoctor\b"), text):
    print("Doctor found")
else:
    print("No Doctor")

print(re.findall(pattern, text))
print(re.sub(r"\bdoctor\b","physician", text))