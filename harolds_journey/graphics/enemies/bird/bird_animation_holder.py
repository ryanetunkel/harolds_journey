"""Bird Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/enemies/bird"
bird_fly_arr = []

bird_animations = {
    "fly": [bird_fly_arr, 12],
}


for keyword,arr_info in bird_animations.items():
    arr = arr_info[0]
    arr_length = arr_info[1]
    for idx in range(arr_length):
        arr.append(pygame.image.load(f"{common_file_path}/bird_{keyword}_animation/bird_{keyword}_{idx:02d}.png").convert_alpha())


def get_bird_fly_arr():
    return bird_fly_arr


def get_bird_animations():
    return bird_animations
