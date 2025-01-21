"""Global Variables"""

import pygame

from controls import *
from menu_vars import *

# Sounds
BG_MUSIC_VOLUME = 0.4
FIREBALL_SOUND_VOLUME = 0.2
WALK_SOUND_VOLUME = 0.3
JUMP_SOUND_VOLUME = 0.3
OBSTACLE_DEATH_VOLUME = 0.2
OBSTACLE_MOVE_VOLUME = 0.2
SECRET_SOUND_VOLUME = 0.6

# Channels
BG_MUSIC_CHANNEL = 0
FIREBALL_SOUND_CHANNEL = 1
WALK_SOUND_CHANNEL = 2
JUMP_SOUND_CHANNEL = 3
OBSTACLE_DEATH_CHANNEL = 4
OBSTACLE_MOVE_CHANNEL = 5
SECRET_SOUND_CHANNEL = 7

# Score
score = 0

pygame.init()
window_size = (window_width,window_height)
global_scalar = pixel_size/4
wizard_width = 32 * pixel_size
wizard_height = 32 * pixel_size
wizard_pixel_size = (wizard_height,wizard_width)
global_gravity = 1 * global_scalar
OBSTACLE_SPAWN_FREQUENCY = 1500 # In milliseconds, 1000 = 1 sec, should be 1500

pygame.display.set_caption("Harold\'s Journey")
pygame_icon = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",int(window_height/16))
game_active = False
intro_played = False
wizard_alive = False
start_time = 0
pause_time = 0
death_timer = 0

# Music
bg_music = pygame.mixer.Sound("harolds_journey/audio/FreeSFX/GameSFX/Ambience/Retro Ambience Short 09.wav")
bg_music.set_volume(BG_MUSIC_VOLUME)
bg_music_timer = 0
# Global Sounds
obstacle_death_sound = pygame.mixer.Sound("harolds_journey/audio/FreeSFX/GameSFX/Explosion/Retro Explosion Short 01.wav")
obstacle_death_sound.set_volume(OBSTACLE_DEATH_VOLUME)

# Sprites
wizard = pygame.sprite.GroupSingle()
harold = pygame.sprite.GroupSingle()

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


# Background Elements
bg_image_path = "harolds_journey/graphics/bg_images/Background.png"
bg_surf = pygame.image.load(bg_image_path).convert_alpha()
bg_height = bg_surf.get_height()  # 640
bg_width = bg_surf.get_width()  # 640
bg_height_scalar = window_height / bg_height  # WINDOW_HEIGHT = 400 * 3/2 / 640 = 600 / 640 = 60/64
bg_width_scalar = window_width / bg_width  # WINDOW_WIDTH = 800 * 3/2 / 640 = 1200 / 640 = 120/64
if window_width > bg_width or window_height > bg_height: # WINDOW_WIDTH > bg_width
    bg_scalar = bg_width_scalar if bg_width_scalar >= bg_height_scalar else bg_height_scalar
    bg_surf = pygame.transform.scale_by(bg_surf,bg_scalar) # bg_scalar = bg_width_scalar = 120/64
else:
    bg_scalar = 1

grass_top_y = int((628/640) * window_height) # Grass at 12/640 pixels when full size, 640-12=268

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)

jump_button,jump_button_is_mouse = get_control("jump_button")
left_button,left_button_is_mouse = get_control("left_button")
right_button,right_button_is_mouse = get_control("right_button")
shoot_button,shoot_button_is_mouse = get_control("shoot_button")

can_edit_controls = False
