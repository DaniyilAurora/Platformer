import settings

blockMap = {
    "#": "grass_block",
    ".": "air"
}

class LevelParser():
    def __init__(self):
        pass

    def readFile(self, filePath):
        file = open(filePath)

        map = [["" for x in range(settings.HORIZONTAL_BLOCKS)] for y in range(settings.VERTICAL_BLOCKS)] # Create 2d array for map

        y = 0
        for line in file:
            line = line.strip() # Remove spaces
            
            x = 0
            for char in line:
                map[y][x] = blockMap[char] # map the values of block through dictionary
                x += 1

            y += 1
        
        return map