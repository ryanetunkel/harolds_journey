from global_vars import *

from pickup import *
import spritesheet

class Buff(pygame.sprite.Sprite):
    def __init__(self, type: str, x_pos: int, y_pos: int):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.gravity_acceleration = GLOBAL_GRAVITY
        self.y_velocity = -20 * GLOBAL_SCALAR
        self.BUFF_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60 / GLOBAL_SCALAR
        self.lifetime = self.LIFETIME_LIMIT
        self.speed = 2 * GLOBAL_SCALAR
        self.default_animation_timer_max = 60
        self.default_animation_timer = self.default_animation_timer_max

        if type == "double_jump":
            self.type = "double_jump"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/double_jump_buff/double_jump_buff_spritesheet.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10), colorkey=(0, 0, 0))
            self.image_coords = [
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(10, 0, 10,10),(20, 0, 10,10),
                (0, 10, 10,10),(10, 10, 10,10),(20, 10, 10,10),
                (10, 20, 10,10),(20, 20, 10,10),
            ]
            # Load two images into an array, their transparent bit is (0, 0, 0)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(0, 0, 0))

        elif type == "shield":
            self.type = "shield"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/shield_buff/shield_buff_spritesheet.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10), colorkey=(0, 0, 0))
            self.image_coords = [
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(10, 0, 10,10),(20, 0, 10,10),
                (0, 10, 10,10),(10, 10, 10,10),(20, 10, 10,10),
                (10, 20, 10,10),(20, 20, 10,10),
            ]
            # Load two images into an array, their transparent bit is (0, 0, 0)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(0, 0, 0))

        elif type == "knockback":
            self.type = "knockback"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/knockback_buff/knockback_buff_spritesheet.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10), colorkey=(0, 0, 0))
            self.image_coords = [
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(0, 0, 10, 10),(0, 0, 10, 10),
                (0, 0, 10, 10),(10, 0, 10,10),(20, 0, 10,10),
                (0, 10, 10,10),(10, 10, 10,10),(20, 10, 10,10),
                (10, 20, 10,10),(20, 20, 10,10),
            ]
            # Load two images into an array, their transparent bit is (0, 0, 0)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(0, 0, 0))
        self.image = self.default_image
        self.animation_index = 0
        self.scale = 3 * GLOBAL_SCALAR
        self.image = pygame.transform.scale_by(self.image,self.scale)
        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

    def get_type(self):
        return self.type

    def get_default_image(self):
        return self.default_image

    def off_screen_recovery(self):
        # If when readjusting the camera to follow player the buffs come with it, this is why
        if self.rect.x >= WINDOW_WIDTH:
            self.rect.x -= self.speed
        if self.rect.y <= 0:
            self.rect.x += self.speed

    def apply_gravity(self):
        self.y_velocity += self.gravity_acceleration
        self.rect.y += self.y_velocity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y

    def animation_state(self):
        self.animation_index += self.BUFF_ANIMATION_SPEED
        if self.animation_index >= len(self.frames) - 1: self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale_by(self.image,self.scale)

    def update(self):
        self.apply_gravity()
        self.off_screen_recovery()
        self.animation_state()
