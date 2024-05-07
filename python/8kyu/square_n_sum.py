#DESCRIPTION
'''Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9.'''

#MY SOLUTION
def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num**2
    return sum

#SECOND SOLUTION
def square_sum(*args):
  sum = 0
  for num in args:
    sum += num**2
  return sum