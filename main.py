import pygame
from constants import *
from player import *

def main():
    pygame.init() # Initialize pygame

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create an clock object to control the frame rate
    clock = pygame.time.Clock();

    #Delta time variable
    dt=0

    # Create the Player object in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen black
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000

        player.update(dt)


if __name__ == "__main__":
    main()
