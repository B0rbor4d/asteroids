import pygame
from constants import *
from player import *
from asteroidfield import *



def main():
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    # Window can be closed by the "Window Close Button (X)"
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update Player
        updatable.update(dt)
        # Draw the Player
        for thing in drawable:
            thing.draw(screen)
        # Screen Update
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000







if __name__ == "__main__":
    main()