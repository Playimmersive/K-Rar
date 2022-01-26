typing_speed = 50 #wpm
def slow_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.8/typing_speed)


import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')





def this_location():
    if player1.location == felzur_city_player_home:
      input("\n>")
      screen_clear()
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      input("\n>")
      screen_clear()
      felzur_city_alley()
    elif player1.location == felzur_city_bar:
      input("\n>")
      screen_clear()
      felzur_city_bar()

    elif player1.location == felzur_city_plaza_shack_01:
      input("\n>")
      screen_clear()
      felzur_city_plaza_shack_01()
    elif player1.location == felzur_city_plaza_stonebuilding_01:
      input("\n>")
      screen_clear()
      felzur_city_plaza_stonebuilding_01()
    elif player1.location == felzur_city_plaza_coluseum:
      input("\n>")
      screen_clear()
      felzur_city_plaza_coluseum()
    elif player1.location == felzur_city_market:
      input("\n>")
      screen_clear()
      felzur_city_market()
    else: input("\n>")
    screen_clear()
    felzur_city_plaza()
