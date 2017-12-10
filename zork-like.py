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
def man_made():
    print("you enter into a dimly lit room")
    print("above you is a night sky")
    print("spelled out in the stars above you is the question")
    print("'WHAT IS THE ONLY MAN MADE OBJECT VISABLE FROM SPACE'")
    print("""
    Over an unseen loud speaker a soft female voice says
    "A: The great wall of china"
    "B: Mount Everest"
    "C: The White house" or
    "D: The empire state building"
    """)
    answer = input(">")
    if answer == "A":
        print("correct, you may advace")
    elif answer == "B" or "C" or "D":
        death("A chinese man drops from the ceiling and kills you")
    else:
        death("dickhead")
    print("ahead of you, to the south, is a a white door with a red H painted on it")
    print("to the east is a door with a picture of a bag of sugar on it")
    direction = input("where to next?")
    if direction == "south" or "s" or "S" or "South":
        rhino_room()
    elif direction == "East" or " east"
