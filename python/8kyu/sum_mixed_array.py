#DESCRIPTION
'''
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
'''

#MY SOLUTION
def sum_mix(arr):
    nums = []
    for char in arr:
        nums.append(int(char))
    return sum(nums)