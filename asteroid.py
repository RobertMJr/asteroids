import pygame # pyright: ignore[reportMissingImports]
from circleshape import CircleShape 
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    # Uses the constructor from the Parent class
    # Used super here in case we might want to add stuff later to the constructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # Override the draw method of the Parent class.
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    # Override the update method of the Parent class.
    def update(self, dt):
        self.position += self.velocity * dt

