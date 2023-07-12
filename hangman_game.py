import random
from hangman_game_others import list_of_words, logo, stages
import os 

print(logo)
print("Welcome to the hangman game.\nThe goal is to completely guess each letter of an unknown word before the image completes(the man is hanged).")


word_choosen = random.choice(list_of_words)

blank_list = []
for alphabet in word_choosen:
 blank_list.append("_")
print(" ".join(blank_list))

lives = 6
end_of_game = False
print(stages[6])
while not end_of_game:
 guess = input("Guess a letter. ").lower()
 os. system('cls||clear')
 if guess in blank_list:
  print(f"You've already guessed {guess}")
 for position in range(len(word_choosen)):
  letter = word_choosen[position]
  if letter == guess:
   blank_list[position] = letter 
 print(" ".join(blank_list)) 

 if guess not in word_choosen:
  print(f"You guessed {guess}, that's not in the word. You lose a life.")
  lives -= 1
  print(stages[lives])
  if lives == 0:
   print("You lose!")
   end_of_game = True
   quit()

 if "_" not in blank_list:
  end_of_game = True
  print("you win!")
  quit()

