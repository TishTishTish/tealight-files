#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
message = int()
send(message, str=False)

def handle_message(message):
  print "Received message: " + message