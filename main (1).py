print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your adventurous mentality led you to this mysterious island after hearing rumors of treasure.") 
print("You start your adventure by walking into the woods.")
choice1 = input("You see two paths. Which path do you choose? 'left' or 'right: ").lower()
if choice1 == 'left':
  print("As you keep walking down this path, you see something crawl out of the nearby bush.")
  choice2 = input("A crawler comes out and attacks you. You have two items on you. Type 'torch' to scare away the crawler. Type 'axe' to use your axe.: ").lower()
  if choice2 == 'torch':
    print("The crawler is afraid of the fire. You are able to escape from it and you soon arrive at lake with an island in the middle.")
    choice3 = input("Type 'swim' to jump into the water and swim to the island. Type 'build' to build a raft out of wood.: ").lower()
    if choice3 == 'build':
      print("You build a raft and slowly drift yourself onto the island.")
      choice4 = input("You arrive on the island. There are 3 chests. Type 'blue' to open the blue chest. Type 'red' to open the red chest. Type 'yellow' to open the yellow chest.: ").lower()
      if choice4 == 'yellow':
        print("You have found the mystery treasure. As you open the chest slowly it reveals...a piece of paper that will grant one wish...You win! Good luck!")
      elif choice4 == 'blue':
        print("You get cursed with 10000000 years of bad luck. Game over.")
      elif choice4 == 'red':
        print("You get sucked into the chest thus trapping you in a chest for centuries. Game over.")
      else:
        print("You didnt choose a chest and walk away with nothing. Game over.")
    
    
  

      
    
    else:
      print("You get sucked into a vortex and perish. Game over.")
  else: 
    print("The crawler is not affected by the strike and attacks you. Game over.")
else:
  print("As you walk down this path, you step on a trapdoor, which sends you falling into a pit. Game over")

