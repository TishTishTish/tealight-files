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
  while left_side() != 'wall':
    turn(-1)
    move()
  while right_side() == 'wall':
    turn(-1)
    move()
  while left_side == 'wall':
    turn(1)
    move()
  while right_side() != 'wall':
    turn(1)
    move()
    
go()