import pygame as pg
import settings
import player
import block

#Requirements:
# - Mario-Style game
# - Player control through keyboard
# - Enemy and simple AI
# - Static maps to complete (2 maps)
# - Goal of the map (reach end)
# - Level creation and management (.lvl files)
# - SFX and GFX

# Initialise pygame
pg.init()
screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pg.display.set_caption("Platformer")

p = player.Player(20, 20)
testRect = block.Block(100, 50, "grass_block")

# Main loop
running = True
clock = pg.time.Clock()
while running:
    # Clear screen
    screen.fill((255, 255, 255))

    screen.blit(p.player, (p.rect.x, p.rect.y))
    screen.blit(testRect.block, (testRect.rect.x, testRect.rect.y))

    #Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
    
    pg.display.flip()
    clock.tick(60)