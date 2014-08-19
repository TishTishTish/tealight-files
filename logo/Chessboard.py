from tealight.logo import move, turn

def whitesquare(side):
  for i in range(0,4):
    move(side)
    turn(90)

def blacksquare(side):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  spiral(size + 0.5)
  
spiral(0)