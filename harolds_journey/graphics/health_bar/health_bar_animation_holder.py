"""Wizard Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/health_bar/health_bar_animation"

health_bar_arr = [
    pygame.image.load(f"{common_file_path}/green_health_bar.png").convert_alpha(),
    pygame.image.load(f"{common_file_path}/yellow_health_bar.png").convert_alpha(),
    pygame.image.load(f"{common_file_path}/red_health_bar.png").convert_alpha(),
    pygame.image.load(f"{common_file_path}/outline_health_bar.png").convert_alpha(),
]


def get_health_bar_arr():
    return health_bar_arr


def get_green_health_bar():
    return health_bar_arr[0]


def get_yellow_health_bar():
    return health_bar_arr[1]


def get_red_health_bar():
    return health_bar_arr[2]

def get_outline_health_bar():
    return health_bar_arr[3]    