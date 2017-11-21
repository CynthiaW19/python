from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	#mc = Minecraft.create("10.183.4.123", 4711)
	#mc = Minecraft.create("10.183.13.13", 4711)
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc
	

 
def igloo(mc, x, y, z):
	
 
	mc.setBlocks(x-2, y, z, x-2, y, z-4, 80)
	mc.setBlocks(x-1, y+1,z, x-1, y+1, z-4, 80)
	mc.setBlocks(x, y+2, z, x, y+2, z-4, 80)
	mc.setBlocks(x+1, y+2, z, x+1, y+2, z-4, 80)
	mc.setBlocks(x+3, y, z, x+3, y, z-4, 80)
	mc.setBlocks(x+1, y+3, z-4, x, y+3, z-4, 80)
	mc.setBlocks(x+2, y+1, z, x+2, y+1, z-4, 80)
	mc.setBlock(x+2, y+2, z-4, 80)
	mc.setBlock(x+3, y+1, z-4, 80)
	mc.setBlock(x-2, y+1, z-4, 80)
	mc.setBlock(x-1, y+2, z-4, 80)
	mc.setBlocks(x+4, y, z-4, x+4, y+1, z-7, 80)
	mc.setBlocks(x+5, y, z-5, x+4, y+1, z-7, 80)
	mc.setBlocks(x+5, y, z-6, x+5,y+1, z-8, 80)
	mc.setBlocks(x-3, y, z-4, x-3, y+1, z-6, 80)
	mc.setBlocks(x-4, y, z-5, x-4, y+1, z-7, 80)
	mc.setBlocks(x-4, y, z-6, x-4 , y+1, z-8, 80)
	mc.setBlock(x-3, y+2, z-6, 80)
	mc.setBlock(x-3, y+2, z-6, 80)
	mc.setBlock(x-2, y+2, z-5, 80)
	mc.setBlock(x-2, y+3, z-6, 80)
	mc.setBlock(x+4, y+2, z-6, 80)
	mc.setBlock(x+3, y+2, z-5, 80)
	mc.setBlock(x+3, y+3, z-6, 80)
	mc.setBlocks(x, y+4, z-5, x+1, y+4, z-5, 80)
	mc.setBlock(x-1, y+3, z-5, 80)
	mc.setBlock(x+2, y+3, z-5, 80)
	mc.setBlocks(x+2, y+4, z-6, x-1, y+4, z-8, 80)
	mc.setBlocks(x-2, y+3, z-7, x-2, y+3, z-8, 80)
	mc.setBlocks(x-3, y+2, z-7, x-3, y+2, z-8, 80)
	mc.setBlocks(x+3, y+3, z-7, x+3, y+3, z-8, 80)
	mc.setBlocks(x+4, y+2, z-7, x+4, y+2, z-8, 80)
	mc.setBlocks(x-2, y+3, z-9, x+3, y+3, z-9, 80)
	mc.setBlock(x-3, y+2, z-9, 80)
	mc.setBlock(x+4, y+2, z-9, 80)
	mc.setBlocks(x+4, y+2, z-10, x-3, y+2, z-10, 80)
	mc.setBlocks(x-4, y, z-9, x-4, y+1, z-10, 80)
	mc.setBlocks(x+5, y, z-9, x+5, y+1, z-10, 80)
	mc.setBlocks(x-4, y, z-11, x+5, y+1, z-11, 80)
	
def loop(mc, x, y, z):
	for n in range(0,10):
		mc = init()
		x, y, z = mc.player.getPos()  
		zz = z + 1
		#mc.player.setPos(0, 0, 0)
		#mc.setBlocks(x-128, y, z-128, x+128, y-100-63, z+128,0)
		mc.setBlocks(x-128, y-n, z-128, x+128, y-n, z+128, 80)
		mc.player.setPos(0, 100, 0)

def snow(mc, x, y, z):
	count = 0
	while count < 100:
		mc = init()
		x, y, z = mc.player.getPos() 
		x = randint(-100,100)
		z = randint(-100,100)
		if count%4 == 0:
			mc.setBlock(x, y, z, 35, count%16)
			mc.setBlock(x-1, y, z, 35, count%16)
			mc.setBlock(x+1, y, z, 35, count%16)
			mc.setBlock(x, y+1, z, 35, count%16)
			mc.setBlock(x, y-1, z, 35, count%16)
			mc.setBlock(x, y, z+1, 35, count%16)
			mc.setBlock(x, y, z-1, 35, count%16)
		mc.setBlock(x, y, z, 35, count%16)
		print(count%16)
		count = count + 1
	
def main():
	mc = init()
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos() 
	#loop(mc, x, y, z)
	igloo(mc, x, y, z)
	snow(mc, x, y, z)
	
main()


  
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
