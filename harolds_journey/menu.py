"""Contains all menu-related items"""

from controls import *
from global_vars import *

# Main Menu Screen
MAIN_MENU = 1
STATISTICS_MENU = 2
SETTINGS_MENU = 3
SOUNDS_MENU = 4
CONTROLS_MENU = 5
DISPLAY_MENU = 6
menu_section = MAIN_MENU
CENTER_SCREEN = WINDOW_WIDTH / 2
# Game Title
main_menu_title_start_x_pos = CENTER_SCREEN
main_menu_title_start_y_pos = 42/400 * WINDOW_HEIGHT
main_menu_title_start_pos = (main_menu_title_start_x_pos,main_menu_title_start_y_pos)
main_menu_title_scale = 1.25 * WINDOW_SCALAR
main_menu_title_surf = test_font.render("Harold\'s Journey",False,"#FCDC4D")
main_menu_title_surf = pygame.transform.scale_by(main_menu_title_surf,main_menu_title_scale)
main_menu_title_rect = main_menu_title_surf.get_rect(center = main_menu_title_start_pos)

# Wizard on Menu Screen
main_menu_wizard_start_x_pos = CENTER_SCREEN
main_menu_wizard_start_y_pos = main_menu_title_start_y_pos + 1.25 * (128 * WINDOW_SCALAR)
main_menu_wizard_hat_size = 32 * WINDOW_SCALAR
main_menu_wizard_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png").convert_alpha()
main_menu_wizard_height_by_scale = 128 * WINDOW_SCALAR
main_menu_wizard_width_by_scale = 128 * WINDOW_SCALAR
main_menu_wizard_size_by_scale = (main_menu_wizard_height_by_scale,main_menu_wizard_width_by_scale)
main_menu_wizard_surf = pygame.transform.scale(main_menu_wizard_surf,main_menu_wizard_size_by_scale)
main_menu_wizard_rect = main_menu_wizard_surf.get_rect(midbottom = (main_menu_wizard_start_x_pos,main_menu_wizard_start_y_pos))

# Harold on Menu Screen
main_menu_harold_start_x_pos = CENTER_SCREEN
main_menu_harold_start_y_pos = main_menu_wizard_rect.top + main_menu_wizard_hat_size
main_menu_harold_surf = pygame.image.load("harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png").convert_alpha()
main_menu_harold_height_by_scale = main_menu_wizard_height_by_scale * 3/8
main_menu_harold_width_by_scale = main_menu_wizard_width_by_scale * 3/8
main_menu_harold_size_by_scale = (main_menu_harold_height_by_scale,main_menu_harold_width_by_scale)
main_menu_harold_surf = pygame.transform.scale(main_menu_harold_surf,main_menu_harold_size_by_scale)
main_menu_harold_rect = main_menu_harold_surf.get_rect(midbottom = (main_menu_harold_start_x_pos,main_menu_harold_start_y_pos))

