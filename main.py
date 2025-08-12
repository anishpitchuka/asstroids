import pygame
from constants import *
from player import *
from asstroidsfield import *

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

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set static containers for Asteroid & AsteroidField
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create asteroid field object
    asteroid_field = AsteroidField()

    # Create Player in both groups
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, updatable, drawable)

     # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatables
        updatable.update(dt)

        # Fill the screen black
        screen.fill("black")

        # Draw all drawables
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
