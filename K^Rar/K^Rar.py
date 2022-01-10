import os,sys,time,random


typing_speed = 50 #wpm
def slow_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2/typing_speed)




def this_location():
    if player1.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      felzur_city_alley()
    elif player1.location == felzur_city_bar:
      felzur_city_bar()

    elif player1.location == felzur_city_place_shack_01:
      felzur_city_place_shack_01()
    elif player1.location == felzur_city_place_stonebuilding_01:
      felzur_city_place_stonbuilding_01()
    elif player1.location == felzur_city_place_coluseum:
      felzur_city_place_coluseum()
    else: felzur_city_place()



###                             Start Menu                          ###

def start_menu():
  slow_print("\n###              This is a Playimmersive production.          ###\n\n\n\n###               Welcome to the world of K^Rar.              ###\n###               A world on the edge of the end!             ###\n\nAre you sure you want to enter this place?\n")
  player1.health = 150
  player1.hunger = 51
  player1.thirst = 43
  player1.strenght = 1
  player1.agility = 1
  player1.weapon = sword
  player1.max_health = 150
  player1.gold = 13
  player1.alive = True
  player_input = (input("\nPress 'yes' to enter.\nPress 'no' to leave.\n\n>"))
  if "yes" in player_input:
    slow_print ("\nYou enter the world of K^Rar!\n")
    player1.location = felzur_city_player_home
    player1.race = "Human"
    slow_print("\nFrom where are you?\n")
    player_input = input("Type 'felzur' to select Felzur as homecity.\n>")
    if "felzur" in player_input:
      slow_print("You are from Felzur, it´s a cold place sourroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.")
      player1.nativity = "Felzur"
      slow_print("\nWhat´s your name?\n")
      player1.name = input(">")
    
      slow_print("\nHow old are you?\n>")
      player1.age = input(">")

      intro()
      
    else:print("\n---------------\nComming soon!\n---------------\n")
    slow_print("You are from Felzur, it´s a cold place surroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.\n")
    player1.nativity = "Felzur"
    
    slow_print("\nWhat´s your name?\n")
    player1.name = input(">")
    
    slow_print("\nHow old are you?\n>")
    player1.age = input(">")
    
    intro()
    
    
  elif "no" in player_input:
    slow_print ("\nYou leave this unholy place!\n\n")
    exit()

  else:print("Can´t handle your input!\n>")
  start_menu()

def intro():
  print("\n" *50)
  slow_print("\n" + player1.name + " wokes up in a tiny room.\nIt´s cold inside and the air is full of dust!\nAfter a while " + player1.name + " is able to move his head, everything hurts!\n" + player1.name + " feels hungry and thirsty.\nThere is a dagger sticking into a little cupboard and a bag with 10 gold benith it.\n" + player1.name + " takes everything!\n\n--------------------------------\n")
  felzur_city_player_home()

###                             Class Human                         ###

class human:
  def __init__(hero, location, race, nativity, citizen, name, age, health, max_health, hunger, thirst, strenght, agility, weapon, gold, fur, medics, meals, water, alive):
    hero.location = location
    hero.race = race
    hero.nativity = nativity
    hero.citizen = citizen
    hero.name = name
    hero.age =age
    hero.health = health
    hero.max_health = max_health
    hero.hunger = hunger
    hero.thirst = thirst
    hero.strenght = strenght
    hero.agility = agility
    hero.weapon = weapon
    hero.gold = gold
    hero.fur = fur
    hero.medics = medics
    hero.meals = meals
    hero.water = water    
    hero.alive = alive


###                         Functions Human                   ###


  def show_hitpoints(player):
    hitpoints = player.strenght * player.weapon[0]
    slow_print("Hitpoints current weapon: " + str(hitpoints) + "\n")
    this_location()


  def rest(player):
    slow_print("\nYou take a break.\n")
    player_input = (input("\nType 'sleep' to sleep a while.\nType 'status' for your status.\nType 'move' to go further.\nType 'medics' to take some medics.\n\nType 'quit' to go back to the start menu.\n\n>"))
    if "sleep" in player_input:
      player1.sleep()

    elif "status" in player_input:
      player1.status()
    elif "move" in player_input:
      this_location()
    elif "medics" in player_input:
      player1.use_medics()
    elif "quit" in player_input:
      start_menu()

    else:print("Can´t handle your input!")
    this_location() 

