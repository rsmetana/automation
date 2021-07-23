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

choice = int(input('What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors. '))
if choice == 0:
  print(rock)
elif choice == 1:
  print(scissors)
elif choice == 2:
  print(paper)

print('Computer chose:')
comp_choice = random.randint(0, 2)
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(scissors)
elif comp_choice == 2:
  print(paper)

if choice == 0 and comp_choice == 0:
  print('Its a draw')
  if choice == 0 and comp_choice == 1:
    print('You win!')
    if choice == 0 and comp_choice ==2:
      print('You lose!')
if choice == 1 and comp_choice == 0:
  print('Your lose!')
  if choice == 1 and comp_choice == 1:
    print('Its a draw!')
    if choice == 1 and comp_choice ==2:
      print('You win!')
if choice == 2 and comp_choice == 0:
  print('You win!')
  if choice == 2 and comp_choice == 1:
    print('You lose!')
    if choice == 2 and comp_choice ==2:
      print('Its a draw!')     
