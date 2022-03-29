import os
import sys
import time
import random

# Import general-functions

exec(open("general-functions.py").read())


def credits():
	slow_print("\n--------------------------------\n\n###Prototype RPG 'ARENA CITY'###\n\n<Copyright 2022 by Marvin Reese>\n\n--------------------------------\n\nPress 'Return' to go leave the game.\n")
	print(input("\n>"))
	exit()


# Import start-menu
exec(open("start-menu.py").read())


# Import intro
exec(open("intro.py").read())


# Import classes
exec(open("classes/Human.py").read())


# Import weapons
exec(open("weapons.py").read())


# Import Items
exec(open("items.py").read())


# Import chars
exec(open("test-init-characters.py").read())

# Import player_diary
exec(open("player_diary.py").read())

# Import combat-system
exec(open("combat-system.py").read())


# Import dialogs
exec(open("dialogs_felzur.py").read())


# Import world_maps
exec(open("world_maps.py").read())


# Import level-felzur

exec(open("level-felzur.py").read())


# Import level-felzur-pass

exec(open("level-felzur-passage.py").read())


#-------------<Spielaufruf>-----------------#
start_menu()
