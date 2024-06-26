"""Pickup Class"""
from random import randint, choice

from global_vars import *

class Pickup(pygame.sprite.Sprite):
    def __init__(self, type: str, x_pos: int, y_pos: int):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.gravity_acceleration = GLOBAL_GRAVITY
        self.y_velocity = -20 * GLOBAL_SCALAR
        self.PICKUP_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60 / GLOBAL_SCALAR
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
            self.bonus = 0.5 * GLOBAL_SCALAR
            speed_pickup = pygame.image.load("harolds_journey/graphics/pickups/speed/speed_pickup.png").convert_alpha()
            self.frames = [speed_pickup]

        elif type == "health": # Flat increases
            self.type = "health"
            self.bonus = 1
            health_pickup = pygame.image.load("harolds_journey/graphics/pickups/health/health_pickup.png").convert_alpha()
            self.frames = [health_pickup]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.scale = 3 * GLOBAL_SCALAR
        self.image = pygame.transform.scale_by(self.image,self.scale)
        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

    def get_bonus(self):
        return self.bonus

    def get_type(self):
        return self.type

    def get_height(self):
        return self.rect.bottom - self.rect.top

    def apply_gravity(self):
        self.y_velocity += self.gravity_acceleration
        self.rect.y += self.y_velocity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y

    def animation_state(self):
        self.animation_index += self.PICKUP_ANIMATION_SPEED
        if self.animation_index >= len(self.frames): self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale_by(self.image,self.scale)

    def update(self):
        self.apply_gravity()
        self.animation_state()
        self.destroy()

    def destroy(self):
        if self.lifetime <= 0:
            self.kill()
        else:
            self.lifetime -= 1