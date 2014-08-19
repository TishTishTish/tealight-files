from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
def waterwheel(edges, size):
  angle = 210.0
  decoration = size / 2
  for i in range(8, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)
waterwheel(12,75)
