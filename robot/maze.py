from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def go():
  while touch() != 'wall':
    move()
  if left_side() != 'wall':
    turn(-1)
    move()
    else right_side() == 'wall':
    turn(-1)
    move()
  else left_side == 'wall':
    turn(1)
    move()
  else right_side() != 'wall':
    turn(1)
    move()
    
go()