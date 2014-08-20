from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  width = 100
  height = 100
  
  for i in range(0, spines):
    x0 = x + ((size*width) * cos(angle))
    y0 = y + ((size*height) * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi/spines)

star(width*3, height*3, "blue", 100, 50)
star(width*6, height*4, "purple", 200, 100)
star(width*4.5, height*2, "orange", 125, 30)