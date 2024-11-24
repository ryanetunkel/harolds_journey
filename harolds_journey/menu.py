"""Contains all menu-related items"""
import math

import pygame_menu
import pygame_menu.locals

from controls import *
from global_vars import *
from harold import *
from player import *

# Global Variables
center_screen = window_width / 2

# Main Menu Screen
MAIN_MENU = 1
STATISTICS_MENU = 2
SETTINGS_MENU = 3
SOUNDS_MENU = 4
CONTROLS_MENU = 5
DISPLAY_MENU = 6
menu_section = MAIN_MENU

controls_update = False

# Statistics Menu
statistics_tracker_scalar = 0.4
statistics_trackers_y_pos_offset = window_height * 1/44
edited_stats_file_dict = get_edited_stats_file_dict()
edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
fireballs_shot = 0
jumps_made = 0
distance_traveled = 0
highest_speed = 0
pre_stat_update_edited_stats_file_dict = {}

# Wizard on Menu Screen
wizard_path = "harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png"
main_menu_wizard_start_x_pos = center_screen
main_menu_wizard_start_y_pos = 54/400 * window_height + (1.5 * (96 * window_scalar))
main_menu_wizard_hat_size = 24 * window_scalar
main_menu_wizard_surf = pygame.image.load(wizard_path).convert_alpha()
main_menu_wizard_height_by_scale = 96 * window_scalar
main_menu_wizard_width_by_scale = 96 * window_scalar
main_menu_wizard_size_by_scale = (main_menu_wizard_height_by_scale,main_menu_wizard_width_by_scale)
main_menu_wizard_surf = pygame.transform.scale(main_menu_wizard_surf,main_menu_wizard_size_by_scale)
main_menu_wizard_rect = main_menu_wizard_surf.get_rect(midbottom = (main_menu_wizard_start_x_pos,main_menu_wizard_start_y_pos))

# Harold on Menu Screen
harold_path = "harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png"
# main_menu_harold_start_x_pos = CENTER_SCREEN
# main_menu_harold_start_y_pos = main_menu_wizard_rect.top + main_menu_wizard_hat_size
# main_menu_harold_surf = pygame.image.load(harold_path).convert_alpha()
main_menu_harold_height_by_scale = main_menu_wizard_height_by_scale * 3/8
main_menu_harold_width_by_scale = main_menu_wizard_width_by_scale * 3/8
# main_menu_harold_size_by_scale = (main_menu_harold_height_by_scale,main_menu_harold_width_by_scale)
# main_menu_harold_surf = pygame.transform.scale(main_menu_harold_surf,main_menu_harold_size_by_scale)
# main_menu_harold_rect = main_menu_harold_surf.get_rect(midbottom = (main_menu_harold_start_x_pos,main_menu_harold_start_y_pos))

button_when_big_scale = 1.1

# Pre-Menu Functions
def on_resize(menu:pygame_menu.Menu) -> None:
    """
    Function checked if the window is resized.
    """
    global window_width
    global window_height
    global window_size
    global window_scalar
    global grass_top_y

    current_window_size = screen.get_size()
    new_w, new_h = current_window_size[0], current_window_size[1]

    new_w = max(new_w,min_window_width)
    new_h = max(new_h,min_window_height)

    window_width = new_w
    window_height = new_h
    window_size = (window_width,window_height)
    window_scalar = ((window_width + window_height)/1200)
    grass_top_y = int((379 / 400) * window_height)
    menu.resize(new_w, new_h)


# Selections
main_menu_selection = pygame_menu.widgets.SimpleSelection()

# Base Images
# Background
main_menu_bg = pygame_menu.BaseImage(
    image_path=bg_image_path,
)
main_menu_bg = main_menu_bg.resize(main_menu_bg.get_width()*bg_scalar,main_menu_bg.get_height()*bg_scalar,smooth=False)
main_menu_bg = main_menu_bg.crop_rect((0,bg_surf.get_height()-window_height,window_width,window_height))
# Adjust cropping based on resizing of window - need to snap to the bottomcenter

# Wizard
main_menu_wizard = pygame_menu.BaseImage(
    image_path=wizard_path,
)
main_menu_wizard = main_menu_wizard.resize(main_menu_wizard_width_by_scale,main_menu_wizard_height_by_scale,smooth=False)

# Harold
main_menu_harold = pygame_menu.BaseImage(
    image_path=harold_path,
)
main_menu_harold = main_menu_harold.resize(main_menu_harold_width_by_scale,main_menu_harold_height_by_scale,smooth=False)

# Maybe add images as blank labels/unreachable small menus

