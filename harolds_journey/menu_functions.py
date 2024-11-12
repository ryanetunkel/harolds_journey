"""Contains all menu related functions"""
from global_vars import *
from menu_vars import *


# Main Menu Functions
# Display High Score
def display_high_score(score_rect):
    # High Score
    score_y_offset = WINDOW_HEIGHT * 1/44
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    high_score_start_x_pos = CENTER_SCREEN
    high_score_start_y_pos = score_rect.bottom + score_y_offset
    high_score_start_pos = (high_score_start_x_pos,high_score_start_y_pos)
    high_score_surf = test_font.render(f"High Score: {high_score}",False,"#FCDC4D")
    high_score_scale = 0.4 * WINDOW_SCALAR
    high_score_surf = pygame.transform.scale_by(high_score_surf,high_score_scale)
    high_score_rect = high_score_surf.get_rect(center = (high_score_start_pos))
    # High Score Blit
    screen.blit(high_score_surf,high_score_rect)

# All Menu Stuff
def main_menu(
    event: pygame.event.Event,
    menu_section: int,
    pre_stat_update_edited_stats_file_dict: dict,
    controls_button_rect_big_dict: dict,
    extras: tuple
):
    """Contains all menu-related vars"""
    print(menu_section)
    # Main Menu Screen
    # MAIN_MENU = 1
    # STATISTICS_MENU = 2
    # SETTINGS_MENU = 3
    # SOUNDS_MENU = 4
    # CONTROLS_MENU = 5
    # DISPLAY_MENU = 6
    # menu_section = MAIN_MENU
    # CENTER_SCREEN = WINDOW_WIDTH / 2
    rect_bigs = {}
    # Game Title
    main_menu_title_start_x_pos = CENTER_SCREEN
    main_menu_title_start_y_pos = 54/400 * WINDOW_HEIGHT
    main_menu_title_start_pos = (main_menu_title_start_x_pos,main_menu_title_start_y_pos)
    main_menu_title_scale = 1.25 * WINDOW_SCALAR
    main_menu_title_surf = test_font.render("Harold\'s Journey",False,"#FCDC4D")
    main_menu_title_surf = pygame.transform.scale_by(main_menu_title_surf,main_menu_title_scale)
    main_menu_title_rect = main_menu_title_surf.get_rect(midbottom = main_menu_title_start_pos)

    # Wizard on Menu Screen
    main_menu_wizard_start_x_pos = CENTER_SCREEN
    main_menu_wizard_start_y_pos = main_menu_title_start_y_pos + (1.5 * (96 * WINDOW_SCALAR))
    main_menu_wizard_hat_size = 24 * WINDOW_SCALAR
    main_menu_wizard_surf = pygame.image.load("harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png").convert_alpha()
    main_menu_wizard_height_by_scale = 96 * WINDOW_SCALAR
    main_menu_wizard_width_by_scale = 96 * WINDOW_SCALAR
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
    rect_bigs.update({"main_menu_start_button_rect_big":main_menu_start_button_rect_big})
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
    rect_bigs.update({"main_menu_statistics_button_rect_big":main_menu_statistics_button_rect_big})
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
    rect_bigs.update({"main_menu_settings_button_rect_big":main_menu_settings_button_rect_big})
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
    rect_bigs.update({"main_menu_exit_button_rect_big":main_menu_exit_button_rect_big})

    # Statistics Menu
    statistics_tracker_scalar = 0.4
    statistics_trackers_y_pos_offset = WINDOW_HEIGHT * 1/44
    edited_stats_file_dict = get_edited_stats_file_dict()
    edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
    edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
    edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
    edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
    # fireballs_shot = 0
    # jumps_made = 0
    # distance_traveled = 0
    # highest_speed = 0
    # pre_stat_update_edited_stats_file_dict = {}
    # Left Side
    # Kills
    # Skeletons Killed Tracker
    skeletons_killed_total = edited_stats_kills_file_dict.get("skeletons_killed")
    statistics_skeletons_killed_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_skeletons_killed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
    statistics_skeletons_killed_tracker_start_pos = (statistics_skeletons_killed_tracker_start_x_pos,statistics_skeletons_killed_tracker_start_y_pos)
    statistics_skeletons_killed_tracker_surf = test_font.render(f"Skeletons Killed: {skeletons_killed_total}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_skeletons_killed_tracker_rect_big":statistics_skeletons_killed_tracker_rect_big})
    # Skeleton Birds Killed Tracker
    skeleton_birds_killed_total = edited_stats_kills_file_dict.get("skeleton_birds_killed")
    statistics_skeleton_birds_killed_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_skeleton_birds_killed_tracker_start_y_pos = statistics_skeletons_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_skeleton_birds_killed_tracker_start_pos = (statistics_skeleton_birds_killed_tracker_start_x_pos,statistics_skeleton_birds_killed_tracker_start_y_pos)
    statistics_skeleton_birds_killed_tracker_surf = test_font.render(f"Skeleton Birds Killed: {skeleton_birds_killed_total}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_skeleton_birds_killed_tracker_rect_big":statistics_skeleton_birds_killed_tracker_rect_big})
    # Interactivity
    # Time Played Tracker
    time_played_total = edited_stats_interactivity_file_dict.get("time_played")
    units = {"weeks":3600 * 24 * 7,"days":3600 * 24,"hours": 3600, "minutes": 60, "seconds": 1}
    final_displayed_time = ""
    for unit, value in units.items():
        count = time_played_total // value
        time_played_total -= count * value
        if count > 0:
            final_displayed_time += f"{count}{unit[0]} "
    if not final_displayed_time:
        final_displayed_time = "0s"
    statistics_time_played_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_time_played_tracker_start_y_pos = statistics_skeleton_birds_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_time_played_tracker_start_pos = (statistics_time_played_tracker_start_x_pos,statistics_time_played_tracker_start_y_pos)
    statistics_time_played_tracker_surf = test_font.render(f"Time Played: {final_displayed_time.strip()}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_time_played_tracker_rect_big":statistics_time_played_tracker_rect_big})
    # High Score Tracker
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    statistics_high_score_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_high_score_tracker_start_y_pos = statistics_time_played_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_high_score_tracker_start_pos = (statistics_high_score_tracker_start_x_pos,statistics_high_score_tracker_start_y_pos)
    statistics_high_score_tracker_surf = test_font.render(f"High Score: {high_score}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_high_score_tracker_rect_big":statistics_high_score_tracker_rect_big})
    # Fireballs Shot Tracker
    fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
    statistics_fireballs_shot_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_fireballs_shot_tracker_start_y_pos = statistics_high_score_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_fireballs_shot_tracker_start_pos = (statistics_fireballs_shot_tracker_start_x_pos,statistics_fireballs_shot_tracker_start_y_pos)
    statistics_fireballs_shot_tracker_surf = test_font.render(f"Fireballs Shot: {fireballs_shot_total}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_fireballs_shot_tracker_rect_big":statistics_fireballs_shot_tracker_rect_big})
    # Jumps Tracker
    jumps_total = edited_stats_interactivity_file_dict.get("jumps")
    statistics_jumps_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_jumps_tracker_start_y_pos = statistics_fireballs_shot_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_jumps_tracker_start_pos = (statistics_jumps_tracker_start_x_pos,statistics_jumps_tracker_start_y_pos)
    statistics_jumps_tracker_surf = test_font.render(f"Jumps: {jumps_total}",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_jumps_tracker_rect_big":statistics_jumps_tracker_rect_big})
    # Distance Traveled Tracker
    distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
    statistics_distance_traveled_tracker_start_x_pos = CENTER_SCREEN - statistics_trackers_y_pos_offset
    statistics_distance_traveled_tracker_start_y_pos = statistics_jumps_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_distance_traveled_tracker_start_pos = (statistics_distance_traveled_tracker_start_x_pos,statistics_distance_traveled_tracker_start_y_pos)
    statistics_distance_traveled_tracker_surf = test_font.render(f"Distance Traveled: {int(distance_traveled_total/WIZARD_WIDTH)}m",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_distance_traveled_tracker_rect_big":statistics_distance_traveled_tracker_rect_big})
    # Right Side
    # In-Game Stat Records
    # Highest Speed Tracker
    highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
    statistics_highest_speed_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_highest_speed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * WINDOW_HEIGHT)
    statistics_highest_speed_tracker_start_pos = (statistics_highest_speed_tracker_start_x_pos,statistics_highest_speed_tracker_start_y_pos)
    statistics_highest_speed_tracker_surf = test_font.render(f"Highest Speed: {round((highest_speed/WIZARD_WIDTH)*60,2)}m/s",False,"#FCDC4D")
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
    rect_bigs.update({"statistics_highest_speed_tracker_rect_big":statistics_highest_speed_tracker_rect_big})
    # Highest Damage Tracker
    highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
    statistics_highest_damage_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_highest_damage_tracker_start_y_pos = statistics_highest_speed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_highest_damage_tracker_start_pos = (statistics_highest_damage_tracker_start_x_pos,statistics_highest_damage_tracker_start_y_pos)
    statistics_highest_damage_tracker_surf = test_font.render(f"Highest Damage: {highest_damage}",False,"#FCDC4D")
    statistics_highest_damage_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_highest_damage_tracker_surf = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_scale)
    statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_start_pos))
    mouse_on_statistics_highest_damage_tracker = False
    statistics_highest_damage_tracker_big_scale = button_when_big_scale
    statistics_highest_damage_tracker_surf_big = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_big_scale)
    statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_start_pos))
    statistics_highest_damage_tracker_new_x_pos = statistics_highest_damage_tracker_start_x_pos + ((statistics_highest_damage_tracker_rect_big.width)/2)
    statistics_highest_damage_tracker_new_pos = (statistics_highest_damage_tracker_new_x_pos,statistics_highest_damage_tracker_start_y_pos)
    statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_new_pos))
    statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_new_pos))
    rect_bigs.update({"statistics_highest_damage_tracker_rect_big":statistics_highest_damage_tracker_rect_big})
    # Highest Piercing Tracker
    highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
    statistics_highest_piercing_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_highest_piercing_tracker_start_y_pos = statistics_highest_damage_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_highest_piercing_tracker_start_pos = (statistics_highest_piercing_tracker_start_x_pos,statistics_highest_piercing_tracker_start_y_pos)
    statistics_highest_piercing_tracker_surf = test_font.render(f"Highest Piercing: {highest_piercing - 1}",False,"#FCDC4D")
    statistics_highest_piercing_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_highest_piercing_tracker_surf = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_scale)
    statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
    mouse_on_statistics_highest_piercing_tracker = False
    statistics_highest_piercing_tracker_big_scale = button_when_big_scale
    statistics_highest_piercing_tracker_surf_big = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_big_scale)
    statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
    statistics_highest_piercing_tracker_new_x_pos = statistics_highest_piercing_tracker_start_x_pos + ((statistics_highest_piercing_tracker_rect_big.width)/2)
    statistics_highest_piercing_tracker_new_pos = (statistics_highest_piercing_tracker_new_x_pos,statistics_highest_piercing_tracker_start_y_pos)
    statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
    statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
    rect_bigs.update({"statistics_highest_piercing_tracker_rect_big":statistics_highest_piercing_tracker_rect_big})
    # Lowest Cooldown Tracker
    lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
    statistics_lowest_cooldown_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_lowest_cooldown_tracker_start_y_pos = statistics_highest_piercing_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_lowest_cooldown_tracker_start_pos = (statistics_lowest_cooldown_tracker_start_x_pos,statistics_lowest_cooldown_tracker_start_y_pos)
    statistics_lowest_cooldown_tracker_surf = test_font.render(f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",False,"#FCDC4D")
    statistics_lowest_cooldown_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_lowest_cooldown_tracker_surf = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_scale)
    statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
    mouse_on_statistics_lowest_cooldown_tracker = False
    statistics_lowest_cooldown_tracker_big_scale = button_when_big_scale
    statistics_lowest_cooldown_tracker_surf_big = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_big_scale)
    statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
    statistics_lowest_cooldown_tracker_new_x_pos = statistics_lowest_cooldown_tracker_start_x_pos + ((statistics_lowest_cooldown_tracker_rect_big.width)/2)
    statistics_lowest_cooldown_tracker_new_pos = (statistics_lowest_cooldown_tracker_new_x_pos,statistics_lowest_cooldown_tracker_start_y_pos)
    statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
    statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
    rect_bigs.update({"statistics_lowest_cooldown_tracker_rect_big":statistics_lowest_cooldown_tracker_rect_big})
    # Buffs
    # Double Jump Buff Tracker
    double_jump_buff_found = edited_stats_buffs_file_dict.get("double_jump_buff")
    double_jump_buff_string = "???: Not Yet Found" if not double_jump_buff_found else "Double Jump Buff: Found"
    statistics_double_jump_buff_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_double_jump_buff_tracker_start_y_pos = statistics_lowest_cooldown_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_double_jump_buff_tracker_start_pos = (statistics_double_jump_buff_tracker_start_x_pos,statistics_double_jump_buff_tracker_start_y_pos)
    statistics_double_jump_buff_tracker_surf = test_font.render(double_jump_buff_string,False,"#FCDC4D")
    statistics_double_jump_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_double_jump_buff_tracker_surf = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_scale)
    statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
    mouse_on_statistics_double_jump_buff_tracker = False
    statistics_double_jump_buff_tracker_big_scale = button_when_big_scale
    statistics_double_jump_buff_tracker_surf_big = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_big_scale)
    statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
    statistics_double_jump_buff_tracker_new_x_pos = statistics_double_jump_buff_tracker_start_x_pos + ((statistics_double_jump_buff_tracker_rect_big.width)/2)
    statistics_double_jump_buff_tracker_new_pos = (statistics_double_jump_buff_tracker_new_x_pos,statistics_double_jump_buff_tracker_start_y_pos)
    statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
    statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
    rect_bigs.update({"statistics_double_jump_buff_tracker_rect_big":statistics_double_jump_buff_tracker_rect_big})
    # Knockback Buff Tracker
    knockback_buff_found = edited_stats_buffs_file_dict.get("knockback_buff")
    knockback_buff_string = "???: Not Yet Found" if not knockback_buff_found else "Knockback Buff: Found"
    statistics_knockback_buff_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_knockback_buff_tracker_start_y_pos = statistics_double_jump_buff_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_knockback_buff_tracker_start_pos = (statistics_knockback_buff_tracker_start_x_pos,statistics_knockback_buff_tracker_start_y_pos)
    statistics_knockback_buff_tracker_surf = test_font.render(knockback_buff_string,False,"#FCDC4D")
    statistics_knockback_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_knockback_buff_tracker_surf = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_scale)
    statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
    mouse_on_statistics_knockback_buff_tracker = False
    statistics_knockback_buff_tracker_big_scale = button_when_big_scale
    statistics_knockback_buff_tracker_surf_big = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_big_scale)
    statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
    statistics_knockback_buff_tracker_new_x_pos = statistics_knockback_buff_tracker_start_x_pos + ((statistics_knockback_buff_tracker_rect_big.width)/2)
    statistics_knockback_buff_tracker_new_pos = (statistics_knockback_buff_tracker_new_x_pos,statistics_knockback_buff_tracker_start_y_pos)
    statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
    statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
    rect_bigs.update({"statistics_knockback_buff_tracker_rect_big":statistics_knockback_buff_tracker_rect_big})
    # Shield Buff Tracker
    shield_buff_found = edited_stats_buffs_file_dict.get("shield_buff")
    shield_buff_string = "???: Not Yet Found" if not shield_buff_found else "Magic Shield Buff: Found"
    statistics_shield_buff_tracker_start_x_pos = CENTER_SCREEN + statistics_trackers_y_pos_offset
    statistics_shield_buff_tracker_start_y_pos = statistics_knockback_buff_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
    statistics_shield_buff_tracker_start_pos = (statistics_shield_buff_tracker_start_x_pos,statistics_shield_buff_tracker_start_y_pos)
    statistics_shield_buff_tracker_surf = test_font.render(shield_buff_string,False,"#FCDC4D")
    statistics_shield_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
    statistics_shield_buff_tracker_surf = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_scale)
    statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_start_pos))
    mouse_on_statistics_shield_buff_tracker = False
    statistics_shield_buff_tracker_big_scale = button_when_big_scale
    statistics_shield_buff_tracker_surf_big = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_big_scale)
    statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_start_pos))
    statistics_shield_buff_tracker_new_x_pos = statistics_shield_buff_tracker_start_x_pos + ((statistics_shield_buff_tracker_rect_big.width)/2)
    statistics_shield_buff_tracker_new_pos = (statistics_shield_buff_tracker_new_x_pos,statistics_shield_buff_tracker_start_y_pos)
    statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_new_pos))
    statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_new_pos))
    rect_bigs.update({"statistics_shield_buff_tracker_rect_big":statistics_shield_buff_tracker_rect_big})
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
    rect_bigs.update({"statistics_back_button_rect_big":statistics_back_button_rect_big})

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
    rect_bigs.update({"settings_sounds_button_rect_big":settings_sounds_button_rect_big})
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
    rect_bigs.update({"settings_controls_button_rect_big":settings_controls_button_rect_big})
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
    rect_bigs.update({"settings_display_button_rect_big":settings_display_button_rect_big})
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
    rect_bigs.update({"settings_back_button_rect_big":settings_back_button_rect_big})

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
    rect_bigs.update({"sounds_back_button_rect_big":sounds_back_button_rect_big})

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
    # for controls_button_rect_big_from_dict_name, controls_button_rect_big_from_dict in controls_button_rect_big_dict.items():
    #     rect_bigs.update({controls_button_rect_big_from_dict_name:controls_button_rect_big_from_dict})
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
    rect_bigs.update({"controls_reset_button_rect_big":controls_reset_button_rect_big})
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
    rect_bigs.update({"controls_back_button_rect_big":controls_back_button_rect_big})

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
    rect_bigs.update({"display_show_controls_button_rect_big":display_show_controls_button_rect_big})
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
    rect_bigs.update({"display_show_in_game_stats_button_rect_big":display_show_in_game_stats_button_rect_big})
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
    rect_bigs.update({"display_show_in_game_health_button_rect_big":display_show_in_game_health_button_rect_big})
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
    rect_bigs.update({"display_show_in_game_buffs_button_rect_big":display_show_in_game_buffs_button_rect_big})
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
    rect_bigs.update({"display_reset_button_rect_big":display_reset_button_rect_big})
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
    rect_bigs.update({"display_back_button_rect_big":display_back_button_rect_big})

    
    
    
    
    fireballs_shot = extras[0]
    jumps_made = extras[1]
    game_active = extras[2]
    wizard_alive = extras[3]
    start_time = extras[4]
    # Menu Interactivity
    (mouse_x,mouse_y) = pygame.mouse.get_pos()
    mouse_pos = (mouse_x,mouse_y)
    clicking_with_left_mouse = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
    # Main Menu
    if menu_section == MAIN_MENU:
        main_menu_start_button_rect_big = rect_bigs.get("main_menu_start_button_rect_big")
        mouse_on_main_menu_start_button = main_menu_start_button_rect_big.collidepoint(mouse_pos)
        main_menu_statistics_button_rect_big = rect_bigs.get("main_menu_statistics_button_rect_big")
        mouse_on_main_menu_statistics_button = main_menu_statistics_button_rect_big.collidepoint(mouse_pos)
        main_menu_settings_button_rect_big = rect_bigs.get("main_menu_settings_button_rect_big")
        mouse_on_main_menu_settings_button = main_menu_settings_button_rect_big.collidepoint(mouse_pos)
        main_menu_exit_button_rect_big = rect_bigs.get("main_menu_exit_button_rect_big")
        mouse_on_main_menu_exit_button = main_menu_exit_button_rect_big.collidepoint(mouse_pos)
        # Start Button
        if mouse_on_main_menu_start_button:
            if clicking_with_left_mouse:
                controls_update = True
                game_active = True
                wizard_alive = True
                start_time = int(pygame.time.get_ticks() / 1000)
                # additional_score = 0 # prob not needed, we shall see
                pre_stat_update_edited_stats_file_dict.update(get_edited_stats_file_dict())
        # Statistics Button
        elif mouse_on_main_menu_statistics_button:
            if clicking_with_left_mouse:
                menu_section = STATISTICS_MENU
        # Settings Button
        elif mouse_on_main_menu_settings_button:
            if clicking_with_left_mouse:
                menu_section = SETTINGS_MENU
        # Exit Button
        elif mouse_on_main_menu_exit_button:
            if clicking_with_left_mouse:
                pygame.quit()
                exit()
    # # Statistics Menu
    # elif menu_section == STATISTICS_MENU:
    #     # Left Side
    #     # Kills
    #     # Skeletons Killed Tracker
    #     statistics_skeletons_killed_tracker_rect_big = rect_bigs.get("statistics_skeletons_killed_tracker_rect_big")
    #     mouse_on_statistics_skeletons_killed_tracker = statistics_skeletons_killed_tracker_rect_big.collidepoint(mouse_pos)
    #     # Skeleton Birds Killed Tracker
    #     statistics_skeleton_birds_killed_tracker_rect_big = rect_bigs.get("statistics_skeleton_birds_killed_tracker_rect_big")
    #     mouse_on_statistics_skeleton_birds_killed_tracker = statistics_skeleton_birds_killed_tracker_rect_big.collidepoint(mouse_pos)
    #     # Interactivity
    #     # Time Played Tracker
    #     statistics_time_played_tracker_rect_big = rect_bigs.get("statistics_time_played_tracker_rect_big")
    #     mouse_on_statistics_time_played_tracker = statistics_time_played_tracker_rect_big.collidepoint(mouse_pos)
    #     # High Score Tracker
    #     statistics_high_score_tracker_rect_big = rect_bigs.get("statistics_high_score_tracker_rect_big")
    #     mouse_on_statistics_high_score_tracker = statistics_high_score_tracker_rect_big.collidepoint(mouse_pos)
    #     # Fireballs Shot Tracker
    #     statistics_fireballs_shot_tracker_rect_big = rect_bigs.get("statistics_fireballs_shot_tracker_rect_big")
    #     mouse_on_statistics_fireballs_shot_tracker = statistics_fireballs_shot_tracker_rect_big.collidepoint(mouse_pos)
    #     # Jumps Tracker
    #     statistics_jumps_tracker_rect_big = rect_bigs.get("statistics_jumps_tracker_rect_big")
    #     mouse_on_statistics_jumps_tracker = statistics_jumps_tracker_rect_big.collidepoint(mouse_pos)
    #     # Distance Traveled Tracker
    #     statistics_distance_traveled_tracker_rect_big = rect_bigs.get("statistics_distance_traveled_tracker_rect_big")
    #     mouse_on_statistics_distance_traveled_tracker = statistics_distance_traveled_tracker_rect_big.collidepoint(mouse_pos)
    #     # Right Side
    #     # In-Game Stat Records
    #     # Highest Speed Tracker
    #     statistics_highest_speed_tracker_rect_big = rect_bigs.get("statistics_highest_speed_tracker_rect_big")
    #     mouse_on_statistics_highest_speed_tracker = statistics_highest_speed_tracker_rect_big.collidepoint(mouse_pos)
    #     # Highest Damage Tracker
    #     statistics_highest_damage_tracker_rect_big = rect_bigs.get("statistics_highest_damage_tracker_rect_big")
    #     mouse_on_statistics_highest_damage_tracker = statistics_highest_damage_tracker_rect_big.collidepoint(mouse_pos)
    #     # Highest Piercing Tracker
    #     statistics_highest_piercing_tracker_rect_big = rect_bigs.get("statistics_highest_piercing_tracker_rect_big")
    #     mouse_on_statistics_highest_piercing_tracker = statistics_highest_piercing_tracker_rect_big.collidepoint(mouse_pos)
    #     # Lowest Cooldown Tracker
    #     statistics_lowest_cooldown_tracker_rect_big = rect_bigs.get("statistics_lowest_cooldown_tracker_rect_big")
    #     mouse_on_statistics_lowest_cooldown_tracker = statistics_lowest_cooldown_tracker_rect_big.collidepoint(mouse_pos)
    #     # Buffs
    #     # Double Jump Buff Tracker
    #     statistics_double_jump_buff_tracker_rect_big = rect_bigs.get("statistics_double_jump_buff_tracker_rect_big")
    #     mouse_on_statistics_double_jump_buff_tracker = statistics_double_jump_buff_tracker_rect_big.collidepoint(mouse_pos)
    #     # Knockback Buff Tracker
    #     statistics_knockback_buff_tracker_rect_big = rect_bigs.get("statistics_knockback_buff_tracker_rect_big")
    #     mouse_on_statistics_knockback_buff_tracker = statistics_knockback_buff_tracker_rect_big.collidepoint(mouse_pos)
    #     # Shield Buff Tracker
    #     statistics_shield_buff_tracker_rect_big = rect_bigs.get("statistics_shield_buff_tracker_rect_big")
    #     mouse_on_statistics_shield_buff_tracker = statistics_shield_buff_tracker_rect_big.collidepoint(mouse_pos)
    #     # Bottom
    #     # Back Button
    #     statistics_back_button_rect_big = rect_bigs.get("statistics_back_button_rect_big")
    #     mouse_on_statistics_back_button = statistics_back_button_rect_big.collidepoint(mouse_pos)
    #     if mouse_on_statistics_back_button:
    #         if clicking_with_left_mouse:
    #             menu_section = MAIN_MENU
    # Settings Menu
    elif menu_section == SETTINGS_MENU:
        settings_sounds_button_rect_big = rect_bigs.get("settings_sounds_button_rect_big")
        mouse_on_settings_sounds_button = settings_sounds_button_rect_big.collidepoint(mouse_pos)
        settings_controls_button_rect_big = rect_bigs.get("settings_controls_button_rect_big")
        mouse_on_settings_controls_button = settings_controls_button_rect_big.collidepoint(mouse_pos)
        settings_display_button_rect_big = rect_bigs.get("settings_display_button_rect_big")
        mouse_on_settings_display_button = settings_display_button_rect_big.collidepoint(mouse_pos)
        settings_back_button_rect_big = rect_bigs.get("settings_back_button_rect_big")
        mouse_on_settings_back_button = settings_back_button_rect_big.collidepoint(mouse_pos)
        # Sounds Button
        if mouse_on_settings_sounds_button:
            if clicking_with_left_mouse:
                menu_section = SOUNDS_MENU
        # Controls Button
        elif mouse_on_settings_controls_button:
            if clicking_with_left_mouse:
                menu_section = CONTROLS_MENU
        # Display Button
        elif mouse_on_settings_display_button:
            if clicking_with_left_mouse:
                menu_section = DISPLAY_MENU
        # Back Button
        elif mouse_on_settings_back_button:
            if clicking_with_left_mouse:
                menu_section = MAIN_MENU
    # Sounds Menu
    elif menu_section == SOUNDS_MENU:
        sounds_back_button_rect_big = rect_bigs.get("sounds_back_button_rect_big")
        mouse_on_sounds_back_button = sounds_back_button_rect_big.collidepoint(mouse_pos)
        # Back Button
        if mouse_on_sounds_back_button:
            if clicking_with_left_mouse:
                menu_section = SETTINGS_MENU
    # Controls Menu
    elif menu_section == CONTROLS_MENU:
        mouse_released = event.type == pygame.MOUSEBUTTONUP
        # Controls Buttons
        for control_name, mouse_on_controls_button in mouse_on_controls_button_dict.items():
            controls_button_rect_big = controls_button_rect_big_dict[control_name]
            mouse_on_controls_button = controls_button_rect_big.collidepoint(mouse_pos)
            edited_controls_file_dict = get_edited_controls_file_dict()
            edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
            edited_control_display_name = edited_controls_display_names_dict.get(control_name)
            edited_controls_pygame_constants_names_dict = edited_controls_file_dict.get("edited_controls_pygame_constants_names_dict")
            edited_control_pygame_constant_name = edited_controls_pygame_constants_names_dict.get(control_name)
            edited_controls_are_mouse_buttons = edited_controls_file_dict.get("edited_controls_are_mouse_buttons")
            edited_control_name_is_mouse = edited_controls_are_mouse_buttons.get(control_name)
            unbound_display_name = get_display_name(list(unbound_constants_dict.keys())[0])
            current_control_set_to_unbound = edited_control_display_name == unbound_display_name
            held_control_filled = held_control_name != ""
            if current_control_set_to_unbound and can_edit_controls:
                MOUSE_WHEEL_UP = 4
                MOUSE_WHEEL_DOWN = 5
                if ((
                    event.type == pygame.KEYDOWN and hasattr(event, "key") and event.key != pygame.K_ESCAPE
                ) or (event.type == pygame.MOUSEBUTTONDOWN and hasattr(event, "button") and event.button != MOUSE_WHEEL_UP and event.button != MOUSE_WHEEL_DOWN)):
                    interpret_input(control_name,event)
                    held_control_name = ""
                    held_control_display_name = unbound_display_name
                    controls_update = True
                can_edit_controls = False
            elif unbound_display_name in edited_controls_display_names_dict and event.type == pygame.KEYDOWN and hasattr(event, "key") and event.key == pygame.K_ESCAPE:
                edited_controls_display_names_dict_index = list(edited_controls_display_names_dict.values()).index(unbound_display_name)
                edited_control_name = list(edited_controls_display_names_dict.keys())[edited_controls_display_names_dict_index]
                edited_controls_display_names_dict.update({edited_control_name:held_control_display_name})
                edited_controls_file_dict.update({"edited_controls_display_names_dict":edited_controls_display_names_dict})
                set_control_display_name_to_other_display_name(control_name, held_control_display_name)
                held_control_name = ""
                held_control_display_name = unbound_display_name
                controls_update = True
                can_edit_controls = False
            elif mouse_on_controls_button and clicking_with_left_mouse and not current_control_set_to_unbound:
                if held_control_filled:
                    set_control_display_name_to_other_display_name(held_control_name, held_control_display_name)
                held_control_name = control_name
                held_control_display_name = edited_control_display_name
                set_control_display_name_to_unbound(control_name)
                controls_update = True
            elif mouse_released:
                can_edit_controls = True
            mouse_on_controls_button_dict.update({control_name: mouse_on_controls_button})

        controls_reset_button_rect_big = rect_bigs.get("controls_reset_button_rect_big")
        mouse_on_controls_reset_button = controls_reset_button_rect_big.collidepoint(mouse_pos)
        controls_back_button_rect_big = rect_bigs.get("controls_back_button_rect_big")
        mouse_on_controls_back_button = controls_back_button_rect_big.collidepoint(mouse_pos)
        # Reset Button
        if mouse_on_controls_reset_button:
            if clicking_with_left_mouse:
                reset_controls()
                controls_update = True
        # Back Button
        elif mouse_on_controls_back_button:
            if clicking_with_left_mouse:
                menu_section = SETTINGS_MENU
    # Display Menu
    elif menu_section == DISPLAY_MENU:
        display_back_button_rect_big = rect_bigs.get("display_back_button_rect_big")
        mouse_on_display_back_button = display_back_button_rect_big.collidepoint(mouse_pos)
        display_show_controls_button_rect_big = rect_bigs.get("display_show_controls_button_rect_big")
        mouse_on_display_show_controls_button = display_show_controls_button_rect_big.collidepoint(mouse_pos)
        display_show_in_game_stats_button_rect_big = rect_bigs.get("display_show_in_game_stats_button_rect_big")
        mouse_on_display_show_in_game_stats_button = display_show_in_game_stats_button_rect_big.collidepoint(mouse_pos)
        display_show_in_game_health_button_rect_big = rect_bigs.get("display_show_in_game_health_button_rect_big")
        mouse_on_display_show_in_game_health_button = display_show_in_game_health_button_rect_big.collidepoint(mouse_pos)
        display_show_in_game_buffs_button_rect_big = rect_bigs.get("display_show_in_game_buffs_button_rect_big")
        mouse_on_display_show_in_game_buffs_button = display_show_in_game_buffs_button_rect_big.collidepoint(mouse_pos)
        display_reset_button_rect_big = rect_bigs.get("display_reset_button_rect_big")
        mouse_on_display_reset_button = display_reset_button_rect_big.collidepoint(mouse_pos)
        # Show Controls Button
        if mouse_on_display_show_controls_button:
            if clicking_with_left_mouse:
                edited_options_file_dict = get_edited_options_file_dict()
                edited_display_controls = edited_options_file_dict.get("edited_display_controls")
                edited_options_file_dict.update({"edited_display_controls":(not edited_display_controls)})
                set_edited_options_file_dict(edited_options_file_dict)
                display_controls_update = True
        # Show In Game Stats Button
        if mouse_on_display_show_in_game_stats_button:
            if clicking_with_left_mouse:
                edited_options_file_dict = get_edited_options_file_dict()
                edited_display_in_game_stats = edited_options_file_dict.get("edited_display_in_game_stats")
                edited_options_file_dict.update({"edited_display_in_game_stats":(not edited_display_in_game_stats)})
                set_edited_options_file_dict(edited_options_file_dict)
                display_in_game_stats_update = True
        # Show In Game Health Button
        if mouse_on_display_show_in_game_health_button:
            if clicking_with_left_mouse:
                edited_options_file_dict = get_edited_options_file_dict()
                edited_display_in_game_health = edited_options_file_dict.get("edited_display_in_game_health")
                edited_options_file_dict.update({"edited_display_in_game_health":(not edited_display_in_game_health)})
                set_edited_options_file_dict(edited_options_file_dict)
                display_in_game_health_update = True
        # Show In Game Buffs Button
        if mouse_on_display_show_in_game_buffs_button:
            if clicking_with_left_mouse:
                edited_options_file_dict = get_edited_options_file_dict()
                edited_display_in_game_buffs = edited_options_file_dict.get("edited_display_in_game_buffs")
                edited_options_file_dict.update({"edited_display_in_game_buffs":(not edited_display_in_game_buffs)})
                set_edited_options_file_dict(edited_options_file_dict)
                display_in_game_buffs_update = True
        # Reset Button
        if mouse_on_display_reset_button:
            if clicking_with_left_mouse:
                reset_display_options()
                display_controls_update = True
                display_in_game_stats_update = True
                display_in_game_health_update = True
                display_in_game_buffs_update = True
        # Back Button
        if mouse_on_display_back_button:
            if clicking_with_left_mouse:
                menu_section = SETTINGS_MENU

    # Main Menu Display
    # Sprite Resets
    wizard.sprite.reset()
    harold.sprite.reset()
    # Event Clear
    pygame.event.clear()
    # Timer Resets
    death_timer = 0
    bg_music_timer = 0
    # Main Menu Background, Wizard, and Harold Blits
    screen.blit(bg_surf,(0,-bg_surf.get_height() + WINDOW_HEIGHT))
    screen.blit(main_menu_wizard_surf,main_menu_wizard_rect)
    screen.blit(main_menu_harold_surf,main_menu_harold_rect)
    # Main Menu Score
    score_message_surf = test_font.render("Score: " + str(score),False,"#FCDC4D")
    score_message_surf = pygame.transform.scale_by(score_message_surf,WINDOW_SCALAR)
    score_message_rect = score_message_surf.get_rect(center = (WINDOW_WIDTH/2,(84/800 * WINDOW_HEIGHT)))
    edited_stats_file_dict = get_edited_stats_file_dict()
    edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    if score > high_score:
        edited_stats_interactivity_file_dict.update({"high_score":score})
        set_edited_stats_file_dict(edited_stats_file_dict)
    # Main Menu Score vs. Title Blit
    if score == 0: screen.blit(main_menu_title_surf,main_menu_title_rect)
    else:
        screen.blit(score_message_surf,score_message_rect)
        display_high_score(score_message_rect)

    # Menu Blits
    # Main Menu Button Blits
    if menu_section == MAIN_MENU:
        # Start Button
        if not mouse_on_main_menu_start_button: screen.blit(main_menu_start_button_surf,main_menu_start_button_rect)
        else: screen.blit(main_menu_start_button_surf_big,main_menu_start_button_rect_big)
        # Statistics Button
        if not mouse_on_main_menu_statistics_button: screen.blit(main_menu_statistics_button_surf,main_menu_statistics_button_rect)
        else: screen.blit(main_menu_statistics_button_surf_big,main_menu_statistics_button_rect_big)
        # Settings Button
        if not mouse_on_main_menu_settings_button: screen.blit(main_menu_settings_button_surf,main_menu_settings_button_rect)
        else: screen.blit(main_menu_settings_button_surf_big,main_menu_settings_button_rect_big)
        # Exit Button
        if not mouse_on_main_menu_exit_button: screen.blit(main_menu_exit_button_surf,main_menu_exit_button_rect)
        else: screen.blit(main_menu_exit_button_surf_big,main_menu_exit_button_rect_big)
    # Statistics Menu Button Blits
    elif menu_section == STATISTICS_MENU:
        # Statistics Menu
        # Left Side
        # Kills
        # Skeletons Killed Tracker
        statistics_skeletons_killed_tracker_rect_big = rect_bigs["statistics_skeletons_killed_tracker_rect_big"]
        mouse_on_statistics_skeletons_killed_tracker = statistics_skeletons_killed_tracker_rect_big.collidepoint(mouse_pos)
        # Skeleton Birds Killed Tracker
        statistics_skeleton_birds_killed_tracker_rect_big = rect_bigs.get("statistics_skeleton_birds_killed_tracker_rect_big")
        mouse_on_statistics_skeleton_birds_killed_tracker = statistics_skeleton_birds_killed_tracker_rect_big.collidepoint(mouse_pos)
        # Interactivity
        # Time Played Tracker
        statistics_time_played_tracker_rect_big = rect_bigs.get("statistics_time_played_tracker_rect_big")
        mouse_on_statistics_time_played_tracker = statistics_time_played_tracker_rect_big.collidepoint(mouse_pos)
        # High Score Tracker
        statistics_high_score_tracker_rect_big = rect_bigs.get("statistics_high_score_tracker_rect_big")
        mouse_on_statistics_high_score_tracker = statistics_high_score_tracker_rect_big.collidepoint(mouse_pos)
        # Fireballs Shot Tracker
        statistics_fireballs_shot_tracker_rect_big = rect_bigs.get("statistics_fireballs_shot_tracker_rect_big")
        mouse_on_statistics_fireballs_shot_tracker = statistics_fireballs_shot_tracker_rect_big.collidepoint(mouse_pos)
        # Jumps Tracker
        statistics_jumps_tracker_rect_big = rect_bigs.get("statistics_jumps_tracker_rect_big")
        mouse_on_statistics_jumps_tracker = statistics_jumps_tracker_rect_big.collidepoint(mouse_pos)
        # Distance Traveled Tracker
        statistics_distance_traveled_tracker_rect_big = rect_bigs.get("statistics_distance_traveled_tracker_rect_big")
        mouse_on_statistics_distance_traveled_tracker = statistics_distance_traveled_tracker_rect_big.collidepoint(mouse_pos)
        # Right Side
        # In-Game Stat Records
        # Highest Speed Tracker
        statistics_highest_speed_tracker_rect_big = rect_bigs.get("statistics_highest_speed_tracker_rect_big")
        mouse_on_statistics_highest_speed_tracker = statistics_highest_speed_tracker_rect_big.collidepoint(mouse_pos)
        # Highest Damage Tracker
        statistics_highest_damage_tracker_rect_big = rect_bigs.get("statistics_highest_damage_tracker_rect_big")
        mouse_on_statistics_highest_damage_tracker = statistics_highest_damage_tracker_rect_big.collidepoint(mouse_pos)
        # Highest Piercing Tracker
        statistics_highest_piercing_tracker_rect_big = rect_bigs.get("statistics_highest_piercing_tracker_rect_big")
        mouse_on_statistics_highest_piercing_tracker = statistics_highest_piercing_tracker_rect_big.collidepoint(mouse_pos)
        # Lowest Cooldown Tracker
        statistics_lowest_cooldown_tracker_rect_big = rect_bigs.get("statistics_lowest_cooldown_tracker_rect_big")
        mouse_on_statistics_lowest_cooldown_tracker = statistics_lowest_cooldown_tracker_rect_big.collidepoint(mouse_pos)
        # Buffs
        # Double Jump Buff Tracker
        statistics_double_jump_buff_tracker_rect_big = rect_bigs.get("statistics_double_jump_buff_tracker_rect_big")
        mouse_on_statistics_double_jump_buff_tracker = statistics_double_jump_buff_tracker_rect_big.collidepoint(mouse_pos)
        # Knockback Buff Tracker
        statistics_knockback_buff_tracker_rect_big = rect_bigs.get("statistics_knockback_buff_tracker_rect_big")
        mouse_on_statistics_knockback_buff_tracker = statistics_knockback_buff_tracker_rect_big.collidepoint(mouse_pos)
        # Shield Buff Tracker
        statistics_shield_buff_tracker_rect_big = rect_bigs.get("statistics_shield_buff_tracker_rect_big")
        mouse_on_statistics_shield_buff_tracker = statistics_shield_buff_tracker_rect_big.collidepoint(mouse_pos)
        # Bottom
        # Back Button
        statistics_back_button_rect_big = rect_bigs.get("statistics_back_button_rect_big")
        mouse_on_statistics_back_button = statistics_back_button_rect_big.collidepoint(mouse_pos)
        if mouse_on_statistics_back_button:
            if clicking_with_left_mouse:
                menu_section = MAIN_MENU
        
        
        
        # Extra Stat Checks
        if fireballs_shot != 0:
            edited_stats_file_dict = get_edited_stats_file_dict()
            edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
            fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
            fireballs_shot_total += fireballs_shot
            edited_stats_interactivity_file_dict.update({"fireballs_shot":fireballs_shot_total})
            set_edited_stats_file_dict(edited_stats_file_dict)
            fireballs_shot = 0
        if jumps_made != 0:
            edited_stats_file_dict = get_edited_stats_file_dict()
            edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
            jumps_total = edited_stats_interactivity_file_dict.get("jumps")
            jumps_total += jumps_made
            edited_stats_interactivity_file_dict.update({"jumps":jumps_total})
            set_edited_stats_file_dict(edited_stats_file_dict)
            jumps_made = 0
        if distance_traveled != 0:
            edited_stats_file_dict = get_edited_stats_file_dict()
            edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
            distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
            distance_traveled_total += distance_traveled
            edited_stats_interactivity_file_dict.update({"distance_traveled":distance_traveled_total})
            set_edited_stats_file_dict(edited_stats_file_dict)
            jumps_made = 0
        # Stats Updates
        if pre_stat_update_edited_stats_file_dict and pre_stat_update_edited_stats_file_dict != get_edited_stats_file_dict():
            pre_stat_update_edited_stats_kills_file_dict = pre_stat_update_edited_stats_file_dict.get("kills")
            pre_stat_update_edited_stats_interactivity_file_dict = pre_stat_update_edited_stats_file_dict.get("interactivity")
            pre_stat_update_edited_stats_in_game_stat_records_file_dict = pre_stat_update_edited_stats_file_dict.get("in_game_stat_records")
            pre_stat_update_edited_stats_buffs_file_dict = pre_stat_update_edited_stats_file_dict.get("buffs")
            edited_stats_file_dict = get_edited_stats_file_dict()
            edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
            edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
            edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
            edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
            # Left Side Updates
            # Kills
            if pre_stat_update_edited_stats_kills_file_dict != edited_stats_kills_file_dict:
                pre_stat_update_skeletons_killed_total = pre_stat_update_edited_stats_kills_file_dict.get("skeletons_killed")
                skeletons_killed_total = edited_stats_kills_file_dict.get("skeletons_killed")
                pre_stat_update_skeleton_birds_killed_total = pre_stat_update_edited_stats_kills_file_dict.get("skeleton_birds_killed")
                skeleton_birds_killed_total = edited_stats_kills_file_dict.get("skeleton_birds_killed")
                # Skeletons Killed Update
                if pre_stat_update_skeletons_killed_total != skeletons_killed_total:
                    statistics_skeletons_killed_tracker_surf = test_font.render(f"Skeletons Killed: {skeletons_killed_total}",False,"#FCDC4D")
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
                # Skeleton Birds Killed Update
                if pre_stat_update_skeleton_birds_killed_total != skeleton_birds_killed_total:
                    statistics_skeleton_birds_killed_tracker_surf = test_font.render(f"Skeleton Birds Killed: {skeleton_birds_killed_total}",False,"#FCDC4D")
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
            # Interactivity
            if pre_stat_update_edited_stats_interactivity_file_dict != edited_stats_interactivity_file_dict:
                pre_stat_update_time_played_total = pre_stat_update_edited_stats_interactivity_file_dict.get("time_played")
                time_played_total = edited_stats_interactivity_file_dict.get("time_played")
                pre_stat_update_high_score_total = pre_stat_update_edited_stats_interactivity_file_dict.get("high_score")
                high_score_total = edited_stats_interactivity_file_dict.get("high_score")
                pre_stat_update_fireballs_shot_total = pre_stat_update_edited_stats_interactivity_file_dict.get("fireballs_shot")
                fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
                pre_stat_update_jumps_total = pre_stat_update_edited_stats_interactivity_file_dict.get("jumps")
                jumps_total = edited_stats_interactivity_file_dict.get("jumps")
                pre_stat_update_distance_traveled_total = pre_stat_update_edited_stats_interactivity_file_dict.get("distance_traveled")
                distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
                # Time Played Update
                if pre_stat_update_time_played_total != time_played_total:
                    time_played_total = edited_stats_interactivity_file_dict.get("time_played")
                    units = {"weeks":3600 * 24 * 7,"days":3600 * 24,"hours": 3600, "minutes": 60, "seconds": 1}
                    final_displayed_time = ""
                    for unit, value in units.items():
                        count = time_played_total // value
                        time_played_total -= count * value
                        if count > 0:
                            final_displayed_time += f"{count}{unit[0]} "
                    if not final_displayed_time:
                        final_displayed_time = "0"
                    statistics_time_played_tracker_surf = test_font.render(f"Time Played: {final_displayed_time.strip()}",False,"#FCDC4D")
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
                # High Score Update
                if pre_stat_update_high_score_total != high_score_total:
                    statistics_high_score_tracker_surf = test_font.render(f"High Score: {high_score}",False,"#FCDC4D")
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
                # Fireballs Shot Update
                if pre_stat_update_fireballs_shot_total != fireballs_shot_total:
                    statistics_fireballs_shot_tracker_surf = test_font.render(f"Fireballs Shot: {fireballs_shot_total}",False,"#FCDC4D")
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
                # Jumps Update
                if pre_stat_update_jumps_total != jumps_total:
                    statistics_jumps_tracker_surf = test_font.render(f"Jumps: {jumps_total}",False,"#FCDC4D")
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
                # Distance Traveled Update
                if pre_stat_update_distance_traveled_total != distance_traveled_total:
                    statistics_distance_traveled_tracker_surf = test_font.render(f"Distance Traveled: {int(distance_traveled_total/WIZARD_WIDTH)}m",False,"#FCDC4D")
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
            # Right Side Updates
            # In-Game Stat Records
            if pre_stat_update_edited_stats_in_game_stat_records_file_dict != edited_stats_in_game_stat_records_file_dict:
                pre_stat_update_highest_speed = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_speed")
                highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
                pre_stat_update_highest_damage = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_damage")
                highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
                pre_stat_update_highest_piercing = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
                highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
                pre_stat_update_lowest_cooldown = pre_stat_update_edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
                lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
                # Highest Speed Update
                if pre_stat_update_highest_speed != highest_speed:
                    statistics_highest_speed_tracker_surf = test_font.render(f"Highest Speed: {round((highest_speed/WIZARD_WIDTH)*60,2)}m/s",False,"#FCDC4D")
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
                # Highest Damage Update
                if pre_stat_update_highest_damage != highest_damage:
                    statistics_highest_damage_tracker_surf = test_font.render(f"Highest Damage: {highest_damage}",False,"#FCDC4D")
                    statistics_highest_damage_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                    statistics_highest_damage_tracker_surf = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_scale)
                    statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_start_pos))
                    mouse_on_statistics_highest_damage_tracker = False
                    statistics_highest_damage_tracker_big_scale = button_when_big_scale
                    statistics_highest_damage_tracker_surf_big = pygame.transform.scale_by(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_big_scale)
                    statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_start_pos))
                    statistics_highest_damage_tracker_new_x_pos = statistics_highest_damage_tracker_start_x_pos + ((statistics_highest_damage_tracker_rect_big.width)/2)
                    statistics_highest_damage_tracker_new_pos = (statistics_highest_damage_tracker_new_x_pos,statistics_highest_damage_tracker_start_y_pos)
                    statistics_highest_damage_tracker_rect = statistics_highest_damage_tracker_surf.get_rect(center = (statistics_highest_damage_tracker_new_pos))
                    statistics_highest_damage_tracker_rect_big = statistics_highest_damage_tracker_surf_big.get_rect(center = (statistics_highest_damage_tracker_new_pos))
                # Highest Piercing Update
                if pre_stat_update_highest_piercing != highest_piercing:
                    statistics_highest_piercing_tracker_surf = test_font.render(f"Highest Piercing: {highest_piercing - 1}",False,"#FCDC4D")
                    statistics_highest_piercing_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                    statistics_highest_piercing_tracker_surf = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_scale)
                    statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
                    mouse_on_statistics_highest_piercing_tracker = False
                    statistics_highest_piercing_tracker_big_scale = button_when_big_scale
                    statistics_highest_piercing_tracker_surf_big = pygame.transform.scale_by(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_big_scale)
                    statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_start_pos))
                    statistics_highest_piercing_tracker_new_x_pos = statistics_highest_piercing_tracker_start_x_pos + ((statistics_highest_piercing_tracker_rect_big.width)/2)
                    statistics_highest_piercing_tracker_new_pos = (statistics_highest_piercing_tracker_new_x_pos,statistics_highest_piercing_tracker_start_y_pos)
                    statistics_highest_piercing_tracker_rect = statistics_highest_piercing_tracker_surf.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
                    statistics_highest_piercing_tracker_rect_big = statistics_highest_piercing_tracker_surf_big.get_rect(center = (statistics_highest_piercing_tracker_new_pos))
                # Lowest Cooldown Update
                if pre_stat_update_lowest_cooldown != lowest_cooldown:
                    statistics_lowest_cooldown_tracker_surf = test_font.render(f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",False,"#FCDC4D")
                    statistics_lowest_cooldown_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                    statistics_lowest_cooldown_tracker_surf = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_scale)
                    statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
                    mouse_on_statistics_lowest_cooldown_tracker = False
                    statistics_lowest_cooldown_tracker_big_scale = button_when_big_scale
                    statistics_lowest_cooldown_tracker_surf_big = pygame.transform.scale_by(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_big_scale)
                    statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_start_pos))
                    statistics_lowest_cooldown_tracker_new_x_pos = statistics_lowest_cooldown_tracker_start_x_pos + ((statistics_lowest_cooldown_tracker_rect_big.width)/2)
                    statistics_lowest_cooldown_tracker_new_pos = (statistics_lowest_cooldown_tracker_new_x_pos,statistics_lowest_cooldown_tracker_start_y_pos)
                    statistics_lowest_cooldown_tracker_rect = statistics_lowest_cooldown_tracker_surf.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
                    statistics_lowest_cooldown_tracker_rect_big = statistics_lowest_cooldown_tracker_surf_big.get_rect(center = (statistics_lowest_cooldown_tracker_new_pos))
            # Buffs
            # Double Jump Buff Update
            if edited_stats_buffs_file_dict.get("double_jump_buff"):
                statistics_double_jump_buff_tracker_surf = test_font.render("Double Jump Buff: Found",False,"#FCDC4D")
                statistics_double_jump_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                statistics_double_jump_buff_tracker_surf = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_scale)
                statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
                mouse_on_statistics_double_jump_buff_tracker = False
                statistics_double_jump_buff_tracker_big_scale = button_when_big_scale
                statistics_double_jump_buff_tracker_surf_big = pygame.transform.scale_by(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_big_scale)
                statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_start_pos))
                statistics_double_jump_buff_tracker_new_x_pos = statistics_double_jump_buff_tracker_start_x_pos + ((statistics_double_jump_buff_tracker_rect_big.width)/2)
                statistics_double_jump_buff_tracker_new_pos = (statistics_double_jump_buff_tracker_new_x_pos,statistics_double_jump_buff_tracker_start_y_pos)
                statistics_double_jump_buff_tracker_rect = statistics_double_jump_buff_tracker_surf.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
                statistics_double_jump_buff_tracker_rect_big = statistics_double_jump_buff_tracker_surf_big.get_rect(center = (statistics_double_jump_buff_tracker_new_pos))
            # Knockback Buff Update
            if edited_stats_buffs_file_dict.get("knockback_buff"):
                statistics_knockback_buff_tracker_surf = test_font.render("Knockback Buff: Found",False,"#FCDC4D")
                statistics_knockback_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                statistics_knockback_buff_tracker_surf = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_scale)
                statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
                mouse_on_statistics_knockback_buff_tracker = False
                statistics_knockback_buff_tracker_big_scale = button_when_big_scale
                statistics_knockback_buff_tracker_surf_big = pygame.transform.scale_by(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_big_scale)
                statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_start_pos))
                statistics_knockback_buff_tracker_new_x_pos = statistics_knockback_buff_tracker_start_x_pos + ((statistics_knockback_buff_tracker_rect_big.width)/2)
                statistics_knockback_buff_tracker_new_pos = (statistics_knockback_buff_tracker_new_x_pos,statistics_knockback_buff_tracker_start_y_pos)
                statistics_knockback_buff_tracker_rect = statistics_knockback_buff_tracker_surf.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
                statistics_knockback_buff_tracker_rect_big = statistics_knockback_buff_tracker_surf_big.get_rect(center = (statistics_knockback_buff_tracker_new_pos))
            # Shield Buff Update
            if edited_stats_buffs_file_dict.get("shield_buff"):
                statistics_shield_buff_tracker_surf = test_font.render("Magic Shield Buff: Found",False,"#FCDC4D")
                statistics_shield_buff_tracker_scale = WINDOW_SCALAR * statistics_tracker_scalar
                statistics_shield_buff_tracker_surf = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_scale)
                statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_start_pos))
                mouse_on_statistics_shield_buff_tracker = False
                statistics_shield_buff_tracker_big_scale = button_when_big_scale
                statistics_shield_buff_tracker_surf_big = pygame.transform.scale_by(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_big_scale)
                statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_start_pos))
                statistics_shield_buff_tracker_new_x_pos = statistics_shield_buff_tracker_start_x_pos + ((statistics_shield_buff_tracker_rect_big.width)/2)
                statistics_shield_buff_tracker_new_pos = (statistics_shield_buff_tracker_new_x_pos,statistics_shield_buff_tracker_start_y_pos)
                statistics_shield_buff_tracker_rect = statistics_shield_buff_tracker_surf.get_rect(center = (statistics_shield_buff_tracker_new_pos))
                statistics_shield_buff_tracker_rect_big = statistics_shield_buff_tracker_surf_big.get_rect(center = (statistics_shield_buff_tracker_new_pos))
        # Left Side
        # Skeletons Killed Tracker
        if not mouse_on_statistics_skeletons_killed_tracker: screen.blit(statistics_skeletons_killed_tracker_surf,statistics_skeletons_killed_tracker_rect)
        else: screen.blit(statistics_skeletons_killed_tracker_surf_big,statistics_skeletons_killed_tracker_rect_big)
        # Skeleton Birds Killed Tracker
        if not mouse_on_statistics_skeleton_birds_killed_tracker: screen.blit(statistics_skeleton_birds_killed_tracker_surf,statistics_skeleton_birds_killed_tracker_rect)
        else: screen.blit(statistics_skeleton_birds_killed_tracker_surf_big,statistics_skeleton_birds_killed_tracker_rect_big)
        # Time Played Tracker
        if not mouse_on_statistics_time_played_tracker: screen.blit(statistics_time_played_tracker_surf,statistics_time_played_tracker_rect)
        else: screen.blit(statistics_time_played_tracker_surf_big,statistics_time_played_tracker_rect_big)
        # High Score Tracker
        if not mouse_on_statistics_high_score_tracker: screen.blit(statistics_high_score_tracker_surf,statistics_high_score_tracker_rect)
        else: screen.blit(statistics_high_score_tracker_surf_big,statistics_high_score_tracker_rect_big)
        # Fireballs Shot Tracker
        if not mouse_on_statistics_fireballs_shot_tracker: screen.blit(statistics_fireballs_shot_tracker_surf,statistics_fireballs_shot_tracker_rect)
        else: screen.blit(statistics_fireballs_shot_tracker_surf_big,statistics_fireballs_shot_tracker_rect_big)
        # Jumps Tracker
        if not mouse_on_statistics_jumps_tracker: screen.blit(statistics_jumps_tracker_surf,statistics_jumps_tracker_rect)
        else: screen.blit(statistics_jumps_tracker_surf_big,statistics_jumps_tracker_rect_big)
        # Distance Traveled Tracker
        if not mouse_on_statistics_distance_traveled_tracker: screen.blit(statistics_distance_traveled_tracker_surf,statistics_distance_traveled_tracker_rect)
        else: screen.blit(statistics_distance_traveled_tracker_surf_big,statistics_distance_traveled_tracker_rect_big)
        # Right Side
        # Highest Speed Tracker
        if not mouse_on_statistics_highest_speed_tracker: screen.blit(statistics_highest_speed_tracker_surf,statistics_highest_speed_tracker_rect)
        else: screen.blit(statistics_highest_speed_tracker_surf_big,statistics_highest_speed_tracker_rect_big)
        # Highest Damage Tracker
        if not mouse_on_statistics_highest_damage_tracker: screen.blit(statistics_highest_damage_tracker_surf,statistics_highest_damage_tracker_rect)
        else: screen.blit(statistics_highest_damage_tracker_surf_big,statistics_highest_damage_tracker_rect_big)
        # Highest Piercing Tracker
        if not mouse_on_statistics_highest_piercing_tracker: screen.blit(statistics_highest_piercing_tracker_surf,statistics_highest_piercing_tracker_rect)
        else: screen.blit(statistics_highest_piercing_tracker_surf_big,statistics_highest_piercing_tracker_rect_big)
        # Lowest Cooldown Tracker
        if not mouse_on_statistics_lowest_cooldown_tracker: screen.blit(statistics_lowest_cooldown_tracker_surf,statistics_lowest_cooldown_tracker_rect)
        else: screen.blit(statistics_lowest_cooldown_tracker_surf_big,statistics_lowest_cooldown_tracker_rect_big)
        # Double Jump Buff Tracker
        if not mouse_on_statistics_double_jump_buff_tracker: screen.blit(statistics_double_jump_buff_tracker_surf,statistics_double_jump_buff_tracker_rect)
        else: screen.blit(statistics_double_jump_buff_tracker_surf_big,statistics_double_jump_buff_tracker_rect_big)
        # Knockback Buff Tracker
        if not mouse_on_statistics_knockback_buff_tracker: screen.blit(statistics_knockback_buff_tracker_surf,statistics_knockback_buff_tracker_rect)
        else: screen.blit(statistics_knockback_buff_tracker_surf_big,statistics_knockback_buff_tracker_rect_big)
        # Shield Buff Tracker
        if not mouse_on_statistics_shield_buff_tracker: screen.blit(statistics_shield_buff_tracker_surf,statistics_shield_buff_tracker_rect)
        else: screen.blit(statistics_shield_buff_tracker_surf_big,statistics_shield_buff_tracker_rect_big)
        # Bottom
        # Back Button
        if not mouse_on_statistics_back_button: screen.blit(statistics_back_button_surf,statistics_back_button_rect)
        else: screen.blit(statistics_back_button_surf_big,statistics_back_button_rect_big)
        pre_stat_update_edited_stats_file_dict = {}
    # Settings Menu Button Blits
    elif menu_section == SETTINGS_MENU:
        # Sounds Button
        if not mouse_on_settings_sounds_button: screen.blit(settings_sounds_button_surf,settings_sounds_button_rect)
        else: screen.blit(settings_sounds_button_surf_big,settings_sounds_button_rect_big)
        # Controls Button
        if not mouse_on_settings_controls_button: screen.blit(settings_controls_button_surf,settings_controls_button_rect)
        else: screen.blit(settings_controls_button_surf_big,settings_controls_button_rect_big)
        # Display Button
        if not mouse_on_settings_display_button: screen.blit(settings_display_button_surf,settings_display_button_rect)
        else: screen.blit(settings_display_button_surf_big,settings_display_button_rect_big)
        # Back Button
        if not mouse_on_settings_back_button: screen.blit(settings_back_button_surf,settings_back_button_rect)
        else: screen.blit(settings_back_button_surf_big,settings_back_button_rect_big)
    # Sounds Menu Button Blits
    elif menu_section == SOUNDS_MENU:
        # Back Button
        if not mouse_on_sounds_back_button: screen.blit(sounds_back_button_surf,sounds_back_button_rect)
        else: screen.blit(sounds_back_button_surf_big,sounds_back_button_rect_big)
    # Controls Menu Button Blits
    elif menu_section == CONTROLS_MENU:
        # Controls Update
        if controls_update:
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
            controls_update = False
        # Controls Buttons
        for control_name, mouse_on_controls_button in mouse_on_controls_button_dict.items():
            if not mouse_on_controls_button: screen.blit(controls_button_surf_dict[control_name],controls_button_rect_dict[control_name])
            else: screen.blit(controls_button_surf_big_dict[control_name],controls_button_rect_big_dict[control_name])
        # Reset Button
        if not mouse_on_controls_reset_button: screen.blit(controls_reset_button_surf,controls_reset_button_rect)
        else: screen.blit(controls_reset_button_surf_big,controls_reset_button_rect_big)
        # Back Button
        if not mouse_on_controls_back_button: screen.blit(controls_back_button_surf,controls_back_button_rect)
        else: screen.blit(controls_back_button_surf_big,controls_back_button_rect_big)
    # Display Menu Button Blits
    elif menu_section == DISPLAY_MENU:
        # Display Controls Update
        if display_controls_update:
            controls_displayed = get_edited_options_file_dict()["edited_display_controls"]
            display_show_controls_button_surf = test_font.render(f"Display Controls: {controls_displayed}",False,"#FCDC4D")
            display_show_controls_button_scale = WINDOW_SCALAR * display_button_scalar
            display_show_controls_button_surf = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_scale)
            display_show_controls_button_rect = display_show_controls_button_surf.get_rect(center = (display_show_controls_button_start_pos))
            mouse_on_display_show_controls_button = False
            display_show_controls_button_big_scale = button_when_big_scale
            display_show_controls_button_surf_big = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_big_scale)
            display_show_controls_button_rect_big = display_show_controls_button_surf_big.get_rect(center = (display_show_controls_button_start_pos))
            display_controls_update = False
        if display_in_game_stats_update:
            in_game_stats_displayed = get_edited_options_file_dict()["edited_display_in_game_stats"]
            display_show_in_game_stats_button_surf = test_font.render(f"Display Stats: {in_game_stats_displayed}",False,"#FCDC4D")
            display_show_in_game_stats_button_scale = WINDOW_SCALAR * display_button_scalar
            display_show_in_game_stats_button_surf = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_scale)
            display_show_in_game_stats_button_rect = display_show_in_game_stats_button_surf.get_rect(center = (display_show_in_game_stats_button_start_pos))
            mouse_on_display_show_in_game_stats_button = False
            display_show_in_game_stats_button_big_scale = button_when_big_scale
            display_show_in_game_stats_button_surf_big = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_big_scale)
            display_show_in_game_stats_button_rect_big = display_show_in_game_stats_button_surf_big.get_rect(center = (display_show_in_game_stats_button_start_pos))
            display_in_game_stats_update = False
        if display_in_game_health_update:
            in_game_health_displayed = get_edited_options_file_dict()["edited_display_in_game_health"]
            display_show_in_game_health_button_surf = test_font.render(f"Display Health: {in_game_health_displayed}",False,"#FCDC4D")
            display_show_in_game_health_button_scale = WINDOW_SCALAR * display_button_scalar
            display_show_in_game_health_button_surf = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_scale)
            display_show_in_game_health_button_rect = display_show_in_game_health_button_surf.get_rect(center = (display_show_in_game_health_button_start_pos))
            mouse_on_display_show_in_game_health_button = False
            display_show_in_game_health_button_big_scale = button_when_big_scale
            display_show_in_game_health_button_surf_big = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_big_scale)
            display_show_in_game_health_button_rect_big = display_show_in_game_health_button_surf_big.get_rect(center = (display_show_in_game_health_button_start_pos))
            display_in_game_health_update = False
        if display_in_game_buffs_update:
            in_game_buffs_displayed = get_edited_options_file_dict()["edited_display_in_game_buffs"]
            display_show_in_game_buffs_button_surf = test_font.render(f"Display Buffs: {in_game_buffs_displayed}",False,"#FCDC4D")
            display_show_in_game_buffs_button_scale = WINDOW_SCALAR * display_button_scalar
            display_show_in_game_buffs_button_surf = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_scale)
            display_show_in_game_buffs_button_rect = display_show_in_game_buffs_button_surf.get_rect(center = (display_show_in_game_buffs_button_start_pos))
            mouse_on_display_show_in_game_buffs_button = False
            display_show_in_game_buffs_button_big_scale = button_when_big_scale
            display_show_in_game_buffs_button_surf_big = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_big_scale)
            display_show_in_game_buffs_button_rect_big = display_show_in_game_buffs_button_surf_big.get_rect(center = (display_show_in_game_buffs_button_start_pos))
            display_in_game_buffs_update = False
        # Show Controls Button
        if not mouse_on_display_show_controls_button: screen.blit(display_show_controls_button_surf,display_show_controls_button_rect)
        else: screen.blit(display_show_controls_button_surf_big,display_show_controls_button_rect_big)
        # Show In Game Stats Button
        if not mouse_on_display_show_in_game_stats_button: screen.blit(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_rect)
        else: screen.blit(display_show_in_game_stats_button_surf_big,display_show_in_game_stats_button_rect_big)
        # Show In Game Health Button
        if not mouse_on_display_show_in_game_health_button: screen.blit(display_show_in_game_health_button_surf,display_show_in_game_health_button_rect)
        else: screen.blit(display_show_in_game_health_button_surf_big,display_show_in_game_health_button_rect_big)
        # Show In Game Buffs Button
        if not mouse_on_display_show_in_game_buffs_button: screen.blit(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_rect)
        else: screen.blit(display_show_in_game_buffs_button_surf_big,display_show_in_game_buffs_button_rect_big)
        # Reset Button
        if not mouse_on_display_reset_button: screen.blit(display_reset_button_surf,display_reset_button_rect)
        else: screen.blit(display_reset_button_surf_big,display_reset_button_rect_big)
        # Back Button
        if not mouse_on_display_back_button: screen.blit(display_back_button_surf,display_back_button_rect)
        else: screen.blit(display_back_button_surf_big,display_back_button_rect_big)