# Buttons
button_when_big_scale = 1.1
# Main Menu
# Start Button
main_menu_start_button_start_x_pos = CENTER_SCREEN
main_menu_start_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
main_menu_start_button_start_pos = (main_menu_start_button_start_x_pos,main_menu_start_button_start_y_pos)
main_menu_start_button_surf = test_font.render("Start Game",False,"#FCDC4D")
main_menu_start_button_scale = WINDOW_SCALAR
main_menu_start_button_surf = pygame.transform.scale_by(main_menu_start_button_surf,main_menu_start_button_scale)
main_menu_start_button_rect = main_menu_start_button_surf.get_rect(center = (main_menu_start_button_start_pos))
mouse_on_main_menu_start_button = False
main_menu_start_button_big_scale = button_when_big_scale
main_menu_start_button_surf_big = pygame.transform.scale_by(main_menu_start_button_surf,main_menu_start_button_big_scale)
main_menu_start_button_rect_big = main_menu_start_button_surf_big.get_rect(center = (main_menu_start_button_start_pos))
# Statistics Button
main_menu_statistics_button_start_x_pos = CENTER_SCREEN
main_menu_statistics_button_start_y_pos = main_menu_start_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
main_menu_statistics_button_start_pos = (main_menu_statistics_button_start_x_pos,main_menu_statistics_button_start_y_pos)
main_menu_statistics_button_surf = test_font.render("Statistics",False,"#FCDC4D")
main_menu_statistics_button_scale = WINDOW_SCALAR
main_menu_statistics_button_surf = pygame.transform.scale_by(main_menu_statistics_button_surf,main_menu_statistics_button_scale)
main_menu_statistics_button_rect = main_menu_statistics_button_surf.get_rect(center = (main_menu_statistics_button_start_pos))
mouse_on_main_menu_statistics_button = False
main_menu_statistics_button_big_scale = button_when_big_scale
main_menu_statistics_button_surf_big = pygame.transform.scale_by(main_menu_statistics_button_surf,main_menu_statistics_button_big_scale)
main_menu_statistics_button_rect_big = main_menu_statistics_button_surf_big.get_rect(center = (main_menu_statistics_button_start_pos))
# Settings Button
main_menu_settings_button_start_x_pos = CENTER_SCREEN
main_menu_settings_button_start_y_pos = main_menu_statistics_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
main_menu_settings_button_start_pos = (main_menu_settings_button_start_x_pos,main_menu_settings_button_start_y_pos)
main_menu_settings_button_surf = test_font.render("Settings",False,"#FCDC4D")
main_menu_settings_button_scale = WINDOW_SCALAR
main_menu_settings_button_surf = pygame.transform.scale_by(main_menu_settings_button_surf,main_menu_settings_button_scale)
main_menu_settings_button_rect = main_menu_settings_button_surf.get_rect(center = (main_menu_settings_button_start_pos))
mouse_on_main_menu_settings_button = False
main_menu_settings_button_big_scale = button_when_big_scale
main_menu_settings_button_surf_big = pygame.transform.scale_by(main_menu_settings_button_surf,main_menu_settings_button_big_scale)
main_menu_settings_button_rect_big = main_menu_settings_button_surf_big.get_rect(center = (main_menu_settings_button_start_pos))
# Exit Button
main_menu_exit_button_start_x_pos = CENTER_SCREEN
main_menu_exit_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
main_menu_exit_button_start_pos = (main_menu_exit_button_start_x_pos,main_menu_exit_button_start_y_pos)
main_menu_exit_button_surf = test_font.render("Exit",False,"#FCDC4D")
main_menu_exit_button_scale = WINDOW_SCALAR
main_menu_exit_button_surf = pygame.transform.scale_by(main_menu_exit_button_surf,main_menu_exit_button_scale)
main_menu_exit_button_rect = main_menu_exit_button_surf.get_rect(center = (main_menu_exit_button_start_pos))
mouse_on_main_menu_exit_button = False
main_menu_exit_button_big_scale = button_when_big_scale
main_menu_exit_button_surf_big = pygame.transform.scale_by(main_menu_exit_button_surf,main_menu_exit_button_big_scale)
main_menu_exit_button_rect_big = main_menu_exit_button_surf_big.get_rect(center = (main_menu_exit_button_start_pos))

