from tealight.logo import move, turn

def blacksquare(size):
  
  if size > 100:
    return
  
  move(size)
  turn(90)
  blacksquare(size + 0.5)
  
blacksquare (0)

