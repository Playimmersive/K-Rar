def world_map_felzur_city():
  player1.location = world_map_felzur_city
  screen_clear()
  slow_print(player1.name + " opens his map to find the right way.\n\n")
  player_input = (input("\n\nType 'Felzur' to enter the city.\nType 'rest' to rest a while\n\n>"))
  if "Felzur" in player_input:
    felzur_city_gate_entrance()
  elif "rest" in player_input:
    player1.rest_unsafe()
  else:slow_print("Can't handle your input!")
  this_location() 
