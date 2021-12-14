from mcpi.minecraft import Minecraft
mc = Minecraft.create()


answer = input("Create a crater? Y/N  ")

if answer == "Y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 5, pos.y + 5, pos.z + 5, pos.x - 5, pos.y - 5, pos.z - 5,0)
    mc.postToChat("Psalm loves Minecraft, BOOM!")

elif answer == "N":
    mc.postToChat("Bomb Defused")