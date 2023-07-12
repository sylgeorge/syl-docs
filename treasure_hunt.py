import os

os.system('cls||clear')

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

def end_of_game():
 print("oops! you are dead,\nGAME OVER!")
 quit()

print("Welcome to Treasure Hunt.")
print("Your mission is to find your way to the treasure forest and get the treasure") 

cross_road = input("You are at a cross road, which way do you choose to go? type 'left' or 'right'\n").lower()
if cross_road == "left":
 
 path = input("You have arrived at the beginning of a tunnel with 3 different entrances. which path do you wish to take? type 'first', 'second' or 'third'\n").lower()
 if path == "first":
  print("Oops! You entered a room filled with traps that are inescapeable.\nGAME OVER!")
  quit()
 elif path == "second":
    
  means_to_cross = input("You passed the tunnel unharmed, But you now find yourself in front of a river without crocodiles. type 'wait' to wait for a boat or type 'swim' to swim across the river.\n").lower()
  if means_to_cross == "wait":
   
   run_or_walk = input("You boarded a boat and you crossed the river safely. now you have to cover a long distance of 5km. Would you like to 'run' or 'walk'\n").lower()
   if run_or_walk == "run":
    print("Too bad, you fainted from exhaustion upon reaching your destination(the treasure forest) and was killed by a Lion.\nGAME OVER!")
    quit()
   elif run_or_walk == "walk":
    reply = input("Great! It took your time but you arrived at your destination(the treasure forest) without exhaustion. Would you like to enter? 'yes' or 'no'\n").lower()
    if reply == "yes":
     
     riddle = input("You are in the forest but you now find yourself in front of an old woman who tells you that before you can proceed to the treasure room, you must answer a riddle. Are you ready to take the riddle? 'yes' or 'no'\n").lower()
     if riddle == "yes":
      
      answer = input("Old woman: what is more valuble than gold, more expensive than diamond, it's hard to find but easy to lose.\nYou: ").lower()
      if answer == "friend":
       print("Old woman: Hmmm, you seem to have gotten that quite easily. well there is no going back from here.")
       print("Old woman: I have one more riddle for you. Failure to give me a correct answer means you die.")
       answer_2 = input("Old woman: Who is more powerful than God, more mighty than Satan, is immortal and controls the entire universe?\n").lower()
       if answer_2 == "nobody" or answer_2 == "no one" or answer_2 == "no body" or answer_2 == "noone":
        print("Old woman: Correct! you are worthy of having the Treasure. You can proceed but be careful, a wrong choice could lead to your death.\n ")
        print("You have finally arrived in front of the treasure room but there is a problem.\nThere are three doors of different colours but only one leads to the treasure room. But not to worry you are given a clue.\n ")
        print("In nature's vast canvas, I often appear,\nA hue so enchanting, so crisp and clear.\nSometimes I'm seen beneath the vast sky,\nAmidst fields and forests, where life passes by.\n ")
        print("Amidst snowy peaks, where cold winds embrace,\nI reflect the sun, adorning with grace.\nWith a touch of frost, I shimmer and glow,\nA majestic presence, like fresh-driven snow.\n ")
        print("From the sky above, where birds freely roam,\nTo the depths below, where the creatures find home,\nI am a color that captivates all you see,\nThough a color I may seem, my essence is of another, believe me.\n ")
        print("In gardens or forests, I'm often found,\nWith leaves and petals, I'm tightly bound.\nThrough me, sunlight paints a lovely scene,\nAs I sway gently, the air turns serene.\n ")
        print("A puzzle I am, with colors to view,\nBlue, green, or white, which one is true?\nThough my identity may seem askew,\nIn the end, I'm the one who shines through.\n ")
       
        colour = input("What am I? 'blue', 'green', or 'white'\n").lower()
        if colour == "blue":
         print("CONGRATULATIONS!!! You have won the game.")
         quit()
        elif colour == "green":
         end_of_game()
        elif colour == "white":
         end_of_game()
        
       else:
        print("Old woman: Wrong!")
        print("You are dead.\nGAME OVER!")
        quit()

      else:
       print("Old woman: Wrong! You cannot have the treasure, go back!\nGAME OVER!")
       quit()

     elif riddle == "no":
      print("GAME OVER!")
      quit()
     
    elif reply == "no":
     print("You were almost close to the Treasure. Too bad!\nGAME OVER!")
     quit()

  elif means_to_cross == "swim":
   print("ouch! You were eaten by carnivorous wild fishes.\nGAME OVER!")
   quit() 

 elif path == "third":
  print("Sorry, you fell into the hole.\nGAME OVER!")
  quit()

elif cross_road == "right":
 print("Sorry, you were attacked by wild dogs.\nGAME OVER!")
 quit()
 

 