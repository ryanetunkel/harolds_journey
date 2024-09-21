"""Main Gameloop"""
from sys import exit
from random import randint, choice

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

moving_sprites = [
    wizard,
    harold,
    obstacle_group,
    projectile_group,
    pickup_group,
    buff_group,
    outline_health_bar_group,
    health_bar_group,
]

objects_to_be_removed = [
    obstacle_group,
    dead_obstacle_group,
    projectile_group,
    pickup_group,
    buff_group,
]

# Functions
def display_score():
    temp_additional_score = wizard.sprite.get_additional_score()
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_title_surf = test_font.render("SCORE", False, "#FCDC4D")
    score_title_rect = score_title_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT*1/16))
    score_surf = test_font.render(str(current_time + temp_additional_score), False, "#FCDC4D")
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/8))
    screen.blit(score_title_surf,score_title_rect)
    screen.blit(score_surf,score_rect)
    return current_time + temp_additional_score


def display_controls():
    edited_controls_file_dict = get_edited_controls_file_dict()
    edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
    displayed_control_y_pos_offset = WINDOW_HEIGHT * 1/44
    displayed_control_index = 0
    displayed_control_scalar = 0.3
    edited_controls_display_names_dict_size = len(list(edited_controls_display_names_dict.keys()))
    control_board_start_y_pos = 0
    control_board_end_y_pos = 0
    biggest_width = 0
    biggest_rect = None
    displayed_control_surf_dict = {}
    displayed_control_rect_dict = {}
    for displayed_control_name in edited_controls_display_names_dict.keys():
        displayed_control_start_x_pos = WINDOW_WIDTH * 7/8
        displayed_control_start_y_pos = (25/32 * WINDOW_HEIGHT) + displayed_control_y_pos_offset * displayed_control_index
        displayed_control_start_pos = (displayed_control_start_x_pos,displayed_control_start_y_pos)
        displayed_control_name_underscore_removed = displayed_control_name.replace("_", " ")
        displayed_control_name_button_removed = displayed_control_name_underscore_removed.replace(" button", "")
        displayed_control_name_capitalized = displayed_control_name_button_removed.title()
        displayed_control_surf = test_font.render(f"{displayed_control_name_capitalized}: {edited_controls_display_names_dict[displayed_control_name]}",False,"#FCDC4D")
        displayed_control_scale = WINDOW_SCALAR * displayed_control_scalar
        displayed_control_surf = pygame.transform.scale_by(displayed_control_surf,displayed_control_scale)
        displayed_control_surf_dict.update({displayed_control_name:displayed_control_surf})
        displayed_control_rect = displayed_control_surf.get_rect(center = (displayed_control_start_pos))
        displayed_control_rect_dict.update({displayed_control_name:displayed_control_rect})
        if displayed_control_rect.width > biggest_width:
            biggest_width = displayed_control_rect.width
            biggest_rect = displayed_control_rect
        if displayed_control_index == 0:
            control_board_start_y_pos = displayed_control_rect.top
        if displayed_control_index == edited_controls_display_names_dict_size - 1:
            control_board_end_y_pos = displayed_control_rect.bottom
        displayed_control_index += 1

    control_board_padding = WINDOW_SCALAR * 2
    control_board_width = biggest_width + control_board_padding * 4
    control_board_height = (control_board_end_y_pos - control_board_start_y_pos) + control_board_padding * 2
    control_board_start_x_pos = biggest_rect.left - (control_board_padding * 2)
    control_board_start_y_pos = control_board_start_y_pos - control_board_padding
    control_board_rect = pygame.Rect(control_board_start_x_pos, control_board_start_y_pos, control_board_width, control_board_height)
    control_board_color = "#442211"
    control_board_stand_height = WINDOW_SCALAR * 4
    control_board_stand_width = control_board_width/16
    control_board_stand_start_x_pos = (control_board_start_x_pos + (control_board_width/2)) - (control_board_stand_width/2)
    control_board_stand_start_y_pos = control_board_rect.bottom
    control_board_stand_rect = pygame.Rect(control_board_stand_start_x_pos, control_board_stand_start_y_pos, control_board_stand_width, control_board_stand_height)
    pygame.draw.rect(screen,control_board_color,control_board_rect)
    pygame.draw.rect(screen,control_board_color,control_board_stand_rect)
    # Drawing Rect

    for displayed_control_name in edited_controls_display_names_dict.keys():
        displayed_control_surf = displayed_control_surf_dict[displayed_control_name]
        displayed_control_rect = displayed_control_rect_dict[displayed_control_name]
        screen.blit(displayed_control_surf,displayed_control_rect)


