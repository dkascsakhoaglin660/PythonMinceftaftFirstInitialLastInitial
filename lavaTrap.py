import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()
mc.postToChat("Welcome to Lava Trap")

#Lava
sleep(3)
pos = mc.player.getTilePos()
mc.setBlocks(pos.x - 20, pos.y - 2, pos.z - 20, pos.x + 20, pos.y - 2, pos.z + 20, block.STONE.id)

mc.setBlocks(pos.x - 20, pos.y - 1, pos.z -20, pos.x + 20, pos.y - 1, pos.z + 20, block.LAVA.id)

mc.setBlock(pos.x, pos.y - 1, pos.z, block.DIAMOND_BLOCK.id)