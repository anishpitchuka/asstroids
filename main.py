import pygame
from constants import *

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

    #Game loop
    while True:
        #Fill the screen black
        screen.fill("black")

        #Refresh the display
        pygame.display.flip()

        #Control the frame rate and calculate the time in seconds
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