def display_in_game_health():
    # Health
    health_stat_image_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_health/heart.png").convert_alpha()
    health_stat_image_surf = pygame.transform.scale_by(health_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    health_stat_image_rect = health_stat_image_surf.get_rect(center = (WINDOW_WIDTH*1/16,WINDOW_HEIGHT*3/32))

    health_stat_surf = test_font.render(str(wizard.sprite.get_wizard_current_health()), False, "#FCDC4D")
    health_stat_surf = pygame.transform.scale_by(health_stat_surf, 1.3)
    health_stat_rect = health_stat_surf.get_rect(center = (WINDOW_WIDTH*7/64,WINDOW_HEIGHT*13/128))

    # Shield Health
    shield_health_stat_x_pos_offset = WINDOW_WIDTH * 1/32
    shield_health_stat_x_pos_0 = WINDOW_WIDTH * 1/16
    shield_health_stat_x_pos_1 = shield_health_stat_x_pos_0 + shield_health_stat_x_pos_offset
    shield_health_stat_x_pos_2 = shield_health_stat_x_pos_1 + shield_health_stat_x_pos_offset
    shield_health_stat_y_pos = WINDOW_HEIGHT * 7/32
    shield_health_stat_image_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_health/shield_stat_display.png").convert_alpha()
    shield_health_stat_image_surf = pygame.transform.scale_by(shield_health_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    shield_health_stat_image_rect_0 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_0,shield_health_stat_y_pos))
    shield_health_stat_image_rect_1 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_1,shield_health_stat_y_pos))
    shield_health_stat_image_rect_2 = shield_health_stat_image_surf.get_rect(center = (shield_health_stat_x_pos_2,shield_health_stat_y_pos))

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
    order_offset = WINDOW_WIDTH*3/64
    default_image_x_pos = WINDOW_WIDTH*15/16
    default_image_y_pos = WINDOW_HEIGHT*3/32
    # Double Jump
    if wizard.sprite.get_double_jump():
        double_jump_idx = wizard.sprite.get_buff_idx_in_buff_list("double_jump")
        double_jump_x_offset = order_offset * double_jump_idx
        double_jump_buff_image_x_pos = default_image_x_pos - double_jump_x_offset
        double_jump_buff_image_y_pos = default_image_y_pos
        double_jump_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(double_jump_idx)
        double_jump_buff_image_surf = pygame.transform.scale_by(double_jump_buff_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
        double_jump_buff_image_rect = double_jump_buff_image_surf.get_rect(center = (double_jump_buff_image_x_pos,double_jump_buff_image_y_pos))
    # Shield
    if wizard.sprite.get_shield():
        shield_idx = wizard.sprite.get_buff_idx_in_buff_list("shield")
        shield_x_offset = order_offset * shield_idx
        shield_buff_image_x_pos = default_image_x_pos - shield_x_offset
        shield_buff_image_y_pos = default_image_y_pos
        shield_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(shield_idx)
        shield_buff_image_surf = pygame.transform.scale_by(shield_buff_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
        shield_buff_image_rect = shield_buff_image_surf.get_rect(center = (shield_buff_image_x_pos,shield_buff_image_y_pos))
    # Knockback
    if wizard.sprite.get_knockback():
        knockback_idx = wizard.sprite.get_buff_idx_in_buff_list("knockback")
        knockback_x_offset = order_offset * knockback_idx
        knockback_buff_image_x_pos = default_image_x_pos - knockback_x_offset
        knockback_buff_image_y_pos = default_image_y_pos
        knockback_buff_image_surf = wizard.sprite.get_buff_image_in_buff_image_list_by_idx(knockback_idx)
        knockback_buff_image_surf = pygame.transform.scale_by(knockback_buff_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
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
    stat_image_surf_x_pos = WINDOW_WIDTH/4 #29/128 dif
    stat_image_surf_y_pos_offset = WINDOW_HEIGHT*3/32
    # First
    damage_stat_image_y_pos = WINDOW_HEIGHT*5/64
    # Second
    piercing_stat_image_y_pos = damage_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Third
    fireball_cooldown_stat_image_y_pos = piercing_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Fourth
    speed_stat_image_y_pos = fireball_cooldown_stat_image_y_pos + stat_image_surf_y_pos_offset
    # Stat text surfs
    stat_surf_x_pos = WINDOW_WIDTH*43/128
    stat_surf_y_pos_offset = stat_image_surf_y_pos_offset
    # First
    damage_stat_x_pos = stat_surf_x_pos
    damage_stat_y_pos = damage_stat_image_y_pos + WINDOW_WIDTH/256
    # Second
    piercing_stat_x_pos = stat_surf_x_pos + WINDOW_WIDTH/128
    piercing_stat_y_pos = damage_stat_y_pos + stat_surf_y_pos_offset
    # Third
    fireball_cooldown_stat_x_pos = stat_surf_x_pos + WINDOW_WIDTH*2/128
    fireball_cooldown_stat_y_pos = piercing_stat_y_pos + stat_surf_y_pos_offset
    # Fourth
    speed_stat_x_pos = stat_surf_x_pos # + WINDOW_WIDTH*2/128
    speed_stat_y_pos = fireball_cooldown_stat_y_pos + stat_surf_y_pos_offset
    # Damage
    damage_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/damage/damage_pickup.png").convert_alpha()
    damage_stat_image_surf = pygame.transform.scale_by(damage_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    damage_stat_image_rect = damage_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,damage_stat_image_y_pos))

    damage_stat_surf = test_font.render("Damage: " + str(wizard.sprite.get_wizard_damage_total()), False, "#FCDC4D")
    damage_stat_surf = pygame.transform.scale_by(damage_stat_surf, 0.9)
    damage_stat_rect = damage_stat_surf.get_rect(center = (damage_stat_x_pos,damage_stat_y_pos))

    # Piercing
    piercing_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/piercing/piercing_pickup.png").convert_alpha()
    piercing_stat_image_surf = pygame.transform.scale_by(piercing_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    piercing_stat_image_rect = piercing_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,piercing_stat_image_y_pos))

    piercing_stat_surf = test_font.render("Piercing: " + str(wizard.sprite.get_wizard_piercing_total() - 1), False, "#FCDC4D")
    piercing_stat_surf = pygame.transform.scale_by(piercing_stat_surf, 0.9)
    piercing_stat_rect = piercing_stat_surf.get_rect(center = (piercing_stat_x_pos,piercing_stat_y_pos))

    # Fireball Cooldown Stat
    fireball_cooldown_stat_image_surf = pygame.image.load("harolds_journey/graphics/pickups/fireball_cooldown/fireball_cooldown_pickup.png").convert_alpha()
    fireball_cooldown_stat_image_surf = pygame.transform.scale_by(fireball_cooldown_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    fireball_cooldown_stat_image_rect = fireball_cooldown_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,fireball_cooldown_stat_image_y_pos))

    fireball_cooldown_stat_surf = test_font.render(f"Cooldown: {round(wizard.sprite.get_max_fireball_cooldown_time()/60, 2)}s", False, "#FCDC4D")
    fireball_cooldown_stat_surf = pygame.transform.scale_by(fireball_cooldown_stat_surf, 0.9)
    fireball_cooldown_stat_rect = fireball_cooldown_stat_surf.get_rect(center = (fireball_cooldown_stat_x_pos,fireball_cooldown_stat_y_pos))

    # Fireball Cooldown Icon
    fireball_cooldown_x_pos = WINDOW_WIDTH * 1/16 # Right of health: 11/64 # Below Health: 1/16
    fireball_cooldown_y_pos_num = 7/32 if not wizard.sprite.get_shield() else 11/32
    fireball_cooldown_y_pos = WINDOW_HEIGHT * fireball_cooldown_y_pos_num # Right of health: 25/256 # Below Health: 7/32
    fireball_cooldown_surf = pygame.image.load("harolds_journey/graphics/fireball/fireball_movement_animation/fireball_movement_00.png").convert_alpha()
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
    speed_stat_image_surf = pygame.transform.scale_by(speed_stat_image_surf,4 * (WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
    speed_stat_image_rect = speed_stat_image_surf.get_rect(center = (stat_image_surf_x_pos,speed_stat_image_y_pos))

    speed_stat_surf = test_font.render("Speed: " + str(round((wizard.sprite.get_wizard_speed()/WIZARD_WIDTH)*60, 2)), False, "#FCDC4D")
    speed_stat_surf = pygame.transform.scale_by(speed_stat_surf, 0.9)
    speed_stat_rect = speed_stat_surf.get_rect(center = (speed_stat_x_pos,speed_stat_y_pos))

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


def player_and_obstacle_collision():
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
                        # Updating Stats
                        wizard_jumps = wizard.sprite.get_jumps_made()
                        distance_traveled = wizard.sprite.get_distance_traveled()
                        current_wizard_speed = wizard.sprite.get_wizard_speed()
                        current_wizard_damage = wizard.sprite.get_wizard_damage_total()
                        current_wizard_piercing = wizard.sprite.get_wizard_piercing_total()
                        current_wizard_fireball_cooldown = wizard.sprite.get_max_fireball_cooldown_time()
                        current_wizard_double_jump_buff = wizard.sprite.get_double_jump()
                        current_wizard_knockback_buff = wizard.sprite.get_knockback()
                        current_wizard_shield_buff = wizard.sprite.get_shield()
                        edited_stats_file_dict = get_edited_stats_file_dict()
                        edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                        edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
                        edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
                        time_played_total = edited_stats_interactivity_file_dict.get("time_played")
                        jumps_total = edited_stats_interactivity_file_dict.get("jumps")
                        distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
                        highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
                        highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
                        highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
                        lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
                        double_jump_buff_found = edited_stats_buffs_file_dict.get("double_jump_buff")
                        knockback_buff_found = edited_stats_buffs_file_dict.get("knockback_buff")
                        shield_buff_found = edited_stats_buffs_file_dict.get("shield_buff")
                        updated_speed = highest_speed if highest_speed > current_wizard_speed else current_wizard_speed
                        updated_damage = highest_damage if highest_damage > current_wizard_damage else current_wizard_damage
                        updated_piercing = highest_piercing if highest_piercing > current_wizard_piercing else current_wizard_piercing
                        updated_cooldown = lowest_cooldown if lowest_cooldown < current_wizard_fireball_cooldown else current_wizard_fireball_cooldown
                        current_time = int(pygame.time.get_ticks() / 1000) - start_time
                        new_time_played_total = time_played_total + current_time
                        edited_stats_interactivity_file_dict.update({"time_played":new_time_played_total})
                        edited_stats_interactivity_file_dict.update({"jumps":jumps_total + wizard_jumps })
                        edited_stats_interactivity_file_dict.update({"distance_traveled":distance_traveled_total + distance_traveled })
                        edited_stats_in_game_stat_records_file_dict.update({"highest_speed":updated_speed})
                        edited_stats_in_game_stat_records_file_dict.update({"highest_damage":updated_damage})
                        edited_stats_in_game_stat_records_file_dict.update({"highest_piercing":updated_piercing})
                        edited_stats_in_game_stat_records_file_dict.update({"lowest_cooldown":updated_cooldown})
                        if current_wizard_double_jump_buff and not double_jump_buff_found:
                            edited_stats_buffs_file_dict.update({"double_jump_buff":current_wizard_double_jump_buff})
                        if current_wizard_knockback_buff and not knockback_buff_found:
                            edited_stats_buffs_file_dict.update({"knockback_buff":current_wizard_knockback_buff})
                        if current_wizard_shield_buff and not shield_buff_found:
                            edited_stats_buffs_file_dict.update({"shield_buff":current_wizard_shield_buff})
                        set_edited_stats_file_dict(edited_stats_file_dict)
                        # Other Death Stuff
                        wizard.sprite.set_wizard_current_health(0)
                        temp_wizard_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
                        wizard.sprite.set_current_fireball_cooldown(temp_wizard_max_fireball_cooldown_time)
                        for objects in objects_to_be_removed:
                            for object in objects:
                                object.kill()
                            objects.empty()
                        outline_health_bar_ownership_group.clear()
                        health_bar_ownership_group.clear()
                        for outline_health_bar in outline_health_bar_group:
                            outline_health_bar.kill()
                        for health_bar in health_bar_group:
                            health_bar.kill()
                        outline_health_bar_group.empty()
                        health_bar_group.empty()
                        wizard.sprite.set_wizard_dead(True)


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
    if not wizard.sprite.get_double_jump() and randint(1,2) == 2: # 1/50
        buff_group.add(Buff("double_jump",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Shield
    elif not wizard.sprite.get_shield() and randint(1,2) == 2: # 1/50
        buff_group.add(Buff("shield",x_pos=temp_obstacle_x_pos,y_pos=temp_obstacle_y_pos))
    # Knockback
    elif not wizard.sprite.get_knockback() and randint(1,2) == 2: # 1/50
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


while True:
    # Useful Function: pygame.mouse.set_visible(False) # Can help to make custom cursors
    for event in pygame.event.get(): # Gets all the events
        # mouse_buttons_pressed = pygame.mouse.get_pressed(5) # 5 means 5 mouse buttons, only supports 3 or 5
        # keys_pressed = pygame.key.get_pressed()
        if controls_update:
            jump_button,jump_button_is_mouse = get_control("jump_button")
            left_button,left_button_is_mouse = get_control("left_button")
            right_button,right_button_is_mouse = get_control("right_button")
            shoot_button,shoot_button_is_mouse = get_control("shoot_button")
            controls_update = False

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
        # Skips Intro
        elif not intro_played and event.type == pygame.KEYUP:
            intro_played = True
        # Intro Played
        elif intro_played:
            # Jumping, Obstacle Timer, and Player Shooting
            if game_active:
                jump_button_press = (not jump_button_is_mouse and hasattr(event, "key") and event.key == jump_button) or (jump_button_is_mouse and hasattr(event, "button") and event.button == jump_button)
                left_button_press = (not left_button_is_mouse and hasattr(event, "key") and event.key == left_button) or (left_button_is_mouse and hasattr(event, "button") and event.button == left_button)
                right_button_press = (not right_button_is_mouse and hasattr(event, "key") and event.key == right_button) or (right_button_is_mouse and hasattr(event, "button") and event.button == right_button)
                shoot_button_press = (not shoot_button_is_mouse and hasattr(event, "key") and event.key == shoot_button) or (shoot_button_is_mouse and hasattr(event, "button") and event.button == shoot_button)
                if not wizard.sprite.get_wizard_dead():
                    edited_controls_are_mouse_buttons = get_edited_controls_file_dict().get("edited_controls_are_mouse_buttons")
                    # Spacebar Release Event Detection
                    if wizard.sprite.get_double_jump() and not wizard.sprite.get_double_jump_used() and ((not jump_button_is_mouse and event.type == pygame.KEYUP) or (jump_button_is_mouse and event.type == pygame.MOUSEBUTTONUP)):
                        if jump_button_press:
                            wizard.sprite.set_first_jump_used(True)
                    # Obstacle Timer Event Detection
                    if event.type == obstacle_timer:
                        new_obstacle = Obstacle(choice(["bird","skeleton","skeleton","skeleton"]),int(pygame.time.get_ticks() / 1000) - start_time)
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
                    if shoot_button_press and int(pygame.time.get_ticks() / 1000) - start_time > 2/60:
                        if wizard.sprite.get_current_fireball_cooldown() == 0: # or wizard.sprite.get_fireball_hit(): # causes fireball_cooldown refresh on hit
                            fireballs_shot += 1
                            wizard.sprite.play_fireball_sound()
                            wizard.sprite.set_fireball_shot(True)
                            temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
                            wizard.sprite.set_current_fireball_cooldown(temp_max_fireball_cooldown_time)
                            wizard.sprite.set_fireball_hit(False)
                            projectile_group.add(Projectile("fireball", wizard))
            # Main Menu (Game Inactive)
            else:
                # Menu Interactivity
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                mouse_pos = (mouse_x,mouse_y)
                clicking_with_left_mouse = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                # Main Menu
                if menu_section == MAIN_MENU:
                    mouse_on_main_menu_start_button = main_menu_start_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_main_menu_statistics_button = main_menu_statistics_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_main_menu_settings_button = main_menu_settings_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_main_menu_exit_button = main_menu_exit_button_rect_big.collidepoint(mouse_pos)
                    # Start Button
                    if mouse_on_main_menu_start_button:
                        if clicking_with_left_mouse:
                            controls_update = True
                            game_active = True
                            wizard_alive = True
                            start_time = int(pygame.time.get_ticks() / 1000)
                            additional_score = 0
                            pre_stat_update_edited_stats_file_dict.update(get_edited_stats_file_dict())
                    # Statistics Button
                    elif mouse_on_main_menu_statistics_button:
                        if clicking_with_left_mouse:
                            menu_section = STATISTICS_MENU
                    # Settings Button
                    elif mouse_on_main_menu_settings_button:
                        if clicking_with_left_mouse:
                            menu_section = SETTINGS_MENU
                    # Exit Button
                    elif mouse_on_main_menu_exit_button:
                        if clicking_with_left_mouse:
                            pygame.quit()
                            exit()
                # Statistics Menu
                elif menu_section == STATISTICS_MENU:
                    # Left Side
                    # Kills
                    # Skeletons Killed Tracker
                    mouse_on_statistics_skeletons_killed_tracker = statistics_skeletons_killed_tracker_rect_big.collidepoint(mouse_pos)
                    # Skeleton Birds Killed Tracker
                    mouse_on_statistics_skeleton_birds_killed_tracker = statistics_skeleton_birds_killed_tracker_rect_big.collidepoint(mouse_pos)
                    # Interactivity
                    # Time Played Tracker
                    mouse_on_statistics_time_played_tracker = statistics_time_played_tracker_rect_big.collidepoint(mouse_pos)
                    # High Score Tracker
                    mouse_on_statistics_high_score_tracker = statistics_high_score_tracker_rect_big.collidepoint(mouse_pos)
                    # Fireballs Shot Tracker
                    mouse_on_statistics_fireballs_shot_tracker = statistics_fireballs_shot_tracker_rect_big.collidepoint(mouse_pos)
                    # Jumps Tracker
                    mouse_on_statistics_jumps_tracker = statistics_jumps_tracker_rect_big.collidepoint(mouse_pos)
                    # Distance Traveled Tracker
                    mouse_on_statistics_distance_traveled_tracker = statistics_distance_traveled_tracker_rect_big.collidepoint(mouse_pos)
                    # Right Side
                    # In-Game Stat Records
                    # Highest Speed Tracker
                    mouse_on_statistics_highest_speed_tracker = statistics_highest_speed_tracker_rect_big.collidepoint(mouse_pos)
                    # Highest Damage Tracker
                    mouse_on_statistics_highest_damage_tracker = statistics_highest_damage_tracker_rect_big.collidepoint(mouse_pos)
                    # Highest Piercing Tracker
                    mouse_on_statistics_highest_piercing_tracker = statistics_highest_piercing_tracker_rect_big.collidepoint(mouse_pos)
                    # Lowest Cooldown Tracker
                    mouse_on_statistics_lowest_cooldown_tracker = statistics_lowest_cooldown_tracker_rect_big.collidepoint(mouse_pos)
                    # Buffs
                    # Double Jump Buff Tracker
                    mouse_on_statistics_double_jump_buff_tracker = statistics_double_jump_buff_tracker_rect_big.collidepoint(mouse_pos)
                    # Knockback Buff Tracker
                    mouse_on_statistics_knockback_buff_tracker = statistics_knockback_buff_tracker_rect_big.collidepoint(mouse_pos)
                    # Shield Buff Tracker
                    mouse_on_statistics_shield_buff_tracker = statistics_shield_buff_tracker_rect_big.collidepoint(mouse_pos)
                    # Bottom
                    # Back Button
                    mouse_on_statistics_back_button = statistics_back_button_rect_big.collidepoint(mouse_pos)
                    if mouse_on_statistics_back_button:
                        if clicking_with_left_mouse:
                            menu_section = MAIN_MENU
                # Settings Menu
                elif menu_section == SETTINGS_MENU:
                    mouse_on_settings_sounds_button = settings_sounds_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_settings_controls_button = settings_controls_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_settings_display_button = settings_display_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_settings_back_button = settings_back_button_rect_big.collidepoint(mouse_pos)
                    # Sounds Button
                    if mouse_on_settings_sounds_button:
                        if clicking_with_left_mouse:
                            menu_section = SOUNDS_MENU
                    # Controls Button
                    elif mouse_on_settings_controls_button:
                        if clicking_with_left_mouse:
                            menu_section = CONTROLS_MENU
                    # Display Button
                    elif mouse_on_settings_display_button:
                        if clicking_with_left_mouse:
                            menu_section = DISPLAY_MENU
                    # Back Button
                    elif mouse_on_settings_back_button:
                        if clicking_with_left_mouse:
                            menu_section = MAIN_MENU
                # Sounds Menu
                elif menu_section == SOUNDS_MENU:
                    mouse_on_sounds_back_button = sounds_back_button_rect_big.collidepoint(mouse_pos)
                    # Back Button
                    if mouse_on_sounds_back_button:
                        if clicking_with_left_mouse:
                            menu_section = SETTINGS_MENU
                # Controls Menu
                elif menu_section == CONTROLS_MENU:
                    mouse_released = event.type == pygame.MOUSEBUTTONUP
                    # Controls Buttons
                    for control_name, mouse_on_controls_button in mouse_on_controls_button_dict.items():
                        controls_button_rect_big = controls_button_rect_big_dict[control_name]
                        mouse_on_controls_button = controls_button_rect_big.collidepoint(mouse_pos)
                        edited_controls_file_dict = get_edited_controls_file_dict()
                        edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
                        edited_control_display_name = edited_controls_display_names_dict.get(control_name)
                        edited_controls_pygame_constants_names_dict = edited_controls_file_dict.get("edited_controls_pygame_constants_names_dict")
                        edited_control_pygame_constant_name = edited_controls_pygame_constants_names_dict.get(control_name)
                        edited_controls_are_mouse_buttons = edited_controls_file_dict.get("edited_controls_are_mouse_buttons")
                        edited_control_name_is_mouse = edited_controls_are_mouse_buttons.get(control_name)
                        unbound_display_name = get_display_name(list(unbound_constants_dict.keys())[0])
                        current_control_set_to_unbound = edited_control_display_name == unbound_display_name
                        held_control_filled = held_control_name != ""
                        if current_control_set_to_unbound and can_edit_controls:
                            MOUSE_WHEEL_UP = 4
                            MOUSE_WHEEL_DOWN = 5
                            if ((
                                event.type == pygame.KEYDOWN and hasattr(event, "key") and event.key != pygame.K_ESCAPE
                            ) or (event.type == pygame.MOUSEBUTTONDOWN and hasattr(event, "button") and event.button != MOUSE_WHEEL_UP and event.button != MOUSE_WHEEL_DOWN)):
                                interpret_input(control_name,event)
                                held_control_name = ""
                                held_control_display_name = unbound_display_name
                                controls_update = True
                            can_edit_controls = False
                        elif unbound_display_name in edited_controls_display_names_dict and event.type == pygame.KEYDOWN and hasattr(event, "key") and event.key == pygame.K_ESCAPE:
                            edited_controls_display_names_dict_index = list(edited_controls_display_names_dict.values()).index(unbound_display_name)
                            edited_control_name = list(edited_controls_display_names_dict.keys())[edited_controls_display_names_dict_index]
                            edited_controls_display_names_dict.update({edited_control_name:held_control_display_name})
                            edited_controls_file_dict.update({"edited_controls_display_names_dict":edited_controls_display_names_dict})
                            set_control_display_name_to_other_display_name(control_name, held_control_display_name)
                            held_control_name = ""
                            held_control_display_name = unbound_display_name
                            controls_update = True
                            can_edit_controls = False
                        elif mouse_on_controls_button and clicking_with_left_mouse and not current_control_set_to_unbound:
                            if held_control_filled:
                                set_control_display_name_to_other_display_name(held_control_name, held_control_display_name)
                            held_control_name = control_name
                            held_control_display_name = edited_control_display_name
                            set_control_display_name_to_unbound(control_name)
                            controls_update = True
                        elif mouse_released:
                            can_edit_controls = True
                        mouse_on_controls_button_dict.update({control_name: mouse_on_controls_button})

                    mouse_on_controls_reset_button = controls_reset_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_controls_back_button = controls_back_button_rect_big.collidepoint(mouse_pos)
                    # Reset Button
                    if mouse_on_controls_reset_button:
                        if clicking_with_left_mouse:
                            reset_controls()
                            controls_update = True
                    # Back Button
                    elif mouse_on_controls_back_button:
                        if clicking_with_left_mouse:
                            menu_section = SETTINGS_MENU
                # Display Menu
                elif menu_section == DISPLAY_MENU:
                    mouse_on_display_back_button = display_back_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_display_show_controls_button = display_show_controls_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_display_show_in_game_stats_button = display_show_in_game_stats_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_display_show_in_game_health_button = display_show_in_game_health_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_display_show_in_game_buffs_button = display_show_in_game_buffs_button_rect_big.collidepoint(mouse_pos)
                    mouse_on_display_reset_button = display_reset_button_rect_big.collidepoint(mouse_pos)
                    # Show Controls Button
                    if mouse_on_display_show_controls_button:
                        if clicking_with_left_mouse:
                            edited_options_file_dict = get_edited_options_file_dict()
                            edited_display_controls = edited_options_file_dict.get("edited_display_controls")
                            edited_options_file_dict.update({"edited_display_controls":(not edited_display_controls)})
                            set_edited_options_file_dict(edited_options_file_dict)
                            display_controls_update = True
                    # Show In Game Stats Button
                    if mouse_on_display_show_in_game_stats_button:
                        if clicking_with_left_mouse:
                            edited_options_file_dict = get_edited_options_file_dict()
                            edited_display_in_game_stats = edited_options_file_dict.get("edited_display_in_game_stats")
                            edited_options_file_dict.update({"edited_display_in_game_stats":(not edited_display_in_game_stats)})
                            set_edited_options_file_dict(edited_options_file_dict)
                            display_in_game_stats_update = True
                    # Show In Game Health Button
                    if mouse_on_display_show_in_game_health_button:
                        if clicking_with_left_mouse:
                            edited_options_file_dict = get_edited_options_file_dict()
                            edited_display_in_game_health = edited_options_file_dict.get("edited_display_in_game_health")
                            edited_options_file_dict.update({"edited_display_in_game_health":(not edited_display_in_game_health)})
                            set_edited_options_file_dict(edited_options_file_dict)
                            display_in_game_health_update = True
                    # Show In Game Buffs Button
                    if mouse_on_display_show_in_game_buffs_button:
                        if clicking_with_left_mouse:
                            edited_options_file_dict = get_edited_options_file_dict()
                            edited_display_in_game_buffs = edited_options_file_dict.get("edited_display_in_game_buffs")
                            edited_options_file_dict.update({"edited_display_in_game_buffs":(not edited_display_in_game_buffs)})
                            set_edited_options_file_dict(edited_options_file_dict)
                            display_in_game_buffs_update = True
                    # Reset Button
                    if mouse_on_display_reset_button:
                        if clicking_with_left_mouse:
                            reset_display_options()
                            display_controls_update = True
                            display_in_game_stats_update = True
                            display_in_game_health_update = True
                            display_in_game_buffs_update = True
                    # Back Button
                    if mouse_on_display_back_button:
                        if clicking_with_left_mouse:
                            menu_section = SETTINGS_MENU

                # Main Menu Display
                # Sprite Resets
                wizard.sprite.reset()
                harold.sprite.reset()
                # Event Clear
                pygame.event.clear()
                # Timer Resets
                death_timer = 0
                bg_music_timer = 0
                # Main Menu Background, Wizard, and Harold Blits
                screen.blit(bg_surf,(0,-bg_surf.get_height() + WINDOW_HEIGHT))
                screen.blit(main_menu_wizard_surf,main_menu_wizard_rect)
                screen.blit(main_menu_harold_surf,main_menu_harold_rect)
                # Main Menu Score
                score_message_surf = test_font.render("Score: " + str(score),False,"#FCDC4D")
                score_message_surf = pygame.transform.scale_by(score_message_surf,WINDOW_SCALAR)
                score_message_rect = score_message_surf.get_rect(center = (WINDOW_WIDTH/2,(84/800 * WINDOW_HEIGHT)))
                edited_stats_file_dict = get_edited_stats_file_dict()
                edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                high_score = edited_stats_interactivity_file_dict.get("high_score")
                if score > high_score:
                    edited_stats_interactivity_file_dict.update({"high_score":score})
                    set_edited_stats_file_dict(edited_stats_file_dict)
                # Main Menu Score vs. Title Blit
                if score == 0: screen.blit(main_menu_title_surf,main_menu_title_rect)
                else: screen.blit(score_message_surf,score_message_rect)

                # Menu Blits
                # Main Menu Button Blits
                if menu_section == MAIN_MENU:
                    # Start Button
                    if not mouse_on_main_menu_start_button: screen.blit(main_menu_start_button_surf,main_menu_start_button_rect)
                    else: screen.blit(main_menu_start_button_surf_big,main_menu_start_button_rect_big)
                    # Statistics Button
                    if not mouse_on_main_menu_statistics_button: screen.blit(main_menu_statistics_button_surf,main_menu_statistics_button_rect)
                    else: screen.blit(main_menu_statistics_button_surf_big,main_menu_statistics_button_rect_big)
                    # Settings Button
                    if not mouse_on_main_menu_settings_button: screen.blit(main_menu_settings_button_surf,main_menu_settings_button_rect)
                    else: screen.blit(main_menu_settings_button_surf_big,main_menu_settings_button_rect_big)
                    # Exit Button
                    if not mouse_on_main_menu_exit_button: screen.blit(main_menu_exit_button_surf,main_menu_exit_button_rect)
                    else: screen.blit(main_menu_exit_button_surf_big,main_menu_exit_button_rect_big)
                # Statistics Menu Button Blits
                elif menu_section == STATISTICS_MENU:
                    # Extra Stat Checks
                    if fireballs_shot != 0:
                        edited_stats_file_dict = get_edited_stats_file_dict()
                        edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                        fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
                        fireballs_shot_total += fireballs_shot
                        edited_stats_interactivity_file_dict.update({"fireballs_shot":fireballs_shot_total})
                        set_edited_stats_file_dict(edited_stats_file_dict)
                        fireballs_shot = 0
                    if jumps_made != 0:
                        edited_stats_file_dict = get_edited_stats_file_dict()
                        edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                        jumps_total = edited_stats_interactivity_file_dict.get("jumps")
                        jumps_total += jumps_made
                        edited_stats_interactivity_file_dict.update({"jumps":jumps_total})
                        set_edited_stats_file_dict(edited_stats_file_dict)
                        jumps_made = 0
                    if distance_traveled != 0:
                        edited_stats_file_dict = get_edited_stats_file_dict()
                        edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                        distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
                        distance_traveled_total += distance_traveled
                        edited_stats_interactivity_file_dict.update({"distance_traveled":distance_traveled_total})
                        set_edited_stats_file_dict(edited_stats_file_dict)
                        jumps_made = 0
                    # Stats Updates
                    if pre_stat_update_edited_stats_file_dict and pre_stat_update_edited_stats_file_dict != get_edited_stats_file_dict():
                        pre_stat_update_edited_stats_kills_file_dict = pre_stat_update_edited_stats_file_dict.get("kills")
                        pre_stat_update_edited_stats_interactivity_file_dict = pre_stat_update_edited_stats_file_dict.get("interactivity")
                        pre_stat_update_edited_stats_in_game_stat_records_file_dict = pre_stat_update_edited_stats_file_dict.get("in_game_stat_records")
                        pre_stat_update_edited_stats_buffs_file_dict = pre_stat_update_edited_stats_file_dict.get("buffs")
                        edited_stats_file_dict = get_edited_stats_file_dict()
                        edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
                        edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
                        edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
                        edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
                        # Left Side Updates
                        # Kills
                        if pre_stat_update_edited_stats_kills_file_dict != edited_stats_kills_file_dict:
                            pre_stat_update_skeletons_killed_total = pre_stat_update_edited_stats_kills_file_dict.get("skeletons_killed")
                            skeletons_killed_total = edited_stats_kills_file_dict.get("skeletons_killed")
                            pre_stat_update_skeleton_birds_killed_total = pre_stat_update_edited_stats_kills_file_dict.get("skeleton_birds_killed")
                            skeleton_birds_killed_total = edited_stats_kills_file_dict.get("skeleton_birds_killed")
                            # Skeletons Killed Update
                            if pre_stat_update_skeletons_killed_total != skeletons_killed_total:
                                statistics_skeletons_killed_tracker_surf = test_font.render(f"Skeletons Killed: {skeletons_killed_total}",False,"#FCDC4D")
                                statistics_skeletons_killed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_skeletons_killed_tracker_surf = pygame.transform.scale_by(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_scale)
                                statistics_skeletons_killed_tracker_rect = statistics_skeletons_killed_tracker_surf.get_rect(center = (statistics_skeletons_killed_tracker_start_pos))
                                mouse_on_statistics_skeletons_killed_tracker = False
                                statistics_skeletons_killed_tracker_big_scale = button_when_big_scale
                                statistics_skeletons_killed_tracker_surf_big = pygame.transform.scale_by(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_big_scale)
                                statistics_skeletons_killed_tracker_rect_big = statistics_skeletons_killed_tracker_surf_big.get_rect(center = (statistics_skeletons_killed_tracker_start_pos))
                                statistics_skeletons_killed_tracker_new_x_pos = statistics_skeletons_killed_tracker_start_x_pos - ((statistics_skeletons_killed_tracker_rect_big.width)/2)
                                statistics_skeletons_killed_tracker_new_pos = (statistics_skeletons_killed_tracker_new_x_pos,statistics_skeletons_killed_tracker_start_y_pos)
                                statistics_skeletons_killed_tracker_rect = statistics_skeletons_killed_tracker_surf.get_rect(center = (statistics_skeletons_killed_tracker_new_pos))
                                statistics_skeletons_killed_tracker_rect_big = statistics_skeletons_killed_tracker_surf_big.get_rect(center = (statistics_skeletons_killed_tracker_new_pos))
                            # Skeleton Birds Killed Update
                            if pre_stat_update_skeleton_birds_killed_total != skeleton_birds_killed_total:
                                statistics_skeleton_birds_killed_tracker_surf = test_font.render(f"Skeleton Birds Killed: {skeleton_birds_killed_total}",False,"#FCDC4D")
                                statistics_skeleton_birds_killed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_skeleton_birds_killed_tracker_surf = pygame.transform.scale_by(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_scale)
                                statistics_skeleton_birds_killed_tracker_rect = statistics_skeleton_birds_killed_tracker_surf.get_rect(center = (statistics_skeleton_birds_killed_tracker_start_pos))
                                mouse_on_statistics_skeleton_birds_killed_tracker = False
                                statistics_skeleton_birds_killed_tracker_big_scale = button_when_big_scale
                                statistics_skeleton_birds_killed_tracker_surf_big = pygame.transform.scale_by(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_big_scale)
                                statistics_skeleton_birds_killed_tracker_rect_big = statistics_skeleton_birds_killed_tracker_surf_big.get_rect(center = (statistics_skeleton_birds_killed_tracker_start_pos))
                                statistics_skeleton_birds_killed_tracker_new_x_pos = statistics_skeleton_birds_killed_tracker_start_x_pos - ((statistics_skeleton_birds_killed_tracker_rect_big.width)/2)
                                statistics_skeleton_birds_killed_tracker_new_pos = (statistics_skeleton_birds_killed_tracker_new_x_pos,statistics_skeleton_birds_killed_tracker_start_y_pos)
                                statistics_skeleton_birds_killed_tracker_rect = statistics_skeleton_birds_killed_tracker_surf.get_rect(center = (statistics_skeleton_birds_killed_tracker_new_pos))
                                statistics_skeleton_birds_killed_tracker_rect_big = statistics_skeleton_birds_killed_tracker_surf_big.get_rect(center = (statistics_skeleton_birds_killed_tracker_new_pos))
                        # Interactivity
                        if pre_stat_update_edited_stats_interactivity_file_dict != edited_stats_interactivity_file_dict:
                            pre_stat_update_time_played_total = pre_stat_update_edited_stats_interactivity_file_dict.get("time_played")
                            time_played_total = edited_stats_interactivity_file_dict.get("time_played")
                            pre_stat_update_high_score_total = pre_stat_update_edited_stats_interactivity_file_dict.get("high_score")
                            high_score_total = edited_stats_interactivity_file_dict.get("high_score")
                            pre_stat_update_fireballs_shot_total = pre_stat_update_edited_stats_interactivity_file_dict.get("fireballs_shot")
                            fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
                            pre_stat_update_jumps_total = pre_stat_update_edited_stats_interactivity_file_dict.get("jumps")
                            jumps_total = edited_stats_interactivity_file_dict.get("jumps")
                            pre_stat_update_distance_traveled_total = pre_stat_update_edited_stats_interactivity_file_dict.get("distance_traveled")
                            distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
                            # Time Played Update
                            if pre_stat_update_time_played_total != time_played_total:
                                time_played_total = edited_stats_interactivity_file_dict.get("time_played")
                                units = {"weeks":3600 * 24 * 7,"days":3600 * 24,"hours": 3600, "minutes": 60, "seconds": 1}
                                final_displayed_time = ""
                                for unit, value in units.items():
                                    count = time_played_total // value
                                    time_played_total -= count * value
                                    if count > 0:
                                        final_displayed_time += f"{count}{unit[0]} "
                                if not final_displayed_time:
                                    final_displayed_time = "0"
                                statistics_time_played_tracker_surf = test_font.render(f"Time Played: {final_displayed_time.strip()}",False,"#FCDC4D")
                                statistics_time_played_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_time_played_tracker_surf = pygame.transform.scale_by(statistics_time_played_tracker_surf,statistics_time_played_tracker_scale)
                                statistics_time_played_tracker_rect = statistics_time_played_tracker_surf.get_rect(center = (statistics_time_played_tracker_start_pos))
                                mouse_on_statistics_time_played_tracker = False
                                statistics_time_played_tracker_big_scale = button_when_big_scale
                                statistics_time_played_tracker_surf_big = pygame.transform.scale_by(statistics_time_played_tracker_surf,statistics_time_played_tracker_big_scale)
                                statistics_time_played_tracker_rect_big = statistics_time_played_tracker_surf_big.get_rect(center = (statistics_time_played_tracker_start_pos))
                                statistics_time_played_tracker_new_x_pos = statistics_time_played_tracker_start_x_pos - ((statistics_time_played_tracker_rect_big.width)/2)
                                statistics_time_played_tracker_new_pos = (statistics_time_played_tracker_new_x_pos,statistics_time_played_tracker_start_y_pos)
                                statistics_time_played_tracker_rect = statistics_time_played_tracker_surf.get_rect(center = (statistics_time_played_tracker_new_pos))
                                statistics_time_played_tracker_rect_big = statistics_time_played_tracker_surf_big.get_rect(center = (statistics_time_played_tracker_new_pos))
                            # High Score Update
                            if pre_stat_update_high_score_total != high_score_total:
                                statistics_high_score_tracker_surf = test_font.render(f"High Score: {high_score}",False,"#FCDC4D")
                                statistics_high_score_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_high_score_tracker_surf = pygame.transform.scale_by(statistics_high_score_tracker_surf,statistics_high_score_tracker_scale)
                                statistics_high_score_tracker_rect = statistics_high_score_tracker_surf.get_rect(center = (statistics_high_score_tracker_start_pos))
                                mouse_on_statistics_high_score_tracker = False
                                statistics_high_score_tracker_big_scale = button_when_big_scale
                                statistics_high_score_tracker_surf_big = pygame.transform.scale_by(statistics_high_score_tracker_surf,statistics_high_score_tracker_big_scale)
                                statistics_high_score_tracker_rect_big = statistics_high_score_tracker_surf_big.get_rect(center = (statistics_high_score_tracker_start_pos))
                                statistics_high_score_tracker_new_x_pos = statistics_high_score_tracker_start_x_pos - ((statistics_high_score_tracker_rect_big.width)/2)
                                statistics_high_score_tracker_new_pos = (statistics_high_score_tracker_new_x_pos,statistics_high_score_tracker_start_y_pos)
                                statistics_high_score_tracker_rect = statistics_high_score_tracker_surf.get_rect(center = (statistics_high_score_tracker_new_pos))
                                statistics_high_score_tracker_rect_big = statistics_high_score_tracker_surf_big.get_rect(center = (statistics_high_score_tracker_new_pos))
                            # Fireballs Shot Update
                            if pre_stat_update_fireballs_shot_total != fireballs_shot_total:
                                statistics_fireballs_shot_tracker_surf = test_font.render(f"Fireballs Shot: {fireballs_shot_total}",False,"#FCDC4D")
                                statistics_fireballs_shot_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_fireballs_shot_tracker_surf = pygame.transform.scale_by(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_scale)
                                statistics_fireballs_shot_tracker_rect = statistics_fireballs_shot_tracker_surf.get_rect(center = (statistics_fireballs_shot_tracker_start_pos))
                                mouse_on_statistics_fireballs_shot_tracker = False
                                statistics_fireballs_shot_tracker_big_scale = button_when_big_scale
                                statistics_fireballs_shot_tracker_surf_big = pygame.transform.scale_by(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_big_scale)
                                statistics_fireballs_shot_tracker_rect_big = statistics_fireballs_shot_tracker_surf_big.get_rect(center = (statistics_fireballs_shot_tracker_start_pos))
                                statistics_fireballs_shot_tracker_new_x_pos = statistics_fireballs_shot_tracker_start_x_pos - ((statistics_fireballs_shot_tracker_rect_big.width)/2)
                                statistics_fireballs_shot_tracker_new_pos = (statistics_fireballs_shot_tracker_new_x_pos,statistics_fireballs_shot_tracker_start_y_pos)
                                statistics_fireballs_shot_tracker_rect = statistics_fireballs_shot_tracker_surf.get_rect(center = (statistics_fireballs_shot_tracker_new_pos))
                                statistics_fireballs_shot_tracker_rect_big = statistics_fireballs_shot_tracker_surf_big.get_rect(center = (statistics_fireballs_shot_tracker_new_pos))
                            # Jumps Update
                            if pre_stat_update_jumps_total != jumps_total:
                                statistics_jumps_tracker_surf = test_font.render(f"Jumps: {jumps_total}",False,"#FCDC4D")
                                statistics_jumps_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_jumps_tracker_surf = pygame.transform.scale_by(statistics_jumps_tracker_surf,statistics_jumps_tracker_scale)
                                statistics_jumps_tracker_rect = statistics_jumps_tracker_surf.get_rect(center = (statistics_jumps_tracker_start_pos))
                                mouse_on_statistics_jumps_tracker = False
                                statistics_jumps_tracker_big_scale = button_when_big_scale
                                statistics_jumps_tracker_surf_big = pygame.transform.scale_by(statistics_jumps_tracker_surf,statistics_jumps_tracker_big_scale)
                                statistics_jumps_tracker_rect_big = statistics_jumps_tracker_surf_big.get_rect(center = (statistics_jumps_tracker_start_pos))
                                statistics_jumps_tracker_new_x_pos = statistics_jumps_tracker_start_x_pos - ((statistics_jumps_tracker_rect_big.width)/2)
                                statistics_jumps_tracker_new_pos = (statistics_jumps_tracker_new_x_pos,statistics_jumps_tracker_start_y_pos)
                                statistics_jumps_tracker_rect = statistics_jumps_tracker_surf.get_rect(center = (statistics_jumps_tracker_new_pos))
                                statistics_jumps_tracker_rect_big = statistics_jumps_tracker_surf_big.get_rect(center = (statistics_jumps_tracker_new_pos))
                            # Distance Traveled Update
                            if pre_stat_update_distance_traveled_total != distance_traveled_total:
                                statistics_distance_traveled_tracker_surf = test_font.render(f"Distance Traveled: {int(distance_traveled_total/WIZARD_WIDTH)}m",False,"#FCDC4D")
                                statistics_distance_traveled_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_distance_traveled_tracker_surf = pygame.transform.scale_by(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_scale)
                                statistics_distance_traveled_tracker_rect = statistics_distance_traveled_tracker_surf.get_rect(center = (statistics_distance_traveled_tracker_start_pos))
                                mouse_on_statistics_distance_traveled_tracker = False
                                statistics_distance_traveled_tracker_big_scale = button_when_big_scale
                                statistics_distance_traveled_tracker_surf_big = pygame.transform.scale_by(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_big_scale)
                                statistics_distance_traveled_tracker_rect_big = statistics_distance_traveled_tracker_surf_big.get_rect(center = (statistics_distance_traveled_tracker_start_pos))
                                statistics_distance_traveled_tracker_new_x_pos = statistics_distance_traveled_tracker_start_x_pos - ((statistics_distance_traveled_tracker_rect_big.width)/2)
                                statistics_distance_traveled_tracker_new_pos = (statistics_distance_traveled_tracker_new_x_pos,statistics_distance_traveled_tracker_start_y_pos)
                                statistics_distance_traveled_tracker_rect = statistics_distance_traveled_tracker_surf.get_rect(center = (statistics_distance_traveled_tracker_new_pos))
                                statistics_distance_traveled_tracker_rect_big = statistics_distance_traveled_tracker_surf_big.get_rect(center = (statistics_distance_traveled_tracker_new_pos))
                        # Right Side Updates
                        # In-Game Stat Records
                        if pre_stat_update_edited_stats_in_game_stat_records_file_dict != edited_stats_in_game_stat_records_file_dict:
                            pre_stat_update_highest_speed = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_speed")
                            highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
                            pre_stat_update_highest_damage = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_damage")
                            highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
                            pre_stat_update_highest_piercing = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
                            highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
                            pre_stat_update_lowest_cooldown = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
                            lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
                            # Highest Speed Update
                            if pre_stat_update_highest_speed != highest_speed:
                                statistics_highest_speed_tracker_surf = test_font.render(f"Highest Speed: {round((highest_speed/WIZARD_WIDTH)*60,2)}m/s",False,"#FCDC4D")
                                statistics_highest_speed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_highest_speed_tracker_surf = pygame.transform.scale_by(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_scale)
                                statistics_highest_speed_tracker_rect = statistics_highest_speed_tracker_surf.get_rect(center = (statistics_highest_speed_tracker_start_pos))
                                mouse_on_statistics_highest_speed_tracker = False
                                statistics_highest_speed_tracker_big_scale = button_when_big_scale
                                statistics_highest_speed_tracker_surf_big = pygame.transform.scale_by(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_big_scale)
                                statistics_highest_speed_tracker_rect_big = statistics_highest_speed_tracker_surf_big.get_rect(center = (statistics_highest_speed_tracker_start_pos))
                                statistics_highest_speed_tracker_new_x_pos = statistics_highest_speed_tracker_start_x_pos + ((statistics_highest_speed_tracker_rect_big.width)/2)
                                statistics_highest_speed_tracker_new_pos = (statistics_highest_speed_tracker_new_x_pos,statistics_highest_speed_tracker_start_y_pos)
                                statistics_highest_speed_tracker_rect = statistics_highest_speed_tracker_surf.get_rect(center = (statistics_highest_speed_tracker_new_pos))
                                statistics_highest_speed_tracker_rect_big = statistics_highest_speed_tracker_surf_big.get_rect(center = (statistics_highest_speed_tracker_new_pos))
                            # Highest Damage Update
                            if pre_stat_update_highest_damage != highest_damage:
                                statistics_highest_damage_tracker_surf = test_font.render(f"Highest Damage: {highest_damage}",False,"#FCDC4D")
                                statistics_highest_damage_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_highest_damage_tracker_surf = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_scale)
                                statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_start_pos))
                                mouse_on_statistics_highest_damage_tracker = False
                                statistics_highest_damage_tracker_big_scale = button_when_big_scale
                                statistics_highest_damage_tracker_surf_big = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_big_scale)
                                statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_start_pos))
                                statistics_highest_damage_tracker_new_x_pos = statistics_highest_damage_tracker_start_x_pos + ((statistics_highest_damage_tracker_rect_big.width)/2)
                                statistics_highest_damage_tracker_new_pos = (statistics_highest_damage_tracker_new_x_pos,statistics_highest_damage_tracker_start_y_pos)
                                statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_new_pos))
                                statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_new_pos))
                            # Highest Piercing Update
                            if pre_stat_update_highest_piercing != highest_piercing:
                                statistics_highest_piercing_tracker_surf = test_font.render(f"Highest Piercing: {highest_piercing - 1}",False,"#FCDC4D")
                                statistics_highest_piercing_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_highest_piercing_tracker_surf = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_scale)
                                statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
                                mouse_on_statistics_highest_piercing_tracker = False
                                statistics_highest_piercing_tracker_big_scale = button_when_big_scale
                                statistics_highest_piercing_tracker_surf_big = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_big_scale)
                                statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
                                statistics_highest_piercing_tracker_new_x_pos = statistics_highest_piercing_tracker_start_x_pos + ((statistics_highest_piercing_tracker_rect_big.width)/2)
                                statistics_highest_piercing_tracker_new_pos = (statistics_highest_piercing_tracker_new_x_pos,statistics_highest_piercing_tracker_start_y_pos)
                                statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
                                statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
                            # Lowest Cooldown Update
                            if pre_stat_update_lowest_cooldown != lowest_cooldown:
                                statistics_lowest_cooldown_tracker_surf = test_font.render(f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",False,"#FCDC4D")
                                statistics_lowest_cooldown_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_lowest_cooldown_tracker_surf = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_scale)
                                statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
                                mouse_on_statistics_lowest_cooldown_tracker = False
                                statistics_lowest_cooldown_tracker_big_scale = button_when_big_scale
                                statistics_lowest_cooldown_tracker_surf_big = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_big_scale)
                                statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
                                statistics_lowest_cooldown_tracker_new_x_pos = statistics_lowest_cooldown_tracker_start_x_pos + ((statistics_lowest_cooldown_tracker_rect_big.width)/2)
                                statistics_lowest_cooldown_tracker_new_pos = (statistics_lowest_cooldown_tracker_new_x_pos,statistics_lowest_cooldown_tracker_start_y_pos)
                                statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
                                statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
                        # Buffs
                        # Double Jump Buff Update
                        if edited_stats_buffs_file_dict.get("double_jump_buff"):
                            statistics_double_jump_buff_tracker_surf = test_font.render("Double Jump Buff: Found",False,"#FCDC4D")
                            statistics_double_jump_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                            statistics_double_jump_buff_tracker_surf = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_scale)
                            statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
                            mouse_on_statistics_double_jump_buff_tracker = False
                            statistics_double_jump_buff_tracker_big_scale = button_when_big_scale
                            statistics_double_jump_buff_tracker_surf_big = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_big_scale)
                            statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
                            statistics_double_jump_buff_tracker_new_x_pos = statistics_double_jump_buff_tracker_start_x_pos + ((statistics_double_jump_buff_tracker_rect_big.width)/2)
                            statistics_double_jump_buff_tracker_new_pos = (statistics_double_jump_buff_tracker_new_x_pos,statistics_double_jump_buff_tracker_start_y_pos)
                            statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
                            statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
                        # Knockback Buff Update
                        if edited_stats_buffs_file_dict.get("knockback_buff"):
                            statistics_knockback_buff_tracker_surf = test_font.render("Knockback Buff: Found",False,"#FCDC4D")
                            statistics_knockback_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                            statistics_knockback_buff_tracker_surf = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_scale)
                            statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
                            mouse_on_statistics_knockback_buff_tracker = False
                            statistics_knockback_buff_tracker_big_scale = button_when_big_scale
                            statistics_knockback_buff_tracker_surf_big = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_big_scale)
                            statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
                            statistics_knockback_buff_tracker_new_x_pos = statistics_knockback_buff_tracker_start_x_pos + ((statistics_knockback_buff_tracker_rect_big.width)/2)
                            statistics_knockback_buff_tracker_new_pos = (statistics_knockback_buff_tracker_new_x_pos,statistics_knockback_buff_tracker_start_y_pos)
                            statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
                            statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
                        # Shield Buff Update
                        if edited_stats_buffs_file_dict.get("shield_buff"):
                                statistics_shield_buff_tracker_surf = test_font.render("Magic Shield Buff: Found",False,"#FCDC4D")
                                statistics_shield_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                                statistics_shield_buff_tracker_surf = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_scale)
                                statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_start_pos))
                                mouse_on_statistics_shield_buff_tracker = False
                                statistics_shield_buff_tracker_big_scale = button_when_big_scale
                                statistics_shield_buff_tracker_surf_big = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_big_scale)
                                statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_start_pos))
                                statistics_shield_buff_tracker_new_x_pos = statistics_shield_buff_tracker_start_x_pos + ((statistics_shield_buff_tracker_rect_big.width)/2)
                                statistics_shield_buff_tracker_new_pos = (statistics_shield_buff_tracker_new_x_pos,statistics_shield_buff_tracker_start_y_pos)
                                statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_new_pos))
                                statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_new_pos))
                    # Left Side
                    # Skeletons Killed Tracker
                    if not mouse_on_statistics_skeletons_killed_tracker: screen.blit(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_rect)
                    else: screen.blit(statistics_skeletons_killed_tracker_surf_big,statistics_skeletons_killed_tracker_rect_big)
                    # Skeleton Birds Killed Tracker
                    if not mouse_on_statistics_skeleton_birds_killed_tracker: screen.blit(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_rect)
                    else: screen.blit(statistics_skeleton_birds_killed_tracker_surf_big,statistics_skeleton_birds_killed_tracker_rect_big)
                    # Time Played Tracker
                    if not mouse_on_statistics_time_played_tracker: screen.blit(statistics_time_played_tracker_surf,statistics_time_played_tracker_rect)
                    else: screen.blit(statistics_time_played_tracker_surf_big,statistics_time_played_tracker_rect_big)
                    # High Score Tracker
                    if not mouse_on_statistics_high_score_tracker: screen.blit(statistics_high_score_tracker_surf,statistics_high_score_tracker_rect)
                    else: screen.blit(statistics_high_score_tracker_surf_big,statistics_high_score_tracker_rect_big)
                    # Fireballs Shot Tracker
                    if not mouse_on_statistics_fireballs_shot_tracker: screen.blit(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_rect)
                    else: screen.blit(statistics_fireballs_shot_tracker_surf_big,statistics_fireballs_shot_tracker_rect_big)
                    # Jumps Tracker
                    if not mouse_on_statistics_jumps_tracker: screen.blit(statistics_jumps_tracker_surf,statistics_jumps_tracker_rect)
                    else: screen.blit(statistics_jumps_tracker_surf_big,statistics_jumps_tracker_rect_big)
                    # Distance Traveled Tracker
                    if not mouse_on_statistics_distance_traveled_tracker: screen.blit(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_rect)
                    else: screen.blit(statistics_distance_traveled_tracker_surf_big,statistics_distance_traveled_tracker_rect_big)
                    # Right Side
                    # Highest Speed Tracker
                    if not mouse_on_statistics_highest_speed_tracker: screen.blit(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_rect)
                    else: screen.blit(statistics_highest_speed_tracker_surf_big,statistics_highest_speed_tracker_rect_big)
                    # Highest Damage Tracker
                    if not mouse_on_statistics_highest_damage_tracker: screen.blit(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_rect)
                    else: screen.blit(statistics_highest_damage_tracker_surf_big,statistics_highest_damage_tracker_rect_big)
                    # Highest Piercing Tracker
                    if not mouse_on_statistics_highest_piercing_tracker: screen.blit(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_rect)
                    else: screen.blit(statistics_highest_piercing_tracker_surf_big,statistics_highest_piercing_tracker_rect_big)
                    # Lowest Cooldown Tracker
                    if not mouse_on_statistics_lowest_cooldown_tracker: screen.blit(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_rect)
                    else: screen.blit(statistics_lowest_cooldown_tracker_surf_big,statistics_lowest_cooldown_tracker_rect_big)
                    # Double Jump Buff Tracker
                    if not mouse_on_statistics_double_jump_buff_tracker: screen.blit(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_rect)
                    else: screen.blit(statistics_double_jump_buff_tracker_surf_big,statistics_double_jump_buff_tracker_rect_big)
                    # Knockback Buff Tracker
                    if not mouse_on_statistics_knockback_buff_tracker: screen.blit(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_rect)
                    else: screen.blit(statistics_knockback_buff_tracker_surf_big,statistics_knockback_buff_tracker_rect_big)
                    # Shield Buff Tracker
                    if not mouse_on_statistics_shield_buff_tracker: screen.blit(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_rect)
                    else: screen.blit(statistics_shield_buff_tracker_surf_big,statistics_shield_buff_tracker_rect_big)
                    # Bottom
                    # Back Button
                    if not mouse_on_statistics_back_button: screen.blit(statistics_back_button_surf,statistics_back_button_rect)
                    else: screen.blit(statistics_back_button_surf_big,statistics_back_button_rect_big)
                    pre_stat_update_edited_stats_file_dict = {}
                # Settings Menu Button Blits
                elif menu_section == SETTINGS_MENU:
                    # Sounds Button
                    if not mouse_on_settings_sounds_button: screen.blit(settings_sounds_button_surf,settings_sounds_button_rect)
                    else: screen.blit(settings_sounds_button_surf_big,settings_sounds_button_rect_big)
                    # Controls Button
                    if not mouse_on_settings_controls_button: screen.blit(settings_controls_button_surf,settings_controls_button_rect)
                    else: screen.blit(settings_controls_button_surf_big,settings_controls_button_rect_big)
                    # Display Button
                    if not mouse_on_settings_display_button: screen.blit(settings_display_button_surf,settings_display_button_rect)
                    else: screen.blit(settings_display_button_surf_big,settings_display_button_rect_big)
                    # Back Button
                    if not mouse_on_settings_back_button: screen.blit(settings_back_button_surf,settings_back_button_rect)
                    else: screen.blit(settings_back_button_surf_big,settings_back_button_rect_big)
                # Sounds Menu Button Blits
                elif menu_section == SOUNDS_MENU:
                    # Back Button
                    if not mouse_on_sounds_back_button: screen.blit(sounds_back_button_surf,sounds_back_button_rect)
                    else: screen.blit(sounds_back_button_surf_big,sounds_back_button_rect_big)
                # Controls Menu Button Blits
                elif menu_section == CONTROLS_MENU:
                    # Controls Update
                    if controls_update:
                        mouse_on_controls_button_dict = {}
                        controls_button_surf_dict = {}
                        controls_button_rect_dict = {}
                        controls_button_surf_big_dict = {}
                        controls_button_rect_big_dict = {}
                        controls_button_index = 0
                        controls_button_scalar = 0.5
                        edited_controls_display_names_dict = get_edited_controls_file_dict().get("edited_controls_display_names_dict")
                        default_controls_pygame_constants_names_dict = get_default_controls_file_dict().get("default_controls_pygame_constants_names_dict")
                        for control_name, control in default_controls_pygame_constants_names_dict.items():
                            controls_button_start_x_pos = main_menu_wizard_rect.centerx
                            controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT) + controls_buttons_y_pos_offset * controls_button_index
                            controls_button_start_pos = (controls_button_start_x_pos,controls_button_start_y_pos)
                            control_name_underscore_removed = control_name.replace("_", " ")
                            control_name_capitalized = control_name_underscore_removed.title()
                            controls_button_surf = test_font.render(f"{control_name_capitalized}: {edited_controls_display_names_dict[control_name]}",False,"#FCDC4D")
                            controls_button_scale = WINDOW_SCALAR * controls_button_scalar
                            controls_button_surf = pygame.transform.scale_by(controls_button_surf,controls_button_scale)
                            controls_button_surf_dict.update({control_name: controls_button_surf})
                            controls_button_rect = controls_button_surf.get_rect(center = (controls_button_start_pos))
                            controls_button_rect_dict.update({control_name: controls_button_rect})
                            mouse_on_controls_button_dict.update({control_name: False})
                            controls_button_big_scale = button_when_big_scale
                            controls_button_surf_big = pygame.transform.scale_by(controls_button_surf,controls_button_big_scale)
                            controls_button_surf_big_dict.update({control_name: controls_button_surf_big})
                            controls_button_rect_big = controls_button_surf_big.get_rect(center = (controls_button_start_pos))
                            controls_button_rect_big_dict.update({control_name: controls_button_rect_big})
                            controls_button_index += 1
                        controls_update = False
                    # Controls Buttons
                    for control_name, mouse_on_controls_button in mouse_on_controls_button_dict.items():
                        if not mouse_on_controls_button: screen.blit(controls_button_surf_dict[control_name],controls_button_rect_dict[control_name])
                        else: screen.blit(controls_button_surf_big_dict[control_name],controls_button_rect_big_dict[control_name])
                    # Reset Button
                    if not mouse_on_controls_reset_button: screen.blit(controls_reset_button_surf,controls_reset_button_rect)
                    else: screen.blit(controls_reset_button_surf_big,controls_reset_button_rect_big)
                    # Back Button
                    if not mouse_on_controls_back_button: screen.blit(controls_back_button_surf,controls_back_button_rect)
                    else: screen.blit(controls_back_button_surf_big,controls_back_button_rect_big)
                # Display Menu Button Blits
                elif menu_section == DISPLAY_MENU:
                    # Display Controls Update
                    if display_controls_update:
                        controls_displayed = get_edited_options_file_dict()["edited_display_controls"]
                        display_show_controls_button_surf = test_font.render(f"Display Controls: {controls_displayed}",False,"#FCDC4D")
                        display_show_controls_button_scale = WINDOW_SCALAR * display_button_scalar
                        display_show_controls_button_surf = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_scale)
                        display_show_controls_button_rect = display_show_controls_button_surf.get_rect(center = (display_show_controls_button_start_pos))
                        mouse_on_display_show_controls_button = False
                        display_show_controls_button_big_scale = button_when_big_scale
                        display_show_controls_button_surf_big = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_big_scale)
                        display_show_controls_button_rect_big = display_show_controls_button_surf_big.get_rect(center = (display_show_controls_button_start_pos))
                        display_controls_update = False
                    if display_in_game_stats_update:
                        in_game_stats_displayed = get_edited_options_file_dict()["edited_display_in_game_stats"]
                        display_show_in_game_stats_button_surf = test_font.render(f"Display Stats: {in_game_stats_displayed}",False,"#FCDC4D")
                        display_show_in_game_stats_button_scale = WINDOW_SCALAR * display_button_scalar
                        display_show_in_game_stats_button_surf = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_scale)
                        display_show_in_game_stats_button_rect = display_show_in_game_stats_button_surf.get_rect(center = (display_show_in_game_stats_button_start_pos))
                        mouse_on_display_show_in_game_stats_button = False
                        display_show_in_game_stats_button_big_scale = button_when_big_scale
                        display_show_in_game_stats_button_surf_big = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_big_scale)
                        display_show_in_game_stats_button_rect_big = display_show_in_game_stats_button_surf_big.get_rect(center = (display_show_in_game_stats_button_start_pos))
                        display_in_game_stats_update = False
                    if display_in_game_health_update:
                        in_game_health_displayed = get_edited_options_file_dict()["edited_display_in_game_health"]
                        display_show_in_game_health_button_surf = test_font.render(f"Display Health: {in_game_health_displayed}",False,"#FCDC4D")
                        display_show_in_game_health_button_scale = WINDOW_SCALAR * display_button_scalar
                        display_show_in_game_health_button_surf = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_scale)
                        display_show_in_game_health_button_rect = display_show_in_game_health_button_surf.get_rect(center = (display_show_in_game_health_button_start_pos))
                        mouse_on_display_show_in_game_health_button = False
                        display_show_in_game_health_button_big_scale = button_when_big_scale
                        display_show_in_game_health_button_surf_big = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_big_scale)
                        display_show_in_game_health_button_rect_big = display_show_in_game_health_button_surf_big.get_rect(center = (display_show_in_game_health_button_start_pos))
                        display_in_game_health_update = False
                    if display_in_game_buffs_update:
                        in_game_buffs_displayed = get_edited_options_file_dict()["edited_display_in_game_buffs"]
                        display_show_in_game_buffs_button_surf = test_font.render(f"Display Buffs: {in_game_buffs_displayed}",False,"#FCDC4D")
                        display_show_in_game_buffs_button_scale = WINDOW_SCALAR * display_button_scalar
                        display_show_in_game_buffs_button_surf = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_scale)
                        display_show_in_game_buffs_button_rect = display_show_in_game_buffs_button_surf.get_rect(center = (display_show_in_game_buffs_button_start_pos))
                        mouse_on_display_show_in_game_buffs_button = False
                        display_show_in_game_buffs_button_big_scale = button_when_big_scale
                        display_show_in_game_buffs_button_surf_big = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_big_scale)
                        display_show_in_game_buffs_button_rect_big = display_show_in_game_buffs_button_surf_big.get_rect(center = (display_show_in_game_buffs_button_start_pos))
                        display_in_game_buffs_update = False
                    # Show Controls Button
                    if not mouse_on_display_show_controls_button: screen.blit(display_show_controls_button_surf,display_show_controls_button_rect)
                    else: screen.blit(display_show_controls_button_surf_big,display_show_controls_button_rect_big)
                    # Show In Game Stats Button
                    if not mouse_on_display_show_in_game_stats_button: screen.blit(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_rect)
                    else: screen.blit(display_show_in_game_stats_button_surf_big,display_show_in_game_stats_button_rect_big)
                    # Show In Game Health Button
                    if not mouse_on_display_show_in_game_health_button: screen.blit(display_show_in_game_health_button_surf,display_show_in_game_health_button_rect)
                    else: screen.blit(display_show_in_game_health_button_surf_big,display_show_in_game_health_button_rect_big)
                    # Show In Game Buffs Button
                    if not mouse_on_display_show_in_game_buffs_button: screen.blit(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_rect)
                    else: screen.blit(display_show_in_game_buffs_button_surf_big,display_show_in_game_buffs_button_rect_big)
                    # Reset Button
                    if not mouse_on_display_reset_button: screen.blit(display_reset_button_surf,display_reset_button_rect)
                    else: screen.blit(display_reset_button_surf_big,display_reset_button_rect_big)
                    # Back Button
                    if not mouse_on_display_back_button: screen.blit(display_back_button_surf,display_back_button_rect)
                    else: screen.blit(display_back_button_surf_big,display_back_button_rect_big)

    # Opening Cinematic (Intro)
    if not intro_played:
        screen.blit(bg_surf,(0,-bg_surf.get_height() + WINDOW_HEIGHT))
        screen.blit(wizard_intro_surf,wizard_intro_rect)
        if harold_turn_animation_complete and not harold_flipped:
            harold_intro_surf = pygame.transform.flip(harold_intro_surf,True,False)
            harold_flipped = True
        screen.blit(harold_intro_surf,harold_intro_rect)
        if not wizard_walk_in_animation_complete:
            if wizard_intro_rect.right < WINDOW_WIDTH / 2 - wizard_intro_width_by_scale/2:
                wizard_intro_rect.centerx += wizard.sprite.get_wizard_speed()
            else:
                wizard_walk_in_animation_complete = True
        elif not harold_jump_on_hat_animation_complete:
            if harold_intro_rect.centerx > wizard_intro_rect.centerx:
                harold_intro_rect.centerx -= (harold.sprite.get_harold_speed() * 2)
            else:
                x_lineup = True
            intro_jump_speed += intro_gravity_acceleration
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
                wizard_intro_rect.centerx += wizard.sprite.get_wizard_speed()
                harold_intro_rect.centerx += harold.sprite.get_harold_speed()
            else:
                wizard_and_harold_center_animation_complete = True
        elif not wizard_and_harold_center_with_title_animation_complete:
            if wizard_intro_rect.bottom > main_menu_wizard_start_y_pos:
                wizard_intro_rect.centery -= wizard.sprite.get_wizard_speed()
                harold_intro_rect.centery -= harold.sprite.get_harold_speed()
            else:
                intro_played = True

    # Active Game - Music, Death Checker, Moving Sprites, Collisions
    elif game_active:
        if bg_music_timer == 0:
            pygame.mixer.Channel(BG_MUSIC_CHANNEL).play(bg_music)
        elif bg_music_timer >= (25 * 60):
            bg_music_timer = -1
        if wizard_alive:
            bg_music_timer += 1
            screen.blit(bg_surf,(0,-bg_surf.get_height() + WINDOW_HEIGHT))
            # Stat Image Postions
            score = display_score()
            if get_edited_options_file_dict()["edited_display_in_game_health"]:
                display_in_game_health() # Displays and updates in game health
            if get_edited_options_file_dict()["edited_display_in_game_buffs"]:
                display_in_game_buffs() # Displays and updates in game buffs
            if get_edited_options_file_dict()["edited_display_in_game_stats"]:
                display_in_game_stats() # Displays and updates in game stats
            if get_edited_options_file_dict()["edited_display_controls"]:
                display_controls() # Displays controls on bottom right of screen

            for sprite in moving_sprites: # Holds all things to be drawn
                sprite.draw(screen)
                sprite.update()

            do_collisions()

            wizard_alive = not wizard.sprite.get_wizard_dead()

        else: # Work on death animation
            wizard.sprite.set_wizard_dead(True)
            screen.blit(bg_surf,(0,-bg_surf.get_height() + WINDOW_HEIGHT))
            if get_edited_options_file_dict()["edited_display_controls"]:
                display_controls() # Maintaining controls on bottom right of screen


            wizard.draw(screen) # Draws sprites
            harold.draw(screen)

            wizard.update() # Updates sprites
            harold.update()
            death_timer += 1
            if death_timer > 180:
                game_active = False

    # Global Clock and Display Update
    pygame.display.update()
    clock.tick(60)