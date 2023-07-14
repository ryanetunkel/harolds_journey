import pygame
from sys import exit

window_width = 800
window_height = 400
window_size = (window_width,window_height)
wizard_pixel_size = (128,128)

jump_button = pygame.K_SPACE
shoot_button = pygame.MOUSEBUTTONDOWN

def display_score():
    current_time = pygame.time.get_ticks()
    # f makes it a string?
    score_surf = test_font.render(f'{current_time}', False, "#FCDC4D")
    score_rect = score_surf.get_rect(center = (window_width/2,50))
    screen.blit(score_surf,score_rect)
    print(current_time)

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python Game/font/Pixeltype.ttf',50)
game_active = True

sky_surf = pygame.image.load('Python Game/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,window_size)

grass_top_y = 371
ground_surf = pygame.image.load('Python Game/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,window_size)



harold_x_pos = 200
harold_y_pos = grass_top_y
harold_surf = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_surf = pygame.transform.flip(harold_surf, True, False)
harold_rect = harold_surf.get_rect(midbottom = (harold_x_pos,harold_y_pos))

enemy_x_pos = 600
enemy_y_pos = grass_top_y
enemy_surf = pygame.image.load('Python Game/graphics/slime/slime/original_frame.png')
enemy_surf = pygame.transform.scale(enemy_surf,wizard_pixel_size)
enemy_surf = pygame.transform.flip(enemy_surf,True, False)
enemy_rect = enemy_surf.get_rect(midbottom = (enemy_x_pos,enemy_y_pos))

wizard_surf = pygame.image.load('Python Game/graphics/wizard/wizard_idle1/sprite_00.png').convert_alpha()
wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
wizard_rect = wizard_surf.get_rect(midbottom = (80,grass_top_y))
wizard_gravity = 0
gravity_acceleration = -20

# Fireball
fireball_x_start = wizard_rect.right - 20
fireball_y_start = wizard_rect.centery + 24

fireball_x_pos = fireball_x_start
fireball_y_pos = fireball_y_start

fireball_x_speed = 0

fireball_speed = 4

fireball_surf = pygame.image.load('Python Game/graphics/fireball/fireball_move/sprite_0.png').convert_alpha()
fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)
fireball_rect = fireball_surf.get_rect(center = (fireball_x_pos,fireball_y_pos))

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        # if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
        #     if wizard_rect.collidepoint(event.pos): print ('collision')
       
        if game_active:
            if event.type == shoot_button:
               fireball_x_speed = fireball_speed

            if event.type == pygame.KEYDOWN:
                if event.key == jump_button and wizard_rect.bottom >= grass_top_y:  
                    wizard_gravity = gravity_acceleration
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = window_width

    # Active Game
    if game_active:    
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,0))
        # pygame.draw.line(screen,"#FCDC4D",score_rect.bottomleft,score_rect.bottomright,3)
        # screen.blit(score_surf,score_rect)

        # mouse_pos = pygame.mouse.get_pos()

        enemy_rect.x -= 4
        fireball_rect.x += fireball_x_speed
        if fireball_rect.left >= 800: 
            fireball_rect.centerx = fireball_x_start
            fireball_x_speed = 0
        # if fireball_x_speed != 0 and fireball_rect.colliderect(slime_rect):
        #     print('boom')
        # else:
        #     print('done boom')
        if enemy_rect.right <= 0: enemy_rect.left = window_width
        screen.blit(enemy_surf,enemy_rect)
        # print(wizard_rect.left) # can be used to get positions

        # Wizard
        wizard_gravity += 1
        wizard_rect.y += wizard_gravity
        if wizard_rect.bottom >= grass_top_y: wizard_rect.bottom = grass_top_y
        screen.blit(wizard_surf,wizard_rect)
        screen.blit(fireball_surf,fireball_rect)

        # Player collides with enemy
        if enemy_rect.colliderect(wizard_rect):
            game_active = False

        # if wizard_rect.colliderect(slime_rect): # returns 0 if no collision 1 if is
        # if wizard_rect.collidepoint(mouse_pos):

    # Menu Screen
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)