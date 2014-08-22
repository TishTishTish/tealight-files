#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
message = "Do you want to play DinOTHELLOsaurus?"
send(message)

def handle_message(message):
  print "You have one message: " + str(message)
  