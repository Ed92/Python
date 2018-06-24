"""
This program will ask the user to make a guess on the sum of a pair of dice. If the user guesses the right sum the user wins, if not, the computer wins.

Author: Erik Djamgarian

"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value is: %d" %max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Sorry, your guess was too high!"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll was: %d" %first_roll
    sleep(1)
    print "The second roll was: %d" %second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is: %d" %total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
      print "Sorry, Computer wins!"



roll_dice(6)
