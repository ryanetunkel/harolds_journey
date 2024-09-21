"""Obstacle Class"""
from random import randint, choice

from global_vars import *
from graphics.enemies.bird.bird_animation_holder import *
from graphics.enemies.skeleton.skeleton_animation_holder import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type: str, time_at_spawn: int):
        super().__init__()

        self.obstacle_type = obstacle_type

        self.ROUND_DIFFICULTY_INCREASE_INCREMENT = 20 # frequency in seconds the difficulty increases
        self.time_scalar = int(time_at_spawn / self.ROUND_DIFFICULTY_INCREASE_INCREMENT) + 1 # Should mean every 20 seconds goes up by 1

        self.enemy_looking_right = False
        self.knockback_value = 8 * GLOBAL_SCALAR
        self.knockback_vector = 0
        self.knockback_timer_max = 8
        self.knockback_timer = self.knockback_timer_max
        self.knockback_active = False
        self.hurt = False
        self.damaged_color = "#550000"

        self.skeleton_walk_animation_speed =  0.32
        self.bird_fly_animation_speed = 0.2

        (self.spawn_range_min,self.spawn_range_max) = (100,300) # 100-300 pixels beyond the edges of the screen, the obstacle will spawn
        self.despawn_range = 100 # 100 pixels beyond the edges of the screen, the obsacle will despawn

        # Skeleton Base Stats
        self.skeleton_value = 2
        self.skeleton_max_health = 1
        self.skeleton_speed = 2 * GLOBAL_SCALAR
        self.skeleton_damage = 1

        # Flying Enemy Base Stats
        self.bird_value = 5
        self.bird_max_health = 1
        self.bird_speed = 2 * GLOBAL_SCALAR
        self.bird_damage = 1
        self.immunity = False
        self.IMMUNITY_LIMIT = 50
        self.immunity_timer = 0 # will need to eventually track what fireball id hit it

        if randint(0,1) == 1:
            self.x_pos = randint(WINDOW_WIDTH + self.spawn_range_min,WINDOW_WIDTH + self.spawn_range_max)
            self.enemy_looking_right = False
        else:
            self.x_pos = randint(-self.spawn_range_max,-self.spawn_range_min)
            self.enemy_looking_right = True

        if self.obstacle_type == 'skeleton':
            self.points = self.skeleton_value
            self.max_health = self.skeleton_max_health * self.time_scalar
            self.current_health = self.max_health
            self.damage = self.skeleton_damage * self.time_scalar
            self.y_pos = GRASS_TOP_Y
            self.obstacle_speed = self.skeleton_speed
            self.obstacle_animation_speed = self.skeleton_walk_animation_speed

            # Skeleton Walk Animation
            self.frames = get_skeleton_walk_arr()
            # Sounds
            self.move_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/FootStep/Retro FootStep Gravel 01.wav')
            self.move_sound.set_volume(OBSTACLE_MOVE_VOLUME)
            self.move_limit = 60
            self.move_timer = self.move_limit
        elif self.obstacle_type == 'bird':
            self.points = self.bird_value
            self.max_health = self.bird_max_health * self.time_scalar
            self.current_health = self.max_health
            self.damage = self.skeleton_damage * self.time_scalar

            self.y_pos = GRASS_TOP_Y - (WIZARD_HEIGHT + (WIZARD_HEIGHT / 4))
            self.obstacle_speed = self.bird_speed
            self.obstacle_animation_speed = self.bird_fly_animation_speed

            # Placeholders
            self.frames = get_bird_fly_arr()

            # Sounds
            self.move_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/Swoosh/Retro Swooosh 07.wav')
            self.move_sound.set_volume(OBSTACLE_MOVE_VOLUME)
            self.move_limit = 60
            self.move_timer = self.move_limit

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
        self.direction_multiplier = 1 if self.enemy_looking_right else -1

        # Outside Source
        self.knockback_direction_multiplier = 0

    # Type
    def get_obstacle_type(self):
        return self.obstacle_type

    def set_obstacle_type(self, new_obstacle_type: str):
        self.obstacle_type = new_obstacle_type

    # Position
    def get_x_pos(self):
        return self.rect.centerx

    def get_y_pos(self):
        return self.rect.centery

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image

    def get_direction_multiplier(self):
        return self.direction_multiplier

    # Health
    def get_current_health(self):
        return self.current_health

    def set_current_health(self, new_health):
        self.current_health = new_health

    def get_max_health(self):
        return self.max_health

    def set_max_health(self, new_max_health):
        self.max_health = new_max_health

    def get_damage(self):
        return self.damage

    def set_damage(self, new_damage):
        self.damage = new_damage

    def get_points(self):
        return self.points

    # Immunity
    def get_immunity(self):
        return self.immunity

    def set_immunity(self,new_immunity):
        self.immunity = new_immunity

    def get_immunity_limit(self):
        return self.IMMUNITY_LIMIT

    def get_immunity_timer(self):
        return self.immunity_timer

    def set_immunity_timer(self,new_immunity_timer):
        self.immunity_timer = new_immunity_timer

    def calculate_immunity(self):
        temp_immunity_timer = self.get_immunity_timer()
        if temp_immunity_timer > 0:
            self.set_immunity(True)
            self.set_immunity_timer(temp_immunity_timer - 1)
        else:
            self.set_immunity(False)

    # Damaged
    def get_damaged_color(self):
        return self.damaged_color

    def set_damaged_color(self,new_damaged_color):
        self.damaged_color = new_damaged_color

    def set_obstacle_color(self,surface, color):
        rect = surface.get_rect()
        surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        surf.fill(color)
        surface.blit(surf, (0, 0), None, pygame.BLEND_ADD)

    # Knockback
    def get_knockback_active(self):
        return self.knockback_active

    def set_knockback_active(self,new_knockback_active):
        self.knockback_active = new_knockback_active

    def get_knockback_value(self):
        return self.knockback_value

    def set_knockback_value(self,new_knockback_value):
        self.knockback_value = new_knockback_value

    def get_knockback_vector(self):
        return self.knockback_vector

    def set_knockback_vector(self,new_knockback_vector):
        self.knockback_vector = new_knockback_vector

    def get_knockback_timer(self):
        return self.knockback_timer

    def set_knockback_timer(self,new_knockback_timer):
        self.knockback_timer = new_knockback_timer

    def get_knockback_direction_multiplier(self):
        return self.knockback_direction_multiplier

    def set_knockback_direction_multiplier(self, new_knockback_direction_multiplier):
        self.knockback_direction_multiplier = new_knockback_direction_multiplier

    def calculate_knockback(self):
        if self.get_knockback_active():
            knockback_time = self.get_knockback_timer()
            if knockback_time > 0:
                self.set_knockback_timer(knockback_time - 1)
            else:
                self.set_knockback_vector(0)
                self.set_knockback_direction_multiplier(0)
                self.set_knockback_active(False)

    # Points
    def get_points(self):
        return self.points

    def set_points(self,new_points):
        self.points = new_points

    # Height
    def get_height(self):
        return self.rect.bottom - self.rect.top

    def animation_state(self):
        self.animation_index += self.obstacle_animation_speed
        if self.animation_index >= len(self.frames): self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)

        if self.enemy_looking_right:
            self.image = pygame.transform.flip(self.image,True,False)

        if self.move_timer >= self.move_limit:
            pygame.mixer.Channel(OBSTACLE_MOVE_CHANNEL).play(self.move_sound)
            self.move_timer = 0
        self.move_timer += 1

    def update(self):
        self.animation_state()
        self.calculate_knockback()
        self.calculate_immunity()
        x_velocity = self.obstacle_speed * self.direction_multiplier
        if self.get_knockback_active():
            knockback_velocity = self.get_knockback_vector() * self.get_knockback_direction_multiplier()
            self.rect.x += x_velocity + knockback_velocity
        else: self.rect.x += x_velocity
        self.destroy()

    def destroy(self):
        if self.rect.x <= -self.despawn_range and not self.enemy_looking_right:
            self.kill()
        if self.rect.x >= WINDOW_WIDTH + self.despawn_range and self.enemy_looking_right:
            self.kill()