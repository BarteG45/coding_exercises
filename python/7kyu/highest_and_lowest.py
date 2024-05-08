#DESCRIPTION
'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.'''

#MY SOLUTION
def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return (f"{(max(nums))} {(min(nums))}")