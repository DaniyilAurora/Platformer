import player
import block
import settings

class Gravity():
    def __init__(self):
        pass

    def applyGravity(self, player: player.Player, blocks: list[block.Block]):
        gravityApply = True

        # Check for collision to stop gravity
        for b in blocks:
            if b.rect.colliderect(player.rect):
                gravityApply = False
                break

        if gravityApply:
            # Apply gravity: increase velocity up to MAX_GRAVITY / 10
            if player.velocity < abs(settings.MAX_GRAVITY):
                player.velocity += settings.MAX_GRAVITY / 10

            # Move the player down
            player.rect.y -= player.velocity

        else:
            # Stop falling when grounded
            player.velocity = 0

            # Correct player position if sinking into a block
            for b in blocks:
                if player.rect.bottom > b.rect.top:
                    player.rect.bottom = b.rect.top
                    break


    def handle_collisions(self, player, blocks):
        player.grounded = False

        # Check if there are any collisions with blocks
        for block in blocks:
            if player.rect.colliderect(block.rect):
                if player.rect.bottom > block.rect.top:
                    player.rect.bottom = block.rect.top
                    player.grounded = True