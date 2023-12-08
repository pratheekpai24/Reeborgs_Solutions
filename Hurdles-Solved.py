#solution code for all 4 hurdles on reborgs world website
def ta():
    turn_left()
    turn_left()
def tl():
    turn_left()
def tr():
    turn_left()
    turn_left()
    turn_left()
while at_goal()==False:
    if right_is_clear() == True:
        tr()
        move()
        tr()
        move()
        while front_is_clear()==True:
            move()
        tl()
        continue
    if front_is_clear() == True:
        move()
        continue
    if wall_in_front() == True:
        tl() 
        move()
        continue