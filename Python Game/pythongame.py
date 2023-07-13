import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()

test_surface = pygame.image.load('Python Game/graphics/Sky.png')
ground_surface = pygame.image.load('Python Game/graphics/ground.png')

while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop

    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)
