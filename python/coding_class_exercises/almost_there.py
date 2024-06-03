#DESCRIPTION
'''
Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
'''

#MY SOLUTION
def almost_there(n):
    return abs(n) > 89 and abs(n) < 111 or abs(n) > 189 and abs(n) < 211