import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, source: pygame.sprite.Sprite, x_pos: int, y_pos: int, current_health: int, max_health: int):
        super().__init__()
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.source = source
        self.current_health = current_health
        MAX_HEALTH = max_health
        self.health_percentage = current_health / MAX_HEALTH
        OUTER_WIDTH = 32
        OUTER_HEIGHT = 8
        OUTER_THICKNESS = 2
        INNER_WIDTH = OUTER_WIDTH - OUTER_THICKNESS
        INNER_HEIGHT = INNER_WIDTH - OUTER_THICKNESS
        outline_color = "#AAAAAA"
        inner_color = "#00AA00"
        outline_left = source.left
        outline_top = source.top + OUTER_HEIGHT + 2
        inner_left = source.left + OUTER_THICKNESS
        inner_top = outline_top - OUTER_THICKNESS
        # keep working
        
        self.outline = pygame.draw.rect(self.source, outline_color, (outline_left, outline_top, OUTER_WIDTH, OUTER_HEIGHT), OUTER_THICKNESS)
        self.moving_bar = pygame.draw.rect(self.source, inner_color, (inner_left, inner_top, INNER_WIDTH, INNER_HEIGHT))
        
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

    
    def animation_state(self):
        self.x_pos = self.source.centerx
        self.y_pos = self.source.topy + 4
    
    def update(self):
        self.animation_state()
        if self.current_health <= 0:
            self.current_health = 0
        
    def destroy(self):
        if self.current_health == 0:
            self.kill()