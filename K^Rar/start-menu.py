
def start_menu():
  slow_print("\n###              This is a Playimmersive production.          ###\n\n\n\n###               Welcome to the world of K^Rar.              ###\n###               A world on the edge of the end!             ###\n\nAre you sure you want to enter this place?\n")
  player1.health = 300
  player1.hunger = 51
  player1.thirst = 43
  player1.strenght = 1
  player1.agility = 3
  player1.weapon = sword
  player1.max_health = 300
  player1.gold = 10
  player1.medics = 1
  player1.meals = 1
  player1.water = 1
  player1.alive = True
  player_input = (input("\nPress 'yes' to enter.\nPress 'no' to leave.\n\n>"))
  if "yes" in player_input:
    print("\n" *50)
    slow_print ("\nYou enter the world of K^Rar!\n")
    player1.location = felzur_city_player_home
    player1.race = "Human"
    slow_print("\nFrom where are you?\n")
    player_input = input("Type 'felzur' to select Felzur as homecity.\n\n>")
    if "felzur" in player_input:
      slow_print("You are from Felzur, it's a cold place sourroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.")
      player1.nativity = "Felzur"
      slow_print("\nWhat's your name?\n")
      player1.name = input(">")
    
      slow_print("\nHow old are you?\n")
      player1.age = input(">")

      intro()
      
    else: print("\n---------------\nComming soon!\n---------------\n")
    slow_print("You are from Felzur, it's a cold place surroundet by mountains.\nIt lies in the south east of K^Rar behind the Felzur Pass.\n")
    player1.nativity = "Felzur"
    
    slow_print("\nWhat's your name?\n")
    player1.name = input(">")
    
    slow_print("\nHow old are you?\n")
    player1.age = input(">")
    
    intro()
    
    
  elif "no" in player_input:
    slow_print ("\nYou leave this unholy place!\n\n")
    credits()

  else: print("Can't handle your input!\n>")
  start_menu()



