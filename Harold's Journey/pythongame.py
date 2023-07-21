import pygame
from sys import exit
from random import randint

window_width = 800
window_height = 400
window_size = (window_width,window_height)
wizard_width = 128
wizard_height = 128
wizard_pixel_size = (wizard_height,wizard_width)

jump_button = pygame.K_SPACE
right_button = pygame.K_d
left_button = pygame.K_a
shoot_button = pygame.MOUSEBUTTONDOWN
additional_score = 0
score = 0
animation_speed = 0.1
wizard_flipped = False
wizard_jumping = False

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    # f makes it a string?
    score_surf = test_font.render(f'{current_time + additional_score}', False, "#FCDC4D")
    score_rect = score_surf.get_rect(center = (window_width/2,50))
    screen.blit(score_surf,score_rect)
    # print(current_time)
    return current_time + additional_score

def obstacle_movement(obstacle_list):
    if obstacle_list: # will only run if obstacle_list is not empty
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= obstacle_speed

            if obstacle_rect.bottom == grass_top_y + 8: screen.blit(skeleton_surf,obstacle_rect)
            else: screen.blit(flying_enemy_surf,obstacle_rect)

            # copies existing list if on screen
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

        return obstacle_list
    else: return []

def projectile_movement(projectile_list):
    if projectile_list: # will only run if projectile_list is not empty
        for projectile_rect in projectile_list:
            projectile_rect.x += projectile_speed 
            # The += will need to vary if player starts facing dif directions, 
            # each projectile will need to have a speed associated with it 
            # and it needs to be negative or positive depending

            # can add in ifs associated with position to make different projectiles appear
            screen.blit(fireball_surf,projectile_rect)

            projectile_list = [projectile for projectile in projectile_list if (projectile.x > 0 and projectile.x < 800)]

        return projectile_list
    else: return []

def wizard_collisions(wizard,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if wizard.colliderect(obstacle_rect): return False
    return True

def projectile_collisions(projectiles,obstacles):
    collisions = 0
    if projectiles and obstacles:
        for projectile in projectiles:
            for obstacle in obstacles:
                if projectile.colliderect(obstacle):
                    projectiles.remove(projectile)
                    obstacles.remove(obstacle)
                    collisions += 1
                    # ********** For some reason it can't see these values, unsure why
                    # ********** Also the game won't restart properly after the 
                    # first game is played while open
    return collisions

    # not including checking if fireball_start_speed is 0 
    # might make it so can still damage enemies if they 
    # walk into you but if you die first it doesn't really 
    # matter - could affect the score though

def wizard_animation():
    global wizard_surf, wizard_index, wizard_jumping

    if wizard_rect.bottom < grass_top_y and wizard_jumping: # and add landing tracker this would be if it is off
        # jump (first half)
        wizard_index += animation_speed # speed of animation, adjust as needed
        if wizard_index >= len(wizard_jump):wizard_index = 0
        wizard_surf = wizard_jump[int(wizard_index)]
        wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
        # this is it raw with no adjustment
        # below is the ideal
        # wizard_surf = wizard_jump[0,7] # can't just do this need to go through
        # 8 - 14 need to be when reach peak, prob cut and edit which goes where
        # and add landing tracker this would be if landed
        # landing animation for a few frames via timer and then when ends revert to idle
        
    elif wizard_x_velocity != 0 and wizard_rect.bottom >= grass_top_y:
        if moving_right:
            wizard_index += animation_speed # speed of animation, adjust as needed
            if wizard_index >= len(wizard_walk):wizard_index = 0
            wizard_surf = wizard_walk[int(wizard_index)]
            wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
            # walk and point direction right (implement tracker for if flipped)
        else:
            wizard_index += animation_speed # speed of animation, adjust as needed
            if wizard_index >= len(wizard_walk):wizard_index = 0
            wizard_surf = wizard_walk[int(wizard_index)]
            wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
            wizard_surf = pygame.transform.flip(wizard_surf,True,False)
            # walk and point direction left
    # elif event.type == pygame.KEYDOWN and event.key == shoot_button:
    #     # wizard fireball animation
    #     wizard_index += animation_speed # speed of animation, adjust as needed
    #     if wizard_index >= len(wizard_fireball):wizard_index = 0
    #     wizard_surf = wizard_idle[int(wizard_index)]
    elif wizard_x_velocity == 0:
        wizard_index += animation_speed # speed of animation, adjust as needed
        if wizard_index >= len(wizard_idle):wizard_index = 0
        wizard_surf = wizard_idle[int(wizard_index)]
        wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
        # idle animation
        # start timer that last for a few rounds of idle animation until would do the second
    
    # Walking animation if on floor and moving side to side
    # Idle animation if not moving or attacking
    # Jumping animation if not on the floor
    # Fireball animation if attacking
    # Death animation if game was ended - rn game ends instantly so can't be implemented
    # Damage animation if hit and not killed - rn can't do cuz no health

# can't implement health and damage sources as the variables aren't attached 
# to the individual projectiles and obstacles, they are global for all of them
# need to implement classes for that I think 
# def deal_damage(damage_source, target):
#     target.obstacle_health -= damage_source.projectile_damage
#     if target.obstacle_health <= 0:
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.obstacle_health > 0]
#         projectile_list = [projectile for projectile in projectile_list if (projectile.x > 0 and projectile.x < 800)]

