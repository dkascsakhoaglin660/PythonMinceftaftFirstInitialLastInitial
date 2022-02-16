from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

#add 10 glass blocks (ID 20) to empty list
blocks.append(20, 20, 20, 20, 20, 20, 20, 20, 20, 20)
blocks = [ ]
Block = 22

count = 0
while count <= len(blocks):
    
    mc.setBlock(x, y, z, blocks[0])
    mc.setBlock(x, y + 1, z, block[1])
    mc.setBlock(x, y + 2, z, block[2])
    
count += 1

#Delete the last block in the list
blocks.del[9]

# Inset a lapis lazuli block at the first position in the list
blocks.append(22)
time.sleep(2)


print(blocks)