from mcpi.mminecraft import Minecraft
mc = Minecraft.create()
import random

def randomBloclocations(blockType, repeates):
    count = 0
    for count in range(10):
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, y)
        mc.setBlock(x, y, z, 103)
        count += 1