def fireball_animation():
    global fireball_surf, fireball_index
    
    fireball_index += animation_speed # speed of animation, adjust as needed
    if fireball_index >= len(fireball_move):fireball_index = 0
    fireball_surf = fireball_move[int(fireball_index)]
    fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)

def harold_animation():
    global harold_surf, harold_index

    harold_index += animation_speed # speed of animation, adjust as needed
    if harold_index >= len(harold_idle):harold_index = 0
    harold_surf = harold_idle[int(harold_index)]
    harold_surf = pygame.transform.scale_by(harold_surf,3/2)

# def skeleton_animation(): # WIP

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Harold\'s Journey')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Harold\'s Journey/font/Pixeltype.ttf',50)
pygame_icon = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
pygame.display.set_icon(pygame_icon)
game_active = False
start_time = 0

sky_surf = pygame.image.load('Harold\'s Journey/graphics/Background.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf,window_size)

grass_top_y = 371
ground_surf = pygame.image.load('Harold\'s Journey/graphics/Grass.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf,window_size)

# ********Hitbox is really big compared to sprite, investigate
# Obstacles
# These might not all be universal, especially health and speed, will be varied
obstacle_speed = 2
obstacle_spawn_frequency = 1500 # In milliseconds, 1000 = 1 sec
obstacle_health = 1
obstacle_points = 5

skeleton_x_pos = randint(window_width + 100,window_width + 300)
skeleton_y_pos = grass_top_y + 8

# Skeleton Walk Animation
skeleton_animation_speed = 50 # milliseconds
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
skeleton_walk = [skeleton_walk_00, skeleton_walk_01, skeleton_walk_02, skeleton_walk_03,
                 skeleton_walk_04, skeleton_walk_05, skeleton_walk_06, skeleton_walk_07,
                 skeleton_walk_08, skeleton_walk_09, skeleton_walk_10, skeleton_walk_11,
                 skeleton_walk_12]
skeleton_index = 0
skeleton_surf = skeleton_walk[skeleton_index]
skeleton_surf = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png')
skeleton_surf = pygame.transform.scale(skeleton_surf,wizard_pixel_size)
skeleton_rect = skeleton_surf.get_rect(midbottom = (skeleton_x_pos,skeleton_y_pos))

flying_enemy_animation_speed = 50 # milliseconds
flying_enemy_x_pos = randint(window_width + 100,window_width + 300)
flying_enemy_y_pos = grass_top_y - 100
flying_enemy_surf = pygame.image.load('Harold\'s Journey/graphics/enemies/skeleton/skeleton_walk_animation/skeleton_walk_00.png')
flying_enemy_surf = pygame.transform.scale(flying_enemy_surf,wizard_pixel_size)
flying_enemy_rect = flying_enemy_surf.get_rect(midbottom = (flying_enemy_x_pos,flying_enemy_y_pos))

obstacle_rect_list = []

# Player
wizard_start_x_pos = 80
wizard_start_y_pos = grass_top_y
wizard_x_pos = wizard_start_x_pos
wizard_speed = 4
wizard_x_velocity = 0
wizard_y_pos = wizard_start_y_pos
wizard_gravity = 0
gravity_acceleration = -20
moving_right = True

# Wizard Idle Animation
wizard_idle_00 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_00.png').convert_alpha()
wizard_idle_01 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_01.png').convert_alpha()
wizard_idle_02 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_02.png').convert_alpha()
wizard_idle_03 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_03.png').convert_alpha()
wizard_idle_04 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_04.png').convert_alpha()
wizard_idle_05 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_05.png').convert_alpha()
wizard_idle_06 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_06.png').convert_alpha()
wizard_idle_07 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_07.png').convert_alpha()
wizard_idle_08 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_08.png').convert_alpha()
wizard_idle_09 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_09.png').convert_alpha()
wizard_idle_10 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_10.png').convert_alpha()
wizard_idle_11 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_11.png').convert_alpha()
wizard_idle_12 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_12.png').convert_alpha()
wizard_idle_13 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_13.png').convert_alpha()
wizard_idle_14 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_14.png').convert_alpha()
wizard_idle_15 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_15.png').convert_alpha()
wizard_idle_16 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_16.png').convert_alpha()
wizard_idle_17 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_17.png').convert_alpha()
wizard_idle_18 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_18.png').convert_alpha()
wizard_idle_19 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_19.png').convert_alpha()
wizard_idle_20 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_20.png').convert_alpha()
wizard_idle_21 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_21.png').convert_alpha()
wizard_idle_22 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_22.png').convert_alpha()
wizard_idle_23 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_23.png').convert_alpha()
wizard_idle = [wizard_idle_00, wizard_idle_01, wizard_idle_02, wizard_idle_03,
               wizard_idle_04, wizard_idle_05, wizard_idle_06, wizard_idle_07,
               wizard_idle_08, wizard_idle_09, wizard_idle_10, wizard_idle_11,
               wizard_idle_12, wizard_idle_13, wizard_idle_14, wizard_idle_15,
               wizard_idle_16, wizard_idle_17, wizard_idle_18, wizard_idle_19,
               wizard_idle_20, wizard_idle_21, wizard_idle_22, wizard_idle_23]

# Wizard Walk Animation
wizard_walk_0 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_0.png').convert_alpha()
wizard_walk_1 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_1.png').convert_alpha()
wizard_walk_2 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_2.png').convert_alpha()
wizard_walk_3 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_3.png').convert_alpha()
wizard_walk_4 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_4.png').convert_alpha()
wizard_walk_5 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_5.png').convert_alpha()
wizard_walk_6 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_6.png').convert_alpha()
wizard_walk_7 = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_walk_animation/wizard_walk_7.png').convert_alpha()
wizard_walk = [wizard_walk_0, wizard_walk_1, wizard_walk_2, wizard_walk_3,
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
wizard_jump = [wizard_jump_00, wizard_jump_01, wizard_jump_02, wizard_jump_03,
               wizard_jump_04, wizard_jump_05, wizard_jump_06, wizard_jump_07,
               wizard_jump_08, wizard_jump_09, wizard_jump_10, wizard_jump_11,
               wizard_jump_12, wizard_jump_13, wizard_jump_14, wizard_jump_15,
               wizard_jump_16, wizard_jump_17, wizard_jump_18, wizard_jump_19,
               wizard_jump_20, wizard_jump_21, wizard_jump_22, wizard_jump_23]
wizard_index = 0
wizard_surf = wizard_walk[wizard_index]
wizard_surf = pygame.transform.scale(wizard_surf,wizard_pixel_size)
wizard_rect = wizard_surf.get_rect(midbottom = (wizard_x_pos,wizard_y_pos))


# Projectiles
# These might not all be universal, especially damage and speed, will be varied
projectile_speed = 5
projectile_damage = 1

# Fireball
fireball_x_start = wizard_rect.right - 20
fireball_y_start = wizard_rect.centery + 24

fireball_x_pos = fireball_x_start
fireball_y_pos = fireball_y_start

fireball_x_start_speed = 0

fireball_speed = 5
fireball_gravity_when_held = 0

fireball_cooldown_time = 60
fireball_cooldown = 0
fireball_hit = False

fireball_damage = 1

# Fireball Transition Animation
fireball_trans_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_0.png').convert_alpha()
fireball_trans_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_1.png').convert_alpha()
fireball_trans_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_2.png').convert_alpha()
fireball_trans_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_transition_animation/fireball_trans_3.png').convert_alpha()
fireball_trans = [fireball_trans_0, fireball_trans_1, fireball_trans_2, fireball_trans_3]

# Fireball Movement Animation
fireball_move_0 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_0.png').convert_alpha()
fireball_move_1 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_1.png').convert_alpha()
fireball_move_2 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_2.png').convert_alpha()
fireball_move_3 = pygame.image.load('Harold\'s Journey/graphics/fireball/fireball_movement_animation/fireball_move_3.png').convert_alpha()
fireball_move = [fireball_move_0, fireball_move_1, fireball_move_2, fireball_move_3]

fireball_index = 0
fireball_surf = fireball_move[fireball_index]
fireball_surf = pygame.transform.scale(fireball_surf,wizard_pixel_size)
fireball_rect = fireball_surf.get_rect(center = (fireball_x_pos,fireball_y_pos))

# class Fireball:
#     def __init__(x_start, y_start, x_speed, surf):
#         self.x_start = x_start
#         self.y_start = y_start
#         self.x_speed = x_speed
#         self.surf = surf

projectile_rect_list = []

# Harold
harold_start_x_pos = wizard_rect.centerx
harold_start_y_pos = wizard_rect.top + 28 # pixels at this scale based on wizard are 4 pixels each
harold_x_pos = harold_start_x_pos
harold_speed = wizard_speed
harold_x_velocity = 0
harold_y_pos = harold_start_y_pos
harold_gravity = 0

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
harold_idle = [harold_idle_00, harold_idle_01, harold_idle_02, harold_idle_03,
               harold_idle_04, harold_idle_05, harold_idle_06, harold_idle_07,
               harold_idle_08, harold_idle_09, harold_idle_10, harold_idle_11,
               harold_idle_12, harold_idle_13, harold_idle_14, harold_idle_15,
               harold_idle_16, harold_idle_17, harold_idle_18, harold_idle_19,
               harold_idle_20]

# harold_surf = pygame.transform.flip(harold_surf, True, False)
harold_index = 0
harold_surf = harold_idle[harold_index]
harold_surf = pygame.transform.scale_by(harold_surf,3/2)
harold_rect = harold_surf.get_rect(midbottom = (harold_x_pos,harold_y_pos))


# Intro Screen
wizard_title_surf = pygame.image.load('Harold\'s Journey/graphics/wizard/wizard_idle_animation_1/wizard_idle_00.png').convert_alpha()
wizard_title_surf = pygame.transform.scale(wizard_title_surf,(192,192))
wizard_title_rect = wizard_title_surf.get_rect(center = (400,250))

harold_title_surf = pygame.image.load('Harold\'s Journey/graphics/harold/harold_idle_animation/harold_idle_00.png').convert_alpha()
# harold_title_surf = pygame.transform.flip(harold_title_surf, True, False)
harold_title_surf = pygame.transform.scale_by(harold_title_surf,2.25)
harold_title_rect = harold_title_surf.get_rect(midbottom = (wizard_title_rect.centerx,wizard_title_rect.top + 42))

title_game_name_surf = test_font.render('Harold\'s Journey',False,"#FCDC4D")
title_game_name_surf = pygame.transform.scale_by(title_game_name_surf,3/2)
title_game_name_rect = title_game_name_surf.get_rect(center = (400,70))

title_info_surf = test_font.render('Press any key or click to Start',False,"#FCDC4D")
title_info_rect = title_info_surf.get_rect(center = (wizard_title_rect.centerx,wizard_title_rect.centery + 120))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # + 1 to avoid events taking previous numbers by default
pygame.time.set_timer(obstacle_timer,obstacle_spawn_frequency)

# Skeleton Animation Timer
skeleton_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(skeleton_animation_timer,skeleton_animation_speed)

# Flying Enemy Animation Timer
flying_enemy_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(flying_enemy_animation_timer,flying_enemy_animation_speed)

# pygame.draw exists, can do rects, circles, lines, points, ellipses etc
while True:
    for event in pygame.event.get(): # gets all the events
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            exit() # breaks out of the while True loop
        # if event.type == pygame.MOUSEMOTION: # MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
        #     if wizard_rect.collidepoint(event.pos): print ('collision')
       
        if game_active:
            # Fireballs come off cooldown or instantly cooldown if you hit an enemy with one
            if event.type == shoot_button and (fireball_cooldown == 0 or fireball_hit):
                fireball_cooldown = fireball_cooldown_time
                fireball_hit = False
                projectile_rect_list.append(fireball_surf.get_rect(center = (wizard_rect.right - 20,wizard_rect.centery + 24)))

            if event.type == pygame.KEYDOWN:
                if event.key == jump_button and wizard_rect.bottom >= grass_top_y:  
                    wizard_jumping = True
                    wizard_gravity = gravity_acceleration
                    harold_gravity = gravity_acceleration
                if event.key == right_button and wizard_rect.x + wizard_width + wizard_x_velocity < window_width:
                    wizard_x_velocity = wizard_speed
                    harold_x_velocity = harold_speed
                    moving_right = True
                if event.key == left_button and wizard_rect.x - wizard_x_velocity > 0:
                    wizard_x_velocity = -wizard_speed
                    harold_x_velocity = -harold_speed
                    moving_right = False
            if event.type == pygame.KEYUP:
                if event.key == right_button:
                    wizard_x_velocity = 0
                    harold_x_velocity = 0
                if event.key == left_button:
                    wizard_x_velocity = 0
                    harold_x_velocity = 0

            # Obstacle Timer Event Detection
            if event.type == obstacle_timer: # moved from bottom compared to video for better format
                if randint(0,2): # gives values of either 0 or 1 which are false or true
                    obstacle_rect_list.append(skeleton_surf.get_rect(midbottom = (skeleton_x_pos,skeleton_y_pos)))
                else:
                    obstacle_rect_list.append(flying_enemy_surf.get_rect(midbottom = (flying_enemy_x_pos,flying_enemy_y_pos)))
            if event.type == skeleton_animation_timer:
                # Horrible Coding
                if skeleton_index == 0: skeleton_index = 1
                elif skeleton_index == 1: skeleton_index = 2
                elif skeleton_index == 2: skeleton_index = 3
                elif skeleton_index == 3: skeleton_index = 4
                elif skeleton_index == 4: skeleton_index = 5
                elif skeleton_index == 5: skeleton_index = 6
                elif skeleton_index == 6: skeleton_index = 7
                elif skeleton_index == 7: skeleton_index = 8
                elif skeleton_index == 8: skeleton_index = 9
                elif skeleton_index == 9: skeleton_index = 10
                elif skeleton_index == 10: skeleton_index = 11
                elif skeleton_index == 11: skeleton_index = 12
                elif skeleton_index == 12: skeleton_index = 0
                skeleton_surf = skeleton_walk[skeleton_index]
            # if event.type == flying_enemy_animation_timer:
            #     # WIP - add when have animation 

        else:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                additional_score = 0


    # Active Game
    if game_active:    
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,0))
        # pygame.draw.line(screen,"#FCDC4D",score_rect.bottomleft,score_rect.bottomright,3)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # enemy_rect.x -= 4

        if fireball_cooldown != 0:
            fireball_cooldown -= 1

        # Wizard
        wizard_gravity += 1
        wizard_rect.y += wizard_gravity
        wizard_rect.x += wizard_x_velocity
        # Harold
        harold_gravity += 1
        harold_rect.y += harold_gravity
        harold_rect.x += harold_x_velocity

        if wizard_rect.bottom >= grass_top_y: 
            wizard_rect.bottom = grass_top_y
            harold_rect.bottom = harold_start_y_pos
        wizard_animation()
        screen.blit(wizard_surf,wizard_rect)

        fireball_animation()
        if fireball_x_start_speed != 0:
            screen.blit(fireball_surf,fireball_rect)
        
        harold_animation()
        screen.blit(harold_surf,harold_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Projectile Movement
        projectile_rect_list = projectile_movement(projectile_rect_list)

        # Collision between Wizard and Enemies
        game_active = wizard_collisions(wizard_rect,obstacle_rect_list)

        # Collision between Enemies and Projectiles
        collisions = projectile_collisions(projectile_rect_list,obstacle_rect_list)
        additional_score += (collisions * obstacle_points)
        if collisions:
            fireball_x_start_speed = 0
            fireball_hit = True
        collisions = 0

    # Menu Screen
    else:
        screen.fill('#54428E')
        wizard_animation()
        screen.blit(wizard_title_surf,wizard_title_rect)
        harold_animation()
        screen.blit(harold_title_surf,harold_title_rect)
        
        screen.blit(title_info_surf,title_info_rect)

        obstacle_rect_list.clear()
        projectile_rect_list.clear()

        wizard_rect.midbottom = (wizard_start_x_pos,wizard_start_y_pos)
        wizard_gravity = 0
        wizard_x_velocity = 0

        harold_rect.midbottom = (harold_start_x_pos,harold_start_y_pos)
        harold_gravity = 0
        harold_x_velocity = 0

        score_message_surf = test_font.render(f'Score: {score}',False,"#FCDC4D")
        score_message_surf = pygame.transform.scale_by(score_message_surf,3/2)
        score_message_rect = score_message_surf.get_rect(center = (400,70))

        if score == 0:
            screen.blit(title_game_name_surf,title_game_name_rect)

        else:
            screen.blit(score_message_surf,score_message_rect)

    pygame.display.update()
    clock.tick(60)