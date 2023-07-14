import pygame
from sys import exit

window_width = 800
window_height = 400
window_size = (window_width,window_height)

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python Game/font/Pixeltype.ttf',50)

test_surface = pygame.image.load('Python Game/graphics/Background.png').convert_alpha()
test_surface = pygame.transform.scale(test_surface,window_size)
ground_surface = pygame.image.load('Python Game/graphics/Grass.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface,window_size)
text_surface = test_font.render('Our Game', False, "#FCDC4D")

harold_x_pos = 600
harold_y_pos = 371
harold_surface = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_rect = harold_surface.get_rect(midbottom = (harold_x_pos,harold_y_pos))

wizard_surf = pygame.image.load('Python Game/graphics/wizard/wizard_idle1/sprite_00.png').convert_alpha()
wizard_surf = pygame.transform.scale(wizard_surf,(128,128))
wizard_rect = wizard_surf.get_rect(midbottom = (80,371))

while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
            if wizard_rect.collidepoint(event.pos): print ('collision')

    screen.blit(test_surface,(0,0))
    screen.blit(ground_surface,(0,0))
    screen.blit(text_surface,(325,50))
    # 371 is top of the grass - where the player should stand

    harold_rect.x -= 4
    if harold_rect.right <= 0: harold_rect.left = window_width
    screen.blit(harold_surface,harold_rect)
    # print(wizard_rect.left) # can be used to get positions
    screen.blit(wizard_surf,wizard_rect)

    # if wizard_rect.colliderect(harold_rect): # returns 0 if no collision 1 if is
    #     print('Collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if wizard_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)