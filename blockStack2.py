from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 6
y = 11
z = 91
blockType = 103
while True:
    mc.setBlock(x, y, z, blockType)
    mc.setBlock(x, y + 1, z, blockType)