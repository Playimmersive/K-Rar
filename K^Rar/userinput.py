import sys

# Optionen-Liste Vorbereiten
option_list = list()



def user_option(name, text, callback):
                                                  #OPTIONAL, Vor erstem Eintrag Ankündigung der Eingabe anzeigen
  if len(option_list) == 0: print("Choose an action what to do:")
  print("Type '", name, "' to ", text)
  option_list.append([name, callback])            #Der Optionen-Liste die Option hinzufügen
 


def user_prompt():
  i = 0
  print("")                                        #Eine Zeile Abstand
  choice =  input(">").trim().lower()              #Zeileneingabe Whitespace entfernen und Kleinschreibung erzwingen
  for option in option_list:
    i++                                            #Entweder den Befehl gefunden oder übereinstimmung der Nummer der Option
    if (option[0] == choice) OR (i == choice):
      option_list.clear()                          #Optionen-Liste löschen für nächste Abfrage
      return option[1]()                           #Callback-Funktion aufrufen
                                                   #Wenn keine Option gefunden wurde
  sys.stdout.write("\033[F")                       #OPTIONAL, nach oben springen
  print("Sorry I did not understand '", choice, "', please pick an action from above")
  return user_prompt()                             #Erneut abfragen



# Beispiel:
# user_option("enter", "Start the Game", start)
# user_option("leave", "Exit the Game", exit)
# user_prompt()
