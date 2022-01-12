
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
  slow_print("\n" + player1.name +" enters the Felzur city alley.\nThe alley leads from the citygate to the plaza of Felzur.\nThere is nobody at the allay, it's cold and windy and the whole ground lies under a thin skin of ice.\n" + player1.name  + " has a room here aside the bar.\n")

  player_input = (input("\nType 'room' to go to your little home.\nType 'bar' to enter the city bar.\nType 'plaza' leave the allay and to go to the city plaza.\nType 'rest' to rest a while\n"))
  if "room" in player_input:
    felzur_city_player_home()
  elif "plaza" in player_input:
    felzur_city_plaza()
  elif "bar" in player_input:
    felzur_city_bar()
  elif "rest" in player_input:
    print(player1.name + " finds a place to rest.\n!")
    player1.rest_unsafe()
  elif "menu" in player_input:
    start_menu()
  else:print("Can't handle your input!\n")
  this_location()  




###                            Felzur City Player Home                         ### Hier müssen alle Namen an 'arena_city_home' angepasst werden

def felzur_city_player_home():
  player1.location = felzur_city_player_home
  slow_print("\nThere is a bed with a little cupboard and a fireplace with some cooking stuff inside your room.\n")
  player_input = (input("\n\nType 'rest' to rest a while.\nType 'leave' to leave your home.\n\n>"))
  if "rest" in player_input:
    player1.rest()
  elif "leave" in player_input:
    felzur_city_alley()
  else:slow_print("Can't handle your input!")
  this_location() 

###                             Felzur City Bar                         ###

def felzur_city_bar():
  player1.location = felzur_city_bar
  slow_print("\n" + player1.name + " can see some dark figures around a dirty table.\nThe barkeeper looks not realy inviting like the rest of this bar.\n")
  player_input = (input("\nType 'rest' to take place.\nType 'meal' to buy a meal. (9 Gold)\nType 'drink' to buy a drink. (6 gold) \nType 'leave' to leave the bar.\nType 'quit' to go back to the start menu.\n\n>"))
  if "meal" in player_input:
    if player1.gold > 9:
      slow_print(player1.name + " buys a meal!\n")
      player1.gold = player1.gold - 9
      player1.meals = player1.meals + 1
      this_location() 
    elif player1.gold < 10:
      slow_print(player1.name + " has not enough gold!\n")
      this_location() 
    else:slow_print(player1.name + " don´t feel hungry.\n")
    this_location()

  elif "drink" in player_input:
    if player1.gold > 5:
      slow_print(player1.name + " buys a drink!\n")
      player1.gold = player1.gold - 6
      player1.water = player1.water +1
      this_location() 
    elif player1.gold < 6:
      slow_print(player1.name + " has not enough gold!\n")
      this_location() 
    else:print(player1.name + " don´t feel thirsty.\n")
    this_location() 
  elif "rest" in player_input:
    print(player1.name + "\n")
    player1.rest_unsafe()
  elif "leave" in player_input:
    felzur_city_alley()
  elif "quit" in player_input:
    start_menu()

  else:print("Can't handle your input!")
  this_location() 

###                             Felzur City Plaza                        ###

def felzur_city_plaza():
  player1.location = felzur_city_plaza
  slow_print("\n" + player1.name + " enters the Felzur city plaza.\nThere are some buildings around a windy place.\nIn the middle of the place is a huge coluseum.\nIn front of it is a little market with some merchants.\n")
  if stray_dog_01.alive == True:
    slow_print("There is a dog in front of a little shack.\n\nType 'pet' to pet him.")
  if stray_dog_01.alive == False:
    slow_print("The stray dog lies in a dark corner aside the shack.\n")
  player_input = (input("\nType 'shack' to go into a shabby shack.\nType 'market' to go to the merchants\nType 'stonebuilding' to go into a old stonebuilding.\nType 'coluseum' to go into the great coluseum.\nType 'alley' to go back to the main alley.\n\n>"))
  if "shack" in player_input:
    felzur_city_plaza_shack_01()
  elif "pet" in player_input:
    slow_print("The stray dog bites " + player1.name + "!\n\n")
    combat_animal(player1, stray_dog_01)
  elif "stonebuilding" in player_input:
    felzur_city_plaza_stonebuilding_01()
  elif "coluseum" in player_input:
    felzur_city_plaza_coluseum()
  elif "alley" in player_input:
    felzur_city_alley()
  elif "market" in player_input:
    felzur_city_market()
  elif "rest" in player_input:
    print("\n")
    player1.rest_unsafe()    
  else:print("Can't handle your input!")
  this_location() 

###                                felzur_city_market                                       ###
  
