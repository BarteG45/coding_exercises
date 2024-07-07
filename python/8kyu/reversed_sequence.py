#DESCRIPTION
'''
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
'''

#MY SOLUTION
def reverse_seq(n):
    x = list(range(1,n+1))
    return x[::-1]