from global_vars import *

from pickup import *
import spritesheet

class Buff(Pickup):
    def __init__(self, type: str, x_pos: int, y_pos: int):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.gravity_intensity = 1
        self.gravity = GLOBAL_GRAVITY
        self.PICKUP_ANIMATION_SPEED = 0.2
        self.LIFETIME_LIMIT = 10 * 60
        self.lifetime = self.LIFETIME_LIMIT
        self.speed = 2

        if type == "double_jump":
            self.type = "double_jump"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/double_jump_buff/double_jump_buff.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10))
            self.image = self.default_image
            self.image_coords = [
                (11, 0, 10,10),(21, 0, 10,10),
                (0, 11, 10,10),(11, 11, 10,10),(21, 11, 10,10),
                (11, 21, 10,10),(21, 21, 10,10),
            ]
            self.frames = []
            # Load two images into an array, their transparent bit is (255, 255, 255)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(255, 255, 255))

        elif type == "shield":
            self.type = "shield"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/shield_buff/shield_buff.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10))
            self.image = self.default_image
            self.image_coords = [
                (11, 0, 10,10),(21, 0, 10,10),
                (0, 11, 10,10),(11, 11, 10,10),(21, 11, 10,10),
                (11, 21, 10,10),(21, 21, 10,10),
            ]
            self.frames = []
            # Load two images into an array, their transparent bit is (255, 255, 255)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(255, 255, 255))

        elif type == "knockback":
            self.type = "knockback"
            self.sprite_sheet = spritesheet.spritesheet("harolds_journey/graphics/buffs/knockback_buff/knockback_buff.png")
            self.default_image = self.sprite_sheet.image_at((0, 0, 10, 10))
            self.image = self.default_image
            self.image_coords = [
                (11, 0, 10,10),(21, 0, 10,10),
                (0, 11, 10,10),(11, 11, 10,10),(21, 11, 10,10),
                (11, 21, 10,10),(21, 21, 10,10),
            ]
            self.frames = []
            # Load two images into an array, their transparent bit is (255, 255, 255)
            self.frames = self.sprite_sheet.images_at(self.image_coords, colorkey=(255, 255, 255))

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
        self.animation_index += self.PICKUP_ANIMATION_SPEED
        if self.animation_index >= len(self.frames): self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]
        self.image = pygame.transform.scale_by(self.image,3)

    def update(self):
        self.apply_gravity()
        self.animation_state()
        self.destroy()

    def get_bonus(self): # Bonuses are irrelevant
        return

    def destroy(self): # Intentionally stays so doesn't despawn
        return