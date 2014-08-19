from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def go():
  distance = 0
  while touch() != 'wall'
    move()
    distance = distance + 1
  else left_side() != 'wall'
    turn(-1)
    move()
    distance = distance + 1
  else right_side != 'wall'
    turn(1)
    move()
    distance = distance + 1

go()