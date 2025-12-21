import pygame # pyright: ignore[reportMissingImports]
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initialize pygame
    pygame.init()
    # A clock object
    Clock = pygame.time.Clock()
    # Delta variable
    dt = 0
    # Use the display.set_mode function to get a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add the Player, Asteroid, Shot and AsteroidField classes to the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Instantiating player
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    # Instantiate asteroid field
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        # Check is user has closed the window and exit the game loop if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # Draw everything
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        # Refreshes the screen
        pygame.display.flip()
        # Call the tick method with a value of 60 -> It pauses the game loop until 1/60th of a second has pased.
        # The tick method also returns the amount of time passed since the last time it was called. 
        # Values is divided by 1000 to convert milliseconds to seconds   
        dt = Clock.tick(60) /1000
if __name__ == "__main__":
    main()

