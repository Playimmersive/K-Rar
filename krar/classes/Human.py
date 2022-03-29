# muss von Character abgeleitet sein
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

	def rest(player):
		slow_print("\n\n" + player1.name + " enjoys the warm fire and rests for a while.\n")
		player_input = (input("\nType 'sleep' to sleep a while.\nType 'meal' to take a meal.\nType 'drink' to drink something.\nType 'status' for your status.\nType 'carry on' to stop rest.\nType 'medics' to take some medics.\n\nType 'diary' to open your diary.Type 'quit' to go back to the start menu.\n\n>"))
		if "sleep" in player_input:
			screen_clear()
			player1.sleep()
		elif "meal" in player_input:
			screen_clear()
			player1.use_meals()
		elif "drink" in player_input:
			screen_clear()
			player1.use_water()
		elif "status" in player_input:
			screen_clear()
			player1.status()
		elif "carry on" in player_input:
			screen_clear()
			this_location()
		elif "medics" in player_input:
			screen_clear()
			player1.use_medics()
		elif "quit" in player_input:
			screen_clear()
			start_menu()
		elif "diary" in player_input:
			screen_clear()
			use_diary()


		else: screen_clear()
		print("Can't handle your input!")
		player1.rest()

	def rest_unsafe(player):
		slow_print("\n\n" + player1.name + " trys to find a safe place and rests a while.\n")
		player_input = (input("\nType 'meal' to take a meal.\nType 'drink' to drink something.\nType 'carry on' to go further.\nType 'medics' to take some medics.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\n\n>"))
		if "meal" in player_input:
			player1.use_meals_unsafe()
		elif "drink" in player_input:
			player1.use_water_unsafe()
		elif "carry on" in player_input:
			this_location()
		elif "medics" in player_input:
			player1.use_medics_unsafe()
		elif "status" in player_input:
			player1.status_unsafe()
		elif "quit" in player_input:
			start_menu()

		else: print("Can't handle your input!")
		player1.rest_unsafe() 

	def rest_public(player):
		slow_print("\n\n" + player1.name + " takes place.\n")
		player_input = (input("\nType 'meal' to take a meal.\nType 'drink' to drink something.\nType 'carry on' to go further.\nType 'medics' to take some medics.\nType 'status' for your status.\nType 'quit' to go back to the start menu.\n\n>"))
		if "meal" in player_input:
			player1.use_meals_public()
		elif "drink" in player_input:
			player1.use_water_public()
		elif "carry on" in player_input:
			this_location()
		elif "medics" in player_input:
			player1.use_medics_public()
		elif "status" in player_input:
			player1.status_public()
		elif "quit" in player_input:
			start_menu()

		else: print("Can't handle your input!")
		player1.rest_public()

	def sleep(player):
		
		if player.health <= player.max_health - 100:
			slow_print(player1.name + " goes to bed!\n")
			player.health = player.health + 100
			player.hunger = player.hunger - 8
			player.thirst = player.thirst - 11
			if player.hunger < 1:
				slow_print(player.name + " starved to death!\nTry to get some food the next time.\n")
				credits()
			if player.thirst <= 1:
				slow_print(player.name + " died of thirst!\nTry to get something to drink the next time.\n")
				credits()
			else: player1.rest()
				

		elif player.health == player.max_health:
			slow_print(player.name + " dont need feel tired.\n\n")
			player1.rest()

		else: player.health = player.max_health
		slow_print(player.name + " goes to bed!\n")
		player.hunger = player.hunger - 4
		player.thirst = player.thirst - 6
		if player.hunger < 1:
				slow_print(player.name + " starved to death!\nTry to get some food the next time.\n")
				credits()
		if player.thirst <= 1:
				slow_print(player.name + " died of thirst!\nTry to get something to drink the next time.\n")
				credits()
		player1.rest()

	def use_medics(player):
		if player.health == player.max_health:
			slow_print(player1.name + " dont need medics")
			player1.rest()
		elif player.medics > 0:
			slow_print(player.name + " takes some healing herbs.")
			player.health = min(player.max_health, player.health + 100)
			player.medics = player.medics - 1
			player1.rest()
		else: print(player1.name + " dont have anything to heal.")
		player1.rest()

	def use_medics_unsafe(player):
		if player.health == player.max_health:
			slow_print(player1.name + " dont need medics")
			player1.rest_unsafe()
		elif player.medics > 0:
			slow_print(player.name + " takes some healing herbs.")
			player.health = min(player.max_health, player.health + 100)
			player.medics = player.medics -1
			player1.rest_unsafe()
		else: print(player1.name + " dont have anything to heal.")
		player1.rest_unsafe()

	def use_medics_public(player):
		if player.health == player.max_health:
			slow_print(player1.name + " dont need medics")
			player1.rest_public()
		elif player.medics > 0:
			slow_print(player.name + " takes some healing herbs.")
			player.health = min(player.max_health, player.health + 100)
			player.medics = player.medics -1
			player1.rest_public()
		else: print(player1.name + " dont have anything to heal.")
		player1.rest_public()

	def use_meals(player):
		if player.hunger > 70:
			slow_print(player1.name + " is not hungry")
			player1.rest()
		elif player.hunger <= 70 and player.meals > 0:
			slow_print(player.name + " takes a meal.")
			player.hunger = player.hunger + 30
			player.meals = player.meals -1
			player1.rest()
		else: print(player1.name + " dont have anything to eat.")
		player1.rest()

	def use_meals_unsafe(player):
		if player.hunger > 70:
			slow_print(player1.name + " is not hungry")
			player1.rest_unsafe()
		elif player.hunger <= 70 and player.meals > 0:
			slow_print(player.name + " takes a meal.")
			player.hunger = player.hunger + 30
			player.meals = player.meals -1
			player1.rest_unsafe()
		else: print(player1.name + " dont have anything to eat.")
		player1.rest_unsafe()

	def use_meals_public(player):
		if player.hunger > 70:
			slow_print(player1.name + " is not hungry")
			player1.rest_public()
		elif player.hunger <= 70 and player.meals > 0:
			slow_print(player.name + " takes a meal.")
			player.hunger = player.hunger + 30
			player.meals = player.meals -1
			player1.rest_public()
		else: print(player1.name + " dont have anything to eat.")
		
		player1.rest_public()

	def use_water(player):
		if player.thirst > 80:
			slow_print(player1.name + " is not thirsty")
			player1.rest()
		elif player.hunger <= 80 and player.water > 0:
			slow_print(player.name + " takes a drink.")
			player.thirst = player.thirst + 20
			player.water = player.water -1
			player1.rest()
		else: print(player1.name + " dont have anything to drink.")
		player1.rest()

	def use_water_unsafe(player):
		if player.thirst > 80:
			slow_print(player1.name + " is not hungry")
			player1.rest_unsafe()
		elif player.thirst <= 80 and player.water > 0:
			slow_print(player.name + " takes a drink.")
			player.thirst = player.thirst + 20
			player.water = player.water -1
			player1.rest_unsafe()
		else: print(player1.name + " dont have anything to drink.")
		player1.rest_unsafe()

	def use_water_public(player):
		if player.thirst > 80:
			slow_print(player1.name + " is not hungry")
			player1.rest_public()
		elif player.thirst <= 80 and player.water > 0:
			slow_print(player.name + " takes a drink.")
			player.thirst = player.thirst + 20
			player.water = player.water -1
			player1.rest_public()
		else: print(player1.name + " dont have anything to drink.")
		player1.rest_public()

	def status(player):
		slow_print("\n" + player.name + "'s Health is at " + str(player.health) + "/" + str(player.max_health) + " points.\nThere are " + str(player1.medics) + " herbs in a pouch, " + str(player1.meals) + " meals, " + str(player1.water) + " bottles of water, " + str(player.gold) + " gold pieces and "+ str(player.fur) + " furs in his bag.\n")
		slow_print(player.name + "'s hunger is at " + str(player.hunger) + " points.\n")
		slow_print(player.name + "'s thirst is at " + str(player.thirst) + " points.\n")
		slow_print(player.name + "'s strenght is at " + str(player.strenght) + " points.\n")
		slow_print(player.name + "'s agility is at " + str(player.agility) + " points.\n")
		slow_print(player.name + " has a " + str.lower(player.weapon[1]) + " in his hand." + "\n\n")
		player1.rest()

	def status_unsafe(player):
		slow_print("\n" + player.name + "'s Health is at " + str(player.health) + "/" + str(player.max_health) + " points.\nThere are " + str(player1.medics) + " herbs in a pouch, " + str(player1.meals) + " meals, " + str(player1.water) + " bottles of water, " + str(player.gold) + " gold pieces and "+ str(player.fur) + " furs in his bag.\n")
		slow_print(player.name + "'s hunger is at " + str(player.hunger) + " points.\n")
		slow_print(player.name + "'s thirst is at " + str(player.thirst) + " points.\n")
		slow_print(player.name + "'s strenght is at " + str(player.strenght) + " points.\n")
		slow_print(player.name + "'s agility is at " + str(player.agility) + " points.\n")
		slow_print(player.name + " has a " + str.lower(player.weapon[1]) + " in his hand." + "\n\n")
		player1.rest_unsafe()

	def status_public(player):
		slow_print("\n" + player.name + "'s Health is at " + str(player.health) + "/" + str(player.max_health) + " points.\nThere are " + str(player1.medics) + " herbs in a pouch, " + str(player1.meals) + " meals, " + str(player1.water) + " bottles of water, " + str(player.gold) + " gold pieces and "+ str(player.fur) + " furs in his bag.\n")
		slow_print(player.name + "'s hunger is at " + str(player.hunger) + " points.\n")
		slow_print(player.name + "'s thirst is at " + str(player.thirst) + " points.\n")
		slow_print(player.name + "'s strenght is at " + str(player.strenght) + " points.\n")
		slow_print(player.name + "'s agility is at " + str(player.agility) + " points.\n")
		slow_print(player.name + " has a " + str.lower(player.weapon[1]) + " in his hand." + "\n\n")
		player1.rest_public()
