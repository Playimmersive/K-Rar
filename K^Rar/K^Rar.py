import os,sys,time,random

#                                   Import general-functions

exec(open("general-functions.py").read())      


def credits():
  slow_print("\n--------------------------------\n\n###Prototype RPG 'ARENA CITY'###\n\n<Copyright 2022 by Marvin Reese>\n\n--------------------------------\n\nPress 'Return' to go leave the game.\n")
  print(input("\n>"))
  exit()

#                                   Import start-menu
exec(open("start-menu.py").read())


#                                   Import intro
exec(open("intro.py").read()) 



#                                   Import classes
exec(open("classes.py").read())


#                                   Import weapons   
exec(open("weapons.py").read())


#                                   Import shars
exec(open("chars.py").read())


#                                   Import combat-system
exec(open("combat-system.py").read())


#                                   Import level-felzur
exec(open("level-felzur.py").read())



#                                    ---<Spielaufruf>---                            <#
start_menu()


