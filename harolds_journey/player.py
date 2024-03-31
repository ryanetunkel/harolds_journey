"""Player Class"""
from random import randint, choice

from global_vars import *
from graphics.wizard.wizard_animation_holder import *

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
        self.fireball_shot = False
        self.start_fireball_animation = False

        # Additional Score
        self.additional_score = 0

        # Death
        self.wizard_dead = False
        self.wizard_start_death = False

        # Health
        self.wizard_max_health = 5
        self.wizard_current_health = self.wizard_max_health
        self.wizard_hurt = False
        self.wizard_max_immunity_frames = 30
        self.wizard_immunity_frames = 0

        # Damage Statistics
        self.WIZARD_STARTING_DAMAGE = 1
        self.wizard_damage_percent = 1
        self.wizard_damage_total = self.WIZARD_STARTING_DAMAGE * self.wizard_damage_percent

        self.WIZARD_STARTING_PIERCING = 1
        self.wizard_piercing_increase = 0
        self.wizard_piercing_total = self.WIZARD_STARTING_PIERCING + self.wizard_piercing_increase

        self.max_fireball_cooldown_time = 60
        self.current_fireball_cooldown = 0

        # Buffs
        self.double_jump = False
        self.double_jump_used = False
        self.shield = False
        self.knockback = False

        # Wizard Idle Animation
        self.wizard_idle = get_wizard_idle_arr()

        # Wizard Secret Idle Animation
        self.wizard_secret_idle = get_wizard_secret_idle_arr()

        # Wizard Walk Animation
        self.wizard_walk = get_wizard_walk_arr()

        # Wizard Jump Animation
        # Ascending - Frames 0-7
        # Top of Jump - Frames 8-14
        # Descending - Frames 15-23
        self.wizard_jump = get_wizard_jump_arr()

        # Wizard Fireball Animation
        self.wizard_fireball = get_wizard_fireball_arr()

        # Wizard Death Animation
        self.wizard_death = get_wizard_death_arr()

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
        self.jump_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/Bounce Jump/Retro Jump Classic 08.wav')
        self.jump_sound.set_volume(JUMP_SOUND_VOLUME)
        self.fireball_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/Blops/Retro Blop 07.wav')
        self.fireball_sound.set_volume(FIREBALL_SOUND_VOLUME)
        self.walk_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/FootStep/Retro FootStep Grass 01.wav')
        self.walk_sound.set_volume(WALK_SOUND_VOLUME)
        self.walk_sound_length = 1 * 40
        self.walk_sound_timer = self.walk_sound_length
        self.secret_sound = pygame.mixer.Sound('harolds_journey/audio/FreeSFX/GameSFX/PowerUp/Retro PowerUP 09.wav')
        self.secret_sound.set_volume(SECRET_SOUND_VOLUME)
        self.secret_sound_timer = 0
        self.secret_sound_length = self.WIZARD_SECRET_ANIMATION_LIMIT
        # self.death_sound = pygame.mixer.Sound('placeholder') # Find Death Sound

    # Positions
    def get_wizard_pos(self):
        return (self.wizard_x_pos,self.wizard_y_pos)

    def get_x_pos(self): # Here for new implementations, eventually switch to just this, just need to replace a lot that uses the old
        return self.rect.centerx

    def set_wizard_x_pos(self,new_wizard_x_pos):
        self.wizard_x_pos = new_wizard_x_pos

    def get_wizard_y_pos(self):
        return self.wizard_y_pos

    def get_y_pos(self): # Here for new implementations, eventually switch to just this, just need to replace a lot that uses the old
        return self.rect.centery

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

    # Buffs
    # Double Jump
    def get_double_jump(self):
        return self.double_jump

    def set_double_jump(self,new_double_jump):
        self.double_jump = new_double_jump
    # Shield
    def get_shield(self):
        return self.shield

    def set_shield(self,new_shield):
        self.shield = new_shield
    # Knockback
    def get_knockback(self):
        return self.knockback

    def set_knockback(self,new_knockback):
        self.knockback = new_knockback

    # Score
    def get_additional_score(self):
        return self.additional_score

    def set_additional_score(self,new_additional_score):
        self.additional_score = new_additional_score

    # Wizard Hurt
    def get_wizard_hurt(self):
        return self.wizard_hurt

    def set_wizard_hurt(self,new_wizard_hurt):
        self.wizard_hurt = new_wizard_hurt

    def set_wizard_color(self,surface, color):
        rect = surface.get_rect()
        surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        surf.fill(color)
        surface.blit(surf, (0, 0), None, pygame.BLEND_ADD)

    # Death
    def get_wizard_dead(self):
        return self.wizard_dead

    def set_wizard_dead(self,new_wizard_dead):
        self.wizard_dead = new_wizard_dead

    # Wizard Game Stats
    # Health
    def get_wizard_max_health(self):
        return self.wizard_max_health

    def set_wizard_max_health(self, new_wizard_max_health):
        self.wizard_max_health = new_wizard_max_health

    def get_wizard_current_health(self):
        return self.wizard_current_health

    def set_wizard_current_health(self, new_wizard_current_health):
        self.wizard_current_health = new_wizard_current_health

    def get_wizard_max_immunity_frames(self):
        return self.wizard_max_immunity_frames

    def set_wizard_max_immunity_frames(self,new_wizard_max_immunity_frames):
        self.wizard_max_immunity_frames = new_wizard_max_immunity_frames

    def get_wizard_immunity_frames(self):
        return self.wizard_immunity_frames

    def set_wizard_immunity_frames(self,new_wizard_immunity_frames):
        self.wizard_immunity_frames = new_wizard_immunity_frames

    def calculate_wizard_immunity_frames(self):
        if self.wizard_immunity_frames > 0:
            self.set_wizard_immunity_frames(self.get_wizard_immunity_frames()-1)
            # If later get immunity frames from a different source, this could cause it to always look like it is caused by damage
        else:
            self.set_wizard_hurt(False)

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
        temp_total = self.WIZARD_STARTING_PIERCING + temp_increase
        self.set_wizard_piercing_total(temp_total)

    # Fireball Stats
    def get_current_fireball_cooldown(self):
        return self.current_fireball_cooldown

    def set_current_fireball_cooldown(self,new_fireball_cooldown):
        self.current_fireball_cooldown = new_fireball_cooldown

    def get_max_fireball_cooldown_time(self):
        return self.max_fireball_cooldown_time

    def set_max_fireball_cooldown_time(self,new_max_fireball_cooldown_time):
        self.max_fireball_cooldown_time = new_max_fireball_cooldown_time

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

    def calculate_wizard_stats(self):
        self.calculate_wizard_damage()
        self.calculate_wizard_piercing()

    def get_height(self):
        return self.rect.bottom - self.rect.top

    def wizard_input(self):
        keys = pygame.key.get_pressed()
        if not self.wizard_dead:
            if keys[jump_button] and (self.rect.bottom >= GRASS_TOP_Y or (self.double_jump and self.rect.bottom < GRASS_TOP_Y and not self.double_jump_used)):
                self.double_jump_used = False
                if self.double_jump:
                    if self.rect.bottom < GRASS_TOP_Y:
                        self.double_jump_used = True
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
            if self.wizard_hurt:
                self.calculate_wizard_immunity_frames()
                # This means if ever get immunity frames from another source they wouldn't be calculated
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
        self.fireball_shot = False
        self.start_fireball_animation = False

        # Additional Score
        self.additional_score = 0

        # Death
        self.wizard_dead = False
        self.wizard_start_death = False

        # Health
        self.wizard_max_health = 5
        self.wizard_current_health = self.wizard_max_health
        self.wizard_hurt = False
        self.wizard_max_immunity_frames = 30
        self.wizard_immunity_frames = 0

        # Damage Statistics
        self.wizard_damage_percent = 1
        self.wizard_damage_total = self.WIZARD_STARTING_DAMAGE * self.wizard_damage_percent

        self.wizard_piercing_increase = 0
        self.wizard_piercing_total = self.WIZARD_STARTING_PIERCING + self.wizard_piercing_increase

        self.max_fireball_cooldown_time = 60
        self.current_fireball_cooldown = 0

        # Buffs
        self.double_jump = False
        self.double_jump_used = False
        self.shield = False
        self.knockback = False

        # Wizard Idle Animation
        self.wizard_idle = get_wizard_idle_arr()

        # Wizard Secret Idle Animation
        self.wizard_secret_idle = get_wizard_secret_idle_arr()

        # Wizard Walk Animation
        self.wizard_walk = get_wizard_walk_arr()

        # Wizard Jump Animation
        # Ascending - Frames 0-7
        # Top of Jump - Frames 8-14
        # Descending - Frames 15-23
        self.wizard_jump = get_wizard_jump_arr()

        # Wizard Fireball Animation
        self.wizard_fireball = get_wizard_fireball_arr()

        # Wizard Death Animation
        self.wizard_death = get_wizard_death_arr()

        self.wizard_index = 0
        self.image = self.wizard_walk[self.wizard_index]
        self.image = pygame.transform.scale(self.image,WIZARD_PIXEL_SIZE)
        self.rect = self.image.get_rect(midbottom = (self.wizard_x_pos,self.wizard_y_pos))
        self.wizard_gravity = 0

        # Secret Animation
        self.wizard_secret_idle_animation_speed = self.WIZARD_IDLE_ANIMATION_SPEED
        self.wizard_secret_animation_timer = self.WIZARD_SECRET_ANIMATION_LIMIT

        # Sounds
        self.walk_sound_length = 1 * 40
        self.walk_sound_timer = self.walk_sound_length
        self.secret_sound_timer = 0
        self.secret_sound_length = self.WIZARD_SECRET_ANIMATION_LIMIT
        # self.death_sound = pygame.mixer.Sound('placeholder') # Find Death Sound