# Text Vars
font_color = "#FCDC4D"
font_name = pygame_menu.font.FONT_MUNRO
# Title Vars
title_font_size = int(window_height/16)
title_padding = int(window_height/64)
title_y_pos_center_offset = -window_height/2+title_font_size+int(window_height/64)


# Themes
# Base Menu Theme
base_menu_theme = pygame_menu.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=main_menu_bg,
    widget_offset=(0,window_height*7/16),
    widget_selection_effect = main_menu_selection,
    widget_border_inflate=(math.ceil(window_scalar*button_when_big_scale),math.ceil(window_scalar*button_when_big_scale)),
    title_font=font_name,
    title_font_color=font_color,
    title_close_button=False,
    title=False,
    cursor_selection_color="#FFFFFF",
)

# Main Menu Theme
main_menu_theme = base_menu_theme.copy()

# Pause Menu Theme
pause_menu_theme = base_menu_theme.copy()
pause_menu_theme.background_color = (50,50,50,50)


# Menus
# Main Menu
main_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=main_menu_theme,
    center_content=False,
)

# Pause Menu
pause_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=pause_menu_theme,
    center_content=False,
)

# Statistics Menu
main_statistics_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=main_menu_theme,
    center_content=False,
)

# Settings Menu
main_settings_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=main_menu_theme,
    center_content=False,
)

# Pause Statistics Menu
pause_statistics_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=pause_menu_theme,
    center_content=False,
)

# Pause Settings Menu
pause_settings_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=pause_menu_theme,
    center_content=False,
)


# Post-Menu Functions
# Main Menu Function
def update_main_menu_and_submenus() -> pygame_menu.Menu:
    global base_menu_theme
    global main_menu_theme
    global main_menu
    global main_statistics_menu
    global main_settings_menu
    global main_menu_start_button

    # Main Menu Theme
    main_menu_theme = base_menu_theme.copy()

    # Menus
    # Main Menu
    main_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_menu_theme,
        center_content=False,
    )

    # Statistics Menu
    main_statistics_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_menu_theme,
        center_content=False,
    )

    # Settings Menu
    main_settings_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_menu_theme,
        center_content=False,
    )


    # Labels
    # Main Menu Label
    main_menu_label = main_menu.add.label(
        title="Harold\'s Journey",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)

    # Main Statistics Menu Label
    main_statistics_menu_label = main_statistics_menu.add.label(
        title="Statistics",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)

    # Main Settings Menu Label
    main_settings_menu_label = main_settings_menu.add.label(
        title="Settings",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)


    # Buttons
    # Main Menu Buttons
    main_menu_start_button = main_menu.add.button(
        title="Start Game",
        action=main_menu.disable,  # Activates as soon as menu is displayed and then doesn't work once the game ends
        font_color=font_color,
        font_name=font_name,
    )
    # start_game() happens right away and then can't be clicked again
    # start_game never starts no matter what even though it should be what works
    main_menu_statistics_button = main_menu.add.button(
        title="Statistics",
        action=main_statistics_menu,
        font_color=font_color,
        font_name=font_name,
    )
    main_menu_settings_button = main_menu.add.button(
        title="Settings",
        action=main_settings_menu,
        font_color=font_color,
        font_name=font_name,
    )
    main_menu_exit_button = main_menu.add.button(
        title="Quit",
        action=pygame_menu.events.EXIT,
        font_color=font_color,
        font_name=font_name,
    )
    # onselect is callback when selected
    # action is when "clicked" - unsure exact but that is what happens usually

    # Statistics Menu Buttons
    main_statistics_menu_back_button = main_statistics_menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
    )

    # Settings Menu Buttons
    main_settings_menu_back_button = main_settings_menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
    )

    # Extra Draws
    # Extra Main Menu Draws
    # WIP
    main_menu_wizard_rect = main_menu_wizard.get_rect()
    main_menu_harold_rect = main_menu_harold.get_rect()
    main_menu_wizard.draw(screen,area=main_menu_wizard_rect)
    main_menu_harold.draw(screen,area=main_menu_harold_rect)
    # Don't work - old attempt
    # main_menu_wizard.draw(screen)
    # main_menu_harold.draw(screen)

    return main_menu


