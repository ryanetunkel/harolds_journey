"""Main Gameloop"""
from math import ceil
from random import randint, choice
from sys import exit

import pygame

from buff import *
from controls import *
from global_vars import *
from graphics.health_bar.health_bar import *
from graphics.health_bar.outline_health_bar import *
from harold import *
from intro import *
from menu import *
from obstacle import *
from pickup import *
from player import *
from projectile import *


wizard.add(Player())
harold.add(Harold(wizard))


# Functions
def calculate_score() -> int:
    global pause_time

    temp_additional_score = wizard.sprite.get_additional_score()
    current_time = ceil((pygame.time.get_ticks() - start_time - pause_time) / 1000)

    return current_time + temp_additional_score


def display_score():
    temp_score = calculate_score()
    # Score
    score_title_surf = base_font.render("SCORE", False, "#FCDC4D")
    score_title_rect = score_title_surf.get_rect(center = (window_width/2,window_height*1/16))
    score_surf = base_font.render(str(temp_score), False, "#FCDC4D")
    score_rect = score_surf.get_rect(center = (window_width/2,window_height/8))
    # Score Blit
    screen.blit(score_title_surf,score_title_rect)
    screen.blit(score_surf,score_rect)
    return temp_score


def display_high_score(score_rect):
    # High Score
    score_y_offset = window_height * 1/44
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    high_score_start_x_pos = center_screen_width
    high_score_start_y_pos = score_rect.bottom + score_y_offset
    high_score_start_pos = (high_score_start_x_pos,high_score_start_y_pos)
    high_score_surf = base_font.render(f"High Score: {high_score}",False,"#FCDC4D")
    high_score_scale = 0.4 * 3/2
    high_score_surf = pygame.transform.scale_by(high_score_surf,high_score_scale)
    high_score_rect = high_score_surf.get_rect(center = (high_score_start_pos))
    # High Score Blit
    screen.blit(high_score_surf,high_score_rect)


def display_controls():
    control_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",int(window_height/8))

    edited_controls_file_dict = get_edited_controls_file_dict()
    edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
    displayed_control_y_pos_offset = window_height * 1/32
    displayed_control_index = 0
    displayed_control_scalar = 0.3
    displayed_control_surf_dict = {}
    displayed_control_rect_dict = {}
    button_scalar = 3/2
    for displayed_control_name in edited_controls_display_names_dict.keys():
        displayed_control_start_x_pos = window_width * 7/8
        displayed_control_start_y_pos = (6/32 * window_height) + displayed_control_y_pos_offset * displayed_control_index
        displayed_control_start_pos = (displayed_control_start_x_pos,displayed_control_start_y_pos)
        displayed_control_name_underscore_removed = displayed_control_name.replace("_", " ")
        displayed_control_name_button_removed = displayed_control_name_underscore_removed.replace(" button", "")
        displayed_control_name_capitalized = displayed_control_name_button_removed.title()
        displayed_control_surf = control_font.render(f"{displayed_control_name_capitalized}: {edited_controls_display_names_dict[displayed_control_name]}",False,"#FCDC4D")
        displayed_control_scale = button_scalar * displayed_control_scalar
        displayed_control_surf = pygame.transform.scale_by(displayed_control_surf,displayed_control_scale)
        displayed_control_surf_dict.update({displayed_control_name:displayed_control_surf})
        displayed_control_rect = displayed_control_surf.get_rect(center = (displayed_control_start_pos))
        displayed_control_rect_dict.update({displayed_control_name:displayed_control_rect})
        displayed_control_index += 1

    for displayed_control_name in edited_controls_display_names_dict.keys():
        displayed_control_surf = displayed_control_surf_dict[displayed_control_name]
        displayed_control_rect = displayed_control_rect_dict[displayed_control_name]
        screen.blit(displayed_control_surf,displayed_control_rect)


