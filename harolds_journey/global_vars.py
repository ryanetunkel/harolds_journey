"""Global Variables"""

import pygame

from controls import *

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

screenInfo = pygame.display.Info()
window_width = 800 * 3/2
window_height = 400 * 3/2
min_window_width = 320
min_window_height = 240
max_window_width = screenInfo.current_w
max_window_height = screenInfo.current_h
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 400
PIXEL_SIZE = 2 # Create a slider for this - will be zoom essentially.
# PIXEL_SIZE currently can only be even numbers else creates .5 addition and rects can only do integer-based moves
# Will need to transition to using math.Vector2 to do all collision and stuff and then render it after as a rect to get subpixel movement
GLOBAL_SCALAR = PIXEL_SIZE/4
window_size = (window_width,window_height) # Create a set of options for this, fullscreen maybe in future, gets tricky
window_scalar = ((window_width + window_height)/1200)
WIZARD_WIDTH = 32 * PIXEL_SIZE
WIZARD_HEIGHT = 32 * PIXEL_SIZE
WIZARD_PIXEL_SIZE = (WIZARD_HEIGHT,WIZARD_WIDTH)
grass_top_y = int((379 / 400) * window_height)
GLOBAL_GRAVITY = 1 * GLOBAL_SCALAR
OBSTACLE_SPAWN_FREQUENCY = 1500 # In milliseconds, 1000 = 1 sec, should be 1500
FPS = 60

screen = pygame.display.set_mode(window_size,pygame.RESIZABLE)
pygame.display.set_caption("Harold\'s Journey")
pygame_icon = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",50)
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

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)

jump_button,jump_button_is_mouse = get_control("jump_button")
left_button,left_button_is_mouse = get_control("left_button")
right_button,right_button_is_mouse = get_control("right_button")
shoot_button,shoot_button_is_mouse = get_control("shoot_button")

can_edit_controls = False


def set_game_active(new_game_active:bool):
    global game_active
    game_active = new_game_active


def set_wizard_alive(new_wizard_alive:bool):
    global wizard_alive
    wizard_alive = new_wizard_alive


def set_start_time(new_start_time:int):
    global start_time
    start_time = new_start_time
