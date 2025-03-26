import settings

blockMap = {
    "#": "grass_block"
}

class LevelReader():
    def __init__(self):
        pass

    def readFile(self, filePath):
        file = open(filePath)
        print(settings.BLOCKS_WIDTH)
        print(settings.BLOCKS_HEIGHT)
        level = [["" for x in range(settings.BLOCKS_WIDTH)] for y in range(settings.BLOCKS_HEIGHT)] 

        y = 0
        for line in file:
            line = line.strip()

            x = 0
            for char in line:
                level[y][x] = blockMap[char]

                x += 1
            
        y += 1

        return level
    
# TODO: For some reason the blocks are weirdly placed, there is not enough block. Fix it.