# Pause Menu Function
def update_pause_menu_and_submenus(new_background_color=None) -> pygame_menu.Menu:
    global base_menu_theme
    global pause_menu_theme
    global pause_menu
    global pause_statistics_menu
    global pause_settings_menu

    # Pause Menu Theme
    pause_menu_theme = base_menu_theme.copy()
    if new_background_color:
        pause_menu_theme.background_color = new_background_color

    # Menus
    # Pause Menu
    pause_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_menu_theme,
        center_content=False,
    )

    # Pause Statistics Menu
    pause_statistics_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_menu_theme,
        center_content=False,
    )

    # Pause Settings Menu
    pause_settings_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_menu_theme,
        center_content=False,
    )

    # Labels
    # Pause Menu Label
    pause_menu_label = pause_menu.add.label(
        title="GAME PAUSED",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)

    # Pause Statistics Menu Label
    pause_statistics_menu_label = pause_statistics_menu.add.label(
        title="Statistics",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)

    # Pause Settings Menu Label
    pause_settings_menu_label = pause_settings_menu.add.label(
        title="Settings",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,title_y_pos_center_offset)

    # Extra Draws
    # Extra Pause Menu Draws

    # Buttons
    # Pause Menu Buttons
    pause_menu_statistics_button = pause_menu.add.button(
        title="Statistics",
        action=pause_statistics_menu,
        font_color=font_color,
        font_name=font_name,
    )
    pause_menu_settings_button = pause_menu.add.button(
        title="Settings",
        action=pause_settings_menu,
        font_color=font_color,
        font_name=font_name,
    )
    pause_menu_back_button = pause_menu.add.button(
        title="Back to Game",
        action=pause_menu.disable,
        font_color=font_color,
        font_name=font_name,
    )
    pause_menu_padding = pause_menu.add.vertical_margin(window_height/16)
    pause_menu_end_game_button = pause_menu.add.button(
        title="End Current Game",
        action=end_game,
        font_color=font_color,
        font_name=font_name,
    )

    # Pause Statistics Menu Buttons
    pause_statistics_menu_back_button = pause_statistics_menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
    )

    # Pause Settings Menu Buttons
    pause_settings_menu_back_button = pause_settings_menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
    )

    return pause_menu


def end_game():
    global wizard
    global pause_menu
    wizard.sprite.set_wizard_dead(True)
    pause_menu.disable()


# Creating Full Main and Pause Menus via Functions
main_menu = update_main_menu_and_submenus()
pause_menu = update_pause_menu_and_submenus((50,50,50,50))

# Enabling Menus
main_menu.enable()
pause_menu.enable()

# Initial Resizing
on_resize(main_menu)
on_resize(pause_menu)



# Old Code
# Main Menu
# Start Button
main_menu_start_button_start_x_pos = center_screen
main_menu_start_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
main_menu_start_button_start_pos = (main_menu_start_button_start_x_pos,main_menu_start_button_start_y_pos)
main_menu_start_button_surf = test_font.render("Start Game",False,font_color)
main_menu_start_button_scale = window_scalar
main_menu_start_button_surf = pygame.transform.scale_by(main_menu_start_button_surf,main_menu_start_button_scale)
main_menu_start_button_rect = main_menu_start_button_surf.get_rect(center = (main_menu_start_button_start_pos))
mouse_on_main_menu_start_button = False
main_menu_start_button_big_scale = button_when_big_scale
main_menu_start_button_surf_big = pygame.transform.scale_by(main_menu_start_button_surf,main_menu_start_button_big_scale)
main_menu_start_button_rect_big = main_menu_start_button_surf_big.get_rect(center = (main_menu_start_button_start_pos))
# Statistics Button
main_menu_statistics_button_start_x_pos = center_screen
main_menu_statistics_button_start_y_pos = main_menu_start_button_rect_big.bottom + ((32/400) * window_height)
main_menu_statistics_button_start_pos = (main_menu_statistics_button_start_x_pos,main_menu_statistics_button_start_y_pos)
main_menu_statistics_button_surf = test_font.render("Statistics",False,font_color)
main_menu_statistics_button_scale = window_scalar
main_menu_statistics_button_surf = pygame.transform.scale_by(main_menu_statistics_button_surf,main_menu_statistics_button_scale)
main_menu_statistics_button_rect = main_menu_statistics_button_surf.get_rect(center = (main_menu_statistics_button_start_pos))
mouse_on_main_menu_statistics_button = False
main_menu_statistics_button_big_scale = button_when_big_scale
main_menu_statistics_button_surf_big = pygame.transform.scale_by(main_menu_statistics_button_surf,main_menu_statistics_button_big_scale)
main_menu_statistics_button_rect_big = main_menu_statistics_button_surf_big.get_rect(center = (main_menu_statistics_button_start_pos))
# Settings Button
main_menu_settings_button_start_x_pos = center_screen
main_menu_settings_button_start_y_pos = main_menu_statistics_button_rect_big.bottom + ((32/400) * window_height)
main_menu_settings_button_start_pos = (main_menu_settings_button_start_x_pos,main_menu_settings_button_start_y_pos)
main_menu_settings_button_surf = test_font.render("Settings",False,font_color)
main_menu_settings_button_scale = window_scalar
main_menu_settings_button_surf = pygame.transform.scale_by(main_menu_settings_button_surf,main_menu_settings_button_scale)
main_menu_settings_button_rect = main_menu_settings_button_surf.get_rect(center = (main_menu_settings_button_start_pos))
mouse_on_main_menu_settings_button = False
main_menu_settings_button_big_scale = button_when_big_scale
main_menu_settings_button_surf_big = pygame.transform.scale_by(main_menu_settings_button_surf,main_menu_settings_button_big_scale)
main_menu_settings_button_rect_big = main_menu_settings_button_surf_big.get_rect(center = (main_menu_settings_button_start_pos))
# Exit Button
main_menu_exit_button_start_x_pos = center_screen
main_menu_exit_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
main_menu_exit_button_start_pos = (main_menu_exit_button_start_x_pos,main_menu_exit_button_start_y_pos)
main_menu_exit_button_surf = test_font.render("Exit",False,font_color)
main_menu_exit_button_scale = window_scalar
main_menu_exit_button_surf = pygame.transform.scale_by(main_menu_exit_button_surf,main_menu_exit_button_scale)
main_menu_exit_button_rect = main_menu_exit_button_surf.get_rect(center = (main_menu_exit_button_start_pos))
mouse_on_main_menu_exit_button = False
main_menu_exit_button_big_scale = button_when_big_scale
main_menu_exit_button_surf_big = pygame.transform.scale_by(main_menu_exit_button_surf,main_menu_exit_button_big_scale)
main_menu_exit_button_rect_big = main_menu_exit_button_surf_big.get_rect(center = (main_menu_exit_button_start_pos))


