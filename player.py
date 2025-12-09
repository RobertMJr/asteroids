import pygame # pyright: ignore[reportMissingImports]
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # left
        if keys[pygame.K_a]:
            self.rotate((dt * -1))
        # right    
        if keys[pygame.K_d]:
            self.rotate(dt)
        # up
        if keys[pygame.K_w]:
            self.move(dt)
        # down
        if keys[pygame.K_s]:
            self.move((dt * -1))

    def move(self, dt):
        # Unit vector pointing from (0, 0) to (0, 1)
        unit_vector = pygame.Vector2(0, 1)
        # Rotate vector by the player's rotation so it points to the same direction as the player
        rotated_vector = unit_vector.rotate(self.rotation)
        # Multiply the vector by the player's speed and dt so that the vector is the length that player should move during this frame
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # Add the vector to the player's position to move them
        self.position += rotated_with_speed_vector