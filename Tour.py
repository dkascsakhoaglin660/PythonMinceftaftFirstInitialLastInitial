from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 100
y = 50
z = 100

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 0
y = 50
z = 0

mc.player.setTilePos(x, y, z)
