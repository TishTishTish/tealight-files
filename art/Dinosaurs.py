#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
message = "Do you want to play DinOTHELLOsaurus?"
send(message)

def handle_message(message):
  print "You have one message: " + str(message)
  
def received_message(message):
  if handle_message =! str("No")
  print "Let's play DinoOTHELLOsaurus!"