import time

def start():
    answer = input("Wake Up? (yes/no)")
    if answer.lower().strip() == "yes":
        stand_up()
    else:
        continue_sleeping()

def end():
    answer = input("Game Over (restart)")
    if answer.lower().strip() == "restart":
        start()
    else:
        print("Invalid choice")

def stand_up():
    answer = input("You wake up. You find yourself in complete darkness, unable to see even your hands. (Stand Up/Wait)")
    if answer == "Stand Up":
        stand_up_again()
    else:
        continue_sleeping()

def stand_up_again():
    answer = input("You stand up and trip. It seems you have been asleep for a long time, and your body still has to adjust. (Stand Up again/go back to bed)")
    if answer == "Stand Up again":
        explore_room()
    else:
        continue_sleeping()

def explore_room():
    answer = input("You stand up again and feel your way around the room. It seems the Room you are in is a rather small Box-shaped Room built of cold Stone. You try to make sense of everything but you can't seem to remember how you got here. As you get farther away from your bed, towards what seems to be a door, you start to hear voices. They should wake up soon, poor souls. Yes, we should get out of here before they do. We don't want to end up like the last batch after all. These people don't know what's com... You hear the voices getting quieter until they fade into silence. You make your way back to the bed as you think about what the voices were talking about. (next)")
    if answer == "next":
        continue_sleeping()

def continue_sleeping():
    answer = input("You Continue Sleeping... (Next)")
    time.sleep(2)
    if answer == "Next":
        awakening()
    else:
        continue_sleeping()

def awakening():
    print("You wake up to a loud creaking sound coming from your door and footsteps approaching you")
    answer = input("The Footsteps are getting closer and closer... (hide/attack)")
    if answer == "hide":
        hide()
    else:
        attack()

def hide():
    print("As the footsteps come closer, you quickly hide under the bed and wait")
    time.sleep(5)
    print("The footsteps stop just before the bed")
    time.sleep(2)
    answer = input("...I can see you, you know (continue hiding/attack)")

    if answer == "continue hiding":
        continue_hiding()
    else:
        attack()

def continue_hiding():
    print("You continue hiding")
    time.sleep(5)
    answer = input("... I'm not here to hurt you... I also just woke up in a room just like this and your room was the only one that would open (still hide/come out)")

    if answer == "still hide":
        print("You continue hiding")
        time.sleep(5)
        print("Fine, I'll go...")

        answer = input("You hear him turn around and the footsteps getting farther and farther away from you until they fade into silence. (come out/continue hiding)")
        if answer == "come out":
            print("You try to come out but you realize you are way too much of a coward")
            time.sleep(1)
            hide_ending()
        else:
            hide_ending()

def hide_ending():
    print("You continue hiding like the coward you are")
    time.sleep(5)
    print("Several hours go by and yet you still hide")
    time.sleep(10)
    print("Days go by but still, you hide")
    time.sleep(15)
    print("How much time has it been? Are you still alive? You are still hiding?! Oh well, Stay there I guess...")
    time.sleep(20)
    print("You hear a bee buzzing around")
    time.sleep(2)
    print("The bee comes closer and closer...")
    time.sleep(2)
    print("The bee has found your hideout!")
    time.sleep(1)
    print("You die of shock... coward")
    time.sleep(1)

    end()

def attack():
    print("You quickly stand up and rush towards the footsteps, swinging your hands blindly through the darkness")
    answer = input("HEY, STOP! (continue attacking/stop)")

    if answer == "continue attacking":
        print("You don't stop throwing your arms at the man until you land a lucky punch to his head")
        print("The Man falls to the ground and you emerge victorious!")
        time.sleep(2)
        print("You search the Man, but it seems that he had nothing on him.")
        time.sleep(3)
        print("Your door now lies open and as you walk out of it, torches light up all around you.")
        time.sleep(2)
        print("You realize that your door is only one of many in a seemingly endless corridor")
        time.sleep(1)
        answer = input("You can barely make out a voice coming from the other side of the door at the end of the corridor. Do you check the other rooms, or make your way to the end of the corridor? (check the other rooms/go to the door)")

        if answer.lower().strip() == "check":
            check()
        else:
            corridor()

def check():
    print("You go to check the other Rooms, but all of them seem locked, besides one other Room that looks just like yours.")
    time.sleep(3)
    print("You go into the room and make out a few symbols carved into the stone: sH3 1s n0t 4 sH3")
    time.sleep(3)
    print("You find nothing else")
    time.sleep(3)
    print("Disappointed you make your way out and go to the corridor")
    time.sleep(5)
    corridor()

def corridor():
    print("You approach the Door at the end of the corridor as the voice gets louder and louder")
    time.sleep(3)
    print("You open the door and walk into the room.")
    time.sleep(3)
    print("In front of you, you see an empty but brightly lit room with only a TV in the middle of the room.")
    print("The door suddenly shuts close behind you.")
    time.sleep(3)
    print("The TV is replaying a video someone took and although the person in the video is trying to remain anonymous by using a voice changing device and masking their face you can make out that it is a rather tall woman")
    time.sleep(3)
    print("HElLO CONTESTANTS! I HOPE YOU AND YOUR PARTNER GET ALONG JUST FINE, BECAUSE THIS ADVENTURE IS JUST ABOUT TO BEGIN!")
    time.sleep(3)
    print("CHOOSE YOUR WEAPONS, GET READY AND DELIVER A SHOW!")
    time.sleep(3)
    print("HERE ARE THE STATISTICS FOR THIS YEARS HUNGER GAMES!")
    print("CONTESTANT COUNT: 100")
    print("THEME: MAGIC")
    print("AREA: WASTELANDS")
    print("TEAMS: 2 Contestants per team")
    print("COUNTDOWN UNTIL RELEASE: 02:11")
    time.sleep(1)
    print("COUNTDOWN UNTIL RELEASE: 02:10")
    time.sleep(1)
    print("COUNTDOWN UNTIL RELEASE: 02:09")
    time.sleep(1)
    print("COUNTDOWN UNTIL RELEASE: 02:08")


start()
