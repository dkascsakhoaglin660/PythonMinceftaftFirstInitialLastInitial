from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#
places = {'Diamond Ore': (-37, 14, -36), 'Random Places':(0,50,5)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close):")
    if choice in places:
        #
        location = places[choice]
        #
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)