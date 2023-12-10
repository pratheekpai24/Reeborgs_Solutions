#This code works for all around puzzle on reeborgs world ie Aroud1(all 3),Around 2,Around 3,Around 4
def tl():
    turn_left()
def tr():
    turn_left()
    turn_left()
    turn_left()
pos = position_here()
while wall_in_front():
    tl()
move()
while position_here()!=pos: 
    if object_here():
        take()
    if right_is_clear():
        tr()
    if front_is_clear() == True:
        move()
    else:
        tl()
    