### Print a welcome message
print("Welcome to the Haunted Mansion!")
print("You are a distant family member of a rich millionaire who has just passed way, leaving this mansion to you.")
print("As the newfound owner, you decide to pay a visit to the mansion.")
print("The house is dated, creaky, and falling apart. You walk in the front door.")
print("Do you want to enter the living room or the dining room?")

### Prompt user for a choice
roomChoice = input("> ")

if(roomChoice == "living room"):
  print("You enter the living room.")
  print("As you walk in, you see a sleeping pitbull guarding some gold jewelry.")
  print("Do you want to steal the jewelry from the pitbull?")

  pitBullChoice = input("> ")

  if(pitBullChoice == "yes"):
    print("You attempt to steal the jewelry, but it wakes up and rips you to shreds.")
    print("You are now dead.")
  elif(pitBullChoice == "no"):
    print("You decide to not steal the dog's jewelry.")
    print("You turn around and leave the house safely.")
  else:
    print("Invalid choice. Please enter yes or no.")
elif(roomChoice == "dining room"):
  print("You chose to go into the dining room.")
  print("As you walk in, you see a shiny vase on the table.")
  print("Do you want to open the vase?")

  vaseChoice = input("> ")

  if(vaseChoice == "yes"):
    print("You open the vase and find a pile of bones!")
  elif(vaseChoice == "no"):
    print("You decide not to open the shiny vase.")
    print("As you turn to leave, you hear a cracking sound coming from the corner.")
    print("A dark figure with glowing red eyes launches at you, knocking you unconcious")
    print("You wake up in your bed. It was all a dream.")
  else:
    print("Invalid choice. Please enter yes or no.")
else:
  print("Invalid choice. Please enter living room or dining room.")
