### chose_combat_long
def chose_combat_long():
	global set_attacker
	global set_defender
	
	attacker = set_attacker
	defender = set_defender
	if player1.weapon == dagger:
		combat_short_weapon(attacker, defender)
	if player1.weapon == sharped_dagger:
		combat_short_weapon(attacker, defender)
	if player1.weapon == log:
		combat(attacker, defender)
	if player1.weapon == sword:
		combat(attacker, defender)
	if player1.weapon == guard_sword:
		combat(attacker, defender)



### chose_combat_short
def chose_combat_short():
	global set_attacker
	global set_defender
	
	attacker = set_attacker
	defender = set_defender
	if player1.weapon == dagger:
		combat_short_weapon_ad(attacker, defender)
	if player1.weapon == sharped_dagger:
		combat_short_weapon_ad(attacker, defender)
	if player1.weapon == log:
		combat_short_weapon_d(attacker, defender)
	if player1.weapon == sword:
		combat_short_weapon_d(attacker, defender)
	if player1.weapon == guard_sword:
		combat_short_weapon_d(attacker, defender)

### chose_combat_animal
def chose_combat_animal():
	global set_attacker
	global set_defender
	
	attacker = set_attacker
	defender = set_defender
	if player1.weapon == dagger:
		combat_animal_short(attacker, defender)
	if player1.weapon == sharped_dagger:
		combat_animal_short(attacker, defender)
	if player1.weapon == log:
		combat_animal(attacker, defender)
	if player1.weapon == sword:
		combat_animal(attacker, defender)
	if player1.weapon == guard_sword:
		combat_animal(attacker, defender)



### Combatsystem "player as attacker" part 1/2 attacker_round ###

		
def combat(attacker, defender):
	global loot_gold
	global loot_medics
	global loot_meals
	global loot_water
	global loot_fur
	loot_gold = defender.gold
	loot_medics = defender.medics
	loot_meals = defender.meals
	loot_water = defender.water
	loot_fur = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True	
	while fight :
		
		if defender.alive == False:
			slow_print("Your opponend is dead.")
			this_location()
		else:		 
			if random.choice(result) == 1:
				hitpoints = attacker.strenght * attacker.weapon[0]
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
				if defender.health <= 0:
					defender.alive = False
					print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.weapon[0]
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat()

			elif random.choice(result) == 3:
				hitpoints = attacker.strenght * attacker.weapon[0] - 1
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself!\nHe needs a moment to regain his composure!")
				slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] / 2
				defender.health = max(0, defender.health - hitpoints)
				slow_print("It was just a light hit, " + defender.name + " is only slightly injured!")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n\n")
					after_combat()

			else: slow_print("\nOh no, " + attacker.name + " missed.\nHe stumbles around!\n------------------------------------\n\n")



### Combatsystem 'player as attacker' part2/2 "defender_round" ###

		if random.choice(result) == 1:
			hitpoints = defender.strenght * defender.weapon[0]
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print(defender.name + " swings his " +	str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + " hitpoints!")
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		elif random.choice(result) == 2:
			hitpoints = defender.strenght * defender.weapon[0] + defender.weapon[0]
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		elif random.choice(result) == 3:
			hitpoints = defender.strenght * defender.weapon[0] - 1
			defender.health = max(0, defender.health - hitpoints)
			slow_print("Hard to belive but, " + defender.name +	" harmed himself with " + str(hitpoints) + " hitpoints!")
			slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

			if defender.health <= 0:
				defender.alive = False
				slow_print(defender.name + " has slained himself!\n------------------------------------\n\n")
				after_combat()
		
		elif random.choice(result) == 4:
			hitpoints = defender.strenght * defender.weapon[0] / 2
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print(attacker.name + " could soften the blow a bit!\n" + defender.name + " hit his enemy with " + str(hitpoints) + " hitpoints.")
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		
		else: slow_print("What a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n------------------------------------\n\n")

