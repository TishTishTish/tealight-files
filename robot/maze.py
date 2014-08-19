from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def go():
  if touch() != 'wall':
    move()
  if left_side() != 'wall':
    turn(-1)
    move()
  if right_side() == 'wall':
    turn(-1)
    move()
  if left_side == 'wall':
    turn(1)
    move()
  if right_side() != 'wall'
    turn(1)
    move()
go()