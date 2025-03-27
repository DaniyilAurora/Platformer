import block
import settings
import levelParser

blockMap = {
    "grass_block": "grass_block",
    "air": "air",
    "": "air"
}

class Map():
    def __init__(self, levelFile: str):
        self.textLevel = levelParser.LevelParser().readFile(levelFile)
        self.level = [["" for x in range(settings.HORIZONTAL_BLOCKS)] for y in range(settings.VERTICAL_BLOCKS)]
        self.blocks = []

        # Fill the array with blocks
        for y in range(len(self.textLevel)):
            for x in range(len(self.textLevel[y])):
                self.level[y][x] = block.Block(x * settings.BLOCKS_WIDTH, y * settings.BLOCKS_HEIGHT, blockMap[self.textLevel[y][x]]) # Add to new 2D array blocks
                self.blocks.append(self.level[y][x]) # Add to list of all blocks new block

    def getMap(self):
        return self.level
    
    def getBlocks(self):
        return self.blocks