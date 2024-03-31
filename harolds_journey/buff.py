from global_vars import *

from pickup import *
import spritesheet

class Buff(pygame.sprite.Sprite):
    def __init__(self, type: str, x_pos: int, y_pos: int):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.gravity_intensity = 1
        self.gravity = GLOBAL_GRAVITY
        self.BUFF_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60
        self.lifetime = self.LIFETIME_LIMIT
        self.speed = 2
        self.default_animation_timer_max = 60
        self.default_animation_timer = self.default_animation_timer_max

        if type == "double_jump":
            self.type = "double_jump"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/double_jump_buff/double_jump_buff.png")
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
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/shield_buff/shield_buff.png")
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
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/knockback_buff/knockback_buff.png")
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
        self.image = pygame.transform.scale_by(self.image,3)
        self.rect = self.image.get_rect(center = (self.x_pos,self.y_pos))

    def apply_gravity(self):
        self.gravity += self.gravity_intensity
        self.rect.y += self.gravity
        if self.rect.bottom >= GRASS_TOP_Y: self.rect.bottom = GRASS_TOP_Y
        # If when readjusting the camera to follow player the buffs come with it, this is why
        if self.rect.x >= WINDOW_WIDTH:
            self.rect.x -= self.speed
        if self.rect.y <= 0:
            self.rect.x += self.speed

    def animation_state(self):
        self.animation_index += self.BUFF_ANIMATION_SPEED
        if self.animation_index >= len(self.frames) - 1:self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale_by(self.image,3)

    def update(self):
        self.apply_gravity()
        self.animation_state()
