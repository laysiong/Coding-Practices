def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if wall_in_front()== True and wall_on_right()!=True:
       turn_right()
       move()
    elif wall_in_front() == True:
       turn_left()
    
while not at_goal():
    if front_is_clear()!=True:
        jump()
    elif wall_in_front()!=True and wall_on_right()!=True:
        turn_right()
        move()
    else:
        move()
    

    
# !front nothing move
# front turn left
# !front !right turn right move
# front !right turn right move
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
################################################################
