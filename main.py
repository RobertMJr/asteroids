import pygame # pyright: ignore[reportMissingImports]
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # Add the Player class to the groups
    Player.containers = (updatable, drawable)

    # Instantiating player
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

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
        # Refreshes the screen
        pygame.display.flip()
        # Call the tick method with a value of 60 -> It pauses the game loop until 1/60th of a second has pased.
        # The tick method also returns the amount of time passed since the last time it was called. 
        # Values is divided by 1000 to convert milliseconds to seconds   
        dt = Clock.tick(60) /1000
if __name__ == "__main__":
    main()

