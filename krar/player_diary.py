import sys,os,random,time
from datetime import datetime

name = ""

typing_speed = 50 #wpm
def slow_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.8/typing_speed)


import os
from time import sleep
#           screen_clear()
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')



def set_date():
  diary = open('diary.txt','a')
  new_entry = datetime.now().strftime('%Y-%m-%d')
  diary.write("\n____________\n\n-" + str(new_entry) +"-\n____________")
  slow_print("\nNew date where set!")
  input("\n>")


def read_diary():
  diary_entrys = open('diary.txt','r')
  slow_print("You open your diary.\n\n")
  print(diary_entrys.read())
  diary_entrys.close()
  input("\n>")

def new_entry_diary():
  diary = open('diary.txt','a')
  print("\nWhat will you write in your diary " + player1.name + ".")
  new_entry = input("\n>")
  diary.write("\n\n- " + str(new_entry))
  slow_print("\nNew entry where archived!")
  input("\n>")

def use_diary():
  screen_clear()
  print("Open dairy from " + player1.name + ".")
  print("\n\nType 'read'     to open your diary.\nType 'Date'     to set a new Date.\nType 'write'   for a new entry.\nType 'close'   to put your diary back in your bag.")
  user_input = input("\n>")
  if "read" in user_input:
    read_diary()
  elif "Date" in user_input:
    set_date()
  elif "write" in user_input:
    new_entry_diary()
  elif "close" in user_input:
    player1.rest()
  else:slow_print("Can't handle your input!\n>")
  use_diary()
  




