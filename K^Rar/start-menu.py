#                           start_menu()


def start_menu():
  slow_print("\n###              This is a Playimmersive production.          ###\n\n\n\n###               Welcome to the world of K^Rar.              ###\n###               A world on the edge of the end!             ###\n\nAre you sure you want to enter this place?\n")
  player1.health = 78
  player1.hunger = 51
  player1.thirst = 43
  player1.weapon = dagger
  player1.max_health = 100
  player1.gold = 10
  player1.medics = 1
  player1.meals = 1
  player1.water = 1
  player1.alive = True
 
  

  player_input = (input("\nType 'yes' to enter.\nType 'no' to leave.\n\n>"))
  
  if "yes" in player_input:
    screen_clear()
    slow_print ("\nYou enter the world of K^Rar!\n")
    player1.location = felzur_city_player_home
    player1.race = "Human"
    slow_print("\nFrom where are you?\n")
    player_input = input("Type 'Felzur' to select Felzur as homecity.\n\n>")
    
    if "Felzur" in player_input:
      slow_print("You are from Felzur, it's a cold place sourroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.\n")
      player1.nativity = "Felzur"
      
      slow_print("\nWhat's your name?\n")
      player1.name = input(">")
    
      slow_print("\nHow old are you?\n")
      player1.age = input(">")
      screen_clear()
      choose_class()
      
    else: print("\n---------------\nComming soon!\n---------------\n")
    slow_print("You are from Felzur, it's a cold place surroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.\n\n")
    player1.nativity = "Felzur"
    
    slow_print("\nWhat's your name?\n")
    player1.name = input(">")
    
    slow_print("\nHow old are you?\n")
    player1.age = input(">")
    screen_clear()
    choose_class()
    
    
  elif "no" in player_input:
    slow_print ("\nYou leave this unholy place!\n\n")
    input("\n>")
    screen_clear()
    credits()

  else: print("Can't handle your input!")
  input("\n>")
  screen_clear()
  start_menu()


#                         choose_class()


def choose_class():
  slow_print("\nType 'strong' to choose a strong body with more power.\nType 'fast' to choose a body with a better agility.\n")
  player_input = input("\n>")
             
  if "strong" in player_input:    
    player1.strenght = 2
    player1.agility  = 1
    intro()
             
  if "fast" in player_input:
    player1.strenght = 1
    player1.agility  = 2
    intro()
             
  else:input("Cant' handle your input\n>")
  screen_clear()
  choose_class()



