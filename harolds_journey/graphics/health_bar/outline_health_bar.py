import pygame

from global_vars import *
from graphics.health_bar.health_bar_animation_holder import *
class OutlineHealthBar(pygame.sprite.Sprite):
    def __init__(self, health_bar: pygame.sprite.Sprite, x_pos: int, y_pos: int):
        super().__init__()

        self.health_bar = health_bar
        self.x_pos = x_pos
        self.OUTER_WIDTH = 18
        self.OUTER_HEIGHT = 6
        self.y_pos = y_pos + (self.health_bar.get_source().get_height() / 2) + self.OUTER_HEIGHT + 2
        inner_centerx = self.x_pos
        inner_centery = self.y_pos + (WIZARD_HEIGHT / 2) + ((self.OUTER_HEIGHT - 2) * 2) # Just to move it up a bit
        self.image = get_outline_health_bar()
        self.image = pygame.transform.scale(self.image,(self.OUTER_WIDTH * 4, self.OUTER_HEIGHT * 2))
        self.rect = self.image.get_rect(center = (inner_centerx,inner_centery))
        # self.moving_bar = pygame.draw.rect(screen, self.inner_color, (inner_left, inner_top, self.INNER_WIDTH, self.INNER_HEIGHT))

    # Coords
    def get_x_pos(self):
        return self.x_pos

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos

    def get_health_bar(self):
        return self.health_bar

    def animation_state(self):
        temp_source = self.health_bar.get_source()
        inner_centerx = temp_source.get_x_pos()
        inner_centery = temp_source.get_y_pos() + (temp_source.get_height() / 2) + 8
        self.image = get_outline_health_bar()
        self.image = pygame.transform.scale(self.image,(self.OUTER_WIDTH * 4, self.OUTER_HEIGHT * 2))
        self.rect = self.image.get_rect(center = (inner_centerx,inner_centery))

    def update(self):
        self.animation_state()
        self.destroy()

    def destroy(self):
        if self.health_bar.get_current_health() == 0:
            self.kill()