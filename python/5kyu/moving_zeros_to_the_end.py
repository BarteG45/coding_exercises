#DESCRIPTION
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

#MY SOLUTION
def move_zeros(lst):
    new = []
    zeros = []
    for num in lst:
        if num != 0:
            new.append(num)
        if num == 0:
            zeros.append(num)
    for num in zeros:
        new.append(num)
    return new
            