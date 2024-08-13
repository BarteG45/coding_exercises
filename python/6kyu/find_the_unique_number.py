#DESCRIPTION
'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
'''

#MY SOLUTION
def find_uniq(arr):
    nums = {}
    for num in arr:
        if num not in nums:
            nums[num] = 1
        else:
            nums[num] +=1
    for key, value in nums.items():
        if value == 1:
            return key