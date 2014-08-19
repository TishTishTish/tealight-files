from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def go():
  moved = 0
  while touch() != 'wall':
    if left_side == 'wall':
      turn(1)
      move()
      moved = moved + 1
    if right_side == 'wall':
      turn (1)
      move()
      moved = moved + 1
      
go()