#DESCRIPTION
'''
Create a list containing numbers from 1 to 10. Use the map function with a lambda expression to create a new list where each number is squared. Use the filter function with a lambda expression to create a new list containing only even numbers.
'''

#MY SOLUTION
list_of_numbers = list(range(1,11))
squared_numbers = list(map(lambda n: n**2, list_of_numbers))

even_numbers = list(filter(lambda n: n%2 == 0, squared_numbers))