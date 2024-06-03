#DESCRIPTION
'''
Write a program that compares two predefined numbers and prints out whether the first number is greater than, less than, or equal to the second number.
'''

#MY SOLUTION
def compare_numbers(a,b):
  if a==b:
    print("both numbers are equal")
  elif a>b:
    print("a is greater than b")
  elif a<b:
    print("a is lesser than b")
  else:
    print("error")