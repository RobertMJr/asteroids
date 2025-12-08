import pygame # pyright: ignore[reportMissingImports]
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        # Calling the parent's class constructor
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Draw a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)