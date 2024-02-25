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
from graphics.health_bar.health_bar import *
from graphics.health_bar.outline_health_bar import *


# Functions
def display_score():
    temp_additional_score = wizard.sprite.get_additional_score()
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(str(current_time + temp_additional_score), False, '#FCDC4D')
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/8))
    screen.blit(score_surf,score_rect)
    return current_time + temp_additional_score


def display_stats():
    # Stat image Surfs - find a centralized place to keep all images so don't have to update this and the pickup class' version of the image
    # Damage
    damage_stat_image_surf = pygame.image.load('harolds_journey/graphics/pickups/damage/damage_pickup.png').convert_alpha()
    damage_stat_image_surf = pygame.transform.scale_by(damage_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    damage_stat_image_rect = damage_stat_image_surf.get_rect(center = (WINDOW_WIDTH*20/32,WINDOW_HEIGHT/8))

    damage_stat_surf = test_font.render('Damage: ' + str(wizard.sprite.get_wizard_damage_total()), False, '#FCDC4D')
    damage_stat_surf = pygame.transform.scale_by(damage_stat_surf, 0.9)
    damage_stat_rect = damage_stat_surf.get_rect(center = (WINDOW_WIDTH*95/128,WINDOW_HEIGHT/8))
    
    # Piercing
    piercing_stat_image_surf = pygame.image.load('harolds_journey/graphics/pickups/piercing/piercing_pickup.png').convert_alpha()
    piercing_stat_image_surf = pygame.transform.scale_by(piercing_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    piercing_stat_image_rect = piercing_stat_image_surf.get_rect(center = (WINDOW_WIDTH*20/32,WINDOW_HEIGHT*7/32))

    piercing_stat_surf = test_font.render('Piercing: ' + str(wizard.sprite.get_wizard_piercing_total()), False, '#FCDC4D')
    piercing_stat_surf = pygame.transform.scale_by(piercing_stat_surf, 0.9)
    piercing_stat_rect = piercing_stat_surf.get_rect(center = (WINDOW_WIDTH*24/32,WINDOW_HEIGHT*7/32))
    
    # Fireball Cooldown Stat
    # Fix text
    fireball_cooldown_stat_image_surf = pygame.image.load('harolds_journey/graphics/pickups/fireball_cooldown/fireball_cooldown_pickup.png').convert_alpha()
    fireball_cooldown_stat_image_surf = pygame.transform.scale_by(fireball_cooldown_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    fireball_cooldown_stat_image_rect = fireball_cooldown_stat_image_surf.get_rect(center = (WINDOW_WIDTH*20/32,WINDOW_HEIGHT*10/32))
    
    fireball_cooldown_stat_surf = test_font.render('Fireball Cooldown: ' + str(wizard.sprite.get_max_fireball_cooldown_time()), False, '#FCDC4D')
    fireball_cooldown_stat_surf = pygame.transform.scale_by(fireball_cooldown_stat_surf, 0.9)
    fireball_cooldown_stat_rect = fireball_cooldown_stat_surf.get_rect(center = (WINDOW_WIDTH*3/4,WINDOW_HEIGHT*9/32))
    
    # Fireball Cooldown Icon
    fireball_cooldown_x_pos = WINDOW_WIDTH * 3/8
    fireball_cooldown_y_pos = WINDOW_HEIGHT * 11/64
    fireball_cooldown_surf = pygame.image.load('harolds_journey/graphics/fireball/fireball_movement_animation/fireball_movement_00.png').convert_alpha()
    fireball_cooldown_rect = fireball_cooldown_surf.get_rect(center = (fireball_cooldown_x_pos,fireball_cooldown_y_pos))
    # Fireball Cooldown Overlay
    current_fireball_cooldown = wizard.sprite.get_current_fireball_cooldown()
    max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
    fireball_cooldown_overlay_function = current_fireball_cooldown / max_fireball_cooldown_time
    fireball_cooldown_overlay_color = pygame.Color(255,255,255)
    fireball_cooldown_overlay_width = fireball_cooldown_surf.get_width()
    fireball_cooldown_overlay_height = fireball_cooldown_surf.get_height() * fireball_cooldown_overlay_function
    fireball_cooldown_overlay_left = fireball_cooldown_rect.left
    fireball_cooldown_overlay_top = fireball_cooldown_rect.bottom - int(fireball_cooldown_overlay_height)
    fireball_cooldown_overlay_surf = pygame.Surface((fireball_cooldown_overlay_width, fireball_cooldown_overlay_height))
    fireball_cooldown_overlay_surf.fill(fireball_cooldown_overlay_color)
    fireball_cooldown_overlay_surf.set_alpha(100)
    # Blits
    screen.blit(damage_stat_image_surf,damage_stat_image_rect)
    screen.blit(damage_stat_surf,damage_stat_rect)
    
    screen.blit(piercing_stat_image_surf,piercing_stat_image_rect)
    screen.blit(piercing_stat_surf,piercing_stat_rect)
    
    screen.blit(fireball_cooldown_stat_image_surf,fireball_cooldown_stat_image_rect)
    screen.blit(fireball_cooldown_stat_surf,fireball_cooldown_stat_rect)
    
    screen.blit(fireball_cooldown_surf,fireball_cooldown_rect)
    screen.blit(fireball_cooldown_overlay_surf, (fireball_cooldown_overlay_left, fireball_cooldown_overlay_top))


def player_and_obstacle_collision_bool(): # Basically game over condition
    if pygame.sprite.spritecollide(wizard.sprite,obstacle_group,False):
        temp_wizard_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
        wizard.sprite.set_current_fireball_cooldown(temp_wizard_max_fireball_cooldown_time)
        for obstacle in obstacle_group:
            obstacle.kill()
        obstacle_group.empty()
        for projectile in projectile_group:
            projectile.kill()
        projectile_group.empty()
        for pickup in pickup_group:
            pickup.kill()
        pickup_group.empty()
        for health_bar in health_bar_group:
            health_bar.kill()
        for outline_health_bar in outline_health_bar_group:
            outline_health_bar.kill()
        health_bar_group.empty()
        outline_health_bar_group.empty()
        pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)
        return False
    else: return True


def obstacle_and_player_owned_projectile_collision():
    temp_additional_score = wizard.sprite.get_additional_score()
    for projectile in projectile_group:
        if pygame.sprite.spritecollide(projectile,obstacle_group,False):
            obstacles_overlapping = pygame.sprite.spritecollide(projectile,obstacle_group,False)
            for obstacle in obstacles_overlapping:
                temp_obstacle_health = obstacle.get_current_health()
                temp_obstacle_immunity_limit = obstacle.get_immunity_limit()
                temp_obstacle_immunity_timer = obstacle.get_immunity_timer()
                temp_projectile_damage = projectile.get_fireball_damage()
                temp_projectile_piercing = projectile.get_fireball_piercing()
                temp_obstacle_x_pos = int(obstacle.get_x_pos())
                temp_obstacle_y_pos = int(obstacle.get_y_pos())
                if temp_obstacle_immunity_timer <= 0:
                    if (temp_obstacle_health - temp_projectile_damage) <= 0:
                        # Pickup Spawn
                        if randint(1,5) == 5: # Chance to drop damage pickup
                            pickup_group.add(Pickup('damage',temp_obstacle_x_pos,temp_obstacle_y_pos))
                        if randint(1,10) == 10: # Chance to drop fireball cooldown pickup
                            pickup_group.add(Pickup('fireball_cooldown',temp_obstacle_x_pos,temp_obstacle_y_pos))
                        if randint(1,20) == 20: # Chance to drop piercing pickup
                            pickup_group.add(Pickup('piercing',temp_obstacle_x_pos,temp_obstacle_y_pos))
                        temp_additional_score += obstacle.get_points()
                        # Health Bar and Outline Health Bar Cleanup
                        old_health_bar = health_bar_ownership_group[obstacle]
                        old_outline_bar = outline_health_bar_ownership_group[old_health_bar]
                        old_outline_bar.kill()
                        old_health_bar.kill()
                        pygame.sprite.spritecollide(projectile,obstacle_group,True)
                        pygame.mixer.Channel(OBSTACLE_DEATH_CHANNEL).play(obstacle_death_sound)
                        wizard.sprite.set_additional_score(temp_additional_score)
                    else:
                        obstacle.set_current_health(temp_obstacle_health - temp_projectile_damage)
                        if (temp_projectile_piercing > 1):
                            obstacle.set_immunity_timer(temp_obstacle_immunity_limit)
                    wizard.sprite.set_fireball_hit(True)
                    temp_projectile_piercing -= 1
                    if temp_projectile_piercing <= 0:
                        projectile_group.remove(projectile)
                    else:
                        projectile.set_fireball_piercing(temp_projectile_piercing)


def player_and_pickup_collision():
    if pygame.sprite.spritecollide(wizard.sprite,pickup_group,False):
        pickups_overlapping = pygame.sprite.spritecollide(wizard.sprite,pickup_group,False)
        for pickup in pickups_overlapping:
            temp_bonus = pickup.get_bonus()
            temp_damage = wizard.sprite.get_wizard_damage_percent()
            temp_piercing = wizard.sprite.get_wizard_piercing_increase()
            temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
            if pickup.get_type() == 'damage':
                wizard.sprite.set_wizard_damage_percent(temp_damage + temp_bonus)
            if pickup.get_type() == 'piercing':
                wizard.sprite.set_wizard_piercing_increase(temp_piercing + temp_bonus)
            if pickup.get_type() == 'fireball_cooldown' and temp_max_fireball_cooldown_time >= 6:
                wizard.sprite.set_max_fireball_cooldown_time(temp_max_fireball_cooldown_time - temp_bonus)
            pygame.sprite.spritecollide(wizard.sprite,pickup_group,True)


wizard = pygame.sprite.GroupSingle()
wizard.add(Player())

harold = pygame.sprite.GroupSingle()
harold.add(Harold(wizard))

obstacle_group = pygame.sprite.Group()

projectile_group = pygame.sprite.Group()

pickup_group = pygame.sprite.Group()

health_bar_group = pygame.sprite.Group() # add this in

outline_health_bar_group = pygame.sprite.Group()

health_bar_ownership_group = {pygame.sprite.Sprite(): pygame.sprite.Sprite()}

outline_health_bar_ownership_group = {pygame.sprite.Sprite(): pygame.sprite.Sprite()}

moving_sprites = [wizard, harold, obstacle_group, projectile_group, pickup_group, outline_health_bar_group, health_bar_group,]

sky_surf = pygame.image.load('harolds_journey/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,WINDOW_SIZE)

ground_surf = pygame.image.load('harolds_journey/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,WINDOW_SIZE)

# Intro Screen
wizard_title_start_x_pos = WINDOW_WIDTH / 2
wizard_title_start_y_pos = WINDOW_HEIGHT * 3/4
wizard_title_surf = pygame.image.load('harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png').convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(WIZARD_WIDTH * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200), WIZARD_HEIGHT * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)))
wizard_title_rect = wizard_title_surf.get_rect(center = (wizard_title_start_x_pos,wizard_title_start_y_pos))

harold_title_start_x_pos = wizard_title_rect.centerx
harold_title_start_y_pos = wizard_title_rect.top - (52/4 * PIXEL_SIZE)
harold_title_surf = pygame.image.load('harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
harold_title_surf = pygame.transform.scale_by(harold_title_surf,(2.25 * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)))
harold_title_rect = harold_title_surf.get_rect(midbottom = (harold_title_start_x_pos,harold_title_start_y_pos))

title_game_name_surf = test_font.render('Harold\'s Journey',False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,((WINDOW_WIDTH + WINDOW_HEIGHT)/1200))
title_game_name_rect = title_game_name_surf.get_rect(center = (WINDOW_WIDTH/2,((70/400) * WINDOW_HEIGHT)))

title_info_start_x_pos = wizard_title_rect.centerx
title_info_start_y_pos = wizard_title_rect.centery + ((40/400) * WINDOW_HEIGHT)
title_info_start_pos = (title_info_start_x_pos,title_info_start_y_pos)
title_info_surf = test_font.render('Press any key or click to Start',False,"#FCDC4D")
title_info_surf = pygame.transform.scale_by(title_info_surf,((WINDOW_WIDTH + WINDOW_HEIGHT)/1200))
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
                new_obstacle = Obstacle(choice(['bird','skeleton','skeleton','skeleton']),int(pygame.time.get_ticks() / 1000) - start_time)
                obstacle_group.add(new_obstacle)
                # Health Bar
                new_health_bar = HealthBar(new_obstacle, new_obstacle.get_current_health(), new_obstacle.get_max_health())
                health_bar_group.add(new_health_bar)
                health_bar_ownership_group[new_obstacle] = new_health_bar
                # Outline Health Bar
                new_outline_health_bar = OutlineHealthBar(new_health_bar, new_obstacle.get_x_pos(), new_obstacle.get_y_pos())
                outline_health_bar_group.add(new_outline_health_bar)
                outline_health_bar_ownership_group[new_health_bar] = new_outline_health_bar
            if wizard.sprite.get_wizard_dead() == False and event.type == shoot_button:
                if wizard.sprite.get_current_fireball_cooldown() == 0 or wizard.sprite.get_fireball_hit():
                    wizard.sprite.play_fireball_sound()
                    wizard.sprite.set_fireball_shot(True)
                    temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
                    wizard.sprite.set_current_fireball_cooldown(temp_max_fireball_cooldown_time)
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
            score = display_score()
            display_stats() # updating stats
            
            for sprite in moving_sprites: # Holds all things to be drawn
                sprite.draw(screen)
                sprite.update()
            
            obstacle_and_player_owned_projectile_collision()
            
            player_and_pickup_collision()

            wizard_alive = player_and_obstacle_collision_bool()

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
        score_message_surf = pygame.transform.scale_by(score_message_surf,((WINDOW_WIDTH + WINDOW_HEIGHT)/1200))
        score_message_rect = score_message_surf.get_rect(center = (WINDOW_WIDTH/2,(100/800 * WINDOW_HEIGHT)))

        if score == 0: screen.blit(title_game_name_surf,title_game_name_rect)
        else: screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)