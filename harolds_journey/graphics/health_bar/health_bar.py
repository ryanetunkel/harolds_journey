import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, source: pygame.sprite.Sprite, x_pos: int, y_pos: int, current_health: int, max_health: int):
        super().__init__()
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.source = source
        self.current_health = current_health
        self.MAX_HEALTH = max_health
        self.health_percentage = current_health / self.MAX_HEALTH
        self.OUTER_WIDTH = 32
        self.OUTER_HEIGHT = 8
        self.OUTER_THICKNESS = 2
        self.INNER_WIDTH = self.OUTER_WIDTH - self.OUTER_THICKNESS
        self.INNER_HEIGHT = self.INNER_WIDTH - self.OUTER_THICKNESS
        self.outline_color = "#AAAAAA"
        self.inner_color = "#00AA00"
        outline_left = source.left
        outline_top = source.top + self.OUTER_HEIGHT + 2
        inner_left = source.left + self.OUTER_THICKNESS
        inner_top = outline_top - self.OUTER_THICKNESS
        
        self.outline = pygame.draw.rect(self.source, self.outline_color, (outline_left, outline_top, self.OUTER_WIDTH, self.OUTER_HEIGHT), self.OUTER_THICKNESS)
        self.moving_bar = pygame.draw.rect(self.source, self.inner_color, (inner_left, inner_top, self.INNER_WIDTH, self.INNER_HEIGHT))
        
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
    
    def get_health_percentage(self):
        return self.health_percentage
    
    def set_health_percentage(self, new_health_percentage):
        self.health_percentage = new_health_percentage

    def get_color(self):
        if self.health_percentage > 0.5:
            self.inner_color = "#00AA00"
        elif self.health_percentage <= 0.5 and self.health_percentage > 0.25:
            self.inner_color = "#AAAA00"
        elif self.health_percentage <= 0.25:
            self.inner_color = "#AA0000"
    
    def animation_state(self):
        outline_left = self.source.left
        outline_top = self.source.top + self.OUTER_HEIGHT + 2
        inner_left = self.source.left + self.OUTER_THICKNESS
        inner_top = outline_top - self.OUTER_THICKNESS
        self.outline = pygame.draw.rect(self.source, self.outline_color, (outline_left, outline_top, self.OUTER_WIDTH, self.OUTER_HEIGHT), self.OUTER_THICKNESS)
        self.moving_bar = pygame.draw.rect(self.source, self.inner_color, (inner_left, inner_top, self.INNER_WIDTH, self.INNER_HEIGHT))
    
    def update(self):
        self.animation_state()
        if self.current_health <= 0:
            self.current_health = 0
        
    def destroy(self):
        if self.current_health == 0:
            self.kill()