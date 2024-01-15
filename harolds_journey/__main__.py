"""Main Gameloop"""
from sys import exit
from random import randint, choice

import pygame

from controls import * 
from global_vars import * 
from harold import *
from obstacle import *
from pickup import *
from player import *
from projectile import *

# Functions
def display_score():
    temp_additional_score = wizard.sprite.get_additional_score()
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(str(current_time + temp_additional_score), False, '#FCDC4D')
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/8))
    screen.blit(score_surf,score_rect)
    return current_time + temp_additional_score

def display_stats():
    damage_stat_surf = test_font.render('Damage: ' + str(wizard.sprite.get_wizard_damage_total()), False, '#FCDC4D')
    damage_stat_rect = damage_stat_surf.get_rect(center = (WINDOW_WIDTH*95/128,WINDOW_HEIGHT/8))
    piercing_stat_surf = test_font.render('Piercing: ' + str(wizard.sprite.get_wizard_piercing_total()), False, '#FCDC4D')
    piercing_stat_rect = piercing_stat_surf.get_rect(center = (WINDOW_WIDTH*24/32,WINDOW_HEIGHT*7/32))
    screen.blit(damage_stat_surf,damage_stat_rect)
    screen.blit(piercing_stat_surf,piercing_stat_rect)

def collision_sprite(): # Basically game over condition
    if pygame.sprite.spritecollide(wizard.sprite,obstacle_group,False):
        temp_wizard_fireball_cooldown_time = wizard.sprite.get_fireball_cooldown_time()
        wizard.sprite.set_current_fireball_cooldown(temp_wizard_fireball_cooldown_time)
        obstacle_group.empty()
        projectile_group.empty()
        pickup_group.empty()
        return False
    else: return True

def projectile_collision():
    temp_additional_score = wizard.sprite.get_additional_score()
    for projectile in projectile_group:
        if pygame.sprite.spritecollide(projectile,obstacle_group,False):
            obstacles_overlapping = pygame.sprite.spritecollide(projectile,obstacle_group,False)
            for obstacle in obstacles_overlapping:
                temp_obstacle_health = obstacle.get_health()
                temp_obstacle_immunity_limit = obstacle.get_immunity_limit()
                temp_obstacle_immunity_timer = obstacle.get_immunity_timer()
                temp_projectile_damage = projectile.get_fireball_damage()
                temp_projectile_piercing = projectile.get_fireball_piercing()
                temp_obstacle_x_pos = int(obstacle.get_x_pos())
                temp_obstacle_y_pos = int(obstacle.get_y_pos())
                if temp_obstacle_immunity_timer <= 0:
                    if (temp_obstacle_health - temp_projectile_damage) <= 0:
                        if randint(1,5) == 5: # Chance to drop pickup
                            pickup_group.add(Pickup(choice(['piercing','damage','damage','damage']),temp_obstacle_x_pos,temp_obstacle_y_pos))
                        temp_additional_score += obstacle.get_points()
                        pygame.sprite.spritecollide(projectile,obstacle_group,True)
                        pygame.mixer.Channel(OBSTACLE_DEATH_CHANNEL).play(obstacle_death_sound)
                        wizard.sprite.set_additional_score(temp_additional_score)
                    else:
                        obstacle.set_health(temp_obstacle_health - temp_projectile_damage)
                        if (temp_projectile_piercing > 1):
                            obstacle.set_immunity_timer(temp_obstacle_immunity_limit)
                    wizard.sprite.set_fireball_hit(True)
                    temp_projectile_piercing -= 1
                    if temp_projectile_piercing <= 0:
                        projectile_group.remove(projectile)
                    else:
                        projectile.set_fireball_piercing(temp_projectile_piercing)

def pickup_collision():
    if pygame.sprite.spritecollide(wizard.sprite,pickup_group,False):
        print('Pickup picked up')
        pickups_overlapping = pygame.sprite.spritecollide(wizard.sprite,pickup_group,False)
        for pickup in pickups_overlapping:
            temp_bonus = pickup.get_bonus()
            temp_damage = wizard.sprite.get_wizard_damage_percent()
            temp_piercing = wizard.sprite.get_wizard_piercing_increase()
            if pickup.get_type() == 'damage':
                wizard.sprite.set_wizard_damage_percent(temp_damage + temp_bonus)
            if pickup.get_type() == 'piercing':
                wizard.sprite.set_wizard_piercing_increase(temp_piercing + temp_bonus)
            pygame.sprite.spritecollide(wizard.sprite,pickup_group,True)

wizard = pygame.sprite.GroupSingle()
wizard.add(Player())

harold = pygame.sprite.GroupSingle()
harold.add(Harold(wizard))

obstacle_group = pygame.sprite.Group()

projectile_group = pygame.sprite.Group()

pickup_group = pygame.sprite.Group()

moving_sprites = [wizard, harold, obstacle_group, projectile_group, pickup_group]

