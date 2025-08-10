import pygame
from constants import *

def main():
    pygame.init() # Initialize pygame

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game loop
    while True:
        #Fill the screen black
        screen.fill("black")

        #Refresh the display
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
