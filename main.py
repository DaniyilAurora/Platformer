import pygame as pg
import settings
import player
import block
import gravity

#Requirements:
# - Mario-Style game
# - Player control through keyboard
# - Enemy and simple AI
# - Static maps to complete (2 maps)
# - Goal of the map (reach end)
# - Level creation and management (.lvl files)
# - SFX and GFX

# TODO: Rewrite physics engine, add map files .lvl, add enemies, create map goal, add sfx and gfx,

# Initialise pygame
pg.init()
screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pg.display.set_caption("Platformer")

# Initialise gravity class
gr = gravity.Gravity()

# Create player
p = player.Player(80, 20)

# Create testing blocks
testRect = block.Block(100, 250, "grass_block")
testRect2 = block.Block(150, 150, "grass_block")

# Blocks list
blocks = []

blocks.append(testRect)
blocks.append(testRect2)

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
    for b in blocks:
        screen.blit(b.block, (b.rect.x, b.rect.y))

    # Apply Gravity
    gr.calculateVelocity(p, blocks)
    gr.applyGravity(p, blocks)

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