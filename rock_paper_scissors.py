import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if player_choice == 0 and computer_choice == 0:
 print(f"{rock}\n \ncomputer choose:{rock}\n \nIt's a draw.")
elif player_choice == 0 and computer_choice == 1:
 print(f"{rock}\n \ncomputer choose:{paper}\n \nYou lose.")
elif player_choice == 0 and computer_choice == 2:
 print(f"{rock}\n \ncomputer choose:{scissors}\n \nYou win.")
elif player_choice == 1 and computer_choice == 0:
 print(f"{paper}\n \ncomputer choose:{rock}\n \nYou win.")
elif player_choice == 1 and computer_choice == 1:
 print(f"{paper}\n \ncomputer choose:{paper}\n \nIt's a draw.")
elif player_choice == 1 and computer_choice == 2:
 print(f"{paper}\n \ncomputer choose:{scissors}\n \nYou lose.")
elif player_choice == 2 and computer_choice == 0:
 print(f"{scissors}\n \ncomputer choose:{rock}\n \nYou lose.")
elif player_choice == 2 and computer_choice == 1:
 print(f"{scissors}\n \ncomputer choose:{paper}\n \nYou win.")
elif player_choice == 2 and computer_choice == 2:
 print(f"{scissors}\n \ncomputer choose:{scissors}\n \nIt's a draw.")
else:
 print("You typed an invalid number, You lose.")