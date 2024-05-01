"""Harold Class"""
from random import randint, choice

from global_vars import *
from player import *
from graphics.harold.harold_animation_holder import *

class Harold(pygame.sprite.Sprite):
    def __init__(self, player: pygame.sprite.GroupSingle):
        super().__init__()

        # Temp Wizard Attribute
        self.player = player
        temp_wizard_rect = self.player.sprite.get_wizard_rect()
        self.DEAD_WIZARD_HAT_SIZE = 5 * PIXEL_SIZE
        self.ALIVE_WIZARD_HAT_SIZE = 7 * PIXEL_SIZE
        self.wizard_was_jumping = False

        # Harold Start
        self.harold_start_x_pos = temp_wizard_rect.centerx
        print(temp_wizard_rect.centerx)
        self.harold_start_y_pos = temp_wizard_rect.top + self.ALIVE_WIZARD_HAT_SIZE

        # Harold X Values
        self.harold_x_pos = self.harold_start_x_pos
        self.harold_speed = self.player.sprite.get_wizard_speed()
        self.harold_x_velocity = 0

        # Harold Y Values
        self.harold_y_pos = self.harold_start_y_pos
        self.harold_y_velocity = 0
        self.jump_speed = -20
        self.gravity_acceleration = GLOBAL_GRAVITY # How quickly gravity accelerates the player

        # Harold Animation Speed
        self.HAROLD_IDLE_ANIMATION_SPEED = 0.1

        # Harold Idle Animation
        self.harold_idle = get_harold_idle_arr()

        self.harold_index = 0
        self.image = self.harold_idle[self.harold_index]
        self.scale = (WIZARD_HEIGHT * 3/8,WIZARD_WIDTH * 3/8)
        # Harold: 32x32 * 3/2 = 48x48
        # Wizard: 32x32 * 4 = 128x128
        # 128/48 = 32/12 = 8/3
        self.image = pygame.transform.scale(self.image,self.scale) # scaleby 3/2
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

    def get_harold_y_velocity(self):
        return self.harold_y_velocity

    def set_harold_y_velocity(self,new_harold_y_velocity):
        self.harold_y_velocity = new_harold_y_velocity

    def get_jump_speed(self):
        return self.jump_speed

    def set_jump_speed(self,new_jump_speed):
        self.jump_speed = new_jump_speed

    def get_harold_gravity_acceleration(self):
        return self.harold_gravity_acceleration

    def set_harold_gravity_acceleration(self,new_harold_gravity_acceleration):
        self.harold_gravity_acceleration = new_harold_gravity_acceleration

    def get_wizard_was_jumping(self):
        return self.wizard_was_jumping

    def set_wizard_was_jumping(self,new_wizard_was_jumping):
        self.wizard_was_jumping = new_wizard_was_jumping

    def get_height(self):
        return self.rect.bottom - self.rect.top

    def harold_input(self):
        keys = pygame.key.get_pressed()
        # Refreshing Harold speed
        self.harold_speed = self.player.sprite.get_wizard_speed()
        if not self.player.sprite.get_wizard_dead() and not self.player.sprite.get_wizard_start_death():
            if keys[jump_button] and self.rect.bottom >= self.harold_start_y_pos:
                self.harold_y_velocity = self.jump_speed
            if keys[right_button] and self.player.sprite.get_wizard_rect().x + WIZARD_WIDTH + self.harold_speed < WINDOW_WIDTH:
                self.harold_x_velocity = self.harold_speed
                self.rect.x += self.harold_x_velocity
            if keys[left_button] and self.player.sprite.get_wizard_rect().x - self.harold_speed > 0:
                self.harold_x_velocity = self.harold_speed
                self.rect.x -= self.harold_x_velocity

    def apply_gravity(self):
        temp_player = self.player.sprite
        temp_wizard_rect = self.player.sprite.get_wizard_rect()
        wizard_was_jumping = self.get_wizard_was_jumping()
        if not self.player.sprite.get_wizard_dead() and not self.player.sprite.get_wizard_start_death():
            self.harold_y_velocity += self.gravity_acceleration
            self.rect.y += self.harold_y_velocity
            if not self.player.sprite.get_wizard_start_death() and self.rect.bottom >= temp_wizard_rect.top + self.ALIVE_WIZARD_HAT_SIZE:
                # No inclusion of setting harold y vel to 0 so he gets flung
                self.rect.bottom = temp_wizard_rect.top + self.ALIVE_WIZARD_HAT_SIZE
            self.set_wizard_was_jumping(temp_player.get_wizard_jumping())
        else:
            if wizard_was_jumping:
                self.harold_y_velocity += 0.4
                self.rect.y += self.harold_y_velocity
            else:
                self.rect.y += 0.5
            if self.rect.bottom >= GRASS_TOP_Y - self.DEAD_WIZARD_HAT_SIZE:
                self.set_harold_y_velocity(0)
                self.rect.bottom = GRASS_TOP_Y - self.DEAD_WIZARD_HAT_SIZE

    def animation_state(self):
        self.harold_index += self.HAROLD_IDLE_ANIMATION_SPEED # speed of animation, adjust as needed
        if self.harold_index >= len(self.harold_idle):self.harold_index = 0
        self.image = self.harold_idle[int(self.harold_index)]
        self.image = pygame.transform.scale(self.image,self.scale)

        if not self.player.sprite.get_looking_right():
            self.image = pygame.transform.flip(self.image,True,False)

    def update(self):
        self.harold_input()
        self.apply_gravity()
        self.animation_state()

    def reset(self):
        # Temp Wizard Attribute
        temp_wizard_rect = self.player.sprite.get_wizard_rect()
        self.DEAD_WIZARD_HAT_SIZE = 5 * PIXEL_SIZE
        self.wizard_was_jumping = False

        # Harold Start
        self.harold_start_x_pos = temp_wizard_rect.centerx
        self.harold_start_y_pos = temp_wizard_rect.top + 7 * PIXEL_SIZE # pixels at this scale based on wizard are 4 pixels each

        # Harold X Values
        self.harold_x_pos = self.harold_start_x_pos
        self.harold_speed = self.player.sprite.get_wizard_speed()
        self.harold_x_velocity = 0

        # Harold Y Values
        self.harold_y_pos = self.harold_start_y_pos
        self.harold_y_velocity = 0
        self.jump_speed = -20
        self.gravity_acceleration = GLOBAL_GRAVITY # How quickly gravity accelerates the player

        # Harold Animation Speed
        self.HAROLD_IDLE_ANIMATION_SPEED = 0.1

        # Harold Idle Animation
        self.harold_idle = get_harold_idle_arr()

        self.harold_index = 0
        self.image = self.harold_idle[self.harold_index]
        self.scale = (WIZARD_HEIGHT * 3/8,WIZARD_WIDTH * 3/8)
        # Harold: 32x32 * 3/2 = 48x48
        # Wizard: 32x32 * 4 = 128x128
        # 128/48 = 32/12 = 8/3
        self.image = pygame.transform.scale(self.image,self.scale) # scaleby 3/2
        self.rect = self.image.get_rect(midbottom = (self.harold_x_pos,self.harold_y_pos))
