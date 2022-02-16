from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    #get players name
    name = input("what is your name?  ")
        if name == #name
        if name == "exit":
            break
        mc.postToChat("Go!")
        
        time.sleep(60)
        blockHits =mc.event.pollBlockHits()
        
        blockHitsLength =len(blockHits)
        mc.postToChat("Your score is " + str(blockHitsLength))
        
        print(scoreboard)
                 