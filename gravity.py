import player
import block
import settings

class Gravity():
    def __init__(self):
        pass

    def calculateVelocity(self, player: player.Player, blocks: list[block.Block]):
        # If player is not grounded, gradually apply gravity until max value
        if not player.grounded and player.velocity >= settings.MAX_GRAVITY:
                player.velocity += settings.MAX_GRAVITY / 10
        elif player.grounded and not player.jumping:
            # Stop falling
            player.velocity = 0

    def applyGravity(self, player: player.Player, blocks: list[block.Block]):
        player.grounded = False
        player.jumping = False

        # Apply velocity to player
        player.rect.y -= player.velocity

        # Check for collisions
        for b in blocks:
            if player.rect.colliderect(b.rect) and b.blockType != "air" and b.blockType != "end":
                player.grounded = True
                player.velocity = 0
                
                # Push player up onto block surface
                player.rect.y = b.rect.top - player.rect.height
                break
            elif player.rect.colliderect(b.rect) and b.blockType == "end":
                 print("You Win!")

        # Check if player below the camera
        if player.rect.y >= 500:
             player.rect.x = settings.SPAWNPOINT[0]
             player.rect.y = settings.SPAWNPOINT[1]