###                         rest                              ###


  def sleep(player):
    
    if player.health <=  player.max_health - 100:
      slow_print("You take a break!\n")
      player.health = player.health + 100
      player.hunger = player.hunger - 8
      player.thirst = player.thirst - 11
      if player.hunger < 1:
        slow_print(player.name + " starved to death!\nTry to get some food the next time.\n")
        credits()
      if player.thirst <= 1:
        slow_print(player.name + " died of thirst!\nTry to get something to drink the next time.\n")
        credits()
      else:this_location()
        

    elif player.health == player.max_health:
      slow_print(player.name + " dont need a break.\n\n")
      if player.location == felzur_city_player_home:
        felzur_city_player_home() 
      elif player.location == felzur_city_alley:
        felzur_city_alley()
      else: felzur_city_place()

    else: player.health = player.max_health
    slow_print("You take a break!\n")
    player.hunger = player.hunger - 4
    player.thirst = player.thirst - 6
    if player.hunger < 1:
        slow_print(player.name + " starved to death!\nTry to get some food the next time.\n")
        credits()
    if player.thirst <= 1:
        slow_print(player.name + " died of thirst!\nTry to get something to drink the next time.\n")
        credits()
    if player.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player.location == felzur_city_alley:
      felzur_city_alley()
    else:felzur_city_place()

### Use Medics

  def use_medics(player):
    if player.health == player.max_health:
      slow_print("You dont need medics")
      this_location()
    elif player.medics > 0:
      slow_print(player.name + " takes some healing herbs.")
      player.health = min(player.max_health, player.health + 100)
      player.medics = player.medics -1
    else:print("You dont have anything to heal.")
    this_location()


  def status(player):
    slow_print("\n" + player.name + "´s Health is at " + str(player.health) + "/" + str(player.max_health) + " points.\nThere are " + str(player.gold) + " gold pieces in the bag.\n")
    slow_print(player.name + "´s hunger is at " + str(player.hunger) + " points.\n")
    slow_print(player.name + "´s thirst is at " + str(player.thirst) + " points.\n")
    slow_print(player.name + "´s strenght is at " + str(player.strenght) + " points.\n")
    slow_print(player.name + " has a " + str.lower(player.weapon[1]) + " in his hand." + "\n\n")
    this_location()

  def show_health(player):
    slow_print("\n(" + player.name + "´s Health is at " + str(player.health) + " points)\n")
    this_location()

  def show_inventory(player):
    slow_print(player.weapon[1])
    this_location



###                                 Import Weapons                              ###
    
exec(open("Weapons.py").read())

###                                 Import Charaktere                           ###

exec(open("Chars.py").read())

###                                 Class Animal                               ###

class animal:
  def __init__(monster, location, race, name, health, strenght, agility, weapon, fur, alive):
    animal.location = location
    animal.race = race
    animal.name = name
    animal.health = health
    animal.strenght = strenght
    animal.agility = agility
    animal.weapon = weapon
    animal.fur = fur
    animal.alive = alive


###                          Functions  Animal                       ###


###

exec(open("CombatSystem.py").read())







######                        -(All Felzur City Places)-                   ######

exec(open("LevelFelzur.py").read())






###                                    Credits                                   ###

def credits():
  slow_print("\n--------------------------------\n\n###Prototype RPG 'ARENA CITY'###\n\n<Copyright 2022 by Marvin Reese>\n\n--------------------------------\n\nPress 'Return' to go to the menu.\n")
  print(input("\n>"))
  start_menu()





#####>                              <Spielaufruf>                            <#####
start_menu()


