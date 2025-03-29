import pygame as pg
import settings
import player
import gravity
import map
import sys

# Initialise pygame
pg.init()
screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pg.display.set_caption("Platformer")

# Initialise gravity class
gr = gravity.Gravity(screen)

# Create player
p = player.Player(settings.SPAWNPOINT[0], settings.SPAWNPOINT[1])

# Initialise map
level = map.Map("lvls/level1.lvl")

# Blocks list
blocks = level.getBlocks()

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
            sys.exit()
    
    # Tick calculation
    if tick >= 60:
        tick = 0

    # Update player walking
    p.walking = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Drawing blocks
    for b in blocks:
        screen.blit(b.block, (b.rect.x, b.rect.y))

    # Apply Gravity
    gr.calculateVelocity(p, blocks)
    gr.applyGravity(p, blocks)

    # Drawing player
    screen.blit(p.player, (p.rect.x, p.rect.y))

    # Keyboard input
    keys = pg.key.get_pressed()
    if keys[pg.K_a] or keys[pg.K_LEFT]:
        p.rect.x -= settings.PLAYER_SPEED
        p.walking = True
        p.direction = "left"
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        p.rect.x += settings.PLAYER_SPEED
        p.walking = True
        p.direction = "right"
    if keys[pg.K_SPACE]:
        if p.grounded:
            p.velocity = 10
            p.jumping = True

    #Player animation
    p.updateAnimations(tick)
    
    pg.display.flip()
    clock.tick(60)
    tick += 1