# Left Side
# Kills
# Skeletons Killed Tracker
skeletons_killed_total = edited_stats_kills_file_dict.get("skeletons_killed")
statistics_skeletons_killed_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_skeletons_killed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
statistics_skeletons_killed_tracker_start_pos = (statistics_skeletons_killed_tracker_start_x_pos,statistics_skeletons_killed_tracker_start_y_pos)
statistics_skeletons_killed_tracker_surf = test_font.render(f"Skeletons Killed: {skeletons_killed_total}",False,font_color)
statistics_skeletons_killed_tracker_scale = window_scalar * statistics_tracker_scalar
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
skeleton_birds_killed_total = edited_stats_kills_file_dict.get("skeleton_birds_killed")
statistics_skeleton_birds_killed_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_skeleton_birds_killed_tracker_start_y_pos = statistics_skeletons_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_skeleton_birds_killed_tracker_start_pos = (statistics_skeleton_birds_killed_tracker_start_x_pos,statistics_skeleton_birds_killed_tracker_start_y_pos)
statistics_skeleton_birds_killed_tracker_surf = test_font.render(f"Skeleton Birds Killed: {skeleton_birds_killed_total}",False,font_color)
statistics_skeleton_birds_killed_tracker_scale = window_scalar * statistics_tracker_scalar
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
statistics_time_played_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_time_played_tracker_start_y_pos = statistics_skeleton_birds_killed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_time_played_tracker_start_pos = (statistics_time_played_tracker_start_x_pos,statistics_time_played_tracker_start_y_pos)
statistics_time_played_tracker_surf = test_font.render(f"Time Played: {final_displayed_time.strip()}",False,font_color)
statistics_time_played_tracker_scale = window_scalar * statistics_tracker_scalar
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
high_score = edited_stats_interactivity_file_dict.get("high_score")
statistics_high_score_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_high_score_tracker_start_y_pos = statistics_time_played_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_high_score_tracker_start_pos = (statistics_high_score_tracker_start_x_pos,statistics_high_score_tracker_start_y_pos)
statistics_high_score_tracker_surf = test_font.render(f"High Score: {high_score}",False,font_color)
statistics_high_score_tracker_scale = window_scalar * statistics_tracker_scalar
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
fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
statistics_fireballs_shot_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_fireballs_shot_tracker_start_y_pos = statistics_high_score_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_fireballs_shot_tracker_start_pos = (statistics_fireballs_shot_tracker_start_x_pos,statistics_fireballs_shot_tracker_start_y_pos)
statistics_fireballs_shot_tracker_surf = test_font.render(f"Fireballs Shot: {fireballs_shot_total}",False,font_color)
statistics_fireballs_shot_tracker_scale = window_scalar * statistics_tracker_scalar
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
jumps_total = edited_stats_interactivity_file_dict.get("jumps")
statistics_jumps_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_jumps_tracker_start_y_pos = statistics_fireballs_shot_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_jumps_tracker_start_pos = (statistics_jumps_tracker_start_x_pos,statistics_jumps_tracker_start_y_pos)
statistics_jumps_tracker_surf = test_font.render(f"Jumps: {jumps_total}",False,font_color)
statistics_jumps_tracker_scale = window_scalar * statistics_tracker_scalar
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
distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
statistics_distance_traveled_tracker_start_x_pos = center_screen - statistics_trackers_y_pos_offset
statistics_distance_traveled_tracker_start_y_pos = statistics_jumps_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_distance_traveled_tracker_start_pos = (statistics_distance_traveled_tracker_start_x_pos,statistics_distance_traveled_tracker_start_y_pos)
statistics_distance_traveled_tracker_surf = test_font.render(f"Distance Traveled: {int(distance_traveled_total/WIZARD_WIDTH)}m",False,font_color)
statistics_distance_traveled_tracker_scale = window_scalar * statistics_tracker_scalar
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
# In-Game Stat Records
# Highest Speed Tracker
highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
statistics_highest_speed_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_highest_speed_tracker_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
statistics_highest_speed_tracker_start_pos = (statistics_highest_speed_tracker_start_x_pos,statistics_highest_speed_tracker_start_y_pos)
statistics_highest_speed_tracker_surf = test_font.render(f"Highest Speed: {round((highest_speed/WIZARD_WIDTH)*60,2)}m/s",False,font_color)
statistics_highest_speed_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Highest Damage Tracker
highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
statistics_highest_damage_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_highest_damage_tracker_start_y_pos = statistics_highest_speed_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_highest_damage_tracker_start_pos = (statistics_highest_damage_tracker_start_x_pos,statistics_highest_damage_tracker_start_y_pos)
statistics_highest_damage_tracker_surf = test_font.render(f"Highest Damage: {highest_damage}",False,font_color)
statistics_highest_damage_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Highest Piercing Tracker
highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
statistics_highest_piercing_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_highest_piercing_tracker_start_y_pos = statistics_highest_damage_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_highest_piercing_tracker_start_pos = (statistics_highest_piercing_tracker_start_x_pos,statistics_highest_piercing_tracker_start_y_pos)
statistics_highest_piercing_tracker_surf = test_font.render(f"Highest Piercing: {highest_piercing - 1}",False,font_color)
statistics_highest_piercing_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Lowest Cooldown Tracker
lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
statistics_lowest_cooldown_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_lowest_cooldown_tracker_start_y_pos = statistics_highest_piercing_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_lowest_cooldown_tracker_start_pos = (statistics_lowest_cooldown_tracker_start_x_pos,statistics_lowest_cooldown_tracker_start_y_pos)
statistics_lowest_cooldown_tracker_surf = test_font.render(f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",False,font_color)
statistics_lowest_cooldown_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Double Jump Buff Tracker
double_jump_buff_found = edited_stats_buffs_file_dict.get("double_jump_buff")
double_jump_buff_string = "???: Not Yet Found" if not double_jump_buff_found else "Double Jump Buff: Found"
statistics_double_jump_buff_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_double_jump_buff_tracker_start_y_pos = statistics_lowest_cooldown_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_double_jump_buff_tracker_start_pos = (statistics_double_jump_buff_tracker_start_x_pos,statistics_double_jump_buff_tracker_start_y_pos)
statistics_double_jump_buff_tracker_surf = test_font.render(double_jump_buff_string,False,font_color)
statistics_double_jump_buff_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Knockback Buff Tracker
knockback_buff_found = edited_stats_buffs_file_dict.get("knockback_buff")
knockback_buff_string = "???: Not Yet Found" if not knockback_buff_found else "Knockback Buff: Found"
statistics_knockback_buff_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_knockback_buff_tracker_start_y_pos = statistics_double_jump_buff_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_knockback_buff_tracker_start_pos = (statistics_knockback_buff_tracker_start_x_pos,statistics_knockback_buff_tracker_start_y_pos)
statistics_knockback_buff_tracker_surf = test_font.render(knockback_buff_string,False,font_color)
statistics_knockback_buff_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Shield Buff Tracker
shield_buff_found = edited_stats_buffs_file_dict.get("shield_buff")
shield_buff_string = "???: Not Yet Found" if not shield_buff_found else "Magic Shield Buff: Found"
statistics_shield_buff_tracker_start_x_pos = center_screen + statistics_trackers_y_pos_offset
statistics_shield_buff_tracker_start_y_pos = statistics_knockback_buff_tracker_rect_big.bottom + statistics_trackers_y_pos_offset
statistics_shield_buff_tracker_start_pos = (statistics_shield_buff_tracker_start_x_pos,statistics_shield_buff_tracker_start_y_pos)
statistics_shield_buff_tracker_surf = test_font.render(shield_buff_string,False,font_color)
statistics_shield_buff_tracker_scale = window_scalar * statistics_tracker_scalar
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
# Bottom
# Back Button
statistics_back_button_start_x_pos = center_screen
statistics_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
statistics_back_button_start_pos = (statistics_back_button_start_x_pos,statistics_back_button_start_y_pos)
statistics_back_button_surf = test_font.render("Main Menu",False,font_color)
statistics_back_button_scale = window_scalar
statistics_back_button_surf = pygame.transform.scale_by(statistics_back_button_surf,statistics_back_button_scale)
statistics_back_button_rect = statistics_back_button_surf.get_rect(center = (statistics_back_button_start_pos))
mouse_on_statistics_back_button = False
statistics_back_button_big_scale = button_when_big_scale
statistics_back_button_surf_big = pygame.transform.scale_by(statistics_back_button_surf,statistics_back_button_big_scale)
statistics_back_button_rect_big = statistics_back_button_surf_big.get_rect(center = (statistics_back_button_start_pos))

# Settings
# Sounds Button
settings_sounds_button_start_x_pos = center_screen
settings_sounds_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
settings_sounds_button_start_pos = (settings_sounds_button_start_x_pos,settings_sounds_button_start_y_pos)
settings_sounds_button_surf = test_font.render("Sounds",False,font_color)
settings_sounds_button_scale = window_scalar
settings_sounds_button_surf = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_scale)
settings_sounds_button_rect = settings_sounds_button_surf.get_rect(center = (settings_sounds_button_start_pos))
mouse_on_settings_sounds_button = False
settings_sounds_button_big_scale = button_when_big_scale
settings_sounds_button_surf_big = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_big_scale)
settings_sounds_button_rect_big = settings_sounds_button_surf_big.get_rect(center = (settings_sounds_button_start_pos))
# Controls Button
settings_controls_button_start_x_pos = center_screen
settings_controls_button_start_y_pos = settings_sounds_button_rect_big.bottom + ((32/400) * window_height)
settings_controls_button_start_pos = (settings_controls_button_start_x_pos,settings_controls_button_start_y_pos)
settings_controls_button_surf = test_font.render("Controls",False,font_color)
settings_controls_button_scale = window_scalar
settings_controls_button_surf = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_scale)
settings_controls_button_rect = settings_controls_button_surf.get_rect(center = (settings_controls_button_start_pos))
mouse_on_settings_controls_button = False
settings_controls_button_big_scale = button_when_big_scale
settings_controls_button_surf_big = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_big_scale)
settings_controls_button_rect_big = settings_controls_button_surf_big.get_rect(center = (settings_controls_button_start_pos))
# Display Button
settings_display_button_start_x_pos = center_screen
settings_display_button_start_y_pos = settings_controls_button_rect_big.bottom + ((32/400) * window_height)
settings_display_button_start_pos = (settings_display_button_start_x_pos,settings_display_button_start_y_pos)
settings_display_button_surf = test_font.render("Display",False,font_color)
settings_display_button_scale = window_scalar
settings_display_button_surf = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_scale)
settings_display_button_rect = settings_display_button_surf.get_rect(center = (settings_display_button_start_pos))
mouse_on_settings_display_button = False
settings_display_button_big_scale = button_when_big_scale
settings_display_button_surf_big = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_big_scale)
settings_display_button_rect_big = settings_display_button_surf_big.get_rect(center = (settings_display_button_start_pos))
# Back Button
settings_back_button_start_x_pos = center_screen
settings_back_button_start_y_pos = settings_display_button_rect_big.bottom + ((32/400) * window_height)
settings_back_button_start_pos = (settings_back_button_start_x_pos,settings_back_button_start_y_pos)
settings_back_button_surf = test_font.render("Main Menu",False,font_color)
settings_back_button_scale = window_scalar
settings_back_button_surf = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_scale)
settings_back_button_rect = settings_back_button_surf.get_rect(center = (settings_back_button_start_pos))
mouse_on_settings_back_button = False
settings_back_button_big_scale = button_when_big_scale
settings_back_button_surf_big = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_big_scale)
settings_back_button_rect_big = settings_back_button_surf_big.get_rect(center = (settings_back_button_start_pos))