def display_in_game_health():
    health_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",int(window_height/18))

    # Health
    health_stat_image_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_health/heart.png").convert_alpha()
    health_stat_image_surf = pygame.transform.scale_by(health_stat_image_surf,4 * (window_width + window_height)/1200)
    health_stat_image_rect = health_stat_image_surf.get_rect(center = (0,0))
    health_stat_image_x_offset = health_stat_image_rect.width/2+window_width/64
    health_stat_image_y_offset = health_stat_image_rect.height/2+window_width/64
    health_stat_image_rect = health_stat_image_surf.get_rect(center = (health_stat_image_x_offset,health_stat_image_y_offset))

    health_stat_surf = health_font.render(str(wizard.sprite.get_wizard_current_health()), False, "#000000")
    health_stat_surf = pygame.transform.scale_by(health_stat_surf, 1.3)
    health_stat_rect = health_stat_surf.get_rect(center = (0,0))
    health_stat_rect_x_offset = health_stat_image_x_offset + health_stat_rect.width/18
    health_stat_rect_y_offset = health_stat_image_y_offset + health_stat_rect.height*3/18
    health_stat_rect = health_stat_surf.get_rect(center = (health_stat_rect_x_offset,health_stat_rect_y_offset))

    # Shield Health
    shield_health_stat_x_pos_offset = health_stat_image_x_offset + health_stat_image_rect.width
    shield_health_stat_image_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_health/shield_stat_display.png").convert_alpha()
    shield_health_stat_image_surf = pygame.transform.scale_by(shield_health_stat_image_surf,4 * (window_width + window_height)/1200)
    # Shield 1
    shield_health_stat_image_rect_0 = shield_health_stat_image_surf.get_rect(center = (0,health_stat_image_y_offset))
    shield_health_stat_x_pos_0 = shield_health_stat_x_pos_offset + shield_health_stat_image_rect_0.width*2
    shield_health_stat_image_rect_0 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_0,health_stat_image_y_offset))
    # Shield 2
    shield_health_stat_image_rect_1 = shield_health_stat_image_surf.get_rect(center = (0,health_stat_image_y_offset))
    shield_health_stat_x_pos_1 = shield_health_stat_x_pos_0 - shield_health_stat_image_rect_1.width
    shield_health_stat_image_rect_1 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_1,health_stat_image_y_offset))
    # Shield 3
    shield_health_stat_image_rect_2 = shield_health_stat_image_surf.get_rect(center = (0,health_stat_image_y_offset))
    shield_health_stat_x_pos_2 = shield_health_stat_x_pos_1 - shield_health_stat_image_rect_2.width
    shield_health_stat_image_rect_2 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_2,health_stat_image_y_offset))

    # Blits
    screen.blit(health_stat_image_surf,health_stat_image_rect)
    screen.blit(health_stat_surf,health_stat_rect)
    # Shield Health Blit
    if wizard.sprite.get_shield():
        shield_stat_images = [
            shield_health_stat_image_rect_0,
            shield_health_stat_image_rect_1,
            shield_health_stat_image_rect_2,
        ]
        for shield_stat_index in range(0,wizard.sprite.get_current_shield_health()):
            screen.blit(shield_health_stat_image_surf,shield_stat_images[shield_stat_index])


def display_in_game_buffs():
    # Buffs
    # Health coords: WINDOW_WIDTH*1/16,WINDOW_HEIGHT*3/32
    # Arrange in order recieved going from right to left
    order_offset = window_width*3/64
    default_image_x_pos = window_width*15/16
    default_image_y_pos = window_height*3/32
    # Double Jump
    if wizard.sprite.get_double_jump():
        double_jump_idx = wizard.sprite.get_buff_idx_in_buff_list("double_jump")
        double_jump_x_offset = order_offset * double_jump_idx
        double_jump_buff_image_x_pos = default_image_x_pos - double_jump_x_offset
        double_jump_buff_image_y_pos = default_image_y_pos
        double_jump_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(double_jump_idx)
        double_jump_buff_image_surf = pygame.transform.scale_by(double_jump_buff_image_surf,4 * (window_width + window_height)/1200)
        double_jump_buff_image_rect = double_jump_buff_image_surf.get_rect(center = (double_jump_buff_image_x_pos,double_jump_buff_image_y_pos))
    # Shield
    if wizard.sprite.get_shield():
        shield_idx = wizard.sprite.get_buff_idx_in_buff_list("shield")
        shield_x_offset = order_offset * shield_idx
        shield_buff_image_x_pos = default_image_x_pos - shield_x_offset
        shield_buff_image_y_pos = default_image_y_pos
        shield_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(shield_idx)
        shield_buff_image_surf = pygame.transform.scale_by(shield_buff_image_surf,4 * (window_width + window_height)/1200)
        shield_buff_image_rect = shield_buff_image_surf.get_rect(center = (shield_buff_image_x_pos,shield_buff_image_y_pos))
    # Knockback
    if wizard.sprite.get_knockback():
        knockback_idx = wizard.sprite.get_buff_idx_in_buff_list("knockback")
        knockback_x_offset = order_offset * knockback_idx
        knockback_buff_image_x_pos = default_image_x_pos - knockback_x_offset
        knockback_buff_image_y_pos = default_image_y_pos
        knockback_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(knockback_idx)
        knockback_buff_image_surf = pygame.transform.scale_by(knockback_buff_image_surf,4 * (window_width + window_height)/1200)
        knockback_buff_image_rect = knockback_buff_image_surf.get_rect(center = (knockback_buff_image_x_pos,knockback_buff_image_y_pos))

    # Blits
    # Double Jump Buff Blit
    if wizard.sprite.get_double_jump():
        screen.blit(double_jump_buff_image_surf,double_jump_buff_image_rect)
    # Shield Buff Blit Blit
    if wizard.sprite.get_shield():
        screen.blit(shield_buff_image_surf,shield_buff_image_rect)
    # Knockback Buff Blit Blit
    if wizard.sprite.get_knockback():
        screen.blit(knockback_buff_image_surf,knockback_buff_image_rect)


