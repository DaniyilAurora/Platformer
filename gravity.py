import player
import block
import settings

class Gravity():
    def __init__(self):
        pass

    def applyGravity(self, player: player.Player, blocks: list[block.Block]):
        gravityApply = True

        for b in blocks:
            if b.rect.colliderect(player.rect):
                gravityApply = False
            pass

            if gravityApply:
                player.rect.y += settings.GRAVITY
            else:
                if player.rect.bottom > b.rect.top:
                    player.rect.bottom = b.rect.top

    def handle_collisions(self, player, blocks):
        player.grounded = False

        for block in blocks:
            if player.rect.colliderect(block.rect):
                if player.rect.bottom > block.rect.top:
                    player.rect.bottom = block.rect.top
                    player.grounded = True