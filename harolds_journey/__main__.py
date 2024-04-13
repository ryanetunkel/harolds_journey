"""Main Gameloop"""
from sys import exit
from random import randint, choice

import pygame

from controls import *
from global_vars import *
from harold import *
from obstacle import *
from pickup import *
from buff import *
from player import *
from projectile import *
from graphics.health_bar.health_bar import *
from graphics.health_bar.outline_health_bar import *


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


def display_stats():
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

    # Stat image Surfs - find a centralized place to keep all images so don't have to update this and the pickup class' version of the image
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

    fireball_cooldown_stat_surf = test_font.render(f"Cooldown: {round(wizard.sprite.get_max_fireball_cooldown_time()/60, 2)}", False, "#FCDC4D")
    fireball_cooldown_stat_surf = pygame.transform.scale_by(fireball_cooldown_stat_surf, 0.9)
    fireball_cooldown_stat_rect = fireball_cooldown_stat_surf.get_rect(center = (fireball_cooldown_stat_x_pos,fireball_cooldown_stat_y_pos))

    # Fireball Cooldown Icon
    fireball_cooldown_x_pos = WINDOW_WIDTH * 1/16 # right of health: 11/64 # Below Health: 1/16
    fireball_cooldown_y_pos_num = 7/32 if not wizard.sprite.get_shield() else 11/32
    fireball_cooldown_y_pos = WINDOW_HEIGHT * fireball_cooldown_y_pos_num # right of health: 25/256 # Below Health: 7/32
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

    speed_stat_surf = test_font.render("Speed: " + str(wizard.sprite.get_wizard_speed()), False, "#FCDC4D")
    speed_stat_surf = pygame.transform.scale_by(speed_stat_surf, 0.9)
    speed_stat_rect = speed_stat_surf.get_rect(center = (speed_stat_x_pos,speed_stat_y_pos))
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
    # Buff Blits
    # Double Jump Buff Blit
    if wizard.sprite.get_double_jump():
        screen.blit(double_jump_buff_image_surf,double_jump_buff_image_rect)
    # Shield Buff Blit Blit
    if wizard.sprite.get_shield():
        screen.blit(shield_buff_image_surf,shield_buff_image_rect)
    # Knockback Buff Blit Blit
    if wizard.sprite.get_knockback():
        screen.blit(knockback_buff_image_surf,knockback_buff_image_rect)


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
                        # pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)
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
                            dead_obstacle_group.add(obstacle)
                            # pygame.sprite.spritecollide(projectile,buff_group,True) # Temporary
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
                                obstacle.set_knockback_direction_multiplier(projectile.get_direction_multiplier())
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
    if randint(1,10) == 10:
        pickup_group.add(Pickup("damage",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Fireball Cooldown
    if randint(1,10) == 10:
        pickup_group.add(Pickup("fireball_cooldown",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Piercing
    if randint(1,25) == 25:
        pickup_group.add(Pickup("piercing",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Speed
    if randint(1,20) == 20:
        pickup_group.add(Pickup("speed",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Health
    if wizard.sprite.get_wizard_current_health() < wizard.sprite.get_wizard_max_health():
        if randint(1,10) == 10:
            pickup_group.add(Pickup("health",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Temporary Placement for buffs, will eventually be in the world, not dropped by enemies
    # Double Jump
    if not wizard.sprite.get_double_jump() and randint(1,50) == 50:
        buff_group.add(Buff("double_jump",temp_obstacle_x_pos,temp_obstacle_y_pos))
    # Shield
    if not wizard.sprite.get_shield() and randint(1,50) == 50:
        buff_group.add(Buff("shield",x_pos=temp_obstacle_x_pos,y_pos=temp_obstacle_y_pos))
    # Knockback
    if not wizard.sprite.get_knockback() and randint(1,50) == 50:
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


wizard = pygame.sprite.GroupSingle()
wizard.add(Player())

harold = pygame.sprite.GroupSingle()
harold.add(Harold(wizard))

obstacle_group = pygame.sprite.Group()

dead_obstacle_group = pygame.sprite.Group()

projectile_group = pygame.sprite.Group()

pickup_group = pygame.sprite.Group()

buff_group = pygame.sprite.Group()

health_bar_group = pygame.sprite.Group()

outline_health_bar_group = pygame.sprite.Group()

# Obstacle: Health Bar
health_bar_ownership_group = {pygame.sprite.Sprite(): pygame.sprite.Sprite()}
# Health Bar: Outline Health Bar
outline_health_bar_ownership_group = {pygame.sprite.Sprite(): pygame.sprite.Sprite()}

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


sky_surf = pygame.image.load("harolds_journey/graphics/bg_images/Background.png").convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,WINDOW_SIZE)

ground_surf = pygame.image.load("harolds_journey/graphics/bg_images/Grass.png").convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,WINDOW_SIZE)

# Intro Screen
wizard_title_start_x_pos = WINDOW_WIDTH / 2
wizard_title_start_y_pos = WINDOW_HEIGHT * 3/4
wizard_title_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png").convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(WIZARD_WIDTH * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200), WIZARD_HEIGHT * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)))
wizard_title_rect = wizard_title_surf.get_rect(center = (wizard_title_start_x_pos,wizard_title_start_y_pos))

harold_title_start_x_pos = wizard_title_rect.centerx
harold_title_start_y_pos = wizard_title_rect.top - (52/4 * PIXEL_SIZE)
harold_title_surf = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
harold_title_surf = pygame.transform.scale_by(harold_title_surf,(2.25 * ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)))
harold_title_rect = harold_title_surf.get_rect(midbottom = (harold_title_start_x_pos,harold_title_start_y_pos))

title_game_name_surf = test_font.render("Harold\'s Journey",False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,((WINDOW_WIDTH + WINDOW_HEIGHT)/1200))
title_game_name_rect = title_game_name_surf.get_rect(center = (WINDOW_WIDTH/2,((70/400) * WINDOW_HEIGHT)))

title_info_start_x_pos = wizard_title_rect.centerx
title_info_start_y_pos = wizard_title_rect.centery + ((40/400) * WINDOW_HEIGHT)
title_info_start_pos = (title_info_start_x_pos,title_info_start_y_pos)
title_info_surf = test_font.render("Press any key or click to Start",False,"#FCDC4D")
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
            if not wizard.sprite.get_wizard_dead():
                # Spacebar Release Event Detection
                if wizard.sprite.get_double_jump() and not wizard.sprite.get_double_jump_used() and event.type == pygame.KEYUP:
                    if event.key == jump_button:
                        wizard.sprite.set_first_jump_used(True)
                # Obstacle Timer Event Detection
                if event.type == obstacle_timer:
                    new_obstacle = Obstacle(choice(["bird","skeleton","skeleton","skeleton"]),int(pygame.time.get_ticks() / 1000) - start_time)
                    print(int(pygame.time.get_ticks() / 1000) - start_time)
                    obstacle_group.add(new_obstacle)
                    # Health Bar
                    new_health_bar = HealthBar(new_obstacle, new_obstacle.get_current_health(), new_obstacle.get_max_health())
                    health_bar_group.add(new_health_bar)
                    health_bar_ownership_group[new_obstacle] = new_health_bar
                    # Outline Health Bar
                    new_outline_health_bar = OutlineHealthBar(new_health_bar, new_obstacle.get_x_pos(), new_obstacle.get_y_pos())
                    outline_health_bar_group.add(new_outline_health_bar)
                    outline_health_bar_ownership_group[new_health_bar] = new_outline_health_bar
                if event.type == shoot_button:
                    if wizard.sprite.get_current_fireball_cooldown() == 0: # or wizard.sprite.get_fireball_hit(): # causes fireball_cooldown refresh on hit
                        wizard.sprite.play_fireball_sound()
                        wizard.sprite.set_fireball_shot(True)
                        temp_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
                        wizard.sprite.set_current_fireball_cooldown(temp_max_fireball_cooldown_time)
                        wizard.sprite.set_fireball_hit(False)
                        projectile_group.add(Projectile("fireball", wizard))

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

            do_collisions()

            wizard_alive = not wizard.sprite.get_wizard_dead()

        else: # Work on death animation
            wizard.sprite.set_wizard_dead(True)
            screen.blit(sky_surf,(0,0))
            screen.blit(ground_surf,(0,0))

            wizard.draw(screen) # draws sprites
            harold.draw(screen)

            wizard.update() # updates sprites
            harold.update()
            death_counter += 1
            if death_counter > 180:
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

        score_message_surf = test_font.render("Score: " + str(score),False,"#FCDC4D")
        score_message_surf = pygame.transform.scale_by(score_message_surf,((WINDOW_WIDTH + WINDOW_HEIGHT)/1200))
        score_message_rect = score_message_surf.get_rect(center = (WINDOW_WIDTH/2,(100/800 * WINDOW_HEIGHT)))

        if score == 0: screen.blit(title_game_name_surf,title_game_name_rect)
        else: screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)