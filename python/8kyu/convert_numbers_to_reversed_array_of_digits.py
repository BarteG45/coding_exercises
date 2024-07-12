#DESCRIPTION
'''Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]'''

#MY SOLUTION
def digitize(n):
    x = str(n)
    answer = []
    for char in x:
        answer.append(char)
    integers = []
    for s in answer:
        integers.append(int(s))
    return integers[::-1]