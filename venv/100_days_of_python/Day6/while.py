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

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# for loops are helpful if you need to do something with each item
# while loop should be used when you dont care numbers just to match a condition
# while loops can run forever infinite loop