def display_in_game_stats():
    # Stat image Surfs - Find a centralized place to keep all images so don't have to update this and the pickup class' version of the image
    stat_image_surf_x_pos = window_width/4 #29/128 dif
    stat_image_surf_y_pos_offset = window_height*3/32
    # First
    damage_stat_image_y_pos = window_height*5/64
    # Second
    piercing_stat_image_y_pos = damage_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Third
    fireball_cooldown_stat_image_y_pos = piercing_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Fourth
    speed_stat_image_y_pos = fireball_cooldown_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Stat text surfs
    stat_surf_x_pos = stat_image_surf_x_pos
    stat_surf_y_pos_offset = stat_image_surf_y_pos_offset
    # First
    damage_stat_x_pos = stat_surf_x_pos
    damage_stat_y_pos = damage_stat_image_y_pos + window_width/256
    # Second
    piercing_stat_x_pos = stat_surf_x_pos
    piercing_stat_y_pos = damage_stat_y_pos + stat_surf_y_pos_offset
    # Third
    fireball_cooldown_stat_x_pos = stat_surf_x_pos
    fireball_cooldown_stat_y_pos = piercing_stat_y_pos + stat_surf_y_pos_offset
    # Fourth
    speed_stat_x_pos = stat_surf_x_pos
    speed_stat_y_pos = fireball_cooldown_stat_y_pos + stat_surf_y_pos_offset
    # Damage
    damage_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/damage/damage_pickup.png").convert_alpha()
    damage_stat_image_surf = pygame.transform.scale_by(damage_stat_image_surf,4 * (window_width + window_height)/1200)
    damage_stat_image_rect = damage_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,damage_stat_image_y_pos))

    damage_stat_surf = base_font.render("Damage: " + str(wizard.sprite.get_wizard_damage_total()), False, "#FCDC4D")
    damage_stat_surf = pygame.transform.scale_by(damage_stat_surf, 0.9)
    damage_stat_rect = damage_stat_surf.get_rect(center = (damage_stat_x_pos,damage_stat_y_pos))
    damage_stat_rect = damage_stat_surf.get_rect(center = (damage_stat_x_pos+damage_stat_rect.width/2+damage_stat_image_rect.width,damage_stat_y_pos))

    # Piercing
    piercing_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/piercing/piercing_pickup.png").convert_alpha()
    piercing_stat_image_surf = pygame.transform.scale_by(piercing_stat_image_surf,4 * (window_width + window_height)/1200)
    piercing_stat_image_rect = piercing_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,piercing_stat_image_y_pos))

    piercing_stat_surf = base_font.render("Piercing: " + str(wizard.sprite.get_wizard_piercing_total() - 1), False, "#FCDC4D")
    piercing_stat_surf = pygame.transform.scale_by(piercing_stat_surf, 0.9)
    piercing_stat_rect = piercing_stat_surf.get_rect(center = (piercing_stat_x_pos,piercing_stat_y_pos))
    piercing_stat_rect = piercing_stat_surf.get_rect(center = (piercing_stat_x_pos+piercing_stat_rect.width/2+piercing_stat_image_rect.width,piercing_stat_y_pos))

    # Fireball Cooldown Stat
    fireball_cooldown_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/fireball_cooldown/fireball_cooldown_pickup.png").convert_alpha()
    fireball_cooldown_stat_image_surf = pygame.transform.scale_by(fireball_cooldown_stat_image_surf,4 * (window_width + window_height)/1200)
    fireball_cooldown_stat_image_rect = fireball_cooldown_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,fireball_cooldown_stat_image_y_pos))

    fireball_cooldown_stat_surf = base_font.render(f"Cooldown: {round(wizard.sprite.get_max_fireball_cooldown_time()/60, 2)}s", False, "#FCDC4D")
    fireball_cooldown_stat_surf = pygame.transform.scale_by(fireball_cooldown_stat_surf, 0.9)
    fireball_cooldown_stat_rect = fireball_cooldown_stat_surf.get_rect(center = (fireball_cooldown_stat_x_pos,fireball_cooldown_stat_y_pos))
    fireball_cooldown_stat_rect = fireball_cooldown_stat_surf.get_rect(center = (fireball_cooldown_stat_x_pos+fireball_cooldown_stat_rect.width/2+fireball_cooldown_stat_image_rect.width,fireball_cooldown_stat_y_pos))

    # Fireball Cooldown Icon
    fireball_cooldown_y_pos = window_height * 7/32
    fireball_cooldown_surf = pygame.image.load("harolds_journey/graphics/fireball/fireball_movement_animation/fireball_movement_00.png").convert_alpha()
    fireball_cooldown_surf = pygame.transform.scale_by(fireball_cooldown_surf,(window_width + window_height)/1200)
    fireball_cooldown_rect = fireball_cooldown_surf.get_rect(center = (0,fireball_cooldown_y_pos))
    fireball_cooldown_x_pos = fireball_cooldown_rect.width/2 + window_width/64
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
    fireball_cooldown_overlay_rect = (fireball_cooldown_overlay_left, fireball_cooldown_overlay_top)

    # Speed
    speed_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/speed/speed_pickup.png").convert_alpha()
    speed_stat_image_surf = pygame.transform.scale_by(speed_stat_image_surf,4 * (window_width + window_height)/1200)
    speed_stat_image_rect = speed_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,speed_stat_image_y_pos))

    speed_stat_surf = base_font.render("Speed: " + str(round((wizard.sprite.get_wizard_speed()/wizard_width)*60, 2)), False, "#FCDC4D")
    speed_stat_surf = pygame.transform.scale_by(speed_stat_surf, 0.9)
    speed_stat_rect = speed_stat_surf.get_rect(center = (speed_stat_x_pos,speed_stat_y_pos))
    speed_stat_rect = speed_stat_surf.get_rect(center = (speed_stat_x_pos+speed_stat_rect.width/2+speed_stat_image_rect.width,speed_stat_y_pos))

    # Blits
    # Damage Blit
    screen.blit(damage_stat_image_surf,damage_stat_image_rect)
    screen.blit(damage_stat_surf,damage_stat_rect)
    # Piercing Blit
    screen.blit(piercing_stat_image_surf,piercing_stat_image_rect)
    screen.blit(piercing_stat_surf,piercing_stat_rect)
    # Fireball Cooldown Blit
    screen.blit(fireball_cooldown_stat_image_surf,fireball_cooldown_stat_image_rect)
    screen.blit(fireball_cooldown_stat_surf,fireball_cooldown_stat_rect)
    # Fireball Cooldown Overlay Blit
    screen.blit(fireball_cooldown_surf,fireball_cooldown_rect)
    screen.blit(fireball_cooldown_overlay_surf,fireball_cooldown_overlay_rect)
    # Speed Stat Blit
    screen.blit(speed_stat_image_surf,speed_stat_image_rect)
    screen.blit(speed_stat_surf,speed_stat_rect)


