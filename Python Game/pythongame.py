import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()

test_surface = pygame.image.load('Python Game/graphics/Background.png')
test_surface = pygame.transform.scale(test_surface,(800,400))
ground_surface = pygame.image.load('Python Game/graphics/Grass.png')
ground_surface = pygame.transform.scale(ground_surface,(800,400))
# line is use to help measure
# line_surface = pygame.Surface((800,1))
# line_surface.fill('Red')

while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop

    screen.blit(test_surface,(0,0))
    screen.blit(ground_surface,(0,0))
    # screen.blit(line_surface,(0,370))
    # 370 is top of the grass - where the player should stand

    pygame.display.update()
    clock.tick(60)