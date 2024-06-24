#DESCRIPTION
'''
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
'''

#MY SOLUTION
def find_average(numbers):
    if sum(numbers) == 0:
        return 0
    else:
        return sum(numbers)/len(numbers)