# Statistics Menu
statistics_tracker_scalar = 0.4
statistics_trackers_y_pos_offset = WINDOW_HEIGHT * 1/44
# Left Side
# Skeletons Killed Tracker
statistics_skeletons_killed_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_skeletons_killed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
statistics_skeletons_killed_tracker_start_pos = (statistics_skeletons_killed_tracker_start_x_pos,statistics_skeletons_killed_tracker_start_y_pos)
statistics_skeletons_killed_tracker_surf = test_font.render("Skeletons Killed: 0",False,"#FCDC4D")
statistics_skeletons_killed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_skeletons_killed_tracker_surf = pygame.transform.scale_by(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_scale)
statistics_skeletons_killed_tracker_rect = statistics_skeletons_killed_tracker_surf.get_rect(center = (statistics_skeletons_killed_tracker_start_pos))
mouse_on_statistics_skeletons_killed_tracker = False
statistics_skeletons_killed_tracker_big_scale = button_when_big_scale
statistics_skeletons_killed_tracker_surf_big = pygame.transform.scale_by(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_big_scale)
statistics_skeletons_killed_tracker_rect_big = statistics_skeletons_killed_tracker_surf_big.get_rect(center = (statistics_skeletons_killed_tracker_start_pos))
statistics_skeletons_killed_tracker_new_x_pos = statistics_skeletons_killed_tracker_start_x_pos - ((statistics_skeletons_killed_tracker_rect_big.width)/2)
statistics_skeletons_killed_tracker_new_pos = (statistics_skeletons_killed_tracker_new_x_pos,statistics_skeletons_killed_tracker_start_y_pos)
statistics_skeletons_killed_tracker_rect = statistics_skeletons_killed_tracker_surf.get_rect(center = (statistics_skeletons_killed_tracker_new_pos))
statistics_skeletons_killed_tracker_rect_big = statistics_skeletons_killed_tracker_surf_big.get_rect(center = (statistics_skeletons_killed_tracker_new_pos))
# Skeleton Birds Killed Tracker
statistics_skeleton_birds_killed_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_skeleton_birds_killed_tracker_start_y_pos = statistics_skeletons_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_skeleton_birds_killed_tracker_start_pos = (statistics_skeleton_birds_killed_tracker_start_x_pos,statistics_skeleton_birds_killed_tracker_start_y_pos)
statistics_skeleton_birds_killed_tracker_surf = test_font.render("Skeleton Birds Killed: 0",False,"#FCDC4D")
statistics_skeleton_birds_killed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_skeleton_birds_killed_tracker_surf = pygame.transform.scale_by(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_scale)
statistics_skeleton_birds_killed_tracker_rect = statistics_skeleton_birds_killed_tracker_surf.get_rect(center = (statistics_skeleton_birds_killed_tracker_start_pos))
mouse_on_statistics_skeleton_birds_killed_tracker = False
statistics_skeleton_birds_killed_tracker_big_scale = button_when_big_scale
statistics_skeleton_birds_killed_tracker_surf_big = pygame.transform.scale_by(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_big_scale)
statistics_skeleton_birds_killed_tracker_rect_big = statistics_skeleton_birds_killed_tracker_surf_big.get_rect(center = (statistics_skeleton_birds_killed_tracker_start_pos))
statistics_skeleton_birds_killed_tracker_new_x_pos = statistics_skeleton_birds_killed_tracker_start_x_pos - ((statistics_skeleton_birds_killed_tracker_rect_big.width)/2)
statistics_skeleton_birds_killed_tracker_new_pos = (statistics_skeleton_birds_killed_tracker_new_x_pos,statistics_skeleton_birds_killed_tracker_start_y_pos)
statistics_skeleton_birds_killed_tracker_rect = statistics_skeleton_birds_killed_tracker_surf.get_rect(center = (statistics_skeleton_birds_killed_tracker_new_pos))
statistics_skeleton_birds_killed_tracker_rect_big = statistics_skeleton_birds_killed_tracker_surf_big.get_rect(center = (statistics_skeleton_birds_killed_tracker_new_pos))
# Time Played Tracker
statistics_time_played_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_time_played_tracker_start_y_pos = statistics_skeleton_birds_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_time_played_tracker_start_pos = (statistics_time_played_tracker_start_x_pos,statistics_time_played_tracker_start_y_pos)
statistics_time_played_tracker_surf = test_font.render("Time Played: 0",False,"#FCDC4D")
statistics_time_played_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_time_played_tracker_surf = pygame.transform.scale_by(statistics_time_played_tracker_surf,statistics_time_played_tracker_scale)
statistics_time_played_tracker_rect = statistics_time_played_tracker_surf.get_rect(center = (statistics_time_played_tracker_start_pos))
mouse_on_statistics_time_played_tracker = False
statistics_time_played_tracker_big_scale = button_when_big_scale
statistics_time_played_tracker_surf_big = pygame.transform.scale_by(statistics_time_played_tracker_surf,statistics_time_played_tracker_big_scale)
statistics_time_played_tracker_rect_big = statistics_time_played_tracker_surf_big.get_rect(center = (statistics_time_played_tracker_start_pos))
statistics_time_played_tracker_new_x_pos = statistics_time_played_tracker_start_x_pos - ((statistics_time_played_tracker_rect_big.width)/2)
statistics_time_played_tracker_new_pos = (statistics_time_played_tracker_new_x_pos,statistics_time_played_tracker_start_y_pos)
statistics_time_played_tracker_rect = statistics_time_played_tracker_surf.get_rect(center = (statistics_time_played_tracker_new_pos))
statistics_time_played_tracker_rect_big = statistics_time_played_tracker_surf_big.get_rect(center = (statistics_time_played_tracker_new_pos))
# High Score Tracker
statistics_high_score_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_high_score_tracker_start_y_pos = statistics_time_played_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_high_score_tracker_start_pos = (statistics_high_score_tracker_start_x_pos,statistics_high_score_tracker_start_y_pos)
statistics_high_score_tracker_surf = test_font.render("High Score: 0",False,"#FCDC4D")
statistics_high_score_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_high_score_tracker_surf = pygame.transform.scale_by(statistics_high_score_tracker_surf,statistics_high_score_tracker_scale)
statistics_high_score_tracker_rect = statistics_high_score_tracker_surf.get_rect(center = (statistics_high_score_tracker_start_pos))
mouse_on_statistics_high_score_tracker = False
statistics_high_score_tracker_big_scale = button_when_big_scale
statistics_high_score_tracker_surf_big = pygame.transform.scale_by(statistics_high_score_tracker_surf,statistics_high_score_tracker_big_scale)
statistics_high_score_tracker_rect_big = statistics_high_score_tracker_surf_big.get_rect(center = (statistics_high_score_tracker_start_pos))
statistics_high_score_tracker_new_x_pos = statistics_high_score_tracker_start_x_pos - ((statistics_high_score_tracker_rect_big.width)/2)
statistics_high_score_tracker_new_pos = (statistics_high_score_tracker_new_x_pos,statistics_high_score_tracker_start_y_pos)
statistics_high_score_tracker_rect = statistics_high_score_tracker_surf.get_rect(center = (statistics_high_score_tracker_new_pos))
statistics_high_score_tracker_rect_big = statistics_high_score_tracker_surf_big.get_rect(center = (statistics_high_score_tracker_new_pos))
# Fireballs Shot Tracker
statistics_fireballs_shot_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_fireballs_shot_tracker_start_y_pos = statistics_high_score_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_fireballs_shot_tracker_start_pos = (statistics_fireballs_shot_tracker_start_x_pos,statistics_fireballs_shot_tracker_start_y_pos)
statistics_fireballs_shot_tracker_surf = test_font.render("Fireballs Shot: 0",False,"#FCDC4D")
statistics_fireballs_shot_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_fireballs_shot_tracker_surf = pygame.transform.scale_by(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_scale)
statistics_fireballs_shot_tracker_rect = statistics_fireballs_shot_tracker_surf.get_rect(center = (statistics_fireballs_shot_tracker_start_pos))
mouse_on_statistics_fireballs_shot_tracker = False
statistics_fireballs_shot_tracker_big_scale = button_when_big_scale
statistics_fireballs_shot_tracker_surf_big = pygame.transform.scale_by(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_big_scale)
statistics_fireballs_shot_tracker_rect_big = statistics_fireballs_shot_tracker_surf_big.get_rect(center = (statistics_fireballs_shot_tracker_start_pos))
statistics_fireballs_shot_tracker_new_x_pos = statistics_fireballs_shot_tracker_start_x_pos - ((statistics_fireballs_shot_tracker_rect_big.width)/2)
statistics_fireballs_shot_tracker_new_pos = (statistics_fireballs_shot_tracker_new_x_pos,statistics_fireballs_shot_tracker_start_y_pos)
statistics_fireballs_shot_tracker_rect = statistics_fireballs_shot_tracker_surf.get_rect(center = (statistics_fireballs_shot_tracker_new_pos))
statistics_fireballs_shot_tracker_rect_big = statistics_fireballs_shot_tracker_surf_big.get_rect(center = (statistics_fireballs_shot_tracker_new_pos))
# Jumps Tracker
statistics_jumps_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_jumps_tracker_start_y_pos = statistics_fireballs_shot_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_jumps_tracker_start_pos = (statistics_jumps_tracker_start_x_pos,statistics_jumps_tracker_start_y_pos)
statistics_jumps_tracker_surf = test_font.render("Jumps: 0",False,"#FCDC4D")
statistics_jumps_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_jumps_tracker_surf = pygame.transform.scale_by(statistics_jumps_tracker_surf,statistics_jumps_tracker_scale)
statistics_jumps_tracker_rect = statistics_jumps_tracker_surf.get_rect(center = (statistics_jumps_tracker_start_pos))
mouse_on_statistics_jumps_tracker = False
statistics_jumps_tracker_big_scale = button_when_big_scale
statistics_jumps_tracker_surf_big = pygame.transform.scale_by(statistics_jumps_tracker_surf,statistics_jumps_tracker_big_scale)
statistics_jumps_tracker_rect_big = statistics_jumps_tracker_surf_big.get_rect(center = (statistics_jumps_tracker_start_pos))
statistics_jumps_tracker_new_x_pos = statistics_jumps_tracker_start_x_pos - ((statistics_jumps_tracker_rect_big.width)/2)
statistics_jumps_tracker_new_pos = (statistics_jumps_tracker_new_x_pos,statistics_jumps_tracker_start_y_pos)
statistics_jumps_tracker_rect = statistics_jumps_tracker_surf.get_rect(center = (statistics_jumps_tracker_new_pos))
statistics_jumps_tracker_rect_big = statistics_jumps_tracker_surf_big.get_rect(center = (statistics_jumps_tracker_new_pos))
# Distance Traveled Tracker
statistics_distance_traveled_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
statistics_distance_traveled_tracker_start_y_pos = statistics_jumps_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_distance_traveled_tracker_start_pos = (statistics_distance_traveled_tracker_start_x_pos,statistics_distance_traveled_tracker_start_y_pos)
statistics_distance_traveled_tracker_surf = test_font.render("Distance Traveled: 0",False,"#FCDC4D")
statistics_distance_traveled_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_distance_traveled_tracker_surf = pygame.transform.scale_by(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_scale)
statistics_distance_traveled_tracker_rect = statistics_distance_traveled_tracker_surf.get_rect(center = (statistics_distance_traveled_tracker_start_pos))
mouse_on_statistics_distance_traveled_tracker = False
statistics_distance_traveled_tracker_big_scale = button_when_big_scale
statistics_distance_traveled_tracker_surf_big = pygame.transform.scale_by(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_big_scale)
statistics_distance_traveled_tracker_rect_big = statistics_distance_traveled_tracker_surf_big.get_rect(center = (statistics_distance_traveled_tracker_start_pos))
statistics_distance_traveled_tracker_new_x_pos = statistics_distance_traveled_tracker_start_x_pos - ((statistics_distance_traveled_tracker_rect_big.width)/2)
statistics_distance_traveled_tracker_new_pos = (statistics_distance_traveled_tracker_new_x_pos,statistics_distance_traveled_tracker_start_y_pos)
statistics_distance_traveled_tracker_rect = statistics_distance_traveled_tracker_surf.get_rect(center = (statistics_distance_traveled_tracker_new_pos))
statistics_distance_traveled_tracker_rect_big = statistics_distance_traveled_tracker_surf_big.get_rect(center = (statistics_distance_traveled_tracker_new_pos))
# Right Side
# Highest Speed Tracker
statistics_highest_speed_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
statistics_highest_speed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
statistics_highest_speed_tracker_start_pos = (statistics_highest_speed_tracker_start_x_pos,statistics_highest_speed_tracker_start_y_pos)
statistics_highest_speed_tracker_surf = test_font.render("Highest Speed: 0",False,"#FCDC4D")
statistics_highest_speed_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
statistics_highest_speed_tracker_surf = pygame.transform.scale_by(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_scale)
statistics_highest_speed_tracker_rect = statistics_highest_speed_tracker_surf.get_rect(center = (statistics_highest_speed_tracker_start_pos))
mouse_on_statistics_highest_speed_tracker = False
statistics_highest_speed_tracker_big_scale = button_when_big_scale
statistics_highest_speed_tracker_surf_big = pygame.transform.scale_by(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_big_scale)
statistics_highest_speed_tracker_rect_big = statistics_highest_speed_tracker_surf_big.get_rect(center = (statistics_highest_speed_tracker_start_pos))
statistics_highest_speed_tracker_new_x_pos = statistics_highest_speed_tracker_start_x_pos + ((statistics_highest_speed_tracker_rect_big.width)/2)
statistics_highest_speed_tracker_new_pos = (statistics_highest_speed_tracker_new_x_pos,statistics_highest_speed_tracker_start_y_pos)
statistics_highest_speed_tracker_rect = statistics_highest_speed_tracker_surf.get_rect(center = (statistics_highest_speed_tracker_new_pos))
statistics_highest_speed_tracker_rect_big = statistics_highest_speed_tracker_surf_big.get_rect(center = (statistics_highest_speed_tracker_new_pos))
# Bottom
# Back Button
statistics_back_button_start_x_pos = CENTER_SCREEN
statistics_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
statistics_back_button_start_pos = (statistics_back_button_start_x_pos,statistics_back_button_start_y_pos)
statistics_back_button_surf = test_font.render("Main Menu",False,"#FCDC4D")
statistics_back_button_scale = WINDOW_SCALAR
statistics_back_button_surf = pygame.transform.scale_by(statistics_back_button_surf,statistics_back_button_scale)
statistics_back_button_rect = statistics_back_button_surf.get_rect(center = (statistics_back_button_start_pos))
mouse_on_statistics_back_button = False
statistics_back_button_big_scale = button_when_big_scale
statistics_back_button_surf_big = pygame.transform.scale_by(statistics_back_button_surf,statistics_back_button_big_scale)
statistics_back_button_rect_big = statistics_back_button_surf_big.get_rect(center = (statistics_back_button_start_pos))

