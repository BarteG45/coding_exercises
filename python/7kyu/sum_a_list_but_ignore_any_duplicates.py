#DESCRIPTION
'''
Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list [3, 4, 3, 6] the function should return 10,
and for the list [1, 10, 3, 10, 10] the function should return 4.
'''

#MY SOLUTION
def sum_no_duplicates(l):
    nums = []
    for el in l:
        if el not in nums and l.count(el)==1:
            nums.append(el)
    return sum(nums)