#DESCRIPTION
'''
Write a program that takes a predefined exam score (out of 100) and prints out the grade according to the following criteria:

90 or above: A 
80-89: B 
70-79: C 
60-69: D 
50-59: E
Below 50: F
'''

#MY SOLUTION:
def grade_calculator(percent):
    if percent >= 90:
      return("A")
    elif percent > 80 and percent < 89:
      return("B")
    elif percent > 70 and percent < 79:
      return("C")
    elif percent > 60 and percent < 69:
      return("D")
    elif percent > 50 and percent < 59:
      return("E")
    else:
      return("F")