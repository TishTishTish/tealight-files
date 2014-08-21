#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
message = 'Hey!'
send(message)

def handle_message(message):
  print "Received message: " + message