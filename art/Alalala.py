#Networking
from tealight.net import (connect, send)

connect(Dinosaurs.py)
send(message, echo=False)

def handle_message(message):
  print "Received message: " + message