# Sounds Menu
# Back Button
sounds_back_button_start_x_pos = center_screen
sounds_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
sounds_back_button_start_pos = (sounds_back_button_start_x_pos,sounds_back_button_start_y_pos)
sounds_back_button_surf = test_font.render("Back to Settings",False,font_color)
sounds_back_button_scale = window_scalar
sounds_back_button_surf = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_scale)
sounds_back_button_rect = sounds_back_button_surf.get_rect(center = (sounds_back_button_start_pos))
mouse_on_sounds_back_button = False
sounds_back_button_big_scale = button_when_big_scale
sounds_back_button_surf_big = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_big_scale)
sounds_back_button_rect_big = sounds_back_button_surf_big.get_rect(center = (sounds_back_button_start_pos))

# Controls Buttons
controls_first_button_start_x_pos = center_screen
controls_first_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
controls_first_button_start_pos = (controls_first_button_start_x_pos,controls_first_button_start_y_pos)
controls_buttons_y_pos_offset = window_height * 1/18
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
    controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height) + controls_buttons_y_pos_offset * controls_button_index
    controls_button_start_pos = (controls_button_start_x_pos,controls_button_start_y_pos)
    control_name_underscore_removed = control_name.replace("_", " ")
    control_name_capitalized = control_name_underscore_removed.title()
    controls_button_surf = test_font.render(f"{control_name_capitalized}: {edited_controls_display_names_dict[control_name]}",False,font_color)
    controls_button_scale = window_scalar * controls_button_scalar
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
controls_reset_button_start_x_pos = center_screen
controls_reset_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height) + (controls_buttons_y_pos_offset * (len(default_controls_pygame_constants_names_dict)))
controls_reset_button_start_pos = (controls_reset_button_start_x_pos,controls_reset_button_start_y_pos)
controls_reset_button_surf = test_font.render("Reset Controls to Default",False,font_color)
controls_reset_button_scale = window_scalar * controls_button_scalar
controls_reset_button_surf = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_scale)
controls_reset_button_rect = controls_reset_button_surf.get_rect(center = (controls_reset_button_start_pos))
mouse_on_controls_reset_button = False
controls_reset_button_big_scale = button_when_big_scale
controls_reset_button_surf_big = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_big_scale)
controls_reset_button_rect_big = controls_reset_button_surf_big.get_rect(center = (controls_reset_button_start_pos))
# Back Button
controls_back_button_start_x_pos = center_screen
controls_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
controls_back_button_start_pos = (controls_back_button_start_x_pos,controls_back_button_start_y_pos)
controls_back_button_surf = test_font.render("Back to Settings",False,font_color)
controls_back_button_scale = window_scalar
controls_back_button_surf = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_scale)
controls_back_button_rect = controls_back_button_surf.get_rect(center = (controls_back_button_start_pos))
mouse_on_controls_back_button = False
controls_back_button_big_scale = button_when_big_scale
controls_back_button_surf_big = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_big_scale)
controls_back_button_rect_big = controls_back_button_surf_big.get_rect(center = (controls_back_button_start_pos))

