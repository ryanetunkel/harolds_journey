"""Skeleton Animation Holder"""
import pygame


common_file_path = "harolds_journey/graphics/enemies/skeleton"
skeleton_walk_arr = []

skeleton_animations = {
    "walk": [skeleton_walk_arr, 12],
}


for keyword,arr_info in skeleton_animations.items():
    arr = arr_info[0]
    arr_length = arr_info[1]
    for idx in range(arr_length):
        arr.append(pygame.image.load(f"{common_file_path}/skeleton_{keyword}_animation/skeleton_{keyword}_{idx:02d}.png").convert_alpha())


def get_skeleton_walk_arr():
    return skeleton_walk_arr


def get_skeleton_animations():
    return skeleton_animations
