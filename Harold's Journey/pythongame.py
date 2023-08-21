import pygame
from sys import exit
from random import randint, choice

# Just put in the Player class, haven't removed any old code it replaces
# Also Harold needs either his own class or to also be a player
# 3 33 20
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.wizard_start_x_pos = 80
        self.wizard_start_y_pos = GRASS_TOP_Y
        self.wizard_x_pos = self.wizard_start_x_pos
        self.wizard_speed = 4
        self.wizard_x_velocity = 0
        self.wizard_y_pos = self.wizard_start_y_pos
        self.gravity_acceleration = -20
        self.wizard_secret_animation_limit = 240
        self.wizard_secret_animation_timer = self.wizard_secret_animation_limit
        self.wizard_jumping = False

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

        self.wizard_index = 0
        self.image = self.wizard_walk[self.wizard_index]
        self.rect = self.image.get_rect(midbottom = (self.wizard_x_pos,self.wizard_y_pos))
        self.wizard_gravity = 0

        self.looking_right = mouse_x >= self.rect.centerx

        # self.jump_sound = pygame.mixer.Sound(...)
        # self.jump_sound.set_volume(0.5)

        # Harold
        self.harold_start_x_pos = self.rect.centerx
        self.harold_start_y_pos = self.rect.top + 28 # pixels at this scale based on wizard are 4 pixels each
        self.harold_x_pos = self.harold_start_x_pos
        self.harold_speed = self.wizard_speed
        self.harold_x_velocity = 0
        self.harold_y_pos = self.harold_start_y_pos
        self.harold_gravity = 0

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

        # harold_surf = pygame.transform.flip(harold_surf, True, False)
        self.harold_index = 0
        self.harold_surf = self.harold_idle[self.harold_index]
        self.harold_surf = pygame.transform.scale_by(self.harold_surf,3/2)
        self.harold_rect = self.harold_surf.get_rect(midbottom = (self.harold_x_pos,self.harold_y_pos))

    def get_wizard_rect(self):
        return (self.rect)

    def get_looking_right(self):
        return self.looking_right

    def wizard_input(self):
        keys = pygame.key.get_pressed()
        if keys[shoot_button] and (fireball_cooldown == 0 or fireball_hit):
            fireball_cooldown = fireball_cooldown_time
            fireball_hit = False
            projectile_group.add(Projectile())
        if keys[jump_button] and self.rect.bottom >= GRASS_TOP_Y:
            self.wizard_jumping = True
            self.wizard_gravity = self.gravity_acceleration
            # self.jump_sound.play()
            self.harold_gravity = self.gravity_acceleration
        if keys[right_button] and self.rect.x + WIZARD_WIDTH + wizard_x_velocity < WINDOW_WIDTH:
            self.wizard_x_pos += self.wizard_speed
            self.harold_x_pos += self.harold_speed
        if keys[left_button] and self.rect.x - wizard_x_velocity > 0:
            self.wizard_x_pos -= self.wizard_speed
            self.harold_x_pos -= self.harold_speed
    
    def apply_gravity(self):
        self.wizard_gravity += 1
        self.rect.y += self.wizard_gravity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y

    def animation_state(self):
        if fireball_cooldown < 60 and fireball_cooldown >= 30:
            # wizard fireball animation
            self.wizard_secret_animation_timer = self.wizard_secret_animation_limit
            self.wizard_index += wizard_fireball_animation_speed # speed of animation, adjust as needed
            if self.wizard_index >= len(self.wizard_fireball):self.wizard_index = 0
            self.image = self.wizard_fireball[int(self.wizard_index)]
        elif self.rect.bottom < GRASS_TOP_Y and self.wizard_jumping: # and add landing tracker this would be if it is off
            # jump (first half)
            self.wizard_secret_animation_timer = self.wizard_secret_animation_limit
            self.wizard_index += wizard_jump_animation_speed # speed of animation, adjust as needed
            if self.wizard_index >= len(self.wizard_jump):self.wizard_index = 0
            self.image = self.wizard_jump[int(self.wizard_index)]
            # this is it raw with no adjustment
            # below is the ideal
            # wizard_surf = wizard_jump[0,7] # can't just do this need to go through
            # 8 - 14 need to be when reach peak, prob cut and edit which goes where
            # and add landing tracker this would be if landed
            # landing animation for a few frames via timer and then when ends revert to idle
        elif wizard_x_velocity != 0 and self.rect.bottom >= GRASS_TOP_Y:
            self.wizard_secret_animation_timer = self.wizard_secret_animation_limit
            self.wizard_index += wizard_walk_animation_speed # speed of animation, adjust as needed
            if self.wizard_index >= len(self.wizard_walk):self.wizard_index = 0
            self.image = self.wizard_walk[int(self.wizard_index)]
        elif wizard_x_velocity == 0:
            if self.wizard_secret_animation_timer != 0:
                self.wizard_index += wizard_idle_animation_speed # speed of animation, adjust as needed
                if self.wizard_index >= len(self.wizard_idle):self.wizard_index = 0
                self.image = self.wizard_idle[int(self.wizard_index)]
                # idle animation
                # start timer that last for a few rounds of idle animation until would do the second
                self.wizard_secret_animation_timer -= 1
            else:
                self.wizard_index += wizard_secret_idle_animation_speed # speed of animation, adjust as needed
                if self.wizard_index >= len(self.wizard_secret_idle):self.wizard_index = 0
                self.image = self.wizard_secret_idle[int(self.wizard_index)]

        self.image = pygame.transform.scale(self.image,wizard_pixel_size)
        if not self.looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        # Death animation if game was ended - rn game ends instantly so can't be implemented
        # Damage animation if hit and not killed - rn can't do cuz no health

    def harold_animation_state(self):    
        self.harold_index += harold_idle_animation_speed # speed of animation, adjust as needed
        if self.harold_index >= len(self.harold_idle):self.harold_index = 0
        self.harold_surf = self.harold_idle[int(self.harold_index)]
        self.harold_surf = pygame.transform.scale_by(self.harold_surf,3/2)

        if not self.looking_right:
            self.harold_surf = pygame.transform.flip(self.harold_surf,True,False)

    def update(self):
        self.wizard_input()
        self.apply_gravity()
        self.animation_state()
        self.harold_animation_state()

