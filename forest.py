from mcpi.minecraft import Minecraft
mc = Minecraft.create()



def growTree(x, y, z):
    mc.setBlocks(x, y, z, x, y + 4, z, 17)
    mc.setBlocks(x - 2, y + 4, z - 2, x + 2, y + 4, z + 2, 18)
    mc.setBlocks(x - 1, y + 5, z - 1, x + 1, y + 5, z + 1, 18)
    mc.setBlocks(x - 0, y + 6, z - 0, x + 0, y + 6, z + 0, 18)
    
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)