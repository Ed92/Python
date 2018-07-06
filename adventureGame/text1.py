"""

Author: Erik Djamgarian

Desc: Text based adventure

"""
from time import sleep
from sys import exit

def start():
    print("The sun, hidden behind the trees, was glowing in a bright orange color. It was Dawn.")
    print("You had to choose some direction and you chose West. You have been walking for miles.... and you're thirsty, and dehydrated.")
    print("The sun's last rays disapeared on the horizon. You seem to be getting somewhere, as there is a glimpse of light in the far distance.")
    sleep(1)
    print("Just as you started to hope, you heard an intense ROAR! You see a Bear swiftly moving towards you. You only have time to react. What do you do?(left/south/right/north)")
    do_what = input()

    if "left" in do_what or "south" in do_what:
        print("As you dive towards the left, the Bear swings at you with full strength and cracks your ribs. Stuck helplessly under the heavy weight of the Bear's claw, your live flashes before your eyes once more..")    
    elif "right" in do_what or "north" in do_what:
        print("You dive to the right, the Bear dives past you, missing you with his gigantic claws by a hair. The Bear stumbles and bounces off a nearby tree and faints. You take this opportunity to sprint towards the light, that shined in the distance."

def intro():
    print("Hello! Welcome to this text based adventure!")
    sleep(2)
    print("You will start the game off in the forest of pandora.")
    sleep(1)
    print("Wake up Hero..")
    sleep(2)

intro()
start()
