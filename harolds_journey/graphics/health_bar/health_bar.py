import pygame

from global_vars import *
from graphics.health_bar.health_bar_animation_holder import *
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, source: pygame.sprite.Sprite, current_health: int, max_health: int):
        super().__init__()
        
        self.source = source
        self.x_pos = self.source.get_x_pos()
        self.INNER_WIDTH = 16
        self.INNER_HEIGHT = 4
        self.y_pos = self.source.get_y_pos() + (source.get_height() / 2) + self.INNER_HEIGHT
        self.current_health = current_health
        self.max_health = max_health
        self.health_percentage = current_health / self.max_health
        inner_centerx = self.x_pos
        inner_centery = self.y_pos + (WIZARD_HEIGHT / 2) + (self.INNER_HEIGHT * 2) # Just to move it up a bit
        self.image = get_green_health_bar()
        self.image = pygame.transform.scale(self.image,(self.INNER_WIDTH * 4, self.INNER_HEIGHT * 2))
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
    
    def get_current_health(self):
        return self.current_health
    
    def set_current_health(self, new_current_health):
        self.current_health = new_current_health
        
    def get_max_health(self):
        return self.max_health
    
    def set_max_health(self, new_max_health):
        self.max_health = new_max_health
    
    def get_health_percentage(self):
        return self.health_percentage
    
    def set_health_percentage(self, new_health_percentage):
        self.health_percentage = new_health_percentage
    
    def get_source(self):
        return self.source
    
    def animation_state(self):
        inner_centerx = self.source.get_x_pos()
        inner_centery = self.source.get_y_pos() + (WIZARD_HEIGHT / 2) + (self.INNER_HEIGHT * 2)
        if self.health_percentage > 0.5:
            self.image = get_green_health_bar()
        elif self.health_percentage <= 0.5 and self.health_percentage > 0.25:
            self.image = get_yellow_health_bar()
        elif self.health_percentage <= 0.25:
            self.image = get_red_health_bar()
        # Calculating position
        # The size of it is always changing in fluctuation with the health_percentage
        self.image = pygame.transform.scale(self.image,(self.INNER_WIDTH * 4 * self.health_percentage, self.INNER_HEIGHT * 2))
        self.rect = self.image.get_rect(center = (inner_centerx,inner_centery))      
        # self.moving_bar = pygame.draw.rect(screen, self.inner_color, (inner_left, inner_top, self.INNER_WIDTH, self.INNER_HEIGHT))
    
    def update(self):
        self.set_current_health(self.source.get_current_health())
        self.set_max_health(self.source.get_max_health())
        self.set_health_percentage(self.current_health / self.max_health)
        self.animation_state()
        if self.current_health <= 0:
            self.current_health = 0
        self.destroy()
        
    def destroy(self):
        if self.current_health == 0:
            self.kill()