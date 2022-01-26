def dialog_bandit1():
  slow_print("\nI told you to fuck off, " + player1.name + "!\nI will kill you if you don't go.\n\n")
  player_input = (input("Type 'city' to ask him about Felzur.\nType 'profession' to ask him about his profession.\nType 'thats all' to end the conversation.\n>"))
  if "city" in player_input:
    slow_print("\nAre you stupid or what?\n\n")
    input("\n>")
    dialog_bandit1()
  if "profession" in player_input:
    slow_print("\nI have no profession idiot.\n\n")
    input("\n>")
    dialog_bandit1()
  if "thats all" in player_input:
    slow_print("\n" + player1.name + " ends the conversation.\n\n")
    input("\n>")
    this_location()



def dialog_bandit2():
  slow_print("\nWhat do you want from me " + player1.name + ".\nThis is no place for bums like you, fuck off back where you came from.\n\n")
  player_input = (input("Type 'city' to ask him about Felzur.\nType 'profession' to ask him about his profession.\nType 'thats all' to end the conversation.\n>"))
  if "city" in player_input:
    slow_print("\nThis city is a poor prison, thats all I can say to you " + player1.name + "!\nI think its time for you to leave.\n")
    input("\n>")
    dialog_bandit2()
  if "profession" in player_input:
    slow_print("\nMy name is " + bandit2.name + " and I am a merchanary from Gundar Grelaf's army.\nYou should go now.\n\n")
    input("\n>")
    dialog_bandit2()
  if "thats all" in player_input:
    slow_print("\n" + player1.name + " ends the conversation.\n\n")
    input("\n>")
    this_location()


def dialog_barkeeper1():
  slow_print("\nWelome to my bar " + player1.name + ". Are you sure you're allowed to come here?\n\n")
  player_input = (input("Type 'city' to ask him about Felzur.\nType 'work' to ask him about some work.\nType 'thats all' to end the conversation.\n>"))
  if "city" in player_input:
    slow_print("\nSlaves like you are likely to commit suicide,\nor they try to escape this ice hell by wandering through the frozen Felzur passage.\n")
    input("\n>")
    dialog_barkeeper1()

  if "work" in player_input:
    slow_print("\nSlaves are not allowed to work for anyone else but their master.\nBut you could try selling wolf pelts in the marketplace, no one will ask where you got them if they have the opportunity to buy them cheaply.\nIts similar with medicinal herbs and other essentials.\n\n")
    input("\n>")
    dialog_barkeeper1()
    
  if "thats all" in player_input:
    slow_print("\n" + player1.name + " ends the conversation.\n\n")
    input("\n>")
    this_location()
