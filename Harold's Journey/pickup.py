"""Pickup Class"""
from random import randint, choice

from global_vars import *


class Pickup(pygame.sprite.Sprite):
    def __init__(self, type, x_pos, y_pos):
        super().__init__()
        
        # Won't agree with x_pos and y_pos fsr
        self.x_pos = WINDOW_WIDTH / 2
        self.y_pos = WIZARD_HEIGHT
        self.gravity_intensity = 1
        self.gravity = GLOBAL_GRAVITY
        self.PICKUP_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60
        self.lifetime = self.LIFETIME_LIMIT
        
        # Pickups don't show up and don't go away when walked over
        if type == 'damage': # Percentages
            self.type = 'damage'
            self.bonus = 0.5
            harold_idle_12 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_12.png').convert_alpha()
            harold_idle_13 = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_13.png').convert_alpha()
            self.frames = [harold_idle_12, harold_idle_13]

        elif type == 'piercing': # Flat increases
            self.type = 'piercing'
            self.bonus = 1
            fireball_trans_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_1.png').convert_alpha()
            fireball_trans_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_2.png').convert_alpha()
            self.frames = [fireball_trans_1, fireball_trans_2]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale_by(self.image,1)
        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos)) 
        print("I'm ") # this triggers so they exist but won't show
        if type == 'damage': print('damage')
        else: print('piercing')

    def get_bonus(self):
        return self.bonus
    
    def get_type(self):
        return self.type
    
    def apply_gravity(self):
        self.gravity += self.gravity_intensity
        self.rect.y += self.gravity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y
    
    def animation_state(self):   
        self.animation_index += self.PICKUP_ANIMATION_SPEED
        if self.animation_index >= len(self.frames): self.animation_index = 0
        
        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale_by(self.image,1)
    
    def update(self):
        self.apply_gravity()
        self.animation_state()
        self.destroy()
        
    def destroy(self):
        if self.lifetime <= 0:
            self.kill()
        else:
            self.lifetime -= 1