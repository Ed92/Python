"""

This program will simulate a round of Rock, Paper, Scissor against the user.

Author: Erik Djamgarian

"""

from random import randint

options = ["ROCK", "PAPER", "SCISSOR"]

message = {
  "tie": "Yawn, its a tie!",
  "won": "Nice, you won!",
  "lost": "Sorry, Computer wins!"
}

def decide_winner(user_choice, computer_choice):
  print "Your choice was: %s" % user_choice
  print "The Computer chose: %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]


def play_RPS():
    user_choice = raw_input("Enter Rock, Paper, Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)


play_RPS()
