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
testRect = block.Block(100, 250, "grass_block")

# Main loop
running = True
clock = pg.time.Clock()
tick = 0
while running:
    #Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
    
    # Tick calculation
    if tick >= 60:
        tick = 0

    # Update player walking
    p.walking = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Drawing player
    screen.blit(p.player, (p.rect.x, p.rect.y))


    # Drawing test block
    screen.blit(testRect.block, (testRect.rect.x, testRect.rect.y))

    # Keyboard input
    keys = pg.key.get_pressed()
    if keys[pg.K_w] or keys[pg.K_UP]:
        p.rect.y -= settings.PLAYER_SPEED
        p.walking = True
    if keys[pg.K_a] or keys[pg.K_LEFT]:
        p.rect.x -= settings.PLAYER_SPEED
        p.walking = True
        p.direction = "left"
    if keys[pg.K_s] or keys[pg.K_DOWN]:
        p.rect.y += settings.PLAYER_SPEED
        p.walking = True
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        p.rect.x += settings.PLAYER_SPEED
        p.walking = True
        p.direction = "right"

    #Player animation
    p.updateAnimations(tick)
    
    pg.display.flip()
    clock.tick(60)
    tick += 1