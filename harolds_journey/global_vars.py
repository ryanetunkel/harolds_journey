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
# Experimental - works though if do this, take out other WINDOW_WIDTH and HEIGHT, and take out other screen
# screenInfo = pygame.display.Info()
# screen = pygame.display.set_mode((screenInfo.current_w, screenInfo.current_h))
# WINDOW_WIDTH = screenInfo.current_w
# WINDOW_HEIGHT = screenInfo.current_h

WINDOW_WIDTH = 800 * 3/2
WINDOW_HEIGHT = 400 * 3/2
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 400
PIXEL_SIZE = 2 # Create a slider for this - will be zoom essentially.
# PIXEL_SIZE currently can only be even numbers else creates .5 addition and rects can only do integer-based moves
# Will need to transition to using math.Vector2 to do all collision and stuff and then render it after as a rect to get subpixel movement
GLOBAL_SCALAR = PIXEL_SIZE/4
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT) # Create a set of options for this, fullscreen maybe in future, gets tricky
WINDOW_SCALAR = ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
WIZARD_WIDTH = 32 * PIXEL_SIZE
WIZARD_HEIGHT = 32 * PIXEL_SIZE
WIZARD_PIXEL_SIZE = (WIZARD_HEIGHT,WIZARD_WIDTH)
GRASS_TOP_Y = int((379 / 400) * WINDOW_HEIGHT)
GLOBAL_GRAVITY = 1 * GLOBAL_SCALAR
OBSTACLE_SPAWN_FREQUENCY = 1500 # In milliseconds, 1000 = 1 sec, should be 1500

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Harold\'s Journey")
pygame_icon = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",50)
game_active = False
intro_played = False
wizard_alive = False
start_time = 0
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
bg_surf = pygame.image.load("harolds_journey/graphics/bg_images/Background.png").convert_alpha()
bg_height = bg_surf.get_height()
bg_width = bg_surf.get_width()
bg_height_scalar = WINDOW_HEIGHT / bg_height
bg_width_scalar = WINDOW_WIDTH / bg_width
if WINDOW_WIDTH > bg_width or WINDOW_HEIGHT > bg_height:
    bg_scalar = bg_width_scalar if bg_width_scalar >= bg_height_scalar else bg_height_scalar
    bg_surf = pygame.transform.scale_by(bg_surf,bg_scalar)


# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,OBSTACLE_SPAWN_FREQUENCY)

jump_button,jump_button_is_mouse = get_control("jump_button")
left_button,left_button_is_mouse = get_control("left_button")
right_button,right_button_is_mouse = get_control("right_button")
shoot_button,shoot_button_is_mouse = get_control("shoot_button")

can_edit_controls = False
