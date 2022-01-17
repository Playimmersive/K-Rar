typing_speed = 50 #wpm
def slow_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.8/typing_speed)




def this_location():
    if player1.location == felzur_city_player_home:
      print("\n" *50)
      felzur_city_player_home()
    elif player1.location == felzur_city_alley:
      print("\n" *50)
      felzur_city_alley()
    elif player1.location == felzur_city_bar:
      print("\n" *50)
      felzur_city_bar()

    elif player1.location == felzur_city_plaza_shack_01:
      print("\n" *50)
      felzur_city_plaza_shack_01()
    elif player1.location == felzur_city_plaza_stonebuilding_01:
      print("\n" *50)
      felzur_city_plaza_stonebuilding_01()
    elif player1.location == felzur_city_plaza_coluseum:
      print("\n" *50)
      felzur_city_plaza_coluseum()
    elif player1.location == felzur_city_market:
      print("\n" *50)
      felzur_city_market()
    else: print("\n" *50)
    felzur_city_plaza()
