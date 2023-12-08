#this is a code to solve the maze on the Reeborgs Website
def ta():
    turn_left()
    turn_left()
def tl():
    turn_left()
def tr():
    turn_left()
    turn_left()
    turn_left()
while at_goal() ==  False:
    if front_is_clear() == True:
        move()
        if wall_on_right() == False:
            tr()
        continue
    if wall_on_right() == False:
        tr() 
    if front_is_clear() == False:
        tl() 