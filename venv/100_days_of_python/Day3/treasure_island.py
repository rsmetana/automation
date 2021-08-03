print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer1 = input('You are standing at a crossroad. Which way are you going? Left or Right: ').lower()
if answer1 == 'left':
  print('you made it to a lake')
  answer2= input('You are standing infront of the lake what will you do? Swim or Wait? ').lower()
  if answer2 == 'wait':
    print('A boat picked you up. After getting off the boat you walk. ')
    answer3 = input('You walk up to 3 doors. Yellow, Blue and Red. Which door do you pick? ').lower()
    if answer3 == 'yellow':
        print('The treasure if found. You win!')
    elif answer3 == 'red':
            print('You were eaten by the chupacabra. Game over!')
    elif answer3 == 'blue':
            print('Your were crushed by a rock. Game over!')
    else:
        print('Thats not allowed. Game over')
  else:
    print('You cant swim you drown. Game over.')
else:
    print('You walked into a grizzly cave. Game over!')

    
