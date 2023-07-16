import pygame
from sys import exit

window_width = 800
window_height = 400
window_size = (window_width,window_height)
wizard_pixel_size = (128,128)

jump_button = pygame.K_SPACE
shoot_button = pygame.MOUSEBUTTONDOWN
additional_score = 0
score = 0

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    # f makes it a string?
    score_surf = test_font.render(f'{current_time + additional_score}', False, "#FCDC4D")
    score_rect = score_surf.get_rect(center = (window_width/2,50))
    screen.blit(score_surf,score_rect)
    # print(current_time)
    return current_time + additional_score

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Python Game - PR')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python Game/font/Pixeltype.ttf',50)
game_active = False
start_time = 0

sky_surf = pygame.image.load('Python Game/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,window_size)

grass_top_y = 371
ground_surf = pygame.image.load('Python Game/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,window_size)

# get dif enemy than slime cuz it's hitbox is really big compared to sprite
enemy_x_pos = 600
enemy_y_pos = grass_top_y + 8
enemy_surf = pygame.image.load('Python Game/graphics/enemy/evil_wizard.png')
enemy_surf = pygame.transform.scale(enemy_surf,wizard_pixel_size)
enemy_rect = enemy_surf.get_rect(midbottom = (enemy_x_pos,enemy_y_pos))

wizard_x_pos = 80
wizard_y_pos = grass_top_y
wizard_surf = pygame.image.load('Python Game/graphics/wizard/wizard_idle1/sprite_00.png').convert_alpha()
wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
wizard_rect = wizard_surf.get_rect(midbottom = (wizard_x_pos,wizard_y_pos))
wizard_gravity = 0
gravity_acceleration = -20



# Fireball
fireball_x_start = wizard_rect.right - 20
fireball_y_start = wizard_rect.centery + 24

fireball_x_pos = fireball_x_start
fireball_y_pos = fireball_y_start

fireball_x_start_speed = 0

fireball_speed = 4
fireball_gravity_when_held = 0

fireball_cooldown_time = 60
fireball_cooldown = 0
fireball_hit = False

fireball_surf = pygame.image.load('Python Game/graphics/fireball/fireball_move/sprite_0.png').convert_alpha()
fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)
fireball_rect = fireball_surf.get_rect(center = (fireball_x_pos,fireball_y_pos))

# class Fireball:
#     def __init__(x_start, y_start, x_speed, surf):
#         self.x_start = x_start
#         self.y_start = y_start
#         self.x_speed = x_speed
#         self.surf = surf

harold_x_pos = wizard_rect.centerx
harold_y_pos = wizard_rect.top + 12 # pixels at this scale based on wizard are 4 pixels each
harold_surf = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_surf = pygame.transform.flip(harold_surf, True, False)
harold_rect = harold_surf.get_rect(midbottom = (harold_x_pos,harold_y_pos))
harold_gravity = 0

# Intro Screen
wizard_title_surf = pygame.image.load('Python Game/graphics/wizard/wizard_idle1/sprite_00.png').convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(192,192))
wizard_title_rect = wizard_title_surf.get_rect(center = (400,250))

harold_title_surf = pygame.image.load('Python Game/graphics/harold/harold1.png').convert_alpha()
harold_title_surf = pygame.transform.flip(harold_title_surf, True, False)
harold_title_surf = pygame.transform.scale_by(harold_title_surf,3/2)
harold_title_rect = harold_title_surf.get_rect(midbottom = (wizard_title_rect.centerx,wizard_title_rect.top + 18))

title_game_name_surf = test_font.render('Harold\'s Journey',False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,3/2)
title_game_name_rect = title_game_name_surf.get_rect(center = (400,70))

title_info_surf = test_font.render('Press any key or click to Start',False,"#FCDC4D")
title_info_rect = title_info_surf.get_rect(center = (wizard_title_rect.centerx,wizard_title_rect.centery + 120))

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        # if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
        #     if wizard_rect.collidepoint(event.pos): print ('collision')
       
        if game_active:
            # temporarily can only have one fireball at a time thanks to first part of 
            # the code after the and. Alternatively you get the fireball back instantly 
            # once you hit an enemy with it
            if event.type == shoot_button and (fireball_cooldown == 0 or fireball_hit):
               fireball_rect.center = (wizard_rect.right - 20,wizard_rect.centery + 24)
               fireball_x_start_speed = fireball_speed
               fireball_cooldown = fireball_cooldown_time
               fireball_hit = False

            if event.type == pygame.KEYDOWN:
                if event.key == jump_button and wizard_rect.bottom >= grass_top_y:  
                    wizard_gravity = gravity_acceleration
                    harold_gravity = gravity_acceleration
        
        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                enemy_rect.left = window_width
                start_time = int(pygame.time.get_ticks() / 1000)
                additional_score = 0

    # Active Game
    if game_active:    
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,0))
        # pygame.draw.line(screen,"#FCDC4D",score_rect.bottomleft,score_rect.bottomright,3)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        enemy_rect.x -= 4
        fireball_rect.x += fireball_x_start_speed
        if fireball_rect.left >= 800: 
            fireball_rect.centerx = fireball_x_start
            fireball_x_start_speed = 0
        if fireball_cooldown != 0:
            fireball_cooldown -= 1

        # Fireball collides with enemy
        if fireball_x_start_speed != 0 and fireball_rect.colliderect(enemy_rect):
            enemy_rect.left = window_width
            fireball_rect.centerx = fireball_x_start
            fireball_x_start_speed = 0
            fireball_hit = True
            additional_score += 5

        if enemy_rect.right <= 0: enemy_rect.left = window_width
        screen.blit(enemy_surf,enemy_rect)
        # print(wizard_rect.left) # can be used to get positions

        # Wizard
        wizard_gravity += 1
        harold_gravity += 1
        wizard_rect.y += wizard_gravity
        harold_rect.y += harold_gravity

        if wizard_rect.bottom >= grass_top_y: 
            wizard_rect.bottom = grass_top_y
            harold_rect.bottom = wizard_rect.top + 12
        screen.blit(wizard_surf,wizard_rect)
        if fireball_x_start_speed != 0:
            screen.blit(fireball_surf,fireball_rect)
        screen.blit(harold_surf,harold_rect)

        # Player collides with enemy
        if enemy_rect.colliderect(wizard_rect):
            game_active = False

        # if wizard_rect.colliderect(slime_rect): # returns 0 if no collision 1 if is
        # if wizard_rect.collidepoint(mouse_pos):

    # Menu Screen
    else:
        screen.fill('#54428E')
        screen.blit(wizard_title_surf,wizard_title_rect)
        screen.blit(harold_title_surf,harold_title_rect)
        screen.blit(title_info_surf,title_info_rect)

        score_message_surf = test_font.render(f'Score: {score}',False,"#FCDC4D")
        score_message_surf = pygame.transform.scale_by(score_message_surf,3/2)
        score_message_rect = score_message_surf.get_rect(center = (400,70))

        if score == 0:
            screen.blit(title_game_name_surf,title_game_name_rect)

        else:
            screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)