### Combat Animal ###

def combat_animal(attacker, defender):
	
	global loot_fur_animal

	loot_fur_animal = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True
	if defender.alive == True:
		slow_print("The " + defender.name + " attacks " + attacker.name + "!\n\n")
	while fight :

		if defender.alive == False:
			slow_print("The animal is dead.\n------------------------------------\n\n")
			this_location()
		else:


			if random.choice(result) == 1:
				hitpoints = attacker.strenght * attacker.weapon[0]
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was a good strike.\n" + attacker.name + " hit's the " + defender.name +" with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
				if defender.health <= 0:
					defender.alive = False
					print(defender.name + " has been slained!\n------------------------------------\n\n")
					after_combat_animal()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.weapon[0]
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!\n------------------------------------\n\n")
					after_combat_animal()

			elif random.choice(result) == 3:
				hitpoints = attacker.strenght * attacker.weapon[0] - 1
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself!\nHe needs a moment to regain his composure!\n" + attacker.name + " hit himself with " + str(hitpoints) + " hitpoints.")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat_animal()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] / 2
				defender.health = max(0, defender.health - hitpoints)
				slow_print("It was just a light hit, the " + defender.name + " is only slightly injured!\n" + attacker.name + " hit his enemy with " + str(hitpoints) + " hitpoints.")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n------------------------------------\n\n")
					after_combat_animal()

			elif random.choice(result) == 0:
				slow_print("\n\nOh no, " + attacker.name + " missed.\nHe stumbles around!\n------------------------------------\n\n")




