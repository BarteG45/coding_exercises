#DESCRIPTION
'''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
'''

#MY SOLUTION
def invert(lst):
    ans = []
    for num in lst:
        ans.append(num*-1)
    return ans