# Settings
# Sounds Button
settings_sounds_button_start_x_pos = CENTER_SCREEN
settings_sounds_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
settings_sounds_button_start_pos = (settings_sounds_button_start_x_pos,settings_sounds_button_start_y_pos)
settings_sounds_button_surf = test_font.render("Sounds",False,"#FCDC4D")
settings_sounds_button_scale = WINDOW_SCALAR
settings_sounds_button_surf = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_scale)
settings_sounds_button_rect = settings_sounds_button_surf.get_rect(center = (settings_sounds_button_start_pos))
mouse_on_settings_sounds_button = False
settings_sounds_button_big_scale = button_when_big_scale
settings_sounds_button_surf_big = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_big_scale)
settings_sounds_button_rect_big = settings_sounds_button_surf_big.get_rect(center = (settings_sounds_button_start_pos))
# Controls Button
settings_controls_button_start_x_pos = CENTER_SCREEN
settings_controls_button_start_y_pos = settings_sounds_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
settings_controls_button_start_pos = (settings_controls_button_start_x_pos,settings_controls_button_start_y_pos)
settings_controls_button_surf = test_font.render("Controls",False,"#FCDC4D")
settings_controls_button_scale = WINDOW_SCALAR
settings_controls_button_surf = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_scale)
settings_controls_button_rect = settings_controls_button_surf.get_rect(center = (settings_controls_button_start_pos))
mouse_on_settings_controls_button = False
settings_controls_button_big_scale = button_when_big_scale
settings_controls_button_surf_big = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_big_scale)
settings_controls_button_rect_big = settings_controls_button_surf_big.get_rect(center = (settings_controls_button_start_pos))
# Display Button
settings_display_button_start_x_pos = CENTER_SCREEN
settings_display_button_start_y_pos = settings_controls_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
settings_display_button_start_pos = (settings_display_button_start_x_pos,settings_display_button_start_y_pos)
settings_display_button_surf = test_font.render("Display",False,"#FCDC4D")
settings_display_button_scale = WINDOW_SCALAR
settings_display_button_surf = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_scale)
settings_display_button_rect = settings_display_button_surf.get_rect(center = (settings_display_button_start_pos))
mouse_on_settings_display_button = False
settings_display_button_big_scale = button_when_big_scale
settings_display_button_surf_big = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_big_scale)
settings_display_button_rect_big = settings_display_button_surf_big.get_rect(center = (settings_display_button_start_pos))
# Back Button
settings_back_button_start_x_pos = CENTER_SCREEN
settings_back_button_start_y_pos = settings_display_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
settings_back_button_start_pos = (settings_back_button_start_x_pos,settings_back_button_start_y_pos)
settings_back_button_surf = test_font.render("Main Menu",False,"#FCDC4D")
settings_back_button_scale = WINDOW_SCALAR
settings_back_button_surf = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_scale)
settings_back_button_rect = settings_back_button_surf.get_rect(center = (settings_back_button_start_pos))
mouse_on_settings_back_button = False
settings_back_button_big_scale = button_when_big_scale
settings_back_button_surf_big = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_big_scale)
settings_back_button_rect_big = settings_back_button_surf_big.get_rect(center = (settings_back_button_start_pos))