def felzur_city_market():
  player1.location = felzur_city_market
  slow_print("\n" + player1.name + " goes to the market, there are some merchants and soldiers around the market.\n")
  player_input = (input("\nType 'sell fur' to sell fur. (15 gold)\nType 'buy sword' to buy a sword. (150 gold) \nType 'leave' to leave the market.\nType 'rest' to take a little break.\n\n>"))
  if "sell fur" in player_input:
    if player1.fur > 0:
      slow_print(player1.name + " goes into a little tent and sells a fur for 15 gold, that was a good deal!\n")
      player1.gold = player1.gold + 15
      player1.fur = player1.fur - 1
      input("Press 'Return'\>n")
      this_location() 
    else: player1.fur < 1
    slow_print(player1.name + " has no fur!\n")
    input("Press 'Return'\>n")
    this_location() 

  elif "buy sword" in player_input:
    if player1.gold > 149:
      slow_print(player1.name + " walkes to the blacksmith and buys a sword for 150 gold.\nIt has a very sharp blade with some beautiful decorations in it!\n")
      player1.gold = player1.gold - 150
      player1.weapon = sword
      input("Press 'Return'\n>")
      this_location() 
    else: player1.gold < 150
    slow_print(player1.name + " has not enough gold!\n")
    input("Press 'Return'\n>")
    this_location() 

  elif "rest" in player_input:
    print(player1.name + "\n")
    player1.rest_unsafe()
  elif "leave" in player_input:
    felzur_city_plaza()
  else:print("Can't handle your input!")
  this_location() 

###                                felzur_city_plaza_shack_01                                ###

def felzur_city_plaza_shack_01():
  global sharped_dagger_found
  player1.location = felzur_city_plaza_shack_01 

  if bandit1.health > 0:
    slow_print("\nAt the door is a little sign with some scratches, it cut means " + bandit1.name  + "'s shack.\nInside you can see a little bit of blood at the floor and at the furniture.\nThe shack owner says 'Get out of here dirty bastard!'\n")
    player_input = (input("Type 'ignore' to ignore the owner and walk into this shack.\nType 'leave' to leave.\n>"))

    if "ignore" in player_input:
      player1.health = player1.health - 10
      slow_print(player1.name + " ignores the shack owner.\nThe small man shows a " + str.lower(bandit1.weapon[1]) + " and starts a attack\n\n" + player1.name + " gets a cut for 10 ponits!\n\n")
      combat(player1, bandit1)


    elif "leave" in player_input:
      slow_print(player1.name + " leaves the Arena.\n")
      felzur_city_plaza()


    else:print("Can´t handle your input!\n>")
    this_location() 


  elif bandit1.alive == False:
    slow_print("\nSome day this was the shack of " + bandit1.name  + " .\nInside the shack you can see blood everywhere!\n" + bandit1.name  + " lies on the floor.\n")
    player_input = (input("\nType 'search' to search for some useable things in this shack.\nType 'leave' to leave.\n>"))

    if "search" in player_input:
        
      if sharped_dagger_found == False:      
        slow_print(player1.name + " found a sharped dagger.\n\n")
        player_input = (input("\nPress 'equip' to equip the sharped dagger.\nPress 'sell' to sell it at the city place.\n>"))
        if "equip" in player_input:
          slow_print(player1.name + " equipes the sharped dagger.\n")
          sharped_dagger_found = True
          player1.weapon = sharped_dagger
        elif "sell" in player_input:
          slow_print(player1.name + " sells the sharped dagger at the city plaza for 22 gold.\n")
          player1.gold = player1.gold + 22
          sharped_dagger_found = True
          felzur_city_plaza()
          
        else:slow_print("Can´t handle your input!")
        input("Press 'return'\n>")
        this_location() 
          
      elif sharped_dagger_found == True:
        slow_print("There is nothing left!")
        input("Press 'return'\n>")
        this_location() 
      else:slow_print("Can´t handle your input!")
      this_location() 
    elif "leave" in player_input:
      slow_print(player1.name + " leaves the little shack.\n")
      felzur_city_plaza()


    else:slow_print("Can't handle your input!")
    input("Press 'return'\n>")
    this_location() 


###                  felzur_city_plaza_stonebuilding_01                      ###


def felzur_city_plaza_stonebuilding_01():
  player1.location = felzur_city_plaza_stonebuilding_01 
  slow_print("\nWelcome to " + bandit2.name  + "´s arena, everywhere is blood and some bones are on the floor!\n")
  player_input = (input("Press 'fight' for next combat.\nPress 'leave' to leave.\n>"))
  if bandit2.health > 0:
    if "fight" in player_input:
      print("There is a huge bandit in front of " + player1.name + "!\n")
      combat(player1, bandit2)


    elif "leave" in player_input:
      print(player1.name + " leaves the stonebuilding.")
      felzur_city_plaza()

    else:print("Can't handle your input!\n>")
    this_location() 

  else:print(bandit2.name + " is still dead!\n" + player1.name + " leaves the Arena!\n")
  felzur_city_plaza()

###                           arena_city_plaza_coluseum                            ###

def felzur_city_plaza_coluseum():
  player1.location = felzur_city_plaza_coluseum 
  slow_print("Welcome to the great coluseum!\n> ")
  player_input = (input("Press 'fight' for a honorfull combat against a gladiator.\nIt cut be " + player1.name + "'s last fight!\nPress 'leave' to leave.\n>"))
  if gladiator1.health > 0:

    if "fight" in player_input:
      slow_print("There is a gladiator in front of " + player1.name + "\nThis fight will be hard!")
      combat(player1, gladiator1)


    elif "leave" in player_input:
      slow_print(player1.name + " leaves the great arena.")
      felzur_city_plaza()

    else:slow_print("Can't handle your input!\n\n>")
    input("Press 'return'\n>")
    this_location() 

  else:slow_print(gladiator1.name + " is still dead!\n" + player1.name + " stands in front of the corpse!\nHe leaves the coluseum after a while!")
  input("Press 'return'\n>")
  felzur_city_plaza()