def display_in_game_fps():
    edited_fps = get_edited_options_file_dict().get("fps")
    # FPS
    fps_surf = base_font.render(f"FPS: {edited_fps}", False, "#FCDC4D")
    fps_rect = fps_surf.get_rect(center = (0,0))
    fps_rect = fps_surf.get_rect(center = (fps_rect.width/2,window_height-fps_rect.height/2))
    screen.blit(fps_surf,fps_rect)


def player_and_obstacle_collision():
    global main_menu
    if obstacles_overlapping:=pygame.sprite.spritecollide(wizard.sprite,obstacle_group,False):
        wizard_shield = wizard.sprite.get_shield()
        temp_shield_health = wizard.sprite.get_current_shield_health()
        temp_health = wizard.sprite.get_wizard_current_health()
        temp_immunity_frames = wizard.sprite.get_wizard_immunity_frames()
        # Wizard color changes to damaged color
        temp_damaged_color = wizard.sprite.get_damaged_color()
        wizard.sprite.set_wizard_color(wizard.sprite.get_wizard_image(),temp_damaged_color)
        # Obstacles colliding with wizard
        for obstacle in obstacles_overlapping:
            if pygame.sprite.collide_mask(wizard.sprite,obstacle):
                if temp_immunity_frames <= 0:
                    temp_obstacle_damage = obstacle.get_damage()
                    # Wizard is hurt
                    wizard.sprite.set_wizard_hurt(True)
                    # Shield Buff Logic
                    if wizard_shield:
                        wizard.sprite.set_current_shield_cooldown(wizard.sprite.get_max_shield_cooldown())
                        new_shield_health = temp_shield_health - temp_obstacle_damage
                        if new_shield_health <= 0:
                            new_shield_health = 0
                            temp_obstacle_damage -= temp_shield_health
                        else:
                            temp_obstacle_damage = 0
                        wizard.sprite.set_current_shield_health(new_shield_health)
                    # Wizard takes damage
                    new_health = temp_health - temp_obstacle_damage
                    if new_health > 0:
                        wizard.sprite.set_wizard_current_health(new_health)
                        wizard.sprite.set_wizard_immunity_frames(wizard.sprite.get_wizard_max_immunity_frames())
                    # Wizard dies
                    else:
                        wizard_death_calls()


