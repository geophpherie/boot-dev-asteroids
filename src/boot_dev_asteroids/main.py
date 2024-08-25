import pygame
from boot_dev_asteroids import constants


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=pygame.Color(0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
