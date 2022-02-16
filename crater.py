from mcpi.minecraft import Minecraft
mc = Minecraft.create()


answer = input("Create a crater? Y/N  ")

if answer == "Y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 99, pos.y + 4, pos.z + 4, pos.x - 99, pos.y - 4, pos.z - 4,0)
    mc.postToChat("Psalm loves Minecraft, BOOM!")

elif answer == "N":
    mc.postToChat("Bomb Defused")