

import os,sys,time,random

typing_speed = 50 #wpm
def slow_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2/typing_speed)








###                             Start Menu                          ###

def start_menu():
  slow_print("\n###              This is a Playimmersive production.          ###\n\n\n\n###               Welcome to the world of K^Rar.              ###\n###               A world on the edge of the end!             ###\n\nAre you sure you want to enter this place?\n")
  player1.health = 78
  player1.hunger = 51
  player1.thirst = 43
  player1.strenght = 1
  player1.agility = 1
  player1.weapon = dagger
  player1.max_health = 100
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
  slow_print("\n" + player1.name + " wokes up in a tiny room.\nIt´s cold inside and the air is full of dust!\nAfter a while " + player1.name + " is able to move his head, everything hurts!\n" + player1.name + " feels hungry and thirsty.\nThere is a dagger sticking into a little cupboard and a bag with 10 gold benith it.\n" + player1.name + " takes everything!\n\n--------------------------------\n")
  felzur_city_player_home()

###                             Class Human                         ###

class human:
  def __init__(hero, location, race, nativity, citizen, name, age, health, max_health, hunger, thirst, strenght, agility, weapon, gold, medics, meals, water, alive):
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
    hero.medics = medics
    hero.meals = meals
    hero.water = water    
    hero.alive = alive


###                         Functions Human                   ###


  def show_hitpoints(player):
    hitpoints = player.strenght * player.weapon[0]
    slow_print("Hitpoints current weapon: " + str(hitpoints) + "\n")
    if player1.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      felzur_city_alley()
    else: felzur_city_place()


###                         rest                              ###


  def rest(player):
    
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
      else:
        if player1.location == felzur_city_player_home:
          felzur_city_player_home()
        elif player1.location == felzur_city_alley:
          felzur_city_alley()
        else: felzur_city_place()

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

  def use_medics(player):
    if player.medics > 0 and player.health < player.max_health - 100:
      slow_print(player.name + " takes some healing herbs.")
      player.health = player.health + 100
      player.medics = player.medics -1
    elif player.medics > 0 and player.health > player.max_health - 100:
      slow_print(player.name + " takes some healing herbs.")
      player.health = player.max_health
      player.medics = player.medics -1
    else:print("You dont have anything to heal.")
    felzur_city_player_home()



  def status(player):
    slow_print("\n" + player.name + "´s Health is at " + str(player.health) + "/" + str(player.max_health) + " points.\nThere are " + str(player.gold) + " gold pieces in the bag.\n")
    slow_print(player.name + "´s hunger is at " + str(player.hunger) + " points.\n")
    slow_print(player.name + "´s thirst is at " + str(player.thirst) + " points.\n")
    slow_print(player.name + "´s strenght is at " + str(player.strenght) + " points.\n")
    slow_print(player.name + " has a " + str.lower(player.weapon[1]) + " in his hand." + "\n\n")
    if player1.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      felzur_city_alley()
    elif player1.location == felzur_city_bar:
      felzur_city_bar()
    else:felzur_city_place()

  def show_health(player):
    slow_print("\n(" + player.name + "´s Health is at " + str(player.health) + " points)\n")
    if player1.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      felzur_city_alley()
    else:felzur_city_place()

  def show_inventory(player):
    slow_print(player.weapon[1])
    if player1.location == felzur_city_player_home:
      felzur_city_player_home()
    elif player1.location == felzur_city_bar:
      felzur_city_bar()
    elif player1.location == felzur_city_alley:
      felzur_city_alley()
    else:felzur_city_place()



###                                 Import Weapons                              ###
    
exec(open("Weapons.py").read())

###                                 Import Charaktere                           ###

exec(open("Chars.py").read())

###                                 Class Monster                               ###

class monster:
  def __init__(monster, location, race, nativity, name, age, health, hunger, thirst, strenght, agility, weapon, gold, alive):
    monster.location = location
    monster.race = race
    monster.nativity = nativity
    monster.name = name
    monster.age =age
    monster.health = health
    monster.hunger = hunger
    monster.thirst = thirst
    monster.strenght = strenght
    monster.agility = agility
    monster.weapon = weapon
    monster.gold = gold
    monster.alive = alive


