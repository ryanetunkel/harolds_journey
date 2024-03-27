"""Pickup Class"""
from random import randint, choice

from global_vars import *

class Pickup(pygame.sprite.Sprite):
    def __init__(self, type: str, x_pos: int, y_pos: int):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.gravity_intensity = 1
        self.gravity = GLOBAL_GRAVITY
        self.PICKUP_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60
        self.lifetime = self.LIFETIME_LIMIT

        if type == "damage": # Percentages
            self.type = "damage"
            self.bonus = 0.5
            damage_pickup = pygame.image.load("harolds_journey/graphics/pickups/damage/damage_pickup.png").convert_alpha()
            self.frames = [damage_pickup]

        elif type == "piercing": # Flat increases
            self.type = "piercing"
            self.bonus = 1
            piercing_pickup = pygame.image.load("harolds_journey/graphics/pickups/piercing/piercing_pickup.png").convert_alpha()
            self.frames = [piercing_pickup]

        elif type == "fireball_cooldown": # Flat increases?
            self.type = "fireball_cooldown"
            self.bonus = 2
            fireball_cooldown_pickup = pygame.image.load("harolds_journey/graphics/pickups/fireball_cooldown/fireball_cooldown_pickup.png").convert_alpha()
            self.frames = [fireball_cooldown_pickup]

        elif type == "speed": # Flat increases
            self.type = "speed"
            self.bonus = 0.5
            speed_pickup = pygame.image.load("harolds_journey/graphics/pickups/speed/speed_pickup.png").convert_alpha()
            self.frames = [speed_pickup]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale_by(self.image,3)
        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

    def get_bonus(self):
        return self.bonus

    def get_type(self):
        return self.type

    def get_height(self):
        return self.rect.bottom - self.rect.top

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