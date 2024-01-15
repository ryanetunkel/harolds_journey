"""Harold Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/harold"
harold_idle_arr = []

harold_animations = {
    "idle": [harold_idle_arr, 8],
}


for keyword,arr_info in harold_animations.items():
    arr = arr_info[0]
    arr_length = arr_info[1]
    for idx in range(arr_length):
        arr.append(pygame.image.load(f"{common_file_path}/harold_{keyword}_animation/harold_{keyword}_{idx:02d}.png").convert_alpha())


def get_harold_idle_arr():
    return harold_idle_arr


def get_harold_animations():
    return harold_animations