###                          Functions  Monster                       ###

  def greetings(monster):
    slow_print("I'am " + monster.name + "\n")


  def race_description(monster):
    slow_print("We " + monster.race + " come from the " + monster.nativity)


  def status(monster):
    slow_print("\n(" + monster.race + "s´Health is at " + str(monster.health) + " points.)")
    slow_print("(" + monster.race + "s´Hunger is at " + str(monster.hunger) + " points.)")
    slow_print("(" + monster.race + "s´Thirst is at " + str(monster.thirst) + " points.)")
    slow_print("(" + monster.name + " has a " + str.lower(monster.weapon[1]) + " in his hand.)" + "\n")


  def show_health(monster):
    slow_print("\n(" + monster.name + "´s Health is at " + str(monster.health) + " points)\n")


  def attack_text(monster):
    slow_print("Puny human, I will squash you to pieces")





###                      Combatsystem "player as attacker" part 1/2 attacker_round                  ###

def combat(attacker, defender):
  attacker.hunger = attacker.hunger - 4
  attacker.thirst = attacker.thirst - 5
  import random
  result = range(0,5)
  fight = True  
  while fight :
#statt if switch
    if random.choice(result) == 1:
      hitpoints = attacker.strenght * attacker.weapon[0]
      defender.health = max(0, defender.health - hitpoints)
      slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " + str(hitpoints) + (" hitpoints.\n"))
      slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n")
      if defender.health <= 0:
        defender.alive = False
        print(defender.name + " has been slained!\n")
        after_combat()

    elif random.choice(result) == 2:
      hitpoints = attacker.strenght * attacker.weapon[0] + 10
      defender.health = max(0, defender.health - hitpoints)
      slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n"))
      slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n")

      if defender.health <= 0:
        defender.alive = False
        slow_print(defender.name + " has been slained!\n")
        after_combat()

    elif random.choice(result) == 3:
      hitpoints = attacker.strenght * attacker.weapon[0] + 2
      attacker.health = max(0, attacker.health - attacker.strenght)
      slow_print("Oh no, " + attacker.name +  " harmed himself!\nHe needs a moment to regain his composure!\n")
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    elif random.choice(result) == 4:
      hitpoints = attacker.strenght * attacker.weapon[0] + 2
      defender.health = max(0, defender.health - hitpoints / 2)
      slow_print("The "+ defender.name + " could soften the blow a bit!\n")
      slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n")

      if defender.health <= 0:
        defender.alive = False
        slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n")
        after_combat()

    else: print("Oh no, " + attacker.name + " missed.\nHe stumbles around!\n")



    ###                    Combatsystem 'player as attacker' part2/2 "defender_round"                ###

    if random.choice(result) == 1:
      hitpoints = defender.strenght * defender.weapon[0]
      attacker.health = max(0, attacker.health - hitpoints)
      slow_print(defender.name + " swings his " +  str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    elif random.choice(result) == 2:
      hitpoints = defender.strenght * defender.weapon[0] + 10
      attacker.health = max(0, attacker.health - hitpoints)
      slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n"))
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    elif random.choice(result) == 3:
      hitpoints = defender.strenght * defender.weapon[0] + 2
      defender.health = max(0, defender.health - defender.strenght)
      slow_print("Hard to belive but, " + defender.name +  " harmed himself!\n")
      slow_print("(" + defender.name + " has " + str(defender.health) + " healthpoints.\n" )

      if defender.health <= 0:
        defender.alive = False
        slow_print(defender.name + " has slained himself!\n")
        after_combat()
    
    elif random.choice(result) == 4:
      hitpoints = defender.strenght * defender.weapon[0] + 2
      attacker.health = max(0, attacker.health - hitpoints / 2)
      slow_print("The "+ attacker.name + " could soften the blow a bit!\n\n")
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    
    else: slow_print("What a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n")





###                           After Combat                          ###

def after_combat():
  if player1.alive == True:
    gold_found = range(0,50)
    player1.gold = player1.gold + random.choice(gold_found)
    print(player1.name + " won this battle.\n" + player1.name + " collected some gold, know are " + str(player1.gold) + " pieces of gold in " + player1.name + "´s bag.")
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


  else: slow_print("It was a hard fight but not enough to escape the death blow!\n" + player1.name + " where slained!\n")
  if player1.hunger <= 0:
    slow_print(player.name + " starved to death!")
    player1.alive = False
    credits()
  if player1.thirst <= 0:
    slow_print(player.name + " died of thirst!")
    player1.alive = False
    credits()
  print(input("Press enter\n>"))
  credits()







#########                           --(World)--                             ###
'''  
Weltbeschreibung:
Orte: felzur_city
      felzur_city_gate
      felzur_city_alley
      felzur_city_bar
      felzur_city_player_home
'''


######                        -(All Felzur City Places)-                   ######





###                               Felzur City Gate                            ###




###                               Felzur City Alley                           ###


def felzur_city_alley():
  player1.location = felzur_city_alley
  slow_print("\n" + player1.name +" enters the Felzur city allay.\n")
  player_input = (input("\nPress 'bar' to enter the city bar.\nPress 'home' to go to your home.\nPress 'place' to go to the  city place.\nPress 'status' to check your stats.\nPress 'menu' to go to the main menu.\n>"))
  if "home" in player_input:
    felzur_city_player_home()
  elif "place" in player_input:
    felzur_city_place()
  elif "bar" in player_input:
    felzur_city_bar()
  elif "rest" in player_input:
    print(player1.name + " can only rest in a safe place\n!")
    felzur_city_alley()
  elif "status" in player_input:
    player1.status()
  elif "menu" in player_input:
    start_menu()

  else:print("Can´t handle your input!\n")
  felzur_city_alley()  




###                            Felzur City Player Home                         ### Hier müssen alle Namen an 'arena_city_home' angepasst werden

def felzur_city_player_home():
  player1.location = felzur_city_player_home
  slow_print("\nThere is a bed with a little cupboard and a fireplace with some cooking stuff inside your room.\n")
  player_input = (input("\n\nType 'leave' to leave your home.\nType 'medics' to take some medics.\nType 'rest' to sleep a while.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\n\n>"))
  if "rest" in player_input:
    player1.rest()

  elif "status" in player_input:
    player1.status()

  elif "leave" in player_input:
    felzur_city_alley()
  elif "medics" in player_input:
    player1.use_medics()
  elif "quit" in player_input:
    start_menu()

  else:print("Can´t handle your input!")
  felzur_city_player_home()

###                             Felzur City Bar                         ###

def felzur_city_bar():
  player1.location = felzur_city_bar
  slow_print("\n" + player1.name + " can see some dark figures around a dirty table.\nThe barkeeper looks not realy inviting like the rest of this bar.\n")
  player_input = (input("\nType 'eat' to have a snack. (9 Gold)\nPress 'drink' to buy a drink. (6 gold) \nType 'leave' to leave the bar.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\n\n>"))
  if "eat" in player_input:
    if player1.hunger < 60 and player1.gold > 9:
      slow_print(player1.name + " takes a snack!\n")
      player1.gold = player1.gold - 10
      player1.hunger = player1.hunger + 40
      felzur_city_bar()
    elif player1.gold < 10:
      slow_print(player1.name + " has not enough gold!\n")
      felzur_city_bar()
    else:slow_print(player1.name + " don´t feel hungry.\n")
    felzur_city_bar()

  elif "drink" in player_input:
    if player1.thirst < 70 and player1.gold > 5:
      slow_print(player1.name + " takes a drink!\n")
      player1.gold = player1.gold - 6
      player1.thirst = player1.thirst + 30
      felzur_city_bar()
    elif player1.gold < 6:
      slow_print(player1.name + " has not enough gold!\n")
      felzur_city_bar()
    else:print(player1.name + " don´t feel thirsty.\n")
    felzur_city_bar()
  elif "status" in player_input:
    player1.status()
  elif "leave" in player_input:
    felzur_city_alley()
  elif "quit" in player_input:
    start_menu()

  else:print("Can´t handle your input!")
  felzur_city_bar()

###                             Felzur City Place                        ###

def felzur_city_place():
  player1.location = felzur_city_place
  slow_print("\n" + player1.name + " enters the Felzur city place.\nThere are some buildings around a dusty place.\n\n")
  player_input = (input("\nPress 'shack' to go into a shabby shack.\nPress 'stonebuilding' to go into a old stonebuilding.\nPress 'coluseum' to go into the great coluseum.\nPress 'allay' to go back to the main allay.\nPress 'status' for your status.\nPress 'quit' to leave the game.\nPress 'menu' to go back to the main menu!\n\n>"))
  if "shack" in player_input:
    felzur_city_place_shack_01()
  elif "stonebuilding" in player_input:
    felzur_city_place_stonebuilding_01()
  elif "coluseum" in player_input:
    felzur_city_place_coluseum()
  elif "allay" in player_input:
    felzur_city_alley()
  elif "rest" in player_input:
    print(player1.name + " can only rest in a safe place!/n")
    felzur_city_place()
  elif "status" in player_input:
    player1.status()
  elif "quit" in player_input:
    credits()
  elif "menu" in player_input:
    start_menu()    
  else:print("Can´t handle your input!")
  felzur_city_place()




###                                arena_city_place_shack_01                                ###

def felzur_city_place_shack_01():
  global sharped_dagger_found
  player1.location = felzur_city_place_shack_01 

  if bandit1.health > 0:
    slow_print("\nAt the door is a little sign with some scratches, it cut means " + bandit1.name  + "´s shack.\nInside you can see a little bit of blood at the floor and at the furniture.\nThe shack owner says 'Get out of here dirty bastard!'\n")
    player_input = (input("Type 'ignore' to ignore the owner and search for usefull stuff in this shack.\nType 'leave' to leave.\n>"))

    if "ignore" in player_input:
      player1.health = player1.health - 10
      slow_print(player1.name + " ignores the shack owner.\nThe small man shows a " + str.lower(bandit1.weapon[1]) + " and starts a attack\n\n" + player1.name + " gets a cut for 10 ponits!\n\n")
      combat(player1, bandit1)


    elif "leave" in player_input:
      slow_print(player1.name + " leaves the Arena.\n")
      felzur_city_place()


    else:print("Can´t handle your input!\n>")
    felzur_city_place_shack_01()


  elif bandit1.alive == False:
    slow_print("\nSome day this was the shack of  " + bandit1.name  + " .\nInside the shack you can see blood everywhere!\n" + bandit1.name  + " lies on the floor.\n")
    player_input = (input("\nPress 'search' to search for some useable things in this shack.\nPress 'leave' to leave.\n>"))

    if "search" in player_input:
        
      if sharped_dagger_found == False:      
        slow_print(player1.name + " found a sharped dagger.\n\n")
        player_input = (input("\nPress 'equip' to equip the sharped dagger.\nPress 'sell' to sell it at the city place.\n>"))
        if "equip" in player_input:
          print(player1.name + " equipes the sharped dagger.\n")
          sharped_dagger_found = True
          player1.weapon = sharped_dagger
        elif "sell" in player_input:
          print(player1.name + " sells the sharped dagger at the city place for 22 gold.\n")
          player1.gold = player1.gold + 22
          sharped_dagger_found = True
        else:print("Can´t handle your input!")  
        felzur_city_place_shack_01()
          
      elif sharped_dagger_found == True:
        print("There is nothing left!")
        felzur_city_place_shack_01()
      else:print("Can´t handle your input!")
      felzur_city_place_shack_01()
    elif "leave" in player_input:
      slow_print(player1.name + " leaves the Arena.\n")
      felzur_city_place()
      slow_print("Here is nothing more to do!\n" + player1.name + " leaves the shack!\n")
      felzur_city_place()

    else:print("Can´t handle your input!")
    felzur_city_place_shack_01()


###                  felzur_city_place_stonebuilding_01                      ###


def felzur_city_place_stonebuilding_01():
  player1.location = felzur_city_place_stonebuilding_01 
  slow_print("\nWelcome to " + bandit2.name  + "´s arena, everywhere is blood and some bones are on the floor!\n ")
  player_input = (input("Press 'fight' for next combat.\nPress 'leave' to leave.\n>"))
  if bandit2.health > 0:
    if "fight" in player_input:
      print("There is a huge bandit in front of " + player1.name + "!\n")
      combat(player1, bandit2)


    elif "leave" in player_input:
      print(player1.name + " leaves the stonebuilding.")
      felzur_city_place()

    else:print("Can´t handle your input!\n>")
    felzur_city_place_stonebuilding_01()

  else:print(bandit2.name + " is still dead!\n" + player1.name + " leaves the Arena!\n")
  felzur_city_place()

###                           arena_city_place_coluseum                            ###

def felzur_city_place_coluseum():
  player1.location = felzur_city_place_coluseum 
  slow_print("Welcome to the great coluseum!\n> ")
  player_input = (input("Press 'fight' for a honorfull combat against a gladiator.\nIt cut be " + player1.name + "s last fight!\nPress 'leave' to leave.\n>"))
  if gladiator1.health > 0:

    if "fight" in player_input:
      print("There is a gladiator in front of " + player1.name + "\nThis fight will be hard!")
      combat(player1, gladiator1)


    elif "leave" in player_input:
      print(player1.name + " leaves the great arena.")
      felzur_city_place()

    else:print("Can´t handle your input!\n\n\n\n>")
    felzur_city_place_coluseum()

  else:print(gladiator1.name + " is still dead!\n" + player1.name + " stands in front of the corpse!\nHe leaves the coluseum after a while!")
  felzur_city_place()








###                                    Credits                                   ###

def credits():
  slow_print("\n--------------------------------\n\n###Prototype RPG 'ARENA CITY'###\n\n  <Copyright by Marvin Reese>\n\n--------------------------------\n\nPress 'Return' to go to the menu.\n")
  print(input("\n>"))
  start_menu()





#####>                              <Spielaufruf>                            <#####

start_menu()