# Might need to make a Harold Class or have him inherit the Player class

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        self.obstacle_health = 1
        self.obstacle_points = 5
        self.enemy_looking_right = False

        if randint(0,2) == 1:
            self.x_pos = randint(WINDOW_WIDTH + 100,WINDOW_WIDTH + 300)
            self.enemy_looking_right = False
        else:
            self.x_pos = randint(-300,-100)
            self.enemy_looking_right = True

        if type == 'skeleton':
            self.y_pos = GRASS_TOP_Y + 8
            self.obstacle_speed = skeleton_speed
            self.obstacle_animation_speed = skeleton_walk_animation_speed_decimal

            # Skeleton Walk Animation
            skeleton_walk_00 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png').convert_alpha()
            skeleton_walk_01 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_01.png').convert_alpha()
            skeleton_walk_02 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_02.png').convert_alpha()
            skeleton_walk_03 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_03.png').convert_alpha()
            skeleton_walk_04 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_04.png').convert_alpha()
            skeleton_walk_05 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_05.png').convert_alpha()
            skeleton_walk_06 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_06.png').convert_alpha()
            skeleton_walk_07 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_07.png').convert_alpha()
            skeleton_walk_08 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_08.png').convert_alpha()
            skeleton_walk_09 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_09.png').convert_alpha()
            skeleton_walk_10 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_10.png').convert_alpha()
            skeleton_walk_11 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_11.png').convert_alpha()
            skeleton_walk_12 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_12.png').convert_alpha()
            self.frames = [skeleton_walk_00, skeleton_walk_01, skeleton_walk_02, skeleton_walk_03,
                            skeleton_walk_04, skeleton_walk_05, skeleton_walk_06, skeleton_walk_07,
                            skeleton_walk_08, skeleton_walk_09, skeleton_walk_10, skeleton_walk_11,
                            skeleton_walk_12]
            # skeleton_surf = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png')

        else:
            self.y_pos = GRASS_TOP_Y - 100
            self.obstacle_speed = flying_enemy_speed
            self.obstacle_animation_speed = flying_enemy_fly_animation_speed_decimal
            # Placeholders
            flying_enemy_fly_1 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png')
            flying_enemy_fly_2 = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png')
            self.frames = [flying_enemy_fly_1,flying_enemy_fly_2]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale(self.image,wizard_pixel_size)
        if self.enemy_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
    
    def animation_state(self):
        if type == 'skeleton':
            self.animation_index += obstacle_animation_speed
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= self.obstacle_speed
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100 and not self.enemy_looking_right:
            self.kill()
        if self.rect.x >= WINDOW_WIDTH + 100 and self.enemy_looking_right:
            self.kill()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        # Projectiles
        # These might not all be universal, especially damage and speed, will be varied
        self.projectile_speed = 5
        self.projectile_damage = 1

        # Fireball
        self.fireball_x_start = wizard.get_wizard_rect().right - 20
        self.fireball_y_start = wizard.get_wizard_rect().centery + 24

        self.fireball_x_pos = self.fireball_x_start
        self.fireball_y_pos = self.fireball_y_start

        self.fireball_x_start_speed = 0

        self.fireball_speed = 5
        self.fireball_gravity_when_held = 0

        self.fireball_damage = 1

        self.wizard_was_looking_right = wizard.get_looking_right()
        self.direction_multiplier = 1 if self.wizard_was_looking_right else -1

        # Fireball Transition Animation
        fireball_trans_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_0.png').convert_alpha()
        fireball_trans_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_1.png').convert_alpha()
        fireball_trans_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_2.png').convert_alpha()
        fireball_trans_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_3.png').convert_alpha()
        self.fireball_trans = [fireball_trans_0, fireball_trans_1, fireball_trans_2, fireball_trans_3]

        # Fireball Movement Animation
        fireball_move_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_0.png').convert_alpha()
        fireball_move_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_1.png').convert_alpha()
        fireball_move_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_2.png').convert_alpha()
        fireball_move_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_3.png').convert_alpha()
        self.fireball_move = [fireball_move_0, fireball_move_1, fireball_move_2, fireball_move_3]

        self.fireball_index = 0
        self.image = self.fireball_move[self.fireball_index]
        self.image = pygame.transform.scale(fireball_surf,wizard_pixel_size)
        if self.wizard_was_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(center = (self.fireball_x_pos,self.fireball_y_pos))
    
    def animation_state(self):
        global fireball_surf, fireball_index

        fireball_index += fireball_move_animation_speed # speed of animation, adjust as needed
        if fireball_index >= len(self.fireball_move):fireball_index = 0
        fireball_surf = self.fireball_move[int(fireball_index)]
        fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)
        # if not looking_right: # Can only be done once can track dif directions for fireballs to go in
        #     fireball_surf = pygame.transform.flip(fireball_surf,True,False)
    
    def update(self):
        self.animation_state()
        self.rect.x += (self.projectile_speed * self.direction_multiplier)
        if self.fireball_cooldown != 0: self.fireball_cooldown -= 1
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100 and not self.wizard_was_looking_right:
            self.kill()
        elif self.rect.x >= WINDOW_WIDTH + 100 and not self.wizard_was_looking_right:
            self.kill()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