### Combatsystem 'player as attacker' part2/2 "defender_round" ###

			if random.choice(result) == 1:
				hitpoints = defender.strenght * defender.weapon[0]
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("The " + defender.name + " hits his opponent with his " +	str.lower(defender.weapon[1]) + " with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat_animal()

			elif random.choice(result) == 2:
				hitpoints = defender.strenght * defender.weapon[0] + defender.weapon[0]
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("That was horrorble.\nThe "+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat_animal()

			elif random.choice(result) == 3:
				hitpoints = defender.strenght * attacker.weapon[0] + attacker.strenght
				defender.health = max(0, defender.health - hitpoints)
				slow_print("The " + defender.name +	" runs into the "+ player1.weapon[1] + " from " + player1.name + "!")
				slow_print("\n\n(The " + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

				if defender.health <= 0:
					defender.alive = False
					slow_print("The " + defender.name + " is slained!\n------------------------------------\n\n")
					after_combat_animal()
		
			elif random.choice(result) == 4:
				hitpoints = defender.strenght * defender.weapon[0] / 2
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("It was just a light hit, " + attacker.name + " is only slightly injured!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat_animal()

		
			elif	random.choice(result) == 0:
				slow_print("What a luck, the " + defender.name + " missed " + attacker.name + ".\n------------------------------------\n\n")


				
### combat_animal_short


def combat_animal_short(attacker, defender):
	
	global loot_fur_animal

	loot_fur_animal = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True
	if defender.alive == True:
		slow_print("The " + defender.name + " attacks " + attacker.name + "!\n\n")
	while fight :

		if defender.alive == False:
			slow_print("Your opponend is dead.")
			this_location()
		else:
			

			i = 0
		while i < attacker.agility:
			i +=1
			if random.choice(result) == 1:
				
					hitpoints = attacker.strenght * attacker.weapon[0]
					defender.health = max(0, defender.health - hitpoints)
					slow_print("That was a good strike.\n" + attacker.name + " hit's the " + defender.name + " with " + str(hitpoints) + (" hitpoints."))
					slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
					if defender.health <= 0:
						defender.alive = False
						print(defender.name + " has been slained!n------------------------------------\n\n")
						after_combat_animal()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.weapon[0]
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with	" + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat_animal()

			elif random.choice(result) == 3:
				hitpoints =	attacker.strenght * attacker.weapon[0] - 1
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself!\nHe needs a moment to regain his composure!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat_animal()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints / 2)
				slow_print("It was just a light hit, the " + defender.name + " is only slightly injured!")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!n------------------------------------\n\n")
					after_combat_animal()

			else: slow_print("\nOh no, " + attacker.name + " missed.\nHe stumbles around!\n------------------------------------\n")



### Combatsystem 'player as attacker' part2/2 "defender_round" ###

		if random.choice(result) == 1:
			hitpoints = defender.strenght * defender.weapon[0]
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print(defender.name + " swings his " +	str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
			slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat_animal()

		elif random.choice(result) == 2:
			hitpoints = defender.strenght * defender.weapon[0] + defender.weapon[0]
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print("That was horrobile.\n" + defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat_animal()

		elif random.choice(result) == 3:
			hitpoints = defender.strenght * attacker.weapon[0] + attacker.strenght
			defender.health = max(0, defender.health - hitpoints)
			slow_print("The " + defender.name +	" runs into the "+ player1.weapon[1] + " from " + player1.name + "!")
			slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

			if defender.health <= 0:
				defender.alive = False
				slow_print(defender.name + " has slained himself!n------------------------------------\n\n")
				after_combat_animal()
		
		elif random.choice(result) == 4:
			hitpoints = defender.strenght * defender.weapon[0] + 2
			attacker.health = max(0, attacker.health - hitpoints / 2)
			slow_print("It was just a light hit, " + attacker.name + " is only slightly injured!" + attacker.name + " where harmed by "+ str(hitpoints) +" hitpoints.")
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat_animal()

		
		else: slow_print("\nWhat a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n------------------------------------\n")



				
### Combat_short_weapons

def combat_short_weapon(attacker, defender):
	global loot_gold
	global loot_medics
	global loot_meals
	global loot_water
	global loot_fur
	loot_gold = defender.gold
	loot_medics = defender.medics
	loot_meals = defender.meals
	loot_water = defender.water
	loot_fur = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True	
	while fight :
		
		if defender.alive == False:
			slow_print("Your opponend is dead.")
			this_location()
		else:

			i = 0
		while i < attacker.agility:
			i +=1
			if random.choice(result) == 1:
				
					hitpoints = attacker.strenght * attacker.weapon[0]
					defender.health = max(0, defender.health - hitpoints)
					slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " +str(hitpoints) + (" hitpoints."))
					slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
					if defender.health <= 0:
						defender.alive = False
						print(defender.name + " has been slained!n------------------------------------\n\n")
						after_combat()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.strenght
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with	" + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat()

			elif random.choice(result) == 3:
				hitpoints =	attacker.strenght * attacker.weapon[0] + (attacker.strenght / 2)
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself with" + str(hitpoints) + " hitpoints!\nHe needs a moment to regain his composure!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints / 2)
				slow_print(defender.name + " could soften the blow a bit!\n")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n\n")
					after_combat()

			else: slow_print("\nOh no, " + attacker.name + " missed.\nHe stumbles around!\n------------------------------------\n")



 ### Combatsystem 'player as attacker' part2/2 "defender_round" ###

		if random.choice(result) == 1:
			hitpoints = defender.strenght * defender.weapon[0]
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print(defender.name + " swings his " +	str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		elif random.choice(result) == 2:
			hitpoints = defender.strenght * defender.weapon[0] + 10
			attacker.health = max(0, attacker.health - hitpoints)
			slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		elif random.choice(result) == 3:
			hitpoints = defender.strenght * defender.weapon[0] + 2
			defender.health = max(0, defender.health - hitpoints)
			slow_print("Hard to belive but, " + defender.name +	" harmed himself!")
			slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

			if defender.health <= 0:
				defender.alive = False
				slow_print(defender.name + " has slained himself!n------------------------------------\n\n")
				after_combat()
		
		elif random.choice(result) == 4:
			hitpoints = defender.strenght * defender.weapon[0] + 2
			attacker.health = max(0, attacker.health - hitpoints / 2)
			slow_print(attacker.name + " could soften the blow a bit!" + attacker.name + " where harmed by "+ str(hitpoints) +" hitpoints.")
			slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

			if attacker.health <= 0:
				attacker.alive = False
				after_combat()

		
		else: slow_print("\nWhat a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around\n------------------------------------\n")

# combat_short_weapon_ad

def combat_short_weapon_ad(attacker, defender):
	global loot_gold
	global loot_medics
	global loot_meals
	global loot_water
	global loot_fur
	loot_gold = defender.gold
	loot_medics = defender.medics
	loot_meals = defender.meals
	loot_water = defender.water
	loot_fur = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True	
	while fight :
		
		if defender.alive == False:
			slow_print("Your opponend is dead.")
			this_location()
		else:

			i = 0
		while i < attacker.agility:
			i +=1

			if random.choice(result) == 1:
				
					hitpoints = attacker.strenght * attacker.weapon[0]
					defender.health = max(0, defender.health - hitpoints)
					slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " +str(hitpoints) + (" hitpoints."))
					slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
					if defender.health <= 0:
						defender.alive = False
						print(defender.name + " has been slained!n------------------------------------\n\n")
						after_combat()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.strenght
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with	" + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat()

			elif random.choice(result) == 3:
				hitpoints =	attacker.strenght * attacker.weapon[0] + (attacker.strenght / 2)
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself!\nHe needs a moment to regain his composure!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints / 2)
				slow_print(defender.name + " could soften the blow a bit!")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n------------------------------------\n\n")
					after_combat()

			else: slow_print("\nOh no, " + attacker.name + " missed.\nHe stumbles around!n------------------------------------\n\n")



 ### Combatsystem 'player as attacker' part2/2 "defender_round" ###
		j = 0
		while j < defender.agility:
			j +=1
			if random.choice(result) == 1:
				hitpoints = defender.strenght * defender.weapon[0]
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print(defender.name + " swings his " +	str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 2:
				hitpoints = defender.strenght * defender.weapon[0] + 10
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 3:
				hitpoints = defender.strenght * defender.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints)
				slow_print("Hard to belive but, " + defender.name +	" harmed himself!")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has slained himself!n------------------------------------\n\n")
					after_combat()
		
			elif random.choice(result) == 4:
				hitpoints = defender.strenght * defender.weapon[0] + 2
				attacker.health = max(0, attacker.health - hitpoints / 2)
				slow_print("It was just a light hit, " + attacker.name + " is only slightly injured!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

		
			else: slow_print("What a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n------------------------------------\n")


# combat_short_weapon_d

def combat_short_weapon_d(attacker, defender):
	global loot_gold
	global loot_medics
	global loot_meals
	global loot_water
	global loot_fur
	loot_gold = defender.gold
	loot_medics = defender.medics
	loot_meals = defender.meals
	loot_water = defender.water
	loot_fur = defender.fur
	attacker.hunger = attacker.hunger - 4
	attacker.thirst = attacker.thirst - 5
	import random
	result = range(0,5)
	fight = True	
	while fight :
		
		if defender.alive == False:
			slow_print("Your opponend is dead.")
			this_location()
		else:


			if random.choice(result) == 1:
				
					hitpoints = attacker.strenght * attacker.weapon[0]
					defender.health = max(0, defender.health - hitpoints)
					slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " +str(hitpoints) + (" hitpoints."))
					slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")
					if defender.health <= 0:
						defender.alive = False
						print(defender.name + " has been slained!n------------------------------------\n\n")
						after_combat()

			elif random.choice(result) == 2:
				hitpoints = attacker.strenght * attacker.weapon[0] + attacker.strenght
				defender.health = max(0, defender.health - hitpoints)
				slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with	" + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has been slained!n------------------------------------\n\n")
					after_combat()

			elif random.choice(result) == 3:
				hitpoints =	attacker.strenght * attacker.weapon[0] + (attacker.strenght / 2)
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("Oh no, " + attacker.name +	" harmed himself!\nHe needs a moment to regain his composure!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 4:
				hitpoints = attacker.strenght * attacker.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints / 2)
				slow_print(defender.name + " could soften the blow a bit!")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n------------------------------------\n\n")

				if defender.health <= 0:
					defender.alive = False
					slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n\n")
					after_combat()

			else: slow_print("\nOh no, " + attacker.name + " missed.\nHe stumbles around!\n------------------------------------\n\n")



		### Combatsystem 'player as attacker' part2/2 "defender_round" ###
		i = 0
		while i < defender.agility:
			i +=1
			if random.choice(result) == 1:
				hitpoints = defender.strenght * defender.weapon[0]
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print(defender.name + " swings his " +	str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 2:
				hitpoints = defender.strenght * defender.weapon[0] + 10
				attacker.health = max(0, attacker.health - hitpoints)
				slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints."))
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

			elif random.choice(result) == 3:
				hitpoints = defender.strenght * defender.weapon[0] + 2
				defender.health = max(0, defender.health - hitpoints)
				slow_print("Hard to belive but, " + defender.name +	" harmed himself with " + str(hitpoints) + " hitpoints.")
				slow_print("\n\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n------------------------------------\n\n" )

				if defender.health <= 0:
					defender.alive = False
					slow_print(defender.name + " has slained himself!\n")
					after_combat()
		
			elif random.choice(result) == 4:
				hitpoints = defender.strenght * defender.weapon[0] + 2
				attacker.health = max(0, attacker.health - hitpoints / 2)
				slow_print(attacker.name + " could soften the blow a bit!")
				slow_print("\n\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n------------------------------------\n\n")

				if attacker.health <= 0:
					attacker.alive = False
					after_combat()

		
			else: slow_print("\nWhat a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n------------------------------------\n")

			 
### After Combat ###

def after_combat():
	if player1.alive == True:
		player1.gold = player1.gold + loot_gold
		player1.medics = player1.medics + loot_medics
		player1.meals = player1.meals + loot_meals
		player1.water = player1.water + loot_water
		player1.fur = player1.fur + loot_fur
		print(player1.name + " won this battle.\n" + player1.name + " collected	" + str(loot_medics) + " herbs, " + str(loot_meals) + " meals, " + str(loot_water) + " bottles of water and " + str(loot_gold) + " pieces of gold, now are " + str(player1.gold) + " pieces of gold in " + player1.name + "'s bag.")
		this_location()


	else: slow_print("It was a hard fight but not enough to escape the death blow!\n" + player1.name + " where slained!\n")
	if player1.hunger <= 0:
		slow_print(player.name + " starved to death!")
		player1.alive = False
		credits()
	if player1.thirst <= 0:
		slow_print(player.name + " died of thirst!")
		player1.alive = False
		credits()
	print(input("\n>"))
	credits()

		
### After Combat Animal ###

def after_combat_animal():
	if player1.alive == True:
		player1.fur = player1.fur + loot_fur_animal
		print(player1.name + " won this battle.\n" + player1.name + " collected	" + str(loot_fur_animal) + " pieces of usable fur.\n" + "Now are " + str(player1.fur) + " pieces of fur in " + player1.name + "'s bag.")
		this_location()


	else: slow_print("It was a hard fight but not enough to escape the death blow!\n" + player1.name + " where slained!\n------------------------------------\n")
	if player1.hunger <= 0:
		slow_print(player.name + " starved to death!")
		player1.alive = False
		credits()
	if player1.thirst <= 0:
		slow_print(player.name + " died of thirst!")
		player1.alive = False
		credits()
	print(input("Press enter\n>"))
	credits()
