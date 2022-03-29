
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
def felzur_city_gate():
  player1.location = felzur_city_gate
  screen_clear()
  slow_print("\nThere is the city gate in front of "+ player1.name + ".\nAbove the gate is a little watch tower with some guards on it.\n")
  player_input = (input("\n\nType 'leave' to pass through the gate and leave the city.\nType 'alley' to go back to the city alley.\n\n>"))
  if "leave" in player_input:
    world_map_felzur_city()
  elif "alley" in player_input:
    felzur_city_alley()
  else:slow_print("Can't handle your input!")
  this_location() 


###                               felzur_city_gate_entrance                            ###
def felzur_city_gate_entrance():
  player1.location = felzur_city_gate_entrance
  screen_clear()
  slow_print("\nThere is the city gate in front of "+ player1.name + ".\n")
  player_input = (input("\n\nType 'enter' to pass through the gate and enter the city alley.\nType 'map' to go back to the regional map.\n\n>"))
  if "enter" in player_input:
    felzur_city_alley()
  elif "map" in player_input:
    world_map_felzur_city()
  else:slow_print("Can't handle your input!")
  this_location() 

###                               Felzur City Alley                           ###


def felzur_city_alley():
  player1.location = felzur_city_alley
  screen_clear()
  slow_print("\n" + player1.name +" enters the Felzur city alley.\nThe alley leads from the citygate to the plaza of Felzur.\nThere is nobody at the allay, it's cold and windy and the whole ground lies under a thin skin of ice.\n" + player1.name  + " has a room here aside the bar.\n")

  player_input = (input("\nType 'room' to go to your little home.\nType 'gate' to go to the city gate.\nType 'bar' to enter the city bar.\nType 'plaza' leave the allay and to go to the city plaza.\nType 'rest' to rest a while\n\n"))
  if "room" in player_input:
    felzur_city_player_home()
  elif "gate" in player_input:
    felzur_city_gate()
  elif "plaza" in player_input:
    felzur_city_plaza()
  elif "bar" in player_input:
    felzur_city_bar()
  elif "rest" in player_input:
    player1.rest_unsafe()
  elif "menu" in player_input:
    start_menu()
  else:print("Can't handle your input!")
  this_location()  




###                            Felzur City Player Home                         
def felzur_city_player_home():
  player1.location = felzur_city_player_home
  screen_clear()
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
  screen_clear()
  slow_print("\n" + player1.name + " can see some dark figures around a dirty table.\nThe barkeeper looks not realy inviting like the rest of this bar.\n\n")
  player_input = (input("\nType 'talk' to start a conversation.\nType 'rest' to take place.\nType 'meal' to buy a meal. (9 Gold)\nType 'drink' to buy a drink. (6 gold) \nType 'leave' to leave the bar.\nType 'quit' to go back to the start menu.\n\n>"))
  if "meal" in player_input:
    if player1.gold > 9:
      slow_print(player1.name + " buys somethig to eat!(-9 gold)\n")
      player1.gold = player1.gold - 9
      player1.meals = player1.meals + 1
      input("\n>")
      this_location() 
    elif player1.gold < 10:
      slow_print(player1.name + " has not enough gold!\n")
      input("\n>")
      this_location() 
    else:slow_print(player1.name + " don´t feel hungry.\n")
    input("\n>")
    this_location()

  elif "drink" in player_input:
    if player1.gold > 5:
      slow_print(player1.name + " buys a drink!(-6 gold)\n")
      player1.gold = player1.gold - 6
      player1.water = player1.water +1
      input("\n>")
      this_location() 
    elif player1.gold < 6:
      slow_print(player1.name + " has not enough gold!\n")
      input("\n>")
      this_location() 
    else:print(player1.name + " don´t feel thirsty.\n")
    input("\n>")
    this_location()
  elif "talk" in player_input:
    dialog_barkeeper1()
  elif "rest" in player_input:
    print(player1.name + "\n")
    player1.rest_unsafe()
  elif "leave" in player_input:
    felzur_city_alley()
  elif "quit" in player_input:
    start_menu()

  else:print("Can't handle your input!")
  input("\n>")
  this_location() 