# Sounds Menu
# Back Button
sounds_back_button_start_x_pos = CENTER_SCREEN
sounds_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
sounds_back_button_start_pos = (sounds_back_button_start_x_pos,sounds_back_button_start_y_pos)
sounds_back_button_surf = test_font.render("Back to Settings",False,"#FCDC4D")
sounds_back_button_scale = WINDOW_SCALAR
sounds_back_button_surf = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_scale)
sounds_back_button_rect = sounds_back_button_surf.get_rect(center = (sounds_back_button_start_pos))
mouse_on_sounds_back_button = False
sounds_back_button_big_scale = button_when_big_scale
sounds_back_button_surf_big = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_big_scale)
sounds_back_button_rect_big = sounds_back_button_surf_big.get_rect(center = (sounds_back_button_start_pos))

# Controls Menu
controls_update = False
# Controls Buttons
controls_first_button_start_x_pos = CENTER_SCREEN
controls_first_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
controls_first_button_start_pos = (controls_first_button_start_x_pos,controls_first_button_start_y_pos)
controls_buttons_y_pos_offset = WINDOW_HEIGHT * 1/18
mouse_on_controls_button_dict = {}
controls_button_surf_dict = {}
controls_button_rect_dict = {}
controls_button_surf_big_dict = {}
controls_button_rect_big_dict = {}
controls_button_index = 0
controls_button_scalar = 0.5
edited_controls_display_names_dict = get_edited_controls_file_dict().get("edited_controls_display_names_dict")
default_controls_pygame_constants_names_dict = get_default_controls_file_dict().get("default_controls_pygame_constants_names_dict")
for control_name, control in default_controls_pygame_constants_names_dict.items():
    controls_button_start_x_pos = main_menu_wizard_rect.centerx
    controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT) + controls_buttons_y_pos_offset * controls_button_index
    controls_button_start_pos = (controls_button_start_x_pos,controls_button_start_y_pos)
    control_name_underscore_removed = control_name.replace("_", " ")
    control_name_capitalized = control_name_underscore_removed.title()
    controls_button_surf = test_font.render(f"{control_name_capitalized}: {edited_controls_display_names_dict[control_name]}",False,"#FCDC4D")
    controls_button_scale = WINDOW_SCALAR * controls_button_scalar
    controls_button_surf = pygame.transform.scale_by(controls_button_surf,controls_button_scale)
    controls_button_surf_dict.update({control_name: controls_button_surf})
    controls_button_rect = controls_button_surf.get_rect(center = (controls_button_start_pos))
    controls_button_rect_dict.update({control_name: controls_button_rect})
    mouse_on_controls_button_dict.update({control_name: False})
    controls_button_big_scale = button_when_big_scale
    controls_button_surf_big = pygame.transform.scale_by(controls_button_surf,controls_button_big_scale)
    controls_button_surf_big_dict.update({control_name: controls_button_surf_big})
    controls_button_rect_big = controls_button_surf_big.get_rect(center = (controls_button_start_pos))
    controls_button_rect_big_dict.update({control_name: controls_button_rect_big})
    controls_button_index += 1
