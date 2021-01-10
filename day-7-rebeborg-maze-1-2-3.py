def turn_around():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_around()
    move()
    turn_around()
     
    while front_is_clear():
        move()
    turn_left()   

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
