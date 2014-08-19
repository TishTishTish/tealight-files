from tealight.logo import move, turn

def whitesquare(side):
  for i in range(0,4):
    move(side)
    turn(90)
