from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = 106.5
y = 4.0
z = 77.3
gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.setBlock(x, y + 1, z - 1, 0)
    mc.setBlock(x, y + 2, z - 1, 0)
else:
    mc.setBlock(pos, 10)
    