# Display Menu
display_button_scalar = 0.5
display_buttons_y_pos_offset = window_height * 1/36
display_controls_update = False
display_in_game_stats_update = False
display_in_game_health_update = False
display_in_game_buffs_update = False
# Show Controls Button
controls_displayed = get_edited_options_file_dict()["edited_display_controls"]
display_show_controls_button_start_x_pos = center_screen
display_show_controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
display_show_controls_button_start_pos = (display_show_controls_button_start_x_pos,display_show_controls_button_start_y_pos)
display_show_controls_button_surf = test_font.render(f"Display Controls: {controls_displayed}",False,font_color)
display_show_controls_button_scale = window_scalar * display_button_scalar
display_show_controls_button_surf = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_scale)
display_show_controls_button_rect = display_show_controls_button_surf.get_rect(center = (display_show_controls_button_start_pos))
mouse_on_display_show_controls_button = False
display_show_controls_button_big_scale = button_when_big_scale
display_show_controls_button_surf_big = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_big_scale)
display_show_controls_button_rect_big = display_show_controls_button_surf_big.get_rect(center = (display_show_controls_button_start_pos))
# Show In Game Stats Button
in_game_stats_displayed = get_edited_options_file_dict()["edited_display_in_game_stats"]
display_show_in_game_stats_button_start_x_pos = center_screen
display_show_in_game_stats_button_start_y_pos = display_show_controls_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_stats_button_start_pos = (display_show_in_game_stats_button_start_x_pos,display_show_in_game_stats_button_start_y_pos)
display_show_in_game_stats_button_surf = test_font.render(f"Display Stats: {in_game_stats_displayed}",False,font_color)
display_show_in_game_stats_button_scale = window_scalar * display_button_scalar
display_show_in_game_stats_button_surf = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_scale)
display_show_in_game_stats_button_rect = display_show_in_game_stats_button_surf.get_rect(center = (display_show_in_game_stats_button_start_pos))
mouse_on_display_show_in_game_stats_button = False
display_show_in_game_stats_button_big_scale = button_when_big_scale
display_show_in_game_stats_button_surf_big = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_big_scale)
display_show_in_game_stats_button_rect_big = display_show_in_game_stats_button_surf_big.get_rect(center = (display_show_in_game_stats_button_start_pos))
# Show In Game Health Button
in_game_health_displayed = get_edited_options_file_dict()["edited_display_in_game_health"]
display_show_in_game_health_button_start_x_pos = center_screen
display_show_in_game_health_button_start_y_pos = display_show_in_game_stats_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_health_button_start_pos = (display_show_in_game_health_button_start_x_pos,display_show_in_game_health_button_start_y_pos)
display_show_in_game_health_button_surf = test_font.render(f"Display Health: {in_game_health_displayed}",False,font_color)
display_show_in_game_health_button_scale = window_scalar * display_button_scalar
display_show_in_game_health_button_surf = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_scale)
display_show_in_game_health_button_rect = display_show_in_game_health_button_surf.get_rect(center = (display_show_in_game_health_button_start_pos))
mouse_on_display_show_in_game_health_button = False
display_show_in_game_health_button_big_scale = button_when_big_scale
display_show_in_game_health_button_surf_big = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_big_scale)
display_show_in_game_health_button_rect_big = display_show_in_game_health_button_surf_big.get_rect(center = (display_show_in_game_health_button_start_pos))
# Show In Game Buffs Button
in_game_buffs_displayed = get_edited_options_file_dict()["edited_display_in_game_buffs"]
display_show_in_game_buffs_button_start_x_pos = center_screen
display_show_in_game_buffs_button_start_y_pos = display_show_in_game_health_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_buffs_button_start_pos = (display_show_in_game_buffs_button_start_x_pos,display_show_in_game_buffs_button_start_y_pos)
display_show_in_game_buffs_button_surf = test_font.render(f"Display Buffs: {in_game_buffs_displayed}",False,font_color)
display_show_in_game_buffs_button_scale = window_scalar * display_button_scalar
display_show_in_game_buffs_button_surf = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_scale)
display_show_in_game_buffs_button_rect = display_show_in_game_buffs_button_surf.get_rect(center = (display_show_in_game_buffs_button_start_pos))
mouse_on_display_show_in_game_buffs_button = False
display_show_in_game_buffs_button_big_scale = button_when_big_scale
display_show_in_game_buffs_button_surf_big = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_big_scale)
display_show_in_game_buffs_button_rect_big = display_show_in_game_buffs_button_surf_big.get_rect(center = (display_show_in_game_buffs_button_start_pos))
# Reset Button
display_reset_button_start_x_pos = center_screen
display_reset_button_start_y_pos = display_show_in_game_buffs_button_rect_big.bottom + display_buttons_y_pos_offset
display_reset_button_start_pos = (display_reset_button_start_x_pos,display_reset_button_start_y_pos)
display_reset_button_surf = test_font.render("Reset Display Options to Default",False,font_color)
display_reset_button_scale = window_scalar * display_button_scalar
display_reset_button_surf = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_scale)
display_reset_button_rect = display_reset_button_surf.get_rect(center = (display_reset_button_start_pos))
mouse_on_display_reset_button = False
display_reset_button_big_scale = button_when_big_scale
display_reset_button_surf_big = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_big_scale)
display_reset_button_rect_big = display_reset_button_surf_big.get_rect(center = (display_reset_button_start_pos))
# Back Button
display_back_button_start_x_pos = center_screen
display_back_button_start_y_pos = main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
display_back_button_start_pos = (display_back_button_start_x_pos,display_back_button_start_y_pos)
display_back_button_surf = test_font.render("Back to Settings",False,font_color)
display_back_button_scale = window_scalar
display_back_button_surf = pygame.transform.scale_by(display_back_button_surf,display_back_button_scale)
display_back_button_rect = display_back_button_surf.get_rect(center = (display_back_button_start_pos))
mouse_on_display_back_button = False
display_back_button_big_scale = button_when_big_scale
display_back_button_surf_big = pygame.transform.scale_by(display_back_button_surf,display_back_button_big_scale)
display_back_button_rect_big = display_back_button_surf_big.get_rect(center = (display_back_button_start_pos))
