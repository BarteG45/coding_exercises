#DESCRIPTION
'''
Write a program that simulates a guessing game. The program should generate a random number between 1 and 100, and then repeatedly ask the user to guess the number. If the user's guess is too high, it should print "Too high, try again." If the guess is too low, it should print "Too low, try again." If the guess is correct, it should print "Congratulations, you guessed it!" and terminate the program.
'''

#MY SOLUTION
from random import randint
num = randint(1,100)
print('Guess the number between 1 and 100')

while True:
  guess = int(input())
  if guess == num:
    print ('Congratulations, you guessed it!')
    break
  elif guess < num:
    print('Too low, try again')
  elif guess > num:
    print ('Too high, try again')