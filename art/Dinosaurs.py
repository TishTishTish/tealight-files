#Networking
from tealight.net import connect, send

connect(Dinosaurs)
send(message, echo=False)

def handle_message(message):
  print "Received message: " + message