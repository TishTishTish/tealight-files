from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0

color("random")

def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  color("green")
  if button == "left":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  color("purple")
  if button == "right":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  
  