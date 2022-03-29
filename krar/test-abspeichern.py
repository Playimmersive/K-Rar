def save():
		global player1
		eingabe = input("'1' Load\n'2' Safe\n'3' Show Name\n'4' Change name\n'5' Close")
	
		if eingabe == "1":
			with open('player_one_save.json', 'r') as player1_file:
				laden = json.load(player1_file, object_hook=lambda d: SimpleNamespace(**d))
				player1 = human (laden.location, laden.race, laden.nativity, laden.citizen, laden.name, laden.age, laden.health, laden.max_health, laden.hunger, laden.thirst, laden.strenght, laden.agility, laden.weapon, laden.gold, laden.fur, laden.medics, laden.meals, laden.water, laden.alive)
		elif eingabe == "2":
			with open("player_one_save.json","w") as speicher:
				json.dump(vars(player1),speicher)
		elif eingabe == "3":
			player1.show_name()
			
		elif eingabe == "4":
			player1.change_name()

		elif eingabe == "5":
			sys.exit()
		else:
			print("Befehl nicht erkannt!")