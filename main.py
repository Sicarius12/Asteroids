import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print(pygame.get_init())
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        group_updatable.update(dt)

        for drawble in group_drawable:
            drawble.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()
    print(pygame.get_init())

if __name__ == "__main__":
    main()