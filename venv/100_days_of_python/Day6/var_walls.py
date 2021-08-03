def jump():
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
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
#while not at_goal():
#    if wall_in_front():
#        jump()
#    else:
#        move()
while not at_goal():
    if wall_in_front():
        turn_left()
        while wall_on_right() and is_facing_north() is True:
            move()
            if right_is_clear():
                turn_right()
    else:
        move()