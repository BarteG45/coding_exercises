#DESCRIPTION
'''Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"'''

#MY SOLUTION
def odd_or_even(arr):
    sum = 0
    for num in arr:
        sum+=num
    if sum%2==0:
        return ("even")
    else:
        return("odd")