window_size = (WINDOW_WIDTH,WINDOW_HEIGHT)
WIZARD_WIDTH = 128
WIZARD_HEIGHT = 128
wizard_pixel_size = (WIZARD_HEIGHT,WIZARD_WIDTH)
GRASS_TOP_Y = 371

jump_button = pygame.K_SPACE
right_button = pygame.K_d
left_button = pygame.K_a
shoot_button = pygame.MOUSEBUTTONDOWN
additional_score = 0
score = 0
fireball_cooldown_time = 60
fireball_cooldown = 0
fireball_hit = False
(mouse_x,mouse_y) = (0,0)

# seconds per frame
wizard_walk_animation_speed = 0.1
wizard_jump_animation_speed = 0.075
wizard_idle_animation_speed = 0.1
wizard_secret_idle_animation_speed = wizard_idle_animation_speed
wizard_fireball_animation_speed = 0.4
fireball_move_animation_speed = wizard_fireball_animation_speed
fireball_transition_animation_speed = wizard_fireball_animation_speed
harold_idle_animation_speed = 0.1
obstacle_animation_speed = 0.1

obstacle_spawn_frequency = 1500 # In milliseconds, 1000 = 1 sec
skeleton_walk_animation_speed_decimal = 0.1 # Changed, won't work in current implementation but will in new ones 
flying_enemy_fly_animation_speed_decimal = 0.1
skeleton_walk_animation_speed = 50
flying_enemy_fly_animation_speed = 50

