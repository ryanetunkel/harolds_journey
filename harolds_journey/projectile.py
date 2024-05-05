"""Projectile Class"""
from random import randint, choice
import math

from global_vars import *
from graphics.fireball.fireball_animation_holder import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, type: str, source: pygame.sprite.Sprite):
        super().__init__()

        # Projectiles
        # These might not all be universal, especially damage and speed, will be varied

        self.projectile_speed = 5
        self.projectile_damage = 1

        (self.mouse_x,self.mouse_y) = pygame.mouse.get_pos()

        if type == 'fireball': # Can't currently handle any projectile other than 'fireball'
            # Fireball - Mess with these values and the wizard's casting aniamtion to get good looking animation
            self.fireball_move_animation_speed = 0.4
            self.fireball_transition_animation_speed = 0.4

            # Wizard related
            self.temp_wizard_rect = source.sprite.get_wizard_rect()
            self.wizard_was_looking_right = source.sprite.get_looking_right()
            self.wizard_was_looking_down = source.sprite.get_looking_down()
            self.wizard_x_velocity = source.sprite.get_wizard_x_velocity()
            self.wizard_y_velocity = source.sprite.get_wizard_y_velocity()
            self.x_direction_multiplier = 1 if self.wizard_was_looking_right else -1
            self.y_direction_multiplier = 1 if self.wizard_was_looking_down else -1
            self.knockback = source.sprite.get_knockback()

            # Start position
            self.fireball_x_start = self.temp_wizard_rect.centerx + ((WIZARD_WIDTH/2) * self.x_direction_multiplier)
            self.fireball_y_start = self.temp_wizard_rect.centery + (6 * PIXEL_SIZE)

            # Position
            self.fireball_x_pos = self.fireball_x_start
            self.fireball_y_pos = self.fireball_y_start
            (self.mouse_x,self.mouse_y) = pygame.mouse.get_pos()
            self.x_dif = self.fireball_x_start - self.mouse_x
            self.y_dif = self.fireball_y_start - self.mouse_y
            self.quadrant = (self.x_direction_multiplier,self.y_direction_multiplier)
            self.angle = math.atan2(self.y_dif,self.x_dif)

            # Speed
            self.speed = 5
            self.fireball_x_start_speed = 0
            self.fireball_x_speed = self.projectile_speed
            self.fireball_y_start_speed = 0
            self.fireball_y_speed = 0
            # Pythagoras' fav time

            # Gravity
            self.fireball_gravity_when_held = 0

            # Statistics - To Be Implemented
            self.fireball_damage = source.sprite.get_wizard_damage_total()
            self.fireball_piercing = source.sprite.get_wizard_piercing_total()

            # Fireball Creation
            self.created = 0

            # Fireball Transition Animation
            self.fireball_transition = get_fireball_transition_arr()

            # Fireball Movement Animation
            self.fireball_movement = get_fireball_movement_arr()

            self.fireball_index = 0
            self.image = self.fireball_transition[self.fireball_index]
            # self.image = pygame.transform.scale_by(self.image,1)
            if not self.wizard_was_looking_right:
                self.image = pygame.transform.flip(self.image,True,False)
            self.scale = GLOBAL_SCALAR
            self.image = pygame.transform.scale_by(self.image,self.scale)
            self.rect = self.image.get_rect(center = (self.fireball_x_pos,self.fireball_y_pos))

    def get_fireball_damage(self):
        return self.fireball_damage

    def set_fireball_damage(self):
        return self.fireball_damage

    def get_fireball_piercing(self):
        return self.fireball_piercing

    def set_fireball_piercing(self,new_fireball_piercing):
        self.fireball_piercing = new_fireball_piercing

    def get_x_pos(self):
        return self.rect.centerx

    def get_y_pos(self):
        return self.rect.centery

    def get_x_direction_multiplier(self):
        return self.x_direction_multiplier

    def get_angle_radians(self):
        return self.angle

    def get_angle_degrees(self):
        return self.angle * 180 / math.pi

    def get_knockback(self):
        return self.knockback

    def set_knockback(self,new_knockback):
        self.knockback = new_knockback

    def animation_state(self):
        if self.created < 4:
            self.created += self.fireball_transition_animation_speed
            self.fireball_index += self.fireball_transition_animation_speed

            if self.fireball_index >= len(self.fireball_transition): self.fireball_index = 0
            self.image = self.fireball_transition[int(self.fireball_index)]
        else:
            self.fireball_index += self.fireball_move_animation_speed # speed of animation, adjust as needed
            if self.fireball_index >= len(self.fireball_movement): self.fireball_index = 0

            self.image = self.fireball_movement[int(self.fireball_index)]

        if not self.wizard_was_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        else:
            self.image = pygame.transform.flip(self.image,True,True)

        self.image = pygame.transform.scale_by(self.image,self.scale)
        self.image = pygame.transform.rotozoom(self.image,self.get_angle_degrees()*-1,1)

    def move_fireball(self):
        # Preference by a pixel to right (+x) and down (+y)
        x_velocity_via_angle = self.projectile_speed * math.cos(self.angle) * -1
        y_velocity_via_angle = self.projectile_speed * math.sin(self.angle) * -1
        wizard_x_velocity_change = (self.wizard_x_velocity / 2) * self.x_direction_multiplier
        wizard_y_velocity_change = (self.wizard_y_velocity / 2) * self.y_direction_multiplier

        x_velocity_without_movement = x_velocity_via_angle
        x_velocity_with_movement = x_velocity_without_movement + wizard_x_velocity_change
        y_velocity_without_movement = y_velocity_via_angle
        y_velocity_with_movement = y_velocity_without_movement + wizard_y_velocity_change

        if self.created >= 4:
            if x_velocity_with_movement > x_velocity_without_movement: # making fireball go with wiz x velocity
                self.rect.centerx += x_velocity_with_movement
            else:
                self.rect.centerx += x_velocity_without_movement
            if y_velocity_with_movement > y_velocity_without_movement: # making fireball go with wiz y velocity
                self.rect.centery += y_velocity_with_movement
            else:
                self.rect.centery += y_velocity_without_movement

    def update(self):
        self.animation_state()
        self.move_fireball()
        self.destroy()

    def destroy(self):
        if self.rect.centerx <= -100 and not self.wizard_was_looking_right:
            self.kill()
        elif self.rect.centerx >= WINDOW_WIDTH + 100 and self.wizard_was_looking_right:
            self.kill()
        if self.rect.centery <= -100:
            self.kill()
        elif self.rect.centery >= GRASS_TOP_Y:
            self.kill()