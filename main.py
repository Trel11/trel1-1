import math
import pygame
from settings import *
from player import Player
from map import w_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    ray_casting(sc, player.pos, player.angle)

#    pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
#    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
#                                             player.y + WIDTH * math.sin(player.angle)))
#    ыfor x, y in w_map:
#      pygame.draw.rect(sc, WHITE, (x, y, TITLE, TITLE), 2)

    pygame.display.flip()
    clock.tick(FPS)
