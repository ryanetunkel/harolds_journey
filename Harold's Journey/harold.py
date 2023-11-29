"""Harold Class"""
from random import randint, choice

from global_vars import *
from player import *


class Harold(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        
        # Temp Wizard Attribute
        self.player = player
        temp_wizard_rect = self.player.sprite.get_wizard_rect()
        
        # Harold Start
        self.harold_start_x_pos = temp_wizard_rect.centerx
        self.harold_start_y_pos = temp_wizard_rect.top + 28 # pixels at this scale based on wizard are 4 pixels each
        
        # Harold X Values
        self.harold_x_pos = self.harold_start_x_pos
        self.harold_speed = self.player.sprite.get_wizard_speed()
        self.harold_x_velocity = 0
        
        # Harold Y Values
        self.harold_y_pos = self.harold_start_y_pos
        self.harold_gravity = 0
        self.gravity_acceleration = GLOBAL_GRAVITY
        
        # Harold Animation Speed
        self.HAROLD_IDLE_ANIMATION_SPEED = 0.1

        # Harold Idle Animation
        harold_idle_00 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
        harold_idle_01 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_01.png').convert_alpha()
        harold_idle_02 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_02.png').convert_alpha()
        harold_idle_03 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_03.png').convert_alpha()
        harold_idle_04 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_04.png').convert_alpha()
        harold_idle_05 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_05.png').convert_alpha()
        harold_idle_06 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_06.png').convert_alpha()
        harold_idle_07 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_07.png').convert_alpha()
        harold_idle_08 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_08.png').convert_alpha()
        harold_idle_09 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_09.png').convert_alpha()
        harold_idle_10 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_10.png').convert_alpha()
        harold_idle_11 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_11.png').convert_alpha()
        harold_idle_12 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_12.png').convert_alpha()
        harold_idle_13 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_13.png').convert_alpha()
        harold_idle_14 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_14.png').convert_alpha()
        harold_idle_15 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_15.png').convert_alpha()
        harold_idle_16 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_16.png').convert_alpha()
        harold_idle_17 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_17.png').convert_alpha()
        harold_idle_18 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_18.png').convert_alpha()
        harold_idle_19 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_19.png').convert_alpha()
        harold_idle_20 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_20.png').convert_alpha()
        self.harold_idle = [harold_idle_00, harold_idle_01, harold_idle_02, harold_idle_03,
                    harold_idle_04, harold_idle_05, harold_idle_06, harold_idle_07,
                    harold_idle_08, harold_idle_09, harold_idle_10, harold_idle_11,
                    harold_idle_12, harold_idle_13, harold_idle_14, harold_idle_15,
                    harold_idle_16, harold_idle_17, harold_idle_18, harold_idle_19,
                    harold_idle_20]

        self.harold_index = 0
        self.image = self.harold_idle[self.harold_index]
        self.image = pygame.transform.scale_by(self.image,3/2)
        self.rect = self.image.get_rect(midbottom = (self.harold_x_pos,self.harold_y_pos))

    def get_harold_x_pos(self):
        return self.harold_x_pos

    def set_harold_x_pos(self,new_harold_x_pos):
        self.harold_x_pos = new_harold_x_pos

    def get_harold_start_x_pos(self):
        return self.harold_start_x_pos

    def set_harold_start_x_pos(self,new_harold_start_x_pos):
        self.harold_start_x_pos = new_harold_start_x_pos

    def get_harold_start_y_pos(self):
        return self.harold_start_y_pos

    def set_harold_start_y_pos(self,new_harold_start_y_pos):
        self.harold_start_y_pos = new_harold_start_y_pos

    def get_harold_speed(self):
        return self.harold_speed
    
    def set_harold_speed(self,new_harold_speed):
        self.harold_speed = new_harold_speed

    def get_harold_gravity(self):
        return self.harold_gravity
    
    def set_harold_gravity(self,new_harold_gravity):
        self.harold_gravity = new_harold_gravity

    def harold_input(self):
        keys = pygame.key.get_pressed()
        if not self.player.sprite.get_wizard_dead():
            if keys[jump_button] and self.rect.bottom >= self.harold_start_y_pos:
                self.harold_gravity = self.gravity_acceleration
            if keys[right_button] and self.player.sprite.get_wizard_rect().x + WIZARD_WIDTH + self.harold_speed < WINDOW_WIDTH:
                self.harold_x_velocity = self.harold_speed
                self.rect.x += self.harold_x_velocity
            if keys[left_button] and self.player.sprite.get_wizard_rect().x - self.harold_speed > 0:
                self.harold_x_velocity = self.harold_speed
                self.rect.x -= self.harold_x_velocity
    
    def apply_gravity(self):
        if not self.player.sprite.get_wizard_dead():
            self.harold_gravity += 1
            self.rect.y += self.harold_gravity
            if self.rect.bottom >= self.harold_start_y_pos: self.rect.bottom = self.harold_start_y_pos
        else:
            if self.player.sprite.get_wizard_jumping():
                self.harold_gravity += 0.4
                self.rect.y += self.harold_gravity
                if self.rect.bottom >= GRASS_TOP_Y - 20 : self.rect.bottom = GRASS_TOP_Y - 20
            else:
                self.rect.y += 0.5
                if self.rect.bottom >= GRASS_TOP_Y - 20: self.rect.bottom = GRASS_TOP_Y - 20

    def animation_state(self):    
        self.harold_index += self.HAROLD_IDLE_ANIMATION_SPEED # speed of animation, adjust as needed
        if self.harold_index >= len(self.harold_idle):self.harold_index = 0
        
        self.image = self.harold_idle[int(self.harold_index)]
        self.image = pygame.transform.scale_by(self.image,3/2)

        if not self.player.sprite.get_looking_right():
            self.image = pygame.transform.flip(self.image,True,False)
    
    def update(self):
        self.harold_input()
        self.apply_gravity()
        self.animation_state()
        
    def reset(self):
        # Temp Wizard Attribute
        temp_wizard_rect = self.player.sprite.get_wizard_rect()
        
        # Harold Start
        self.harold_start_x_pos = temp_wizard_rect.centerx
        self.harold_start_y_pos = temp_wizard_rect.top + 28 # pixels at this scale based on wizard are 4 pixels each
        
        # Harold X Values
        self.harold_x_pos = self.harold_start_x_pos
        self.harold_speed = self.player.sprite.get_wizard_speed()
        self.harold_x_velocity = 0
        
        # Harold Y Values
        self.harold_y_pos = self.harold_start_y_pos
        self.harold_gravity = 0
        self.gravity_acceleration = GLOBAL_GRAVITY
        
        # Harold Animation Speed
        self.HAROLD_IDLE_ANIMATION_SPEED = 0.1

        self.harold_index = 0
        self.image = self.harold_idle[self.harold_index]
        self.image = pygame.transform.scale_by(self.image,3/2)
        self.rect = self.image.get_rect(midbottom = (self.harold_x_pos,self.harold_y_pos))