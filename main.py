import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    log_state()   # no args
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))  # Fill background
        player.draw(screen)   # Draw player
        log_state()   # write a frame's state
        pygame.display.flip()   # Update display
        dt = clock.tick(60) / 1000
        player.update(dt)

    pygame.quit()

if __name__ == "__main__":
    main()
