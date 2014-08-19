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
    turn(-2)
    move(1)
    moved = moved + 1
    
    turn (-1)
    if touch() == 'wall': #If there is a wall, then turn
      go()
    turn (2)
    if touch() == 'wall':
      go()
      
    turn(1)
    for i in range(0,moved):
      move()
    turn(2)
      
go()