from tealight.art import (color, line, spot, circle, box, image, text, background)

def handle_mousedown(x,y):
  color("blue")
  spot(x,y,10)
  
def handle_mousemove(x,y,button):
  if button == "left":
    color("cyan")
    circle(x,y,10)
  if button == "right":
    color("random")
    circle(x,y,5)