def obstacle_and_player_owned_projectile_collision():
    temp_additional_score = wizard.sprite.get_additional_score()
    for projectile in projectile_group:
        if pygame.sprite.spritecollide(projectile,obstacle_group,False):
            obstacles_overlapping = pygame.sprite.spritecollide(projectile,obstacle_group,False)
            for obstacle in obstacles_overlapping:
                if pygame.sprite.collide_mask(projectile,obstacle):
                    temp_obstacle_health = obstacle.get_current_health()
                    temp_obstacle_immunity_limit = obstacle.get_immunity_limit()
                    temp_obstacle_immunity_timer = obstacle.get_immunity_timer()
                    temp_projectile_damage = projectile.get_fireball_damage()
                    temp_projectile_piercing = projectile.get_fireball_piercing()
                    temp_obstacle_x_pos = int(obstacle.get_x_pos())
                    temp_obstacle_y_pos = int(obstacle.get_y_pos())
                    # Damage Color Set
                    obstacle.set_obstacle_color(obstacle.get_image(),obstacle.get_damaged_color())
                    if temp_obstacle_immunity_timer <= 0:
                        # Death
                        if (temp_obstacle_health - temp_projectile_damage) <= 0:
                            do_drop_spawns(obstacle)
                            temp_additional_score += obstacle.get_points()
                            # Health Bar and Outline Health Bar Cleanup
                            old_health_bar = health_bar_ownership_group[obstacle]
                            old_outline_health_bar = outline_health_bar_ownership_group[old_health_bar]
                            old_outline_health_bar.kill()
                            old_health_bar.kill()
                            # Tracking Kills
                            if obstacle.get_obstacle_type() == "skeleton":
                                name = "skeletons"
                            elif obstacle.get_obstacle_type() == "bird":
                                name = "skeleton_birds"
                            edited_stats_file_dict = get_edited_stats_file_dict()
                            edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
                            obstacle_killed_total = int(edited_stats_kills_file_dict.get(f"{name}_killed"))
                            obstacle_killed_total += 1
                            edited_stats_kills_file_dict.update({f"{name}_killed":obstacle_killed_total})
                            set_edited_stats_file_dict(edited_stats_file_dict)
                            dead_obstacle_group.add(obstacle)
                            pygame.mixer.Channel(OBSTACLE_DEATH_CHANNEL).play(obstacle_death_sound)
                            wizard.sprite.set_additional_score(temp_additional_score)
                        # Damaged
                        else:
                            obstacle.set_current_health(temp_obstacle_health - temp_projectile_damage)
                            if temp_projectile_piercing > 1:
                                obstacle.set_immunity_timer(temp_obstacle_immunity_limit)
                            # Knockback Calc
                            if projectile.get_knockback():
                                obstacle.set_knockback_active(True)
                                obstacle.set_knockback_direction_multiplier(projectile.get_x_direction_multiplier())
                                if temp_obstacle_x_pos > projectile.get_x_pos():
                                    obstacle.set_knockback_vector(obstacle.get_knockback_value() * 1.25)
                                else:
                                    obstacle.set_knockback_vector(obstacle.get_knockback_value())
                        wizard.sprite.set_fireball_hit(True)
                        temp_projectile_piercing -= 1
                        if temp_projectile_piercing <= 0:
                            projectile_group.remove(projectile)
                        else:
                            projectile.set_fireball_piercing(temp_projectile_piercing)
            pygame.sprite.spritecollide(projectile,dead_obstacle_group,True)