skeleton_speed = 2
flying_enemy_speed = 2


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(str(current_time + additional_score), False, '#FCDC4D')
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2,50))
    screen.blit(score_surf,score_rect)
    # print(current_time)
    return current_time + additional_score

# def obstacle_movement(obstacle_list):
#     if obstacle_list: # will only run if obstacle_list is not empty
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= obstacle_speed

#             if obstacle_rect.bottom == GRASS_TOP_Y + 8: screen.blit(skeleton_surf,obstacle_rect)
#             else: screen.blit(flying_enemy_surf,obstacle_rect)

#             # copies existing list if on screen
#             obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

#         return obstacle_list
#     else: return []

# def projectile_movement(projectile_list):
#     if projectile_list: # will only run if projectile_list is not empty
#         for projectile_rect in projectile_list:
#             projectile_rect.x += projectile_speed 
#             # The += will need to vary if player starts facing dif directions, 
#             # each projectile will need to have a speed associated with it 
#             # and it needs to be negative or positive depending

#             # can add in ifs associated with position to make different projectiles appear
#             screen.blit(fireball_surf,projectile_rect)

#             projectile_list = [projectile for projectile in projectile_list if (projectile.x > 0 and projectile.x < 800)]

#         return projectile_list
#     else: return []

# def wizard_collisions(wizard,obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if wizard.colliderect(obstacle_rect): return False
#     return True

def collision_sprite(): # Basically game over condition
    if pygame.sprite.spritecollide(wizard.sprite,obstacle_group,False):
        obstacle_group.empty()
        projectile_group.empty()
        return False
    else: return True

def projectile_collision():
    if pygame.sprite.spritecollide(projectile_group,obstacle_group,False):
        for projectile in projectile_group:
            for obstacle in obstacle_group:
                if projectile.colliderect(obstacle):
                    projectile_group.remove(projectile)
                    obstacle_group.remove(obstacle)
                    additional_score += 1
                    fireball_hit = True

# def projectile_collisions(projectiles,obstacles):
#     collisions = 0
#     if projectiles and obstacles:
#         for projectile in projectiles:
#             for obstacle in obstacles:
#                 if projectile.colliderect(obstacle):
#                     projectiles.remove(projectile)
#                     obstacles.remove(obstacle)
#                     collisions += 1
#                     # ********** For some reason it can't see these values, unsure why
#                     # ********** Also the game won't restart properly after the 
#                     # first game is played while open
#     return collisions

    # not including checking if fireball_start_speed is 0 
    # might make it so can still damage enemies if they 
    # walk into you but if you die first it doesn't really 
    # matter - could affect the score though

# can't implement health and damage sources as the variables aren't attached 
# to the individual projectiles and obstacles, they are global for all of them
# need to implement classes for that I think 
# def deal_damage(damage_source, target):
#     target.obstacle_health -= damage_source.projectile_damage
#     if target.obstacle_health <= 0:
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.obstacle_health > 0]
#         projectile_list = [projectile for projectile in projectile_list if (projectile.x > 0 and projectile.x < 800)]

# def fireball_animation():
#     global fireball_surf, fireball_index
    
#     fireball_index += fireball_move_animation_speed # speed of animation, adjust as needed
#     if fireball_index >= len(fireball_move):fireball_index = 0
#     fireball_surf = fireball_move[int(fireball_index)]
#     fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)
#     # if not looking_right: # Can only be done once can track dif directions for fireballs to go in
#     #     fireball_surf = pygame.transform.flip(fireball_surf,True,False)

