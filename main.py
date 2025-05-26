import pygame
from constants import *

def main():
    pygame.init()
    print(pygame.get_init())
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    running = True

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()
    print(pygame.get_init())

if __name__ == "__main__":
    main()