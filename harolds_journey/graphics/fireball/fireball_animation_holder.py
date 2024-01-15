"""Projectile Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/fireball"
fireball_movement_arr = []
fireball_transition_arr = []

fireball_animations = {
    "movement": [fireball_movement_arr, 4],
    "transition": [fireball_transition_arr, 4],
}


for keyword,arr_info in fireball_animations.items():
    arr = arr_info[0]
    arr_length = arr_info[1]
    for idx in range(arr_length):
        arr.append(pygame.image.load(f"{common_file_path}/fireball_{keyword}_animation/fireball_{keyword}_{idx:02d}.png").convert_alpha())


def get_fireball_movement_arr():
    return fireball_movement_arr


def get_fireball_transition_arr():
    return fireball_transition_arr


def get_harold_animations():
    return fireball_animations
