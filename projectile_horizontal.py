import pygame
import sys
import math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Projectile Motion')

BLACK = (10, 105, 255)
WHITE = (255, 0, 0)

delta_t = 0.01
m = 1
g = 9.8

fx = 0
fy = m * g

x = 0
y = 0

vx = 50
vy = 0

while True:
    screen.fill(BLACK)

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
fpsClock.tick(FPS)
