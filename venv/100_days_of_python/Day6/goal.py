def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

#for step in range(6):
#    jump()
#while at_goal != True:
#    jump()

while not at_goal():
    jump()