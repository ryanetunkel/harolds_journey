import pygame

from controls import *

pygame.init()

edited_options_file_dict = get_edited_options_file_dict()

# Window
# Min and Max
screenInfo = pygame.display.Info()
min_window_width = 320
min_window_height = 240
max_window_width = screenInfo.current_w
max_window_height = screenInfo.current_h
# Width, Height, and Size
window_width = edited_options_file_dict.get("window_width") # 800 * 3/2 = 1200
window_height = edited_options_file_dict.get("window_height")  # 400 * 3/2 = 600
window_width = max(window_width,min_window_width)
window_width = min(window_width,max_window_width)
window_height = max(window_height,min_window_height)
window_height = min(window_height,max_window_height)
screen = pygame.display.set_mode((window_width,window_height),pygame.RESIZABLE)
window_width = screen.get_width()
window_height = screen.get_height()
edited_options_file_dict.update({"window_width":window_width})
edited_options_file_dict.update({"window_height":window_height})
# Global Variables
center_screen_width = window_width / 2
center_screen_height = window_height / 2

# Surface Sizing
pixel_size = edited_options_file_dict.get("pixel_size") # can be 1
zoom = edited_options_file_dict.get("zoom")
zoom_x_limit = center_screen_width / 2
zoom_y_limit = center_screen_height / 2
# PIXEL_SIZE currently can only be even numbers else creates .5 addition and rects can only do integer-based moves
# Will need to transition to using math.Vector2 to do all collision and stuff and then render it after as a rect to get subpixel movement

# Framerate
fps = edited_options_file_dict.get("fps")

# Update
set_edited_options_file_dict(edited_options_file_dict)
