"""
Desc: This is a program that enables users to interact with the calendar through the terminal.

Author: Erik Djamgarian

"""

from time import sleep, strftime

USER_FIRST_NAME = 'Erik'

calendar = {}

def welcome():
  print('Welcome to your Calendar' + ' ' + USER_FIRST_NAME + '!')
  print('Calendar is opening...')
  sleep(1)
  print('today is: ' + strftime("%A %B %D, %Y"))
  print('The time is: ' + strftime("%H:%M:%S"))
  sleep(1)
  print('What would you like to do? ')
 
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input('Press A to add, U to update, V to view, D to delete or X to Exit: ')
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print('Calendar is empty')
      else:
        print(calendar)
    elif user_choice == 'U':
      date = input('What date would you like to update?')
      calendar[date] = update
      print('Update successful!')
      print(calendar)
    elif user_choice == 'A':
      event = input('Enter event: ')
      date = input('Please enter a date (MM/DD/YYYY): ')
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
            print('You have entered an invalid date.')
            try_again = input('Would you like to try again? Y/N')
            if try_again == 'Y':
                continue
            else:
                calendar[date] = event
                print('Event has been successfully added!')
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print('The Calendar is empty.')
      else:
        event = input('What event?')
        for date in calendar.keys():
          if event == calenar[event]:
            del calendar[date]
            print('Event has been deleted!')
            print(calendar)
          else:
            print('Incorrect event specified.')
    elif user_choice == 'X':
      start = False
    else:
      print('Incorrect command.')
      start = False

start_calendar()
