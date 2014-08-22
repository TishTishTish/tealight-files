#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
send(message)
def received_message(message):
  if message == "Yes" or "yes" or "Yes!":
  print "Let's play DinOTHELLOsaurus!"

def handle_message(message):
  print "You have one message: " + str(message)