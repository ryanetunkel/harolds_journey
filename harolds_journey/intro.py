"""Contains the opening cinematic and related items"""

import pygame

from global_vars import *

# Intro
wizard_walk_in_animation_complete = False
harold_jump_on_hat_animation_complete = False
intro_jump_speed = -14 * GLOBAL_SCALAR
intro_gravity_acceleration = GLOBAL_GRAVITY
x_lineup = False
y_lineup = False
fall = False
harold_turn_animation_complete = False
harold_flipped = False
wizard_and_harold_center_animation_complete = False
wizard_and_harold_center_with_title_animation_complete = False

wizard_intro_start_x_pos = -(128 * WINDOW_SCALAR)
wizard_intro_start_y_pos = GRASS_TOP_Y
wizard_intro_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png").convert_alpha()
wizard_intro_height_by_scale = 96 * WINDOW_SCALAR
wizard_intro_width_by_scale = 96 * WINDOW_SCALAR
wizard_intro_size_by_scale = (wizard_intro_height_by_scale,wizard_intro_width_by_scale)
wizard_intro_surf = pygame.transform.scale(wizard_intro_surf,wizard_intro_size_by_scale)
wizard_intro_rect = wizard_intro_surf.get_rect(midbottom = (wizard_intro_start_x_pos,wizard_intro_start_y_pos))

harold_intro_start_x_pos = WINDOW_WIDTH / 2
harold_intro_start_y_pos = GRASS_TOP_Y + 6/32 * (wizard_intro_width_by_scale * 3/8)
harold_intro_surf = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
harold_intro_height_by_scale = wizard_intro_height_by_scale * 3/8
harold_intro_width_by_scale = wizard_intro_width_by_scale * 3/8
harold_intro_size_by_scale = (harold_intro_height_by_scale,harold_intro_width_by_scale)
harold_intro_surf = pygame.transform.scale(harold_intro_surf,harold_intro_size_by_scale)
harold_intro_surf = pygame.transform.flip(harold_intro_surf,True,False)
harold_intro_rect = harold_intro_surf.get_rect(midbottom = (harold_intro_start_x_pos,harold_intro_start_y_pos))
