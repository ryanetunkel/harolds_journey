"""Player Class"""
from random import randint, choice

from global_vars import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Start
        self.WIZARD_START_X_POS = WINDOW_WIDTH / 2
        self.WIZARD_START_Y_POS = GRASS_TOP_Y
        
        # X Directions
        self.wizard_x_pos = self.WIZARD_START_X_POS
        self.wizard_speed = 4
        self.wizard_x_velocity = 0
        self.looking_right = True
        self.wizard_moving = False
        
        # Y Directions
        self.wizard_y_pos = self.WIZARD_START_Y_POS
        self.gravity_acceleration = GLOBAL_GRAVITY
        self.gravity_intensity = 1 # How quickly gravity accelerates the player
        self.wizard_jumping = False

        # Fireball
        self.fireball_hit = False
        self.fireball_cooldown_time = 60
        self.current_fireball_cooldown = 0
        self.fireball_shot = False
        self.start_fireball_animation = False
        
        # Additional Score
        self.additional_score = 0
        
        # Death
        self.wizard_dead = False
        self.wizard_start_death = False
        
        # Damage Statistics
        self.WIZARD_STARTING_DAMAGE = 1
        self.wizard_damage_percent = 1
        self.wizard_damage_total = self.WIZARD_STARTING_DAMAGE * self.wizard_damage_percent
        self.WIZARD_STARTING_PIERCING = 1
        self.wizard_piercing_increase = 0
        self.wizard_piercing_total = self.WIZARD_STARTING_PIERCING + self.wizard_piercing_increase

        # Wizard Idle Animation  
        wizard_idle_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png').convert_alpha()
        wizard_idle_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_01.png').convert_alpha()
        wizard_idle_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_02.png').convert_alpha()
        wizard_idle_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_03.png').convert_alpha()
        wizard_idle_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_04.png').convert_alpha()
        wizard_idle_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_05.png').convert_alpha()
        wizard_idle_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_06.png').convert_alpha()
        wizard_idle_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_07.png').convert_alpha()
        wizard_idle_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_08.png').convert_alpha()
        wizard_idle_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_09.png').convert_alpha()
        wizard_idle_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_10.png').convert_alpha()
        wizard_idle_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_11.png').convert_alpha()
        wizard_idle_12 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_12.png').convert_alpha()
        wizard_idle_13 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_13.png').convert_alpha()
        wizard_idle_14 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_14.png').convert_alpha()
        wizard_idle_15 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_15.png').convert_alpha()
        wizard_idle_16 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_16.png').convert_alpha()
        wizard_idle_17 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_17.png').convert_alpha()
        wizard_idle_18 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_18.png').convert_alpha()
        wizard_idle_19 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_19.png').convert_alpha()
        wizard_idle_20 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_20.png').convert_alpha()
        wizard_idle_21 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_21.png').convert_alpha()
        wizard_idle_22 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_22.png').convert_alpha()
        wizard_idle_23 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_23.png').convert_alpha()
        self.wizard_idle = [wizard_idle_00, wizard_idle_01, wizard_idle_02, wizard_idle_03,
                    wizard_idle_04, wizard_idle_05, wizard_idle_06, wizard_idle_07,
                    wizard_idle_08, wizard_idle_09, wizard_idle_10, wizard_idle_11,
                    wizard_idle_12, wizard_idle_13, wizard_idle_14, wizard_idle_15,
                    wizard_idle_16, wizard_idle_17, wizard_idle_18, wizard_idle_19,
                    wizard_idle_20, wizard_idle_21, wizard_idle_22, wizard_idle_23]

        # Wizard Secret Idle Animation
        wizard_secret_idle_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_00.png').convert_alpha()
        wizard_secret_idle_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_01.png').convert_alpha()
        wizard_secret_idle_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_02.png').convert_alpha()
        wizard_secret_idle_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_03.png').convert_alpha()
        wizard_secret_idle_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_04.png').convert_alpha()
        wizard_secret_idle_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_05.png').convert_alpha()
        wizard_secret_idle_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_06.png').convert_alpha()
        wizard_secret_idle_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_07.png').convert_alpha()
        wizard_secret_idle_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_08.png').convert_alpha()
        wizard_secret_idle_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_09.png').convert_alpha()
        wizard_secret_idle_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_10.png').convert_alpha()
        wizard_secret_idle_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_11.png').convert_alpha()
        wizard_secret_idle_12 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_12.png').convert_alpha()
        wizard_secret_idle_13 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_13.png').convert_alpha()
        wizard_secret_idle_14 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_14.png').convert_alpha()
        wizard_secret_idle_15 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_15.png').convert_alpha()
        wizard_secret_idle_16 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_16.png').convert_alpha()
        wizard_secret_idle_17 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_17.png').convert_alpha()
        wizard_secret_idle_18 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_18.png').convert_alpha()
        wizard_secret_idle_19 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_19.png').convert_alpha()
        wizard_secret_idle_20 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_20.png').convert_alpha()
        wizard_secret_idle_21 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_21.png').convert_alpha()
        wizard_secret_idle_22 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_22.png').convert_alpha()
        wizard_secret_idle_23 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_secret_idle_animation/wizard_secret_idle_23.png').convert_alpha()
        self.wizard_secret_idle = [wizard_secret_idle_00, wizard_secret_idle_01, wizard_secret_idle_02, wizard_secret_idle_03,
                            wizard_secret_idle_04, wizard_secret_idle_05, wizard_secret_idle_06, wizard_secret_idle_07,
                            wizard_secret_idle_08, wizard_secret_idle_09, wizard_secret_idle_10, wizard_secret_idle_11,
                            wizard_secret_idle_12, wizard_secret_idle_13, wizard_secret_idle_14, wizard_secret_idle_15,
                            wizard_secret_idle_16, wizard_secret_idle_17, wizard_secret_idle_18, wizard_secret_idle_19,
                            wizard_secret_idle_20, wizard_secret_idle_21, wizard_secret_idle_22, wizard_secret_idle_23]

        # Wizard Walk Animation
        wizard_walk_0 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_0.png').convert_alpha()
        wizard_walk_1 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_1.png').convert_alpha()
        wizard_walk_2 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_2.png').convert_alpha()
        wizard_walk_3 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_3.png').convert_alpha()
        wizard_walk_4 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_4.png').convert_alpha()
        wizard_walk_5 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_5.png').convert_alpha()
        wizard_walk_6 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_6.png').convert_alpha()
        wizard_walk_7 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_7.png').convert_alpha()
        self.wizard_walk = [wizard_walk_0, wizard_walk_1, wizard_walk_2, wizard_walk_3,
                    wizard_walk_4, wizard_walk_5, wizard_walk_6, wizard_walk_7]

        # Wizard Jump Animation
        # Ascending
        wizard_jump_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_00.png').convert_alpha()
        wizard_jump_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_01.png').convert_alpha()
        wizard_jump_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_02.png').convert_alpha()
        wizard_jump_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_03.png').convert_alpha()
        wizard_jump_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_04.png').convert_alpha()
        wizard_jump_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_05.png').convert_alpha()
        wizard_jump_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_06.png').convert_alpha()
        wizard_jump_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_07.png').convert_alpha()
        # Top of Jump
        wizard_jump_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_08.png').convert_alpha()
        wizard_jump_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_09.png').convert_alpha()
        wizard_jump_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_10.png').convert_alpha()
        wizard_jump_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_11.png').convert_alpha()
        wizard_jump_12 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_12.png').convert_alpha()
        wizard_jump_13 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_13.png').convert_alpha()
        wizard_jump_14 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_14.png').convert_alpha()
        # Descending
        wizard_jump_15 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_15.png').convert_alpha()
        wizard_jump_16 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_16.png').convert_alpha()
        wizard_jump_17 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_17.png').convert_alpha()
        wizard_jump_18 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_18.png').convert_alpha()
        wizard_jump_19 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_19.png').convert_alpha()
        wizard_jump_20 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_20.png').convert_alpha()
        wizard_jump_21 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_21.png').convert_alpha()
        wizard_jump_22 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_22.png').convert_alpha()
        wizard_jump_23 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_jump_animation/wizard_jump_23.png').convert_alpha()
        self.wizard_jump = [wizard_jump_00, wizard_jump_01, wizard_jump_02, wizard_jump_03,
                    wizard_jump_04, wizard_jump_05, wizard_jump_06, wizard_jump_07,
                    wizard_jump_08, wizard_jump_09, wizard_jump_10, wizard_jump_11,
                    wizard_jump_12, wizard_jump_13, wizard_jump_14, wizard_jump_15,
                    wizard_jump_16, wizard_jump_17, wizard_jump_18, wizard_jump_19,
                    wizard_jump_20, wizard_jump_21, wizard_jump_22, wizard_jump_23]

        # Wizard Fireball Animation
        wizard_fireball_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_00.png').convert_alpha()
        wizard_fireball_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_01.png').convert_alpha()
        wizard_fireball_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_02.png').convert_alpha()
        wizard_fireball_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_03.png').convert_alpha()
        wizard_fireball_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_04.png').convert_alpha()
        wizard_fireball_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_05.png').convert_alpha()
        wizard_fireball_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_06.png').convert_alpha()
        wizard_fireball_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_07.png').convert_alpha()
        wizard_fireball_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_08.png').convert_alpha()
        wizard_fireball_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_09.png').convert_alpha()
        wizard_fireball_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_10.png').convert_alpha()
        wizard_fireball_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_fireball_animation/wizard_fireball_11.png').convert_alpha()
        self.wizard_fireball = [wizard_fireball_00, wizard_fireball_01, wizard_fireball_02, wizard_fireball_03,
                        wizard_fireball_04, wizard_fireball_05, wizard_fireball_06, wizard_fireball_07,
                        wizard_fireball_08, wizard_fireball_09, wizard_fireball_10, wizard_fireball_11]

        # Wizard Death Animation
        wizard_death_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_00.png').convert_alpha()
        wizard_death_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_01.png').convert_alpha()
        wizard_death_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_02.png').convert_alpha()
        wizard_death_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_03.png').convert_alpha()
        wizard_death_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_04.png').convert_alpha()
        wizard_death_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_05.png').convert_alpha()
        wizard_death_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_06.png').convert_alpha()
        wizard_death_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_07.png').convert_alpha()
        wizard_death_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_08.png').convert_alpha()
        wizard_death_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_09.png').convert_alpha()
        wizard_death_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_10.png').convert_alpha()
        wizard_death_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_11.png').convert_alpha()
        wizard_death_12 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_12.png').convert_alpha()
        wizard_death_13 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_13.png').convert_alpha()
        wizard_death_14 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_14.png').convert_alpha()
        wizard_death_15 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_15.png').convert_alpha()
        wizard_death_16 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_16.png').convert_alpha()
        wizard_death_17 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_17.png').convert_alpha()
        wizard_death_18 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_18.png').convert_alpha()
        wizard_death_19 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_19.png').convert_alpha()
        wizard_death_20 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_20.png').convert_alpha()
        wizard_death_21 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_21.png').convert_alpha()
        wizard_death_22 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_22.png').convert_alpha()
        wizard_death_23 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_23.png').convert_alpha()
        wizard_death_24 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_24.png').convert_alpha()
        wizard_death_25 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_25.png').convert_alpha()
        wizard_death_26 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_26.png').convert_alpha()
        wizard_death_27 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_death_animation/wizard_death_27.png').convert_alpha()
        self.wizard_death = [wizard_death_00, wizard_death_01, wizard_death_02, wizard_death_03,
                    wizard_death_04, wizard_death_05, wizard_death_06, wizard_death_07,
                    wizard_death_08, wizard_death_09, wizard_death_10, wizard_death_11,
                    wizard_death_12, wizard_death_13, wizard_death_14, wizard_death_15,
                    wizard_death_16, wizard_death_17, wizard_death_18, wizard_death_19,
                    wizard_death_20, wizard_death_21, wizard_death_22, wizard_death_23,
                    wizard_death_24, wizard_death_25, wizard_death_26, wizard_death_27]

        self.wizard_index = 0
        self.image = self.wizard_walk[self.wizard_index]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        self.rect = self.image.get_rect(midbottom = (self.wizard_x_pos,self.wizard_y_pos))
        self.wizard_gravity = 0

        # Animation Speeds
        self.WIZARD_WALK_ANIMATION_SPEED = 0.1
        self.WIZARD_JUMP_ANIMATION_SPEED = 0.075
        self.WIZARD_IDLE_ANIMATION_SPEED = 0.1
        self.WIZARD_FIREBALL_ANIMATION_SPEED = 0.4
        self.WIZARD_DEATH_ANIMATION_SPEED = 0.2
        
        # Secret Animation
        self.wizard_secret_idle_animation_speed = self.WIZARD_IDLE_ANIMATION_SPEED
        self.WIZARD_SECRET_ANIMATION_LIMIT = 240
        self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT

        # Sounds
        self.jump_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/Bounce Jump/Retro Jump Classic 08.wav')
        self.jump_sound.set_volume(JUMP_SOUND_VOLUME)
        self.fireball_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/Blops/Retro Blop 07.wav')
        self.fireball_sound.set_volume(FIREBALL_SOUND_VOLUME)
        self.walk_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/FootStep/Retro FootStep Grass 01.wav')
        self.walk_sound.set_volume(WALK_SOUND_VOLUME)
        self.walk_sound_length = 1 * 40
        self.walk_sound_timer = self.walk_sound_length
        self.secret_sound = pygame.mixer.Sound('Harold\'s Journey/audio/FreeSFX/GameSFX/PowerUp/Retro PowerUP 09.wav')
        self.secret_sound.set_volume(SECRET_SOUND_VOLUME)
        self.secret_sound_timer = 0
        self.secret_sound_length = self.WIZARD_SECRET_ANIMATION_LIMIT
        # self.death_sound = pygame.mixer.Sound('placeholder') # Find Death Sound

    # Positions
    def get_wizard_pos(self):
        return (self.wizard_x_pos,self.wizard_y_pos)
    
    def set_wizard_x_pos(self,new_wizard_x_pos):
        self.wizard_x_pos = new_wizard_x_pos

    def get_wizard_y_pos(self):
        return self.wizard_y_pos
    
    def set_wizard_y_pos(self,new_wizard_y_pos):
        self.wizard_y_pos = new_wizard_y_pos

    def get_wizard_start_x_pos(self):
        return self.WIZARD_START_X_POS
    
    def set_wizard_start_x_pos(self,new_wizard_start_x_pos):
        self.WIZARD_START_X_POS = new_wizard_start_x_pos
    
    def get_wizard_start_y_pos(self):
        return self.WIZARD_START_Y_POS
    
    def set_wizard_start_y_pos(self,new_wizard_start_y_pos):
        self.WIZARD_START_Y_POS = new_wizard_start_y_pos

    # Rects and Images
    def get_wizard_rect(self):
        return self.rect
    
    def set_wizard_rect(self,new_rect):
        self.rect = new_rect
    
    def get_wizard_image(self):
        return self.image
    
    def set_wizard_image(self,new_image):
        self.image = new_image
    
    # Speed
    def get_wizard_speed(self):
        return self.wizard_speed

    def set_wizard_speed(self,new_wizard_speed):
        self.wizard_speed = new_wizard_speed

    # Looking Right
    def get_looking_right(self):
        return self.looking_right
    
    # Fireball Stats
    def get_current_fireball_cooldown(self):
        return self.current_fireball_cooldown

    def set_current_fireball_cooldown(self,new_fireball_cooldown):
        self.current_fireball_cooldown = new_fireball_cooldown
    
    def get_fireball_cooldown_time(self):
        return self.fireball_cooldown_time
    
    def set_fireball_cooldown_time(self,new_fireball_cooldown_time):
        self.fireball_cooldown_time = new_fireball_cooldown_time
    
    # X Velocity
    def get_wizard_x_velocity(self):
        return self.wizard_x_velocity
    
    def set_wizard_x_velocity(self,new_wizard_x_velocity):
        self.wizard_x_velocity = new_wizard_x_velocity

    # Gravity Stats
    def get_wizard_gravity(self):
        return self.wizard_gravity
    
    def set_wizard_gravity(self,new_wizard_gravity):
        self.wizard_gravity = new_wizard_gravity

    def get_gravity_acceleration(self):
        return self.gravity_acceleration
    
    def set_gravity_acceleration(self,new_gravity_acceleration):
        self.gravity_acceleration = new_gravity_acceleration

    def get_fireball_hit(self):
        return self.fireball_hit
    
    def set_fireball_hit(self,new_fireball_hit):
        self.fireball_hit = new_fireball_hit
        
    def get_fireball_shot(self):
        return self.fireball_shot

    def set_fireball_shot(self,new_fireball_shot):
        self.fireball_shot = new_fireball_shot
    
    def play_fireball_sound(self):
        pygame.mixer.Channel(FIREBALL_SOUND_CHANNEL).play(self.fireball_sound)
    
    # Wizard Moving
    def get_wizard_moving(self):
        return self.wizard_moving

    def set_wizard_moving(self,new_wizard_moving):
        self.wizard_moving = new_wizard_moving
    
    # Wizard Jumping
    def get_wizard_jumping(self):
        return self.wizard_jumping
    
    def set_wizard_jumping(self,new_wizard_jumping):
        self.wizard_jumping = new_wizard_jumping
    
    # Score
    def get_additional_score(self):
        return self.additional_score

    def set_additional_score(self,new_additional_score):
        self.additional_score = new_additional_score

    # Death
    def get_wizard_dead(self):
        return self.wizard_dead
    
    def set_wizard_dead(self,new_wizard_dead):
        self.wizard_dead = new_wizard_dead
    
    # Wizard Game Stats
    # Damage    
    def get_wizard_damage_percent(self):
        return self.wizard_damage_percent
    
    def set_wizard_damage_percent(self,new_wizard_damage_percent):
        self.wizard_damage_percent = new_wizard_damage_percent
        
    def get_wizard_damage_total(self):
        return self.wizard_damage_total
    
    def set_wizard_damage_total(self,new_wizard_damage_total):
        self.wizard_damage_total = new_wizard_damage_total
    
    def calculate_wizard_damage(self):
        temp_percent = self.get_wizard_damage_percent()
        temp_total = self.WIZARD_STARTING_DAMAGE * temp_percent
        self.set_wizard_damage_total(temp_total)
    # Piercing    
    def get_wizard_piercing_increase(self):
        return self.wizard_piercing_increase
    
    def set_wizard_piercing_increase(self,new_wizard_piercing_increase):
        self.wizard_piercing_increase = new_wizard_piercing_increase
        
    def get_wizard_piercing_total(self):
        return self.wizard_piercing_total
    
    def set_wizard_piercing_total(self,new_wizard_piercing_total):
        self.wizard_piercing_total = new_wizard_piercing_total
    
    def calculate_wizard_piercing(self):
        temp_increase = self.get_wizard_piercing_increase()
        temp_total = self.WIZARD_STARTING_PIERCING * temp_increase
        self.set_wizard_piercing_total(temp_total)
    
    def calculate_wizard_stats(self):
        self.calculate_wizard_damage()
        self.calculate_wizard_piercing()

    def wizard_input(self):
        keys = pygame.key.get_pressed()
        if not self.wizard_dead:
            if keys[jump_button] and self.rect.bottom >= GRASS_TOP_Y:
                self.wizard_jumping = True
                self.wizard_gravity = self.gravity_acceleration
                # Jump Sound
                pygame.mixer.Channel(JUMP_SOUND_CHANNEL).play(self.jump_sound)
            if keys[right_button] and self.rect.x + WIZARD_WIDTH + self.wizard_speed < WINDOW_WIDTH:
                self.wizard_x_velocity = self.wizard_speed
                self.rect.x += self.wizard_x_velocity
                self.wizard_moving = True
            if keys[left_button] and self.rect.x - self.wizard_speed > 0:
                self.wizard_x_velocity = self.wizard_speed
                self.rect.x -= self.wizard_x_velocity
                self.wizard_moving = True
            elif (not keys[left_button] and not keys[right_button] and not keys[jump_button]): 
                self.wizard_x_velocity = 0
                self.wizard_moving = False
                self.wizard_jumping = False
            if self.wizard_moving and self.rect.bottom >= GRASS_TOP_Y and self.walk_sound_timer >= self.walk_sound_length:
                # Walk Sound
                pygame.mixer.Channel(WALK_SOUND_CHANNEL).play(self.walk_sound)
                self.walk_sound_timer = 0
            if self.walk_sound_timer < self.walk_sound_length:
                self.walk_sound_timer += 1
        
    def apply_gravity(self):
        self.wizard_gravity += self.gravity_intensity
        self.rect.y += self.wizard_gravity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y
        
    def animation_state(self):
        if not self.wizard_dead:
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            self.looking_right = mouse_x >= self.rect.centerx
            if self.fireball_shot:
                # wizard fireball animation
                if self.start_fireball_animation:
                    self.wizard_index = 0
                    self.start_fireball_animation = False
                self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT
                self.secret_sound_timer = 0
                self.wizard_index += self.WIZARD_FIREBALL_ANIMATION_SPEED # speed of animation, adjust as needed
                if self.wizard_index >= len(self.wizard_fireball): 
                    self.wizard_index = 0
                    self.start_fireball_animation = True
                    self.fireball_shot = False
                self.image = self.wizard_fireball[int(self.wizard_index)]
            elif self.rect.bottom < GRASS_TOP_Y and self.wizard_jumping: # and add landing tracker this would be if it is off
                # jump (first half)
                self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT
                self.secret_sound_timer = 0
                self.wizard_index += self.WIZARD_JUMP_ANIMATION_SPEED # speed of animation, adjust as needed
                if self.wizard_index >= len(self.wizard_jump): self.wizard_index = 0
                self.image = self.wizard_jump[int(self.wizard_index)]
                # this is it raw with no adjustment
                # below is the ideal
                # wizard_surf = wizard_jump[0,7] # can't just do this need to go through
                # 8 - 14 need to be when reach peak, prob cut and edit which goes where
                # and add landing tracker this would be if landed
                # landing animation for a few frames via timer and then when ends revert to idle
            elif self.wizard_moving and self.rect.bottom >= GRASS_TOP_Y:
                self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT
                self.wizard_jumping = False
                self.secret_sound_timer = 0
                self.wizard_index += self.WIZARD_WALK_ANIMATION_SPEED # speed of animation, adjust as needed
                if self.wizard_index >= len(self.wizard_walk): self.wizard_index = 0
                self.image = self.wizard_walk[int(self.wizard_index)]
            elif not self.wizard_moving and self.rect.bottom >= GRASS_TOP_Y:
                self.wizard_jumping = False
                if self.wizard_secret_animation_timer != 0:
                    self.wizard_index += self.WIZARD_IDLE_ANIMATION_SPEED # speed of animation, adjust as needed
                    if self.wizard_index >= len(self.wizard_idle): self.wizard_index = 0
                    self.image = self.wizard_idle[int(self.wizard_index)]
                    # idle animation
                    # start timer that last for a few rounds of idle animation until would do the second
                    self.wizard_secret_animation_timer -= 1
                else:
                    self.wizard_index += self.wizard_secret_idle_animation_speed # speed of animation, adjust as needed
                    if self.wizard_index >= len(self.wizard_secret_idle): self.wizard_index = 0
                    self.image = self.wizard_secret_idle[int(self.wizard_index)]
                    
                    if self.secret_sound_timer >= self.secret_sound_length:
                        # Secret Sound - Plays too much, look at how secret_sound_timer and secret_sound_limit work together
                        # Should work as timer counts up to limit, plays song, resets to 0, begins counting up again
                        # Want the sound to play at the end of the animation, seems to play from beginning to end every frame-ish
                        pygame.mixer.Channel(SECRET_SOUND_CHANNEL).play(self.secret_sound)
                        self.secret_sound_timer = 0
                    if self.secret_sound_timer < self.secret_sound_length:
                        self.secret_sound_timer += 1
        else:
            if not self.wizard_start_death:
                self.wizard_index = 0
                self.wizard_start_death = True
            self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT
            if self.wizard_index + self.WIZARD_DEATH_ANIMATION_SPEED < len(self.wizard_death):
                self.wizard_index += self.WIZARD_DEATH_ANIMATION_SPEED
            self.image = self.wizard_death[int(self.wizard_index)]
        
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        
        if not self.looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        # Death animation if game was ended - rn game ends instantly so can't be implemented
        # Damage animation if hit and not killed - rn can't do cuz no health

    def fireball_timer_tick(self):
        if self.current_fireball_cooldown > 0:
            self.current_fireball_cooldown -= 1            

    def update(self):
        self.wizard_input()
        self.apply_gravity()
        self.animation_state()
        self.fireball_timer_tick()
        self.calculate_wizard_stats()
    
    def reset(self):
        # X Directions
        self.wizard_x_pos = self.WIZARD_START_X_POS
        self.wizard_speed = 4
        self.wizard_x_velocity = 0
        self.looking_right = True
        self.wizard_moving = False
        
        # Y Directions
        self.wizard_y_pos = self.WIZARD_START_Y_POS
        self.gravity_acceleration = GLOBAL_GRAVITY
        self.gravity_intensity = 1 # How quickly gravity accelerates the player
        self.wizard_jumping = False

        # Fireball
        self.fireball_hit = False
        self.fireball_cooldown_time = 60
        self.current_fireball_cooldown = 0
        self.fireball_shot = False
        self.start_fireball_animation = False
        
        # Additional Score
        self.additional_score = 0
        
        # Death
        self.wizard_dead = False
        self.wizard_start_death = False
        
        # Damage Statistics
        self.WIZARD_STARTING_DAMAGE = 1
        self.wizard_damage_percent = 1
        self.wizard_damage_total = self.WIZARD_STARTING_DAMAGE * self.wizard_damage_percent
        self.WIZARD_STARTING_PIERCING = 1
        self.wizard_piercing_increase = 0
        self.wizard_piercing = self.WIZARD_STARTING_PIERCING + self.wizard_piercing_increase
        
        # Secret Animation
        self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT
        
        # Wizard Index
        self.wizard_index = 0
        self.image = self.wizard_walk[self.wizard_index]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        self.rect = self.image.get_rect(midbottom = (self.wizard_x_pos,self.wizard_y_pos))
        
        # Sounds
        self.walk_sound_length = 1 * 40
        self.walk_sound_timer = self.walk_sound_length
        self.secret_sound_timer = 0
        self.secret_sound_length = self.WIZARD_SECRET_ANIMATION_LIMIT # gives exact time for animation to play once
