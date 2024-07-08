#DESCRIPTION
'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''
#MY SOLUTION
def maps(a):
    answer = []
    for num in a:
        answer.append(num*2)
    return answer