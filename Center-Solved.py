# this code is applicable for both Cebter 1 and 2 on Reeborgs world
def ta():
    turn_left()
    turn_left()
def tl():
    turn_left()
def tr():
    turn_left()
    turn_left()
    turn_left()
i = 1
b = 1
if wall_in_front():
    tl()
    while front_is_clear():
        move()
        b+=1
    if wall_in_front():
        ta()
    while front_is_clear():
        a = round(b/1.8)
        if position_here() == (i,a):
            put()
            done()
        move()
if wall_in_front():
            put()
            done()  
while front_is_clear():
    move()
    i+=1
    if wall_in_front():
        ta()
        
        while front_is_clear():
            move()
            j = round(i/1.8)
            if position_here() == (j,1):
                tr()
                while front_is_clear():
                    b+=1
                    move()
                    if wall_in_front():
                        ta()
                        while front_is_clear():
                            move()
                            a = round(b/1.8)
                            if position_here() == (j,a):
                                put()
                                done()
                put()
                done()
       