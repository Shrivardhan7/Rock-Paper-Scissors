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
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  else:
    print("You lose")
