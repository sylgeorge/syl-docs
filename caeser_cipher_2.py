import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

os.system('cls||clear')

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

should_continue = True
while should_continue:
 direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))

 def encrypt(message, no_of_steps):
  encrypted_message = ""
  for char in message:
   if char in alphabet:
    position = alphabet.index(char)
    char = alphabet[position + no_of_steps]
    encrypted_message += char
   else:
    encrypted_message += char
  print(f"The encoded text is {encrypted_message}")

 def decrypt(message, no_of_steps):
  decrypted_message = ""
  for char in message:
   if char in alphabet:
    position = alphabet.index(char)
    char = alphabet[position - no_of_steps]
    decrypted_message += char
   else:
    decrypted_message += char
  print(f"The decoded text is {decrypted_message}")

 shift = shift % 25

 if direction == "encode":
  encrypt(message = text, no_of_steps = shift)

 elif direction == "decode":
  decrypt(message = text, no_of_steps = shift)

 result = input("Would you like to go again? 'yes' or 'no'")
 if result == "no":
  should_continue = False
  print("Goodbye.")