import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python Game/font/Pixeltype.ttf',50)

test_surface = pygame.image.load('Python Game/graphics/Background.png').convert_alpha()
test_surface = pygame.transform.scale(test_surface,(800,400))
ground_surface = pygame.image.load('Python Game/graphics/Grass.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface,(800,400))
# line is use to help measure
# line_surface = pygame.Surface((800,1))
# line_surface.fill('Red')
text_surface = test_font.render('Our Game', False, "#FCDC4D")

# tutorial calls it snail_surface
harold_surface = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_x_pos = 600
harold_y_pos = 335

wizard_surf = pygame.image.load('Python Game/graphics/wizard/player_walk_1.png')
wizard_rect = wizard_surf.get_rect(bottomleft = (80,370))

while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop

    screen.blit(test_surface,(0,0))
    screen.blit(ground_surface,(0,0))
    screen.blit(text_surface,(325,50))
    # screen.blit(line_surface,(0,370))
    # 370 is top of the grass - where the player should stand
    harold_x_pos -= 4
    if harold_x_pos < -100: harold_x_pos = 800

    screen.blit(harold_surface,(harold_x_pos,harold_y_pos))
    screen.blit(wizard_surf,wizard_rect)

    pygame.display.update()
    clock.tick(60)