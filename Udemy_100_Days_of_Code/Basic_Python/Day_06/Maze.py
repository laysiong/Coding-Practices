def turn_right():
    turn_left()
    turn_left()
    turn_left()

def collision():
    if wall_in_front() and wall_on_right():
       turn_left()
    elif wall_in_front() and wall_on_right()!=True:
       turn_right()
       move()
    
while not at_goal():
    if front_is_clear()!= True:
       collision()
    else:
        if right_is_clear():
           turn_right()
           move()
        else:
           move()
      
   
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
################################################################
