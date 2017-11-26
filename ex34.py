from sys import exit
def gold_room():
    print("This room is full of gold. how much did you take")

    next = int(input(">"))

    if next < 50:
        print("Nice, you're not greedy")
        exit(0)
    else:
        dead("you're a greedy mother fuvker!!!")

def bear_room():
    print("There is a bear in here")
    print("the bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How're you going to move the bear?")
    bear_moved = False

    while True:
        next = input(">")

        if next == "take honey":
            dead("The bear looks at you and slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulu_room():
    print("here you see the great evil cthulu")
    print("He, it, whatever stares at you and you go insane")
    print("do you flee for your life or eat your head")
    next = input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty")
    else:
        cthulu_room()

def dead(why):
    print(why, " Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    next = input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