###                             Felzur City Plaza                        ###

def felzur_city_plaza():
  player1.location = felzur_city_plaza
  screen_clear()
  slow_print("\n" + player1.name + " enters the Felzur city plaza.\nThere are some buildings around a windy place.\nIn the middle of the place is a huge coluseum.\nIn front of it is a little market with some merchants.\n\n")

  if stray_dog_01.alive == True:
    slow_print("There is a dog in front of a little shack.\n\nType 'pet' to pet him.")

  if stray_dog_01.alive == False:
    slow_print("The stray dog lies in a dark corner aside the shack.\n")

  player_input = (input("\nType 'shack' to go into a shabby shack.\nType 'market' to go to the merchants\nType 'stonebuilding' to go into a old stonebuilding.\nType 'coluseum' to go into the great coluseum.\nType 'alley' to go back to the main alley.\n\n>"))
  if "shack" in player_input:
    felzur_city_plaza_shack_01()

  elif "pet" in player_input:    
    global set_attacker
    set_attacker = player1
    global set_defender
    set_defender = stray_dog_01
    chose_combat_animal()

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
  screen_clear()
  slow_print("\n" + player1.name + " goes to the market, there are some merchants and soldiers around the market.\n(" + player1.name + " has " + str(player1.gold) + " gold.)\n")
  player_input = (input("\nType 'sell fur' to sell fur. (" + str(fur_price) + " gold)\nType 'sell herbs' to sell herbs. (" + str(herbs_price) + " gold)\nType 'sell water' to sell water. (" + str(water_price) + " gold)\nType 'sell meal' to sell meals. (" + str(meals_price) + " gold)\n\nType 'buy log' to buy a log. (" + str(log[2]) + " gold)\nType 'buy sharped dagger' to buy a sharped dagger. (" + str(sharped_dagger[2]) + " gold) \nType 'buy sword' to buy a sword. (" + str(sword[2]) + " gold) \n\nType 'leave' to leave the market.\nType 'rest' to take a little break.\n\n>"))
  if "sell fur" in player_input:
    if player1.fur > 0:
      slow_print(player1.name + " goes into a little tent and sells a fur for " + str(fur_price) + " gold, that was a good deal!\n")
      player1.gold = player1.gold + fur_price
      player1.fur = player1.fur - 1
      this_location() 
    else: player1.fur < 1
    slow_print(player1.name + " has no fur!\n")
    this_location()

    
  elif "sell herbs" in player_input:
    if player1.medics > 0:
      slow_print(player1.name + " goes into a little tent and sells a herbs for " + str(herbs_price) + " gold, that was a good deal!\n")
      player1.gold = player1.gold + herbs_price
      player1.medics = player1.medics - 1
      this_location() 
    else: player1.medics < 1
    slow_print(player1.name + " has no herbs!\n")
    this_location()

  elif "sell water" in player_input:
    if player1.water > 0:
      slow_print(player1.name + " goes into a little tent and sells a water for " + str(water_price) + " gold, that was a good deal!\n")
      player1.gold = player1.gold + water_price
      player1.water = player1.water - 1
      this_location() 
    else: player1.water < 1
    slow_print(player1.name + " has no water!\n")
    this_location()

  elif "sell meal" in player_input:
    if player1.meals > 0:
      slow_print(player1.name + " goes into a little tent and sells a meal for " + str(meals_price) + " gold, that was a good deal!\n")
      player1.gold = player1.gold + meals_price
      player1.meals = player1.meals - 1
      this_location() 
    else: player1.meals < 1
    slow_print(player1.name + " has no meal!\n")
    this_location()

  elif "buy sharped dagger" in player_input:
    if player1.gold >= sharped_dagger[2]:
      slow_print(player1.name + " walkes to the blacksmith and buys a sharped dagger for " + str(sharped_dagger[2]) + " gold.\nIt has some scratches at the blade!\n")
      player1.gold = player1.gold - sharped_dagger[2]
      player1.weapon = sharped_dagger
      this_location() 
    else: player1.gold < 150
    slow_print(player1.name + " has not enough gold!\n")
    this_location() 

  elif "buy log" in player_input:
    if player1.gold >= log[2]:
      slow_print(player1.name + " walkes into a little tent and buys a log for " + str(log[2]) + " gold.\n\n")
      player1.gold = player1.gold +log[2]
      player1.weapon = log
      this_location() 
    else: player1.gold < 70
    slow_print(player1.name + " has not enough gold!\n")
    this_location() 
    
  elif "buy sword" in player_input:
    if player1.gold >= sword[2]:
      slow_print(player1.name + " walkes to the blacksmith and buys a sword for " + str(sword[2]) + " gold.\nIt has a very sharp blade with some beautiful decorations in it!\n")
      player1.gold = player1.gold - sword[2]
      player1.weapon = sword
      this_location() 
    else: player1.gold < sword[2]
    slow_print(player1.name + " has not enough gold!\n")
    this_location() 

  elif "rest" in player_input:
    player1.rest_unsafe()
    
  elif "leave" in player_input:
    felzur_city_plaza()
  else:print("Can't handle your input!")
  this_location() 

