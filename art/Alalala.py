#Networking
from tealight.net import (connect, send)

connect('Dinosaurs.py')
message = "hello"
send(message)

def handle_message(message):
  print "Received message: " + str(message)