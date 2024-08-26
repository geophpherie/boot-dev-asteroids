import pygame
from boot_dev_asteroids import constants, player


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )

    # clock = pygame.time.Clock()
    # dt = 0

    # p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # p.draw(screen)

        # dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