###                                felzur_city_plaza_shack_01                                ###

def felzur_city_plaza_shack_01():
  global sharped_dagger_found
  player1.location = felzur_city_plaza_shack_01
  screen_clear()

  if bandit1.health > 0:
    slow_print("\nAt the door is a little sign with some scratches, it cut means " + bandit1.name  + "'s shack.\nInside you can see a little bit of blood at the floor and at the furniture.\nThe shack owner says 'Get out of here dirty bastard!'\n")
    player_input = (input("Type 'talk' to start a conversation.\nType 'ignore' to ignore the owner and walk into this shack.\nType 'leave' to leave.\n>"))

    if "ignore" in player_input:
      player1.health = player1.health - 10
      slow_print(player1.name + " ignores the shack owner.\nThe small man shows a " + str.lower(bandit1.weapon[1]) + " and starts a attack\n\n" + player1.name + " gets a cut for 10 ponits!\n\n")

      global set_attacker
      set_attacker = player1
      global set_defender
      set_defender = bandit1

      chose_combat_short()


    elif "talk" in player_input:
      dialog_bandit1()

    elif "leave" in player_input:
      slow_print(player1.name + " leaves the shabby shack.\n")
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
          input("\n>")
          sharped_dagger_found = True
          player1.weapon = sharped_dagger
        elif "sell" in player_input:
          slow_print(player1.name + " sells the sharped dagger at the city plaza for 22 gold.\n")
          player1.gold = player1.gold + 22
          sharped_dagger_found = True
          input("\n>")
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
  screen_clear()
  if bandit2.alive == False:
    slow_print(bandit2.name + " lies dead on the floor, its better to leave now!\n" + player1.name + " leaves the stonebuilding!\n")
    input("\n>")
    felzur_city_plaza()

  else:slow_print("\n" + player1.name + " enters the building.\nThe owner exhorts to leave his house.\n\n")
  player_input = (input("Type 'ignore' to walk into the building.\nType 'talk' to start a conversation.\nType 'plaza' to leave his house.\n\n>"))
  if "ignore" in player_input:
      slow_print("The merchanary attacks " + player1.name + "!\n\n")
      
      global set_attacker
      set_attacker = player1
      global set_defender
      set_defender = bandit2

      chose_combat_long()

  elif "talk" in player_input:
      dialog_bandit2()
  elif "plaza" in player_input:
      slow_print(player1.name + " leaves the stonebuilding.")
      input("\n>")
      felzur_city_plaza()

  else:slow_print("Can't handle your input!\n>")
  this_location() 



###                           arena_city_plaza_coluseum                            ###

def felzur_city_plaza_coluseum():
  player1.location = felzur_city_plaza_coluseum
  screen_clear()
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