sky_surf = pygame.image.load('harolds_journey/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,WINDOW_SIZE)

ground_surf = pygame.image.load('harolds_journey/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,WINDOW_SIZE)

# Stat image Surfs - find a centralized place to keep all images so don't have to update this and the pickup class' version of the image
damage_stat_image_surf = pygame.image.load('harolds_journey\graphics\pickups\damage\damage_pickup.png').convert_alpha()
damage_stat_image_surf = pygame.transform.scale_by(damage_stat_image_surf,4)
damage_stat_image_rect = damage_stat_image_surf.get_rect(center = (WINDOW_WIDTH*21/32,WINDOW_HEIGHT/8))
piercing_stat_image_surf = pygame.image.load('harolds_journey\graphics\pickups\piercing\piercing_pickup.png').convert_alpha()
piercing_stat_image_surf = pygame.transform.scale_by(piercing_stat_image_surf,4)
piercing_stat_image_rect = piercing_stat_image_surf.get_rect(center = (WINDOW_WIDTH*21/32,WINDOW_HEIGHT*7/32))

# Intro Screen
wizard_title_start_x_pos = WINDOW_WIDTH / 2
wizard_title_start_y_pos = WINDOW_HEIGHT  * 3/4
wizard_title_surf = pygame.image.load('harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png').convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(WIZARD_WIDTH * (WINDOW_WIDTH/WINDOW_HEIGHT), WIZARD_HEIGHT * (WINDOW_WIDTH/WINDOW_HEIGHT)))
wizard_title_rect = wizard_title_surf.get_rect(center = (wizard_title_start_x_pos,wizard_title_start_y_pos))

harold_title_start_x_pos = wizard_title_rect.centerx
harold_title_start_y_pos = wizard_title_rect.top - (52/4 * PIXEL_SIZE)
harold_title_surf = pygame.image.load('harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
harold_title_surf = pygame.transform.scale_by(harold_title_surf,(2.25 * (WINDOW_WIDTH/WINDOW_HEIGHT)))
harold_title_rect = harold_title_surf.get_rect(midbottom = (harold_title_start_x_pos,harold_title_start_y_pos))

title_game_name_surf = test_font.render('harolds_journey',False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,(WINDOW_WIDTH/WINDOW_HEIGHT))
title_game_name_rect = title_game_name_surf.get_rect(center = (WINDOW_WIDTH/2,((70/400) * WINDOW_HEIGHT)))

title_info_start_x_pos = wizard_title_rect.centerx
title_info_start_y_pos = wizard_title_rect.centery + ((40/400) * WINDOW_HEIGHT)
title_info_start_pos = (title_info_start_x_pos,title_info_start_y_pos)
title_info_surf = test_font.render('Press any key or click to Start',False,"#FCDC4D")
title_info_surf = pygame.transform.scale_by(title_info_surf,(WINDOW_WIDTH/WINDOW_HEIGHT))
title_info_rect = title_info_surf.get_rect(center = (title_info_start_pos))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
       
        if game_active:
            # Obstacle Timer Event Detection
            if event.type == obstacle_timer: 
                obstacle_group.add(Obstacle(choice(['bird','skeleton','skeleton','skeleton']),int(pygame.time.get_ticks() / 1000) - start_time))
                print(int(pygame.time.get_ticks() / 1000) - start_time)
            if wizard.sprite.get_wizard_dead() == False and event.type == shoot_button:
                if wizard.sprite.get_current_fireball_cooldown() == 0 or wizard.sprite.get_fireball_hit():
                    wizard.sprite.play_fireball_sound()
                    wizard.sprite.set_fireball_shot(True)
                    temp_fireball_cooldown_time = wizard.sprite.get_fireball_cooldown_time()
                    wizard.sprite.set_current_fireball_cooldown(temp_fireball_cooldown_time)
                    wizard.sprite.set_fireball_hit(False)
                    projectile_group.add(Projectile('fireball', wizard))

        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                wizard_alive = True
                start_time = int(pygame.time.get_ticks() / 1000)
                additional_score = 0

    # Active Game
    if game_active:
        if bg_music_timer == 0:
            pygame.mixer.Channel(BG_MUSIC_CHANNEL).play(bg_music)
        elif bg_music_timer >= (25 * 60):
            bg_music_timer = -1
        if wizard_alive: 
            bg_music_timer += 1
            screen.blit(sky_surf,(0,0))
            screen.blit(ground_surf,(0,0))
            # Stat Image Postions
            screen.blit(damage_stat_image_surf,damage_stat_image_rect)
            screen.blit(piercing_stat_image_surf,piercing_stat_image_rect)
            score = display_score()
            display_stats() # updating stats
            
            for sprite in moving_sprites: # Holds all things to be drawn
                sprite.draw(screen)
                sprite.update()
            
            projectile_collision()
            
            pickup_collision()

            wizard_alive = collision_sprite()

        else: # Work on death animation
            wizard.sprite.set_wizard_dead(True)
            screen.blit(sky_surf,(0,0))
            screen.blit(ground_surf,(0,0))
            
            wizard.draw(screen) # draws sprites
            harold.draw(screen)
            
            wizard.update() # updates sprites
            harold.update()
            death_counter += 1
            if death_counter > 120:
                game_active = False
            
    # Menu Screen
    else:         
        wizard.sprite.reset()
        harold.sprite.reset()
        pygame.event.clear()
        death_counter = 0
        bg_music_timer = 0
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,0))
        screen.blit(wizard_title_surf,wizard_title_rect)
        screen.blit(harold_title_surf,harold_title_rect)
        screen.blit(title_info_surf,title_info_rect)

        wizard_title_rect.midbottom = (wizard_title_start_x_pos,wizard_title_start_y_pos)

        harold_title_rect.midbottom = (harold_title_start_x_pos,harold_title_start_y_pos)

        score_message_surf = test_font.render('Score: ' + str(score),False,"#FCDC4D")
        score_message_surf = pygame.transform.scale_by(score_message_surf,3/2)
        score_message_rect = score_message_surf.get_rect(center = (WINDOW_WIDTH/2,(100/800 * WINDOW_HEIGHT)))

        if score == 0: screen.blit(title_game_name_surf,title_game_name_rect)
        else: screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)