# def harold_animation():
#     global harold_surf, harold_index
    
#     harold_index += harold_idle_animation_speed # speed of animation, adjust as needed
#     if harold_index >= len(harold_idle):harold_index = 0
#     harold_surf = harold_idle[int(harold_index)]
#     harold_surf = pygame.transform.scale_by(harold_surf,3/2)

#     if not looking_right:
#         harold_surf = pygame.transform.flip(harold_surf,True,False)

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Harold\'s Journey')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Harold\'s Journey/font/Pixeltype.ttf',50)
pygame_icon = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
pygame.display.set_icon(pygame_icon)
game_active = False
start_time = 0
# Music
# bg_music = pygame.mixer.Sound()
# bg_music.play(loops = -1)

wizard = pygame.sprite.GroupSingle()
wizard.add(Player())

obstacle_group = pygame.sprite.Group()

projectile_group = pygame.sprite.Group()

sky_surf = pygame.image.load('Harold\'s Journey/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,window_size)

ground_surf = pygame.image.load('Harold\'s Journey/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,window_size)

# Intro Screen
wizard_title_start_x_pos = 400
wizard_title_start_y_pos = 320
wizard_title_surf = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png').convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(192,192))
wizard_title_rect = wizard_title_surf.get_rect(center = (wizard_title_start_x_pos,wizard_title_start_y_pos))

harold_title_start_x_pos = wizard_title_rect.centerx
harold_title_start_y_pos = wizard_title_rect.top - 46
harold_title_surf = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
harold_title_surf = pygame.transform.scale_by(harold_title_surf,2.25)
harold_title_rect = harold_title_surf.get_rect(midbottom = (harold_title_start_x_pos,harold_title_start_y_pos))

title_game_name_surf = test_font.render('Harold\'s Journey',False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,3/2)
title_game_name_rect = title_game_name_surf.get_rect(center = (400,70))

title_info_start_x_pos = wizard_title_rect.centerx
title_info_start_y_pos = wizard_title_rect.centery + 40
title_info_start_pos = (title_info_start_x_pos,title_info_start_y_pos)
title_info_surf = test_font.render('Press any key or click to Start',False,"#FCDC4D")
title_info_rect = title_info_surf.get_rect(center = (title_info_start_pos))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,obstacle_spawn_frequency)

# # Won't need animation timers once done with classes
# # Skeleton Animation Timer
# skeleton_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(skeleton_animation_timer,skeleton_walk_animation_speed)

# # Flying Enemy Animation Timer
# flying_enemy_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(flying_enemy_animation_timer,flying_enemy_fly_animation_speed)

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        # if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
        #     if wizard_rect.collidepoint(event.pos): print ('collision')
       
        if game_active:
            (mouse_x,mouse_y) = pygame.mouse.get_pos()
            # Fireballs come off cooldown or instantly cooldown if you hit an enemy with one

            # if event.type == shoot_button and (fireball_cooldown == 0 or fireball_hit):
            #     fireball_cooldown = fireball_cooldown_time
            #     fireball_hit = False
            #     projectile_group.add(Projectile()) # fireball_surf.get_rect(center = (wizard_rect.right - 20,wizard_rect.centery + 24)))

            # looking_right = mouse_x >= wizard_rect.centerx

            # if event.type == pygame.KEYDOWN:
            #     if event.key == jump_button and wizard_rect.bottom >= GRASS_TOP_Y:  
            #         wizard_jumping = True
            #         wizard_gravity = gravity_acceleration
            #         harold_gravity = gravity_acceleration
            #     if event.key == right_button and wizard_rect.x + WIZARD_WIDTH + wizard_x_velocity < WINDOW_WIDTH:
            #         wizard_x_velocity = wizard_speed
            #         harold_x_velocity = harold_speed
            #     if event.key == left_button and wizard_rect.x - wizard_x_velocity > 0:
            #         wizard_x_velocity = -wizard_speed
            #         harold_x_velocity = -harold_speed
            # if event.type == pygame.KEYUP:
            #     if event.key == right_button:
            #         wizard_x_velocity = 0
            #         harold_x_velocity = 0
            #     if event.key == left_button:
            #         wizard_x_velocity = 0
            #         harold_x_velocity = 0

            # Obstacle Timer Event Detection
            if event.type == obstacle_timer: # moved from bottom compared to video for better format
                obstacle_group.add(Obstacle(choice(['flying_enemy','skeleton','skeleton','skeleton'])))
                # if randint(0,2): # gives values of either 0 or 1 which are false or true
                #     obstacle_rect_list.append(skeleton_surf.get_rect(midbottom = (skeleton_x_pos,skeleton_y_pos)))
                # else:
                #     obstacle_rect_list.append(flying_enemy_surf.get_rect(midbottom = (flying_enemy_x_pos,flying_enemy_y_pos)))
            # if event.type == skeleton_animation_timer:
            #     # Horrible Coding
            #     if skeleton_index != 12: skeleton_index += 1
            #     else: skeleton_index = 0
            #     skeleton_surf = skeleton_walk[skeleton_index]
            # if event.type == flying_enemy_animation_timer:
            #     # WIP - add when have animation 
            #     # Horrible Coding
            #     if flying_enemy_index != 12: flying_enemy_index += 1
            #     else: flying_enemy_index = 0
            #     flying_enemy_surf = flying_enemy_walk[flying_enemy_index]

        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                additional_score = 0

    # Active Game
    if game_active:    
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,0))
        score = display_score()

        # enemy_rect.x -= 4

        # Wizard
        # wizard_gravity += 1
        # wizard_rect.y += wizard_gravity
        # wizard_rect.x += wizard_x_velocity
        # # Harold
        # harold_gravity += 1
        # harold_rect.y += harold_gravity
        # harold_rect.x += harold_x_velocity

        # if wizard_rect.bottom >= grass_top_y: 
        #     wizard_rect.bottom = grass_top_y
        #     harold_rect.bottom = harold_start_y_pos
        # wizard_animation()
        # screen.blit(wizard_surf,wizard_rect)
        wizard.draw(screen) # draws sprites
        wizard.update() # updates sprites

        obstacle_group.draw(screen)
        obstacle_group.update()

        projectile_group.draw(screen)
        projectile_group.update()

        # Will be changed to be sprites
        # fireball_animation()
        # if fireball_x_start_speed != 0:
        #     screen.blit(fireball_surf,fireball_rect)
        
        # harold_animation()
        # screen.blit(harold_surf,harold_rect)

        # Obstacle Movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Projectile Movement
        # projectile_rect_list = projectile_movement(projectile_rect_list)

        # Collision between Wizard and Enemies
        # game_active = wizard_collisions(wizard_rect,obstacle_rect_list)

        # Collision between Enemies and Projectiles
        # collisions = projectile_collisions(projectile_rect_list,obstacle_rect_list)
        # additional_score += (collisions * obstacle_points)
        # if collisions:
        #     fireball_x_start_speed = 0
        #     fireball_hit = True
        # collisions = 0

        game_active = collision_sprite()

    # Menu Screen
    else:
        screen.fill('#54428E')
        # wizard_animation()
        screen.blit(wizard_title_surf,wizard_title_rect)
        screen.blit(harold_title_surf,harold_title_rect)
        screen.blit(title_info_surf,title_info_rect)

        # obstacle_rect_list.clear()
        # projectile_rect_list.clear()

        wizard_title_rect.midbottom = (wizard_title_start_x_pos,wizard_title_start_y_pos)
        wizard_gravity = 0
        wizard_x_velocity = 0

        harold_title_rect.midbottom = (harold_title_start_x_pos,harold_title_start_y_pos)
        harold_gravity = 0
        harold_x_velocity = 0

        score_message_surf = test_font.render('Score: ' + str(score),False,"#FCDC4D")
        score_message_surf = pygame.transform.scale_by(score_message_surf,3/2)
        score_message_rect = score_message_surf.get_rect(center = (400,70))

        if score == 0:
            screen.blit(title_game_name_surf,title_game_name_rect)

        else:
            screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)