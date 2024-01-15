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
            damage_pickup = pygame.image.load('harolds_journey/graphics/pickups/damage/damage_pickup.png').convert_alpha()
            self.frames = [damage_pickup]

        elif type == 'piercing': # Flat increases
            self.type = 'piercing'
            self.bonus = 1
            piercing_pickup = pygame.image.load('harolds_journey\graphics\pickups\piercing\piercing_pickup.png').convert_alpha()
            self.frames = [piercing_pickup]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale_by(self.image,3)
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
        self.image = pygame.transform.scale_by(self.image,3)
    
    def update(self):
        self.apply_gravity()
        self.animation_state()
        self.destroy()
        
    def destroy(self):
        if self.lifetime <= 0:
            self.kill()
        else:
            self.lifetime -= 1