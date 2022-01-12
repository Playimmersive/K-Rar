###                      Combatsystem "player as attacker" part 1/2 attacker_round                  ###

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
        slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n\n")
        if defender.health <= 0:
          defender.alive = False
          print(defender.name + " has been slained!\n")
          after_combat()

      elif random.choice(result) == 2:
        hitpoints = attacker.strenght * attacker.weapon[0] + 10
        defender.health = max(0, defender.health - hitpoints)
        slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n\n")

        if defender.health <= 0:
          defender.alive = False
          slow_print(defender.name + " has been slained!\n")
          after_combat()

      elif random.choice(result) == 3:
        hitpoints = attacker.strenght * attacker.weapon[0] + 2
        attacker.health = max(0, attacker.health - hitpoints)
        slow_print("Oh no, " + attacker.name +  " harmed himself!\nHe needs a moment to regain his composure!\n\n")
        slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n\n")

        if attacker.health <= 0:
          attacker.alive = False
          after_combat()

      elif random.choice(result) == 4:
        hitpoints = attacker.strenght * attacker.weapon[0] + 2
        defender.health = max(0, defender.health - hitpoints / 2)
        slow_print(defender.name + " could soften the blow a bit!\n")
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n\n")

        if defender.health <= 0:
          defender.alive = False
          slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n\n")
          after_combat()

      else: print("Oh no, " + attacker.name + " missed.\nHe stumbles around!\n")



    ###                    Combatsystem 'player as attacker' part2/2 "defender_round"                ###

    if random.choice(result) == 1:
      hitpoints = defender.strenght * defender.weapon[0]
      attacker.health = max(0, attacker.health - hitpoints)
      slow_print(defender.name + " swings his " +  str.lower(defender.weapon[1]) + " and hits the opponent with " + str(hitpoints) + (" hitpoints."))
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    elif random.choice(result) == 2:
      hitpoints = defender.strenght * defender.weapon[0] + 10
      attacker.health = max(0, attacker.health - hitpoints)
      slow_print("What a heavy punch.\n"+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    elif random.choice(result) == 3:
      hitpoints = defender.strenght * defender.weapon[0] + 2
      defender.health = max(0, defender.health - hitpoints)
      slow_print("Hard to belive but, " + defender.name +  " harmed himself!\n\n")
      slow_print("(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n\n" )

      if defender.health <= 0:
        defender.alive = False
        slow_print(defender.name + " has slained himself!\n")
        after_combat()
    
    elif random.choice(result) == 4:
      hitpoints = defender.strenght * defender.weapon[0] + 2
      attacker.health = max(0, attacker.health - hitpoints / 2)
      slow_print(attacker.name + " could soften the blow a bit!\n\n")
      slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

      if attacker.health <= 0:
        attacker.alive = False
        after_combat()

    
    else: slow_print("What a luck, " + defender.name + " missed " + attacker.name + ".\n" + defender.name + " stumbles around!\n")

###                           Combat Animal                         ###

def combat_animal(attacker, defender):

  global loot_fur_animal

  loot_fur_animal = defender.fur
  attacker.hunger = attacker.hunger - 4
  attacker.thirst = attacker.thirst - 5
  import random
  result = range(0,5)
  fight = True  
  while fight :

    if defender.alive == False:
      slow_print("The animal is dead.")
      this_location()
    else: 
      if random.choice(result) == 1:
        hitpoints = attacker.strenght * attacker.weapon[0]
        defender.health = max(0, defender.health - hitpoints)
        slow_print("That was a good strike.\n" + attacker.name + " hit's his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints)\n\n")
        if defender.health <= 0:
          defender.alive = False
          print(defender.name + " has been slained!\n")
          after_combat_animal()

      elif random.choice(result) == 2:
        hitpoints = attacker.strenght * attacker.weapon[0] + 10
        defender.health = max(0, defender.health - hitpoints)
        slow_print("That was intense, you could hear some bones breaking!\n"+ attacker.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n\n")

        if defender.health <= 0:
          defender.alive = False
          slow_print(defender.name + " has been slained!\n")
          after_combat_animal()

      elif random.choice(result) == 3:
        hitpoints = attacker.strenght * attacker.weapon[0] + 2
        attacker.health = max(0, attacker.health - hitpoints)
        slow_print("Oh no, " + attacker.name +  " harmed himself!\nHe needs a moment to regain his composure!\n")
        slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints)\n\n")

        if attacker.health <= 0:
          attacker.alive = False
          after_combat_animal()

      elif random.choice(result) == 4:
        hitpoints = attacker.strenght * attacker.weapon[0] + 2
        defender.health = max(0, defender.health - hitpoints / 2)
        slow_print(defender.name + " could soften the blow a bit!\n")
        slow_print("\n(" + defender.name + " has " + str(defender.health) + " healthpoints.)\n\n")

        if defender.health <= 0:
          defender.alive = False
          slow_print("It was still not enough to escape the death blow " + defender.name + " where slained!\n")
          after_combat_animal()

      elif random.choice(result) == 0:
        print("Oh no, " + attacker.name + " missed.\nHe stumbles around!\n\n")




    ###                    Combatsystem 'player as attacker' part2/2 "defender_round"                ###

      if random.choice(result) == 1:
        hitpoints = defender.strenght * defender.weapon[0]
        attacker.health = max(0, attacker.health - hitpoints)
        slow_print("The " + defender.name + " hits his opponent with his " +  str.lower(defender.weapon[1]) + " with " + str(hitpoints) + (" hitpoints."))
        slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

        if attacker.health <= 0:
          attacker.alive = False
          after_combat_animal()

      elif random.choice(result) == 2:
        hitpoints = defender.strenght * defender.weapon[0] + 10
        attacker.health = max(0, attacker.health - hitpoints)
        slow_print("That was horrorble.\nThe "+ defender.name + " hit his enemy with " + str(hitpoints) + (" hitpoints.\n\n"))
        slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

        if attacker.health <= 0:
          attacker.alive = False
          after_combat_animal()

      elif random.choice(result) == 3:
        hitpoints = defender.strenght * defender.weapon[0] + 2
        defender.health = max(0, defender.health - hitpoints)
        slow_print("The " + defender.name +  " harmed himself!\n")
        slow_print("(The " + defender.name + " has " + str(defender.health) + " healthpoints.)\n\n" )

        if defender.health <= 0:
          defender.alive = False
          slow_print("The " + defender.name + " has slained himself!\n\n")
          after_combat_animal()
    
      elif random.choice(result) == 4:
        hitpoints = defender.strenght * defender.weapon[0] + 2
        attacker.health = max(0, attacker.health - hitpoints / 2)
        slow_print(attacker.name + " could soften the blow a bit!\n\n")
        slow_print("\n(" + attacker.name + " has " + str(attacker.health) + " healthpoints.)\n\n")

        if attacker.health <= 0:
          attacker.alive = False
          after_combat_animal()

    
      elif  random.choice(result) == 0:
        slow_print("What a luck, the " + defender.name + " missed " + attacker.name + ".\n\n")

       
###                           After Combat                          ###

def after_combat():
  if player1.alive == True:
    player1.gold = player1.gold + loot_gold
    player1.medics = player1.medics + loot_medics
    player1.meals = player1.meals + loot_meals
    player1.water = player1.water + loot_water
    player1.fur = player1.fur + loot_fur
    print(player1.name + " won this battle.\n" + player1.name + " collected  " + str(loot_medics) + " herbs, " + str(loot_meals) + " meals, " + str(loot_water) + " bottles of water and " + str(loot_gold) + " pieces of gold, now are " + str(player1.gold) + " pieces of gold in " + player1.name + "'s bag.")
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
  print(input("Press enter\n>"))
  credits()

    
###                           After Combat Animal                         ###

def after_combat_animal():
  if player1.alive == True:
    player1.fur = player1.fur + loot_fur_animal
    print(player1.name + " won this battle.\n" + player1.name + " collected  " + str(loot_fur_animal) + "pieces of usable fur.\n" + "Now are " + str(player1.fur) + " pieces of fur in " + player1.name + "'s bag.")
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
  print(input("Press enter\n>"))
  credits()