def do_drop_spawns(obstacle):
    temp_obstacle_x_pos = int(obstacle.get_x_pos())
    temp_obstacle_y_pos = int(obstacle.get_y_pos())
    # Pickup Spawn
    # Damage
    if randint(1,10) == 10: # 1/10
        pickup_group.add(Pickup("damage",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Fireball Cooldown
    if randint(1,10) == 10: # 1/10
        pickup_group.add(Pickup("fireball_cooldown",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Piercing
    if randint(1,25) == 25: # 1/25
        pickup_group.add(Pickup("piercing",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Speed
    if randint(1,15) == 15: # 1/15
        pickup_group.add(Pickup("speed",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Health
    if wizard.sprite.get_wizard_current_health() < wizard.sprite.get_wizard_max_health():
        if randint(1,10) == 10: # 1/10
            pickup_group.add(Pickup("health",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Temporary Placement for buffs, will eventually be in the world, not dropped by enemies
    # Double Jump
    if not wizard.sprite.get_double_jump() and randint(1,50) == 50: # 1/50
        buff_group.add(Buff("double_jump",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Shield
    elif not wizard.sprite.get_shield() and randint(1,50) == 50: # 1/50
        buff_group.add(Buff("shield",x_pos=temp_obstacle_x_pos,y_pos=temp_obstacle_y_pos))
    # Knockback
    elif not wizard.sprite.get_knockback() and randint(1,50) == 50: # 1/50
        buff_group.add(Buff("knockback",x_pos=temp_obstacle_x_pos,y_pos=temp_obstacle_y_pos))


def player_and_pickup_collision():
    if pygame.sprite.spritecollide(wizard.sprite,pickup_group,False):
        pickups_overlapping = pygame.sprite.spritecollide(wizard.sprite,pickup_group,False)
        for pickup in pickups_overlapping:
            # if pygame.sprite.collide_mask(wizard.sprite,pickup):
            temp_bonus = pickup.get_bonus()
            temp_damage = wizard.sprite.get_wizard_damage_percent()
            temp_piercing = wizard.sprite.get_wizard_piercing_increase()
            temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
            temp_speed = wizard.sprite.get_wizard_speed()
            temp_current_health = wizard.sprite.get_wizard_current_health()
            temp_max_health = wizard.sprite.get_wizard_max_health()
            if pickup.get_type() == "damage":
                wizard.sprite.set_wizard_damage_percent(temp_damage + temp_bonus)
            if pickup.get_type() == "piercing":
                wizard.sprite.set_wizard_piercing_increase(temp_piercing + temp_bonus)
            if pickup.get_type() == "fireball_cooldown" and temp_max_fireball_cooldown_time >= 6:
                wizard.sprite.set_max_fireball_cooldown_time(temp_max_fireball_cooldown_time - temp_bonus)
            if pickup.get_type() == "speed" and temp_speed < 8:
                wizard.sprite.set_wizard_speed(temp_speed + temp_bonus)
            if pickup.get_type() == "health" and temp_current_health < temp_max_health:
                if temp_current_health + temp_bonus <= temp_max_health:
                    wizard.sprite.set_wizard_current_health(temp_current_health + temp_bonus)
                else:
                    wizard.sprite.set_wizard_current_health(temp_max_health)
            pygame.sprite.spritecollide(wizard.sprite,pickup_group,True)


def player_and_buff_collision():
    if pygame.sprite.spritecollide(wizard.sprite,buff_group,False):
        buffs_overlapping = pygame.sprite.spritecollide(wizard.sprite,buff_group,False)
        for buff in buffs_overlapping:
            # if pygame.sprite.collide_mask(wizard.sprite,buff):
            wizard.sprite.add_buff_to_buff_list(buff.get_type())
            wizard.sprite.add_buff_image_to_buff_image_list(buff.get_default_image())
            if buff.get_type() == "double_jump":
                wizard.sprite.set_double_jump(True)
            if buff.get_type() == "shield":
                wizard.sprite.set_shield(True)
            if buff.get_type() == "knockback":
                wizard.sprite.set_knockback(True)
            if wizard.sprite.get_double_jump():
                for buff in buff_group:
                    if buff.get_type() == "double_jump":
                        buff.kill()
            if wizard.sprite.get_shield():
                for buff in buff_group:
                    if buff.get_type() == "shield":
                        buff.kill()
            if wizard.sprite.get_knockback():
                for buff in buff_group:
                    if buff.get_type() == "knockback":
                        buff.kill()
            pygame.sprite.spritecollide(wizard.sprite,buff_group,True)


def do_collisions():
    obstacle_and_player_owned_projectile_collision()
    player_and_buff_collision()
    player_and_pickup_collision()
    player_and_obstacle_collision()


def screenshot_screen(zoom=200,left=0,top=0,width=window_width,height=window_height):
    # zoom = 200 -> screen at 100%, zoom = 100 -> screen at 75%, zoom = 0 -> screen at 50%
    zoom_width = int(((zoom/4 + 50)/100) * width)
    zoom_height = int(((zoom/4 + 50)/100) * height)
    zoom_x_offset = (width-zoom_width)/2 # Focuses on the center x of the screen
    zoom_y_offset = (height-zoom_height) # Focuses on the bottom y of the screen
    sub_screen = screen.subsurface(left+zoom_x_offset,top+zoom_y_offset,zoom_width,zoom_height)
    screenshot = pygame.transform.scale(sub_screen,(window_size),screen)

    return screenshot


# Main Gameloop
while True:
    # Voids screen each frame
    # screen.fill((0,0,0))  # Messes with screenshotting bg, remove this but fix resizing to snap to perfect resolutions
    # Useful Function: pygame.mouse.set_visible(False) # Can help to make custom cursors
    events = pygame.event.get()
    for event in events: # Gets all the events
        # mouse_buttons_pressed = pygame.mouse.get_pressed(5) # 5 means 5 mouse buttons, only supports 3 or 5
        # keys_pressed = pygame.key.get_pressed()
        # Updates Control Vars
        if controls_update:
            jump_button,jump_button_is_mouse = get_control("jump_button")
            left_button,left_button_is_mouse = get_control("left_button")
            right_button,right_button_is_mouse = get_control("right_button")
            shoot_button,shoot_button_is_mouse = get_control("shoot_button")
            update_jump_button(jump_button)
            update_left_button(left_button)
            update_right_button(right_button)
            update_shoot_button(shoot_button)
            controls_update = False

        # Quitting the Game
        if event.type == pygame.QUIT:
            edited_controls_file_dict = get_edited_controls_file_dict()
            edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
            unbound_display_name = get_display_name(list(unbound_constants_dict.keys())[0])
            if unbound_display_name in edited_controls_display_names_dict:
                edited_controls_display_names_dict_index = list(edited_controls_display_names_dict.values()).index(unbound_display_name)
                edited_control_name = list(edited_controls_display_names_dict.keys())[edited_controls_display_names_dict_index]
                edited_controls_display_names_dict.update({edited_control_name:held_control_display_name})
                edited_controls_file_dict.update({"edited_controls_display_names_dict":edited_controls_display_names_dict})
            pygame.quit() # Opposite of pygame.init()
            exit() # Breaks out of the while True loop

        # Resizing the Window
        if event.type == pygame.VIDEORESIZE:
            # Update the surface
            screen = pygame.display.set_mode((
                max(min_window_width,min(event.w,max_window_width)),
                max(min_window_height,min(event.h,max_window_height)),
                ),pygame.RESIZABLE)
            # Call the menu event
            if game_active:
                on_resize(pause_menu)
            else:
                on_resize(main_menu)

        # Skipping Intro
        elif not intro_played and (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN):
            intro_played = True

        # Intro Played
        elif intro_played:
            if controls_update:
                jump_button,jump_button_is_mouse = get_control("jump_button")
                left_button,left_button_is_mouse = get_control("left_button")
                right_button,right_button_is_mouse = get_control("right_button")
                shoot_button,shoot_button_is_mouse = get_control("shoot_button")
                update_jump_button(jump_button)
                update_left_button(left_button)
                update_right_button(right_button)
                update_shoot_button(shoot_button)
                controls_update = False
            # Game (Game Active)
            if game_active:
                # Controls
                jump_button_press = (not jump_button_is_mouse and hasattr(event, "key") and event.key == jump_button) or (jump_button_is_mouse and hasattr(event, "button") and event.button == jump_button)
                left_button_press = (not left_button_is_mouse and hasattr(event, "key") and event.key == left_button) or (left_button_is_mouse and hasattr(event, "button") and event.button == left_button)
                right_button_press = (not right_button_is_mouse and hasattr(event, "key") and event.key == right_button) or (right_button_is_mouse and hasattr(event, "button") and event.button == right_button)
                shoot_button_press = (not shoot_button_is_mouse and hasattr(event, "key") and event.key == shoot_button) or (shoot_button_is_mouse and hasattr(event, "button") and event.button == shoot_button)
                # If Wizard isn't dead
                if not wizard.sprite.get_wizard_dead():
                    edited_controls_are_mouse_buttons = get_edited_controls_file_dict().get("edited_controls_are_mouse_buttons")
                    # Spacebar Release Event Detection
                    if wizard.sprite.get_double_jump() and not wizard.sprite.get_double_jump_used() and ((not jump_button_is_mouse and event.type == pygame.KEYUP) or (jump_button_is_mouse and event.type == pygame.MOUSEBUTTONUP)):
                        if jump_button_press:
                            wizard.sprite.set_first_jump_used(True)
                    # Obstacle Timer Event Detection
                    if event.type == obstacle_timer:
                        current_time = int((pygame.time.get_ticks() - start_time) / 1000)
                        new_obstacle = Obstacle(choice(["bird","skeleton","skeleton","skeleton"]),current_time)
                        obstacle_group.add(new_obstacle)
                        # Health Bar
                        new_health_bar = HealthBar(new_obstacle, new_obstacle.get_current_health(), new_obstacle.get_max_health())
                        health_bar_group.add(new_health_bar)
                        health_bar_ownership_group[new_obstacle] = new_health_bar
                        # Outline Health Bar
                        new_outline_health_bar = OutlineHealthBar(new_health_bar, new_obstacle.get_x_pos(), new_obstacle.get_y_pos())
                        outline_health_bar_group.add(new_outline_health_bar)
                        outline_health_bar_ownership_group[new_health_bar] = new_outline_health_bar
                    # Player Shooting
                    if shoot_button_press and int((pygame.time.get_ticks() - start_time) / 1000) > 2/60:
                        if wizard.sprite.get_current_fireball_cooldown() == 0: # or wizard.sprite.get_fireball_hit(): # causes fireball_cooldown refresh on hit
                            increase_fireballs_shot()
                            wizard.sprite.play_fireball_sound()
                            wizard.sprite.set_fireball_shot(True)
                            temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
                            wizard.sprite.set_current_fireball_cooldown(temp_max_fireball_cooldown_time)
                            wizard.sprite.set_fireball_hit(False)
                            projectile_group.add(Projectile("fireball", wizard))
                    # Pausing the Game
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pause_time_1 = pygame.time.get_ticks()
                        pause_menu.enable()
                        on_resize(pause_menu)

                        screenshot = screenshot_screen()
                        screenshot.fill((150,150,150),special_flags=pygame.BLEND_MULT)

                        pygame.image.save(screenshot,"screenshot.jpg")
                        pause_menu_background_image = pygame_menu.BaseImage(
                            image_path="screenshot.jpg",
                        )
                        pause_menu = update_pause_menu(new_bg)

                        pause_menu.mainloop(screen,clear_surface=True)
                        pause_time_2 = pygame.time.get_ticks()
                        pause_time = pause_time_2 - pause_time_1

            # Main Menu (Game Inactive)
            if not game_active:
                # Menu Interactivity
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                mouse_pos = (mouse_x,mouse_y)
                clicking_with_left_mouse = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

                #     # Reset Button
                #     if mouse_on_controls_reset_button:
                #         if clicking_with_left_mouse:
                #             reset_controls()
                #             controls_update = True
                #     # Back Button
                #     elif mouse_on_controls_back_button:
                #         if clicking_with_left_mouse:
                #             menu_section = SETTINGS_MENU

                # Main Menu Display
                # Sprite Resets
                wizard.sprite.reset()
                harold.sprite.reset()
                additional_score = 0
                # Event Clear
                pygame.event.clear()
                # Timer Resets
                death_timer = 0
                bg_music_timer = 0

                # Starts Main Menu
                main_menu.enable()
                if get_score() != 0:
                    main_menu_label = main_menu.get_widget("main_menu_label")
                    main_menu_label.set_title(f"Score: {get_score()}")
                    main_menu.force_surface_update()
                    pygame.display.update(main_menu_label.get_rect())
                    # This stuff doesn't work unless can actually make them into submenus - figure it out
                    # check_for_menu_updates(main_menu,pause_menu)
                    main_menu = update_main_menu()
                main_menu.mainloop(screen,clear_surface=True)
                # When exits main menu through only way other than quitting, runs this code which starts the game
                controls_update = True
                game_active = True
                wizard_alive = True
                set_score(0)
                pause_time = 0
                start_time = pygame.time.get_ticks()
                pre_stat_update_edited_stats_file_dict.update(get_edited_stats_file_dict())
                #     # Reset Button
                #     if not mouse_on_controls_reset_button: screen.blit(controls_reset_button_surf,controls_reset_button_rect)
                #     else: screen.blit(controls_reset_button_surf_big,controls_reset_button_rect_big)
                #     # Back Button
                #     if not mouse_on_controls_back_button: screen.blit(controls_back_button_surf,controls_back_button_rect)
                #     else: screen.blit(controls_back_button_surf_big,controls_back_button_rect_big)


    # Opening Cinematic (Intro)
    if not intro_played:
        screen.blit(bg_surf,(0,window_height-bg_surf.get_height()))
        screen.blit(wizard_intro_surf,wizard_intro_rect)
        main_menu_wizard_start_x_pos = center_screen_width
        main_menu_wizard_start_y_pos = main_menu_wizard_surf.get_rect().height + title_font_size * (7/2)
        if harold_turn_animation_complete and not harold_flipped:
            harold_intro_surf = pygame.transform.flip(harold_intro_surf,True,False)
            harold_flipped = True
        screen.blit(harold_intro_surf,harold_intro_rect)
        if not wizard_walk_in_animation_complete:
            if wizard_intro_rect.right < window_width / 2 - wizard_intro_width_by_scale/2:
                wizard_intro_rect.centerx += (wizard.sprite.get_wizard_speed() / global_scalar)
            else:
                wizard_walk_in_animation_complete = True
        elif not harold_jump_on_hat_animation_complete:
            if harold_intro_rect.centerx > wizard_intro_rect.centerx:
                harold_intro_rect.centerx -= ((harold.sprite.get_harold_speed() * 2) / global_scalar)
            else:
                x_lineup = True
            intro_jump_speed += (intro_gravity_acceleration / global_scalar)
            harold_intro_rect.centery += intro_jump_speed
            if not fall:
                if harold_intro_rect.bottom >= wizard_intro_rect.top:
                    fall = True
            elif harold_intro_rect.bottom >= wizard_intro_rect.top + main_menu_wizard_hat_size:
                harold_intro_rect.bottom = wizard_intro_rect.top + main_menu_wizard_hat_size
                harold_jump_on_hat_animation_complete = x_lineup
        elif not harold_turn_animation_complete:
            harold_turn_animation_complete = True
        elif not wizard_and_harold_center_animation_complete:
            if wizard_intro_rect.centerx < main_menu_wizard_start_x_pos:
                wizard_intro_rect.centerx += (wizard.sprite.get_wizard_speed() / global_scalar)
                harold_intro_rect.centerx += (harold.sprite.get_harold_speed() / global_scalar)
            else:
                wizard_and_harold_center_animation_complete = True
        elif not wizard_and_harold_center_with_title_animation_complete:
            if wizard_intro_rect.bottom > main_menu_wizard_start_y_pos:
                wizard_intro_rect.centery -= (wizard.sprite.get_wizard_speed() / global_scalar)
                harold_intro_rect.centery -= (harold.sprite.get_harold_speed() / global_scalar)
            else:
                intro_played = True

    # Intro Played - Check for Resizing
    elif intro_played and not game_active and main_menu.is_enabled():
        main_menu.update(events)

    # Active Game - Music, Death Checker, Moving Sprites, Collisions
    if game_active:
        if bg_music_timer == 0:
            pygame.mixer.Channel(BG_MUSIC_CHANNEL).play(bg_music)
        elif bg_music_timer >= (25 * 60):
            bg_music_timer = -1

        screen.blit(bg_surf,(0,-bg_surf.get_height() + window_height))

        if wizard_alive:
            bg_music_timer += 1

            for sprite in moving_sprites: # Holds all things to be drawn
                sprite.draw(screen)
                sprite.update()

            do_collisions()

            wizard_alive = not wizard.sprite.get_wizard_dead()

        else: # Work on death animation
            wizard.sprite.set_wizard_dead(True)

            wizard.draw(screen) # Draws sprites
            harold.draw(screen)

            wizard.update() # Updates sprites
            harold.update()
            death_timer += 1
            if death_timer > 180:
                game_active = False

        # May need for resizing - before fixing black border issue it wasn't needed
        # if pause_menu.is_enabled():
        #     pause_menu.update(events)
            # pause_menu.draw(screen)
            # pygame.display.flip()

        # Take screenshot every frame and show it scaled to zoom
        edited_options_file_dict = get_edited_options_file_dict()
        new_zoom = edited_options_file_dict.get("zoom")
        screenshot = screenshot_screen(new_zoom)
        screenshot.blit(screen,(0,0,window_width,window_height))

        # Overlay
        if wizard_alive:
            # Stat Image Postions
            set_score(display_score())
            if get_edited_options_file_dict()["display_in_game_health"]:
                display_in_game_health() # Displays and updates in game health
            if get_edited_options_file_dict()["display_in_game_buffs"]:
                display_in_game_buffs() # Displays and updates in game buffs
            if get_edited_options_file_dict()["display_in_game_stats"]:
                display_in_game_stats() # Displays and updates in game stats
            if get_edited_options_file_dict()["display_controls"]:
                display_controls() # Displays controls on bottom right of screen, change from board to normal display
            if get_edited_options_file_dict()["display_in_game_fps"]:
                display_in_game_fps()

    # Global Clock and Display Update
    pygame.display.flip()
    # pygame.display.update()
    clock.tick(fps)
