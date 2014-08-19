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
      if left_side() != 'wall' && right_side() == 'wall'
        move()
          if left_side == 'wall' && right_side() != 'wall'
            move()

go()