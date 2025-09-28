import pygame
from constants import *
from circleshape import *
from player import *

    
def main():
    pygame.init()
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    one = Player(x, y)
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        one.draw(screen)
        pygame.display.flip()
        one.update(dt)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
