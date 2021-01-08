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
rps = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer = random.randint(0,2)

if user >= 3 or user <= 0:
   print("You chose an invalid number, you lose!")
else:
  print(rps[user])
  print("Computer chose:")
  print(rps[computer])

  if user == computer:
    print("DRAW!")
  elif user == 0 and computer == 2:
    print("You Win!")
  elif user == 1 and computer == 0:
    print("You Win!")
  elif user == 2 and computer == 1:
    print("You Win!")
  else:
    print("You lose!")
