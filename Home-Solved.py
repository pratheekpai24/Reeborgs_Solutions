## this works for all 4 home puzzles
def tl():
    turn_left()
def tr():
    turn_left()
    turn_left()
    turn_left()
while at_goal() == False:
    if front_is_clear() == True:
        move()
        continue
    if right_is_clear() == True:
        tr()
    if(front_is_clear() == False):
        tl()
    