# Reset Button
controls_reset_button_start_x_pos = CENTER_SCREEN
controls_reset_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT) + (controls_buttons_y_pos_offset * (len(default_controls_pygame_constants_names_dict)))
controls_reset_button_start_pos = (controls_reset_button_start_x_pos,controls_reset_button_start_y_pos)
controls_reset_button_surf = test_font.render("Reset Controls to Default",False,"#FCDC4D")
controls_reset_button_scale = WINDOW_SCALAR * controls_button_scalar
controls_reset_button_surf = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_scale)
controls_reset_button_rect = controls_reset_button_surf.get_rect(center = (controls_reset_button_start_pos))
mouse_on_controls_reset_button = False
controls_reset_button_big_scale = button_when_big_scale
controls_reset_button_surf_big = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_big_scale)
controls_reset_button_rect_big = controls_reset_button_surf_big.get_rect(center = (controls_reset_button_start_pos))
# Back Button
controls_back_button_start_x_pos = CENTER_SCREEN
controls_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
controls_back_button_start_pos = (controls_back_button_start_x_pos,controls_back_button_start_y_pos)
controls_back_button_surf = test_font.render("Back to Settings",False,"#FCDC4D")
controls_back_button_scale = WINDOW_SCALAR
controls_back_button_surf = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_scale)
controls_back_button_rect = controls_back_button_surf.get_rect(center = (controls_back_button_start_pos))
mouse_on_controls_back_button = False
controls_back_button_big_scale = button_when_big_scale
controls_back_button_surf_big = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_big_scale)
controls_back_button_rect_big = controls_back_button_surf_big.get_rect(center = (controls_back_button_start_pos))

# Display Menu
display_button_scalar = 0.5
display_buttons_y_pos_offset = WINDOW_HEIGHT * 1/36
display_controls_update = False
display_in_game_stats_update = False
display_in_game_health_update = False
display_in_game_buffs_update = False
# Show Controls Button
controls_displayed = get_edited_options_file_dict()["edited_display_controls"]
display_show_controls_button_start_x_pos = CENTER_SCREEN
display_show_controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
display_show_controls_button_start_pos = (display_show_controls_button_start_x_pos,display_show_controls_button_start_y_pos)
display_show_controls_button_surf = test_font.render(f"Display Controls: {controls_displayed}",False,"#FCDC4D")
display_show_controls_button_scale = WINDOW_SCALAR * display_button_scalar
display_show_controls_button_surf = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_scale)
display_show_controls_button_rect = display_show_controls_button_surf.get_rect(center = (display_show_controls_button_start_pos))
mouse_on_display_show_controls_button = False
display_show_controls_button_big_scale = button_when_big_scale
display_show_controls_button_surf_big = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_big_scale)
display_show_controls_button_rect_big = display_show_controls_button_surf_big.get_rect(center = (display_show_controls_button_start_pos))
# Show In Game Stats Button
in_game_stats_displayed = get_edited_options_file_dict()["edited_display_in_game_stats"]
display_show_in_game_stats_button_start_x_pos = CENTER_SCREEN
display_show_in_game_stats_button_start_y_pos = display_show_controls_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_stats_button_start_pos = (display_show_in_game_stats_button_start_x_pos,display_show_in_game_stats_button_start_y_pos)
display_show_in_game_stats_button_surf = test_font.render(f"Display Stats: {in_game_stats_displayed}",False,"#FCDC4D")
display_show_in_game_stats_button_scale = WINDOW_SCALAR * display_button_scalar
display_show_in_game_stats_button_surf = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_scale)
display_show_in_game_stats_button_rect = display_show_in_game_stats_button_surf.get_rect(center = (display_show_in_game_stats_button_start_pos))
mouse_on_display_show_in_game_stats_button = False
display_show_in_game_stats_button_big_scale = button_when_big_scale
display_show_in_game_stats_button_surf_big = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_big_scale)
display_show_in_game_stats_button_rect_big = display_show_in_game_stats_button_surf_big.get_rect(center = (display_show_in_game_stats_button_start_pos))
# Show In Game Health Button
in_game_health_displayed = get_edited_options_file_dict()["edited_display_in_game_health"]
display_show_in_game_health_button_start_x_pos = CENTER_SCREEN
display_show_in_game_health_button_start_y_pos = display_show_in_game_stats_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_health_button_start_pos = (display_show_in_game_health_button_start_x_pos,display_show_in_game_health_button_start_y_pos)
display_show_in_game_health_button_surf = test_font.render(f"Display Health: {in_game_health_displayed}",False,"#FCDC4D")
display_show_in_game_health_button_scale = WINDOW_SCALAR * display_button_scalar
display_show_in_game_health_button_surf = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_scale)
display_show_in_game_health_button_rect = display_show_in_game_health_button_surf.get_rect(center = (display_show_in_game_health_button_start_pos))
mouse_on_display_show_in_game_health_button = False
display_show_in_game_health_button_big_scale = button_when_big_scale
display_show_in_game_health_button_surf_big = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_big_scale)
display_show_in_game_health_button_rect_big = display_show_in_game_health_button_surf_big.get_rect(center = (display_show_in_game_health_button_start_pos))
# Show In Game Buffs Button
in_game_buffs_displayed = get_edited_options_file_dict()["edited_display_in_game_buffs"]
display_show_in_game_buffs_button_start_x_pos = CENTER_SCREEN
display_show_in_game_buffs_button_start_y_pos = display_show_in_game_health_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_buffs_button_start_pos = (display_show_in_game_buffs_button_start_x_pos,display_show_in_game_buffs_button_start_y_pos)
display_show_in_game_buffs_button_surf = test_font.render(f"Display Buffs: {in_game_buffs_displayed}",False,"#FCDC4D")
display_show_in_game_buffs_button_scale = WINDOW_SCALAR * display_button_scalar
display_show_in_game_buffs_button_surf = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_scale)
display_show_in_game_buffs_button_rect = display_show_in_game_buffs_button_surf.get_rect(center = (display_show_in_game_buffs_button_start_pos))
mouse_on_display_show_in_game_buffs_button = False
display_show_in_game_buffs_button_big_scale = button_when_big_scale
display_show_in_game_buffs_button_surf_big = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_big_scale)
display_show_in_game_buffs_button_rect_big = display_show_in_game_buffs_button_surf_big.get_rect(center = (display_show_in_game_buffs_button_start_pos))
# Reset Button
display_reset_button_start_x_pos = CENTER_SCREEN
display_reset_button_start_y_pos = display_show_in_game_buffs_button_rect_big.bottom + display_buttons_y_pos_offset
display_reset_button_start_pos = (display_reset_button_start_x_pos,display_reset_button_start_y_pos)
display_reset_button_surf = test_font.render("Reset Display Options to Default",False,"#FCDC4D")
display_reset_button_scale = WINDOW_SCALAR * display_button_scalar
display_reset_button_surf = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_scale)
display_reset_button_rect = display_reset_button_surf.get_rect(center = (display_reset_button_start_pos))
mouse_on_display_reset_button = False
display_reset_button_big_scale = button_when_big_scale
display_reset_button_surf_big = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_big_scale)
display_reset_button_rect_big = display_reset_button_surf_big.get_rect(center = (display_reset_button_start_pos))
# Back Button
display_back_button_start_x_pos = CENTER_SCREEN
display_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * WINDOW_HEIGHT)
display_back_button_start_pos = (display_back_button_start_x_pos,display_back_button_start_y_pos)
display_back_button_surf = test_font.render("Back to Settings",False,"#FCDC4D")
display_back_button_scale = WINDOW_SCALAR
display_back_button_surf = pygame.transform.scale_by(display_back_button_surf,display_back_button_scale)
display_back_button_rect = display_back_button_surf.get_rect(center = (display_back_button_start_pos))
mouse_on_display_back_button = False
display_back_button_big_scale = button_when_big_scale
display_back_button_surf_big = pygame.transform.scale_by(display_back_button_surf,display_back_button_big_scale)
display_back_button_rect_big = display_back_button_surf_big.get_rect(center = (display_back_button_start_pos))
