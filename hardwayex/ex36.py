#!/usr/bin/python
from sys import argv, exit

print("you wake up in a dark room")
def start():
    print("to the south there is door surrounded by bright neon lights")
    print("to the east is a dark corridor, from it you can hear a rushing river")
    dec = input("direction: ")
    if dec == "south" or "s" or "S" or "South":
        man_made("Start")
    elif dec == "E" or "e" or "East" or "east":
        loud_room()
    else:
        death("you stumble around and die from hunger")
def man_made(pos):
    
