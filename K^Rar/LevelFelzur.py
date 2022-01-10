
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
  player_input = (input("\nType 'bar' to enter the city bar.\nType 'home' to go to your home.\nPress 'place' to go to the  city place.\nType 'status' to check your stats.\nType 'menu' to go to the main menu.\n>"))
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
  this_location()  




###                            Felzur City Player Home                         ### Hier müssen alle Namen an 'arena_city_home' angepasst werden

def felzur_city_player_home():
  player1.location = felzur_city_player_home
  slow_print("\nThere is a bed with a little cupboard and a fireplace with some cooking stuff inside your room.\n")
  player_input = (input("\n\nType 'rest' to take a break.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\nType 'leave' to leave your home.\n\n>"))
  if "rest" in player_input:
    player1.rest()

  elif "status" in player_input:
    player1.status()

  elif "leave" in player_input:
    felzur_city_alley()

  elif "quit" in player_input:
    start_menu()

  else:print("Can´t handle your input!")
  this_location() 

###                             Felzur City Bar                         ###

def felzur_city_bar():
  player1.location = felzur_city_bar
  slow_print("\n" + player1.name + " can see some dark figures around a dirty table.\nThe barkeeper looks not realy inviting like the rest of this bar.\n")
  player_input = (input("\nType 'eat' to have a snack. (9 Gold)\nPress 'drink' to buy a drink. (6 gold) \nType 'leave' to leave the bar.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\n\n>"))
  if "eat" in player_input:
    if player1.hunger < 60 and player1.gold > 9:
      slow_print(player1.name + " takes a snack!\n")
      player1.gold = player1.gold - 9
      player1.hunger = player1.hunger + 40
      this_location() 
    elif player1.gold < 10:
      slow_print(player1.name + " has not enough gold!\n")
      this_location() 
    else:slow_print(player1.name + " don´t feel hungry.\n")
    this_location()

  elif "drink" in player_input:
    if player1.thirst < 70 and player1.gold > 5:
      slow_print(player1.name + " takes a drink!\n")
      player1.gold = player1.gold - 6
      player1.thirst = player1.thirst + 30
      this_location() 
    elif player1.gold < 6:
      slow_print(player1.name + " has not enough gold!\n")
      this_location() 
    else:print(player1.name + " don´t feel thirsty.\n")
    this_location() 
  elif "status" in player_input:
    player1.status()
  elif "leave" in player_input:
    felzur_city_alley()
  elif "quit" in player_input:
    start_menu()

  else:print("Can´t handle your input!")
  this_location() 

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
  this_location() 




###                                arena_city_place_shack_01                                ###

def felzur_city_place_shack_01():
  global sharped_dagger_found
  player1.location = felzur_city_place_shack_01 

  if bandit1.health > 0:
    slow_print("\nAt the door is a little sign with some scratches, it cut means " + bandit1.name  + "'s shack.\nInside you can see a little bit of blood at the floor and at the furniture.\nThe shack owner says 'Get out of here dirty bastard!'\n")
    player_input = (input("Type 'ignore' to ignore the owner and search for usefull stuff in this shack.\nType 'leave' to leave.\n>"))

    if "ignore" in player_input:
      player1.health = player1.health - 10
      slow_print(player1.name + " ignores the shack owner.\nThe small man shows a " + str.lower(bandit1.weapon[1]) + " and starts a attack\n\n" + player1.name + " gets a cut for 10 ponits!\n\n")
      combat(player1, bandit1)


    elif "leave" in player_input:
      slow_print(player1.name + " leaves the Arena.\n")
      felzur_city_place()


    else:print("Can´t handle your input!\n>")
    this_location() 


  elif bandit1.alive == False:
    slow_print("\nSome day this was the shack of " + bandit1.name  + " .\nInside the shack you can see blood everywhere!\n" + bandit1.name  + " lies on the floor.\n")
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
        this_location() 
          
      elif sharped_dagger_found == True:
        print("There is nothing left!")
        this_location() 
      else:print("Can´t handle your input!")
      this_location() 
    elif "leave" in player_input:
      slow_print(player1.name + " leaves the Arena.\n")
      felzur_city_place()


    else:print("Can´t handle your input!")
    this_location() 


###                  felzur_city_place_stonebuilding_01                      ###


def felzur_city_place_stonebuilding_01():
  player1.location = felzur_city_place_stonebuilding_01 
  slow_print("\nWelcome to " + bandit2.name  + "´s arena, everywhere is blood and some bones are on the floor!\n")
  player_input = (input("Press 'fight' for next combat.\nPress 'leave' to leave.\n>"))
  if bandit2.health > 0:
    if "fight" in player_input:
      print("There is a huge bandit in front of " + player1.name + "!\n")
      combat(player1, bandit2)


    elif "leave" in player_input:
      print(player1.name + " leaves the stonebuilding.")
      felzur_city_place()

    else:print("Can´t handle your input!\n>")
    this_location() 

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
    this_location() 

  else:print(gladiator1.name + " is still dead!\n" + player1.name + " stands in front of the corpse!\nHe leaves the coluseum after a while!")
  felzur_city_place()







