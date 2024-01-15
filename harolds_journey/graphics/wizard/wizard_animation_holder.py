"""Wizard Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/wizard"
wizard_death_arr = []
wizard_fireball_arr = []
wizard_idle_arr = []
wizard_jump_arr = []
wizard_secret_idle_arr = []
wizard_walk_arr = []

wizard_animations = {
    "death": [wizard_death_arr, 28],
    "fireball": [wizard_fireball_arr, 12],
    "idle": [wizard_idle_arr, 24],
    "jump": [wizard_jump_arr, 24],
    "secret_idle": [wizard_secret_idle_arr, 24],
    "walk": [wizard_walk_arr, 8],
}


for keyword,arr_info in wizard_animations.items():
    arr = arr_info[0]
    arr_length = arr_info[1]
    for idx in range(arr_length):
        arr.append(pygame.image.load(f"{common_file_path}/wizard_{keyword}_animation/wizard_{keyword}_{idx:02d}.png").convert_alpha())


def get_wizard_death_arr():
    return wizard_death_arr


def get_wizard_fireball_arr():
    return wizard_fireball_arr


def get_wizard_idle_arr():
    return wizard_idle_arr


def get_wizard_jump_arr():
    return wizard_jump_arr


def get_wizard_secret_idle_arr():
    return wizard_secret_idle_arr


def get_wizard_walk_arr():
    return wizard_walk_arr


def get_wizard_animations():
    return wizard_animations
