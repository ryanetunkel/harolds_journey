import pygame
from sys import exit

window_width = 800
window_height = 400
window_size = (window_width,window_height)
jump_button = pygame.K_SPACE
shoot_button = pygame.MOUSEBUTTONDOWN

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python Game/font/Pixeltype.ttf',50)

sky_surf = pygame.image.load('Python Game/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,window_size)

grass_top_y = 371
ground_surf = pygame.image.load('Python Game/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,window_size)

score_surf = test_font.render('Our Game', False, "#FCDC4D")
score_rect = score_surf.get_rect(center = (window_width/2,50))

harold_x_pos = 600
harold_y_pos = grass_top_y
harold_surf = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_rect = harold_surf.get_rect(midbottom = (harold_x_pos,harold_y_pos))

wizard_surf = pygame.image.load('Python Game/graphics/wizard/wizard_idle1/sprite_00.png').convert_alpha()
wizard_surf = pygame.transform.scale(wizard_surf,(128,128))
wizard_rect = wizard_surf.get_rect(midbottom = (80,grass_top_y))
wizard_gravity = 0

fireball_x_start = wizard_rect.right - 20
fireball_y_start = wizard_rect.centery + 24
fireball_x_pos = fireball_x_start
fireball_y_pos = fireball_y_start
fireball_x_speed = 0
fireball_surf = pygame.image.load('Python Game/graphics/fireball/fireball_move/sprite_0.png').convert_alpha()
fireball_surf = pygame.transform.scale(fireball_surf,(128,128))
fireball_rect = fireball_surf.get_rect(center= (fireball_x_pos,fireball_y_pos))

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        # if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
        #     if wizard_rect.collidepoint(event.pos): print ('collision')
        if event.type == shoot_button:
            fireball_x_speed = 4
        if event.type == pygame.KEYDOWN:
            if event.key == jump_button:
                wizard_gravity = -20


    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,0))
    pygame.draw.line(screen,"#FCDC4D",score_rect.bottomleft,score_rect.bottomright,3)
    screen.blit(score_surf,score_rect)
    # 371 is top of the grass - where the player should stand

    # mouse_pos = pygame.mouse.get_pos()

    harold_rect.x -= 4
    fireball_rect.x += fireball_x_speed
    if fireball_rect.left >= 800: 
        fireball_rect.centerx = fireball_x_start
        fireball_x_speed = 0
    # if fireball_x_speed != 0 and fireball_rect.colliderect(harold_rect):
    #     print('boom')
    # else:
    #     print('done boom')
    if harold_rect.right <= 0: harold_rect.left = window_width
    screen.blit(harold_surf,harold_rect)
    # print(wizard_rect.left) # can be used to get positions

    wizard_gravity += 1
    wizard_rect.y += wizard_gravity
    screen.blit(wizard_surf,wizard_rect)
    screen.blit(fireball_surf,fireball_rect)

    # if wizard_rect.colliderect(harold_rect): # returns 0 if no collision 1 if is
    #     print('Collision')

    # if wizard_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)