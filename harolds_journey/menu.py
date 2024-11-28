"""Contains all menu-related items"""
import math

import pygame_menu
import pygame_menu.locals

from controls import *
from global_vars import *
from harold import *
from player import *

# Global Variables
center_screen_width = window_width / 2
center_screen_height = window_height / 2

# Main Menu Screen
MAIN_MENU = 1
STATISTICS_MENU = 2
SETTINGS_MENU = 3
SOUNDS_MENU = 4
CONTROLS_MENU = 5
DISPLAY_MENU = 6
menu_section = MAIN_MENU

controls_update = False
# Text Vars
font_color = "#FCDC4D"
font_name = pygame_menu.font.FONT_MUNRO
# Title Vars
title_font_size = int(window_height/16)
title_padding = int(window_height/64)
title_y_pos_center_offset = -center_screen_height+title_font_size
widget_y_offset = center_screen_height

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


def increase_fireballs_shot():
    global fireballs_shot
    fireballs_shot += 1

# Wizard on Menu Screen
wizard_path = "harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png"
main_menu_wizard_hat_size = 24 * (window_height/400)
main_menu_wizard_start_x_pos = center_screen_width
main_menu_wizard_start_y_pos = 54/400 * window_height + (1.5 * (96 * (window_height/400))) # 297
main_menu_wizard_surf = pygame.image.load(wizard_path).convert_alpha()
main_menu_wizard_height_by_scale = 96 * (window_height/400)
main_menu_wizard_width_by_scale = 96 * (window_width/800)
main_menu_wizard_size_by_scale = (main_menu_wizard_height_by_scale,main_menu_wizard_width_by_scale)
main_menu_wizard_surf = pygame.transform.scale(main_menu_wizard_surf,main_menu_wizard_size_by_scale)
main_menu_wizard_rect = main_menu_wizard_surf.get_rect(midbottom = (main_menu_wizard_start_x_pos,main_menu_wizard_start_y_pos))

# Harold on Menu Screen
harold_path = "harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png"
# main_menu_harold_start_x_pos = CENTER_SCREEN
# main_menu_harold_start_y_pos = main_menu_wizard_rect.top + main_menu_wizard_hat_size
main_menu_harold_surf = pygame.image.load(harold_path).convert_alpha()
main_menu_harold_height_by_scale = main_menu_wizard_height_by_scale * 3/8
main_menu_harold_width_by_scale = main_menu_wizard_width_by_scale * 3/8
main_menu_harold_size_by_scale = (main_menu_harold_height_by_scale,main_menu_harold_width_by_scale)
main_menu_harold_surf = pygame.transform.scale(main_menu_harold_surf,main_menu_harold_size_by_scale)
# main_menu_harold_rect = main_menu_harold_surf.get_rect(midbottom = (main_menu_harold_start_x_pos,main_menu_harold_start_y_pos))

main_menu_wizard_start_y_pos = widget_y_offset-title_font_size/2

button_when_big_scale = 1.1

# Pre-Menu Functions
def on_resize(menu:pygame_menu.Menu) -> None:
    """
    Function checked if the window is resized.
    """
    global window_width
    global window_height
    global window_size
    global grass_top_y

    current_window_size = screen.get_size()
    new_w, new_h = current_window_size[0], current_window_size[1]

    new_w = max(new_w,min_window_width)
    new_h = max(new_h,min_window_height)

    window_width = new_w
    window_height = new_h
    window_size = (window_width,window_height)
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

# Themes
# Base Menu Theme
base_menu_theme = pygame_menu.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=main_menu_bg,
    widget_offset=(0,widget_y_offset),
    widget_selection_effect = main_menu_selection,
    title_font=font_name,
    title_font_color=font_color,
    title_close_button=False,
    title=False,
    cursor_selection_color="#FFFFFF",
)

# Main Menu Theme
main_menu_theme = base_menu_theme.copy()
# Main Statistics Menu Theme
main_statistics_menu_theme = base_menu_theme.copy()
# Main Settings Menu Theme
main_settings_menu_theme = base_menu_theme.copy()

# Pause Menu Theme
pause_menu_theme = base_menu_theme.copy()


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
    theme=main_statistics_menu_theme,
    center_content=False,
)

# Settings Menu
main_settings_menu = pygame_menu.Menu(
    title="",
    width=window_width,
    height=window_height,
    surface=screen,
    theme=main_settings_menu_theme,
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
    global main_statistics_menu_theme
    global main_settings_menu_theme
    global main_menu
    global main_statistics_menu
    global main_settings_menu
    global fireballs_shot
    global jumps_made
    global distance_traveled
    global pre_stat_update_edited_stats_file_dict

    edited_stats_file_dict = get_edited_stats_file_dict()
    edited_stats_kills_file_dict = edited_stats_file_dict.get("kills")
    edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
    edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
    edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")

    skeletons_killed_total = edited_stats_kills_file_dict.get("skeletons_killed")
    skeleton_birds_killed_total = edited_stats_kills_file_dict.get("skeleton_birds_killed")
    time_played_total = edited_stats_interactivity_file_dict.get("time_played")
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    fireballs_shot_total = edited_stats_interactivity_file_dict.get("fireballs_shot")
    jumps_total = edited_stats_interactivity_file_dict.get("jumps")
    distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
    highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
    highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
    highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
    lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
    double_jump_buff_found = edited_stats_buffs_file_dict.get("double_jump_buff")
    knockback_buff_found = edited_stats_buffs_file_dict.get("knockback_buff")
    shield_buff_found = edited_stats_buffs_file_dict.get("shield_buff")


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
    # Main Menu Theme
    main_menu_theme = base_menu_theme.copy()
    # Main Statistics Menu Theme
    main_statistics_menu_theme = base_menu_theme.copy()
    main_statistics_menu_theme.widget_offset = (0,int(widget_y_offset/2))
    # Main Settings Menu Theme
    main_settings_menu_theme = base_menu_theme.copy()
    main_settings_menu_theme.widget_offset = (0,int(widget_y_offset/2))

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
        theme=main_statistics_menu_theme,
        center_content=False,
    )

    # Settings Menu
    main_settings_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_settings_menu_theme,
        center_content=False,
    )


    # Labels
    # Main Menu Label
    main_menu_label = main_menu.add.label(
        title="Harold\'s Journey",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size*2),
    ).translate(0,title_y_pos_center_offset-title_font_size)

    # Main Statistics Menu Label
    main_statistics_menu_label = main_statistics_menu.add.label(
        title="Statistics",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,-title_font_size)
    # Main Statistics Menu Sublabels
    # Left Side
    # Kills
    # Skeletons Killed
    main_statistics_menu_skeletons_killed_label = main_statistics_menu.add.label(
        title=f"Skeletons Killed: {skeletons_killed_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Birds Killed
    main_statistics_menu_birds_killed_label = main_statistics_menu.add.label(
        title=f"Skeleton Birds Killed: {skeleton_birds_killed_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Interactivity
    # Time Played
    units = {"weeks":3600 * 24 * 7,"days":3600 * 24,"hours": 3600, "minutes": 60, "seconds": 1}
    final_displayed_time = ""
    for unit, value in units.items():
        count = time_played_total // value
        time_played_total -= count * value
        if count > 0:
            final_displayed_time += f"{count}{unit[0]} "
    if not final_displayed_time:
        final_displayed_time = "0s"
    main_statistics_menu_time_played_label = main_statistics_menu.add.label(
        title=f"Time Played: {final_displayed_time.strip()}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # High Score
    main_statistics_menu_high_score_label = main_statistics_menu.add.label(
        title=f"High Score: {high_score}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Fireballs Shot
    main_statistics_menu_fireballs_shot_label = main_statistics_menu.add.label(
        title=f"Fireballs Shot: {fireballs_shot_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Jumps
    main_statistics_menu_jumps_label = main_statistics_menu.add.label(
        title=f"Jumps: {jumps_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Distance Traveled
    main_statistics_menu_distance_traveled_label = main_statistics_menu.add.label(
        title=f"Distance Traveled: {int(distance_traveled_total/WIZARD_WIDTH)}m",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(-center_screen_width/4,0)
    # Right Side
    right_side_y_offset = -int(title_font_size/2)*10
    # In-Game Stat Records
    # Highest Speed
    main_statistics_menu_highest_speed_label = main_statistics_menu.add.label(
        title=f"Highest Speed: {round((highest_speed/WIZARD_WIDTH)*60,2)}m/s",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Highest Damage
    main_statistics_menu_highest_damage_label = main_statistics_menu.add.label(
        title=f"Highest Damage: {highest_damage}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Highest Piercing
    main_statistics_menu_highest_piercing_label = main_statistics_menu.add.label(
        title=f"Highest Piercing: {highest_piercing - 1}",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Lowest Cooldown
    main_statistics_menu_lowest_cooldown_label = main_statistics_menu.add.label(
        title=f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Buffs
    # Double Jump Buff
    double_jump_buff_string = "???: Not Yet Found" if not double_jump_buff_found else "Double Jump Buff: Found"
    main_statistics_menu_double_jump_buff_label = main_statistics_menu.add.label(
        title=double_jump_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Knockback Buff
    knockback_buff_string = "???: Not Yet Found" if not knockback_buff_found else "Knockback Buff: Found"
    main_statistics_menu_knockback_buff_label = main_statistics_menu.add.label(
        title=knockback_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)
    # Shield Buff
    shield_buff_string = "???: Not Yet Found" if not shield_buff_found else "Magic Shield Buff: Found"
    main_statistics_menu_shield_buff_label = main_statistics_menu.add.label(
        title=shield_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size/2),
    ).translate(center_screen_width/4,right_side_y_offset)

    # Main Settings Menu Label
    main_settings_menu_label = main_settings_menu.add.label(
        title="Settings",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
    ).translate(0,-title_font_size)


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
        title="Exit Game",
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
    main_menu_wizard_y_offset = -int(widget_y_offset)+title_font_size/2
    main_menu_wizard_menu_surf = main_menu.add.surface(
        surface=main_menu_wizard_surf,
        float=True,
    ).translate(0,main_menu_wizard_y_offset)
    main_menu_harold_menu_surf = main_menu.add.surface(
        surface=main_menu_harold_surf,
        float=True,
    ).translate(0,main_menu_wizard_y_offset-(main_menu_wizard_hat_size/2))

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
    pause_menu_back_button = pause_menu.add.button(
        title="Back to Game",
        action=pause_menu.disable,
        font_color=font_color,
        font_name=font_name,
    )
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
    wizard_death_calls()
    pause_menu.disable()


def wizard_death_calls():
    global main_menu
    global objects_to_be_removed
    global wizard
    # Updating Stats
    wizard_jumps = wizard.sprite.get_jumps_made()
    distance_traveled = wizard.sprite.get_distance_traveled()
    current_wizard_speed = wizard.sprite.get_wizard_speed()
    current_wizard_damage = wizard.sprite.get_wizard_damage_total()
    current_wizard_piercing = wizard.sprite.get_wizard_piercing_total()
    current_wizard_fireball_cooldown = wizard.sprite.get_max_fireball_cooldown_time()
    current_wizard_double_jump_buff = wizard.sprite.get_double_jump()
    current_wizard_knockback_buff = wizard.sprite.get_knockback()
    current_wizard_shield_buff = wizard.sprite.get_shield()
    edited_stats_file_dict = get_edited_stats_file_dict()
    edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
    edited_stats_in_game_stat_records_file_dict = edited_stats_file_dict.get("in_game_stat_records")
    edited_stats_buffs_file_dict = edited_stats_file_dict.get("buffs")
    time_played_total = edited_stats_interactivity_file_dict.get("time_played")
    jumps_total = edited_stats_interactivity_file_dict.get("jumps")
    distance_traveled_total = edited_stats_interactivity_file_dict.get("distance_traveled")
    highest_speed = edited_stats_in_game_stat_records_file_dict.get("highest_speed")
    highest_damage = edited_stats_in_game_stat_records_file_dict.get("highest_damage")
    highest_piercing = edited_stats_in_game_stat_records_file_dict.get("highest_piercing")
    lowest_cooldown = edited_stats_in_game_stat_records_file_dict.get("lowest_cooldown")
    double_jump_buff_found = edited_stats_buffs_file_dict.get("double_jump_buff")
    knockback_buff_found = edited_stats_buffs_file_dict.get("knockback_buff")
    shield_buff_found = edited_stats_buffs_file_dict.get("shield_buff")
    updated_speed = highest_speed if highest_speed > current_wizard_speed else current_wizard_speed
    updated_damage = highest_damage if highest_damage > current_wizard_damage else current_wizard_damage
    updated_piercing = highest_piercing if highest_piercing > current_wizard_piercing else current_wizard_piercing
    updated_cooldown = lowest_cooldown if lowest_cooldown < current_wizard_fireball_cooldown else current_wizard_fireball_cooldown
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    new_time_played_total = time_played_total + current_time
    edited_stats_interactivity_file_dict.update({"time_played":new_time_played_total})
    edited_stats_interactivity_file_dict.update({"jumps":jumps_total + wizard_jumps })
    edited_stats_interactivity_file_dict.update({"distance_traveled":distance_traveled_total + distance_traveled })
    edited_stats_in_game_stat_records_file_dict.update({"highest_speed":updated_speed})
    edited_stats_in_game_stat_records_file_dict.update({"highest_damage":updated_damage})
    edited_stats_in_game_stat_records_file_dict.update({"highest_piercing":updated_piercing})
    edited_stats_in_game_stat_records_file_dict.update({"lowest_cooldown":updated_cooldown})
    if current_wizard_double_jump_buff and not double_jump_buff_found:
        edited_stats_buffs_file_dict.update({"double_jump_buff":current_wizard_double_jump_buff})
    if current_wizard_knockback_buff and not knockback_buff_found:
        edited_stats_buffs_file_dict.update({"knockback_buff":current_wizard_knockback_buff})
    if current_wizard_shield_buff and not shield_buff_found:
        edited_stats_buffs_file_dict.update({"shield_buff":current_wizard_shield_buff})
    set_edited_stats_file_dict(edited_stats_file_dict)
    main_menu = update_main_menu_and_submenus()
    # Other Death Stuff
    wizard.sprite.set_wizard_current_health(0)
    temp_wizard_max_fireball_cooldown_time = wizard.sprite.get_max_fireball_cooldown_time()
    wizard.sprite.set_current_fireball_cooldown(temp_wizard_max_fireball_cooldown_time)
    for objects in objects_to_be_removed:
        for object in objects:
            object.kill()
        objects.empty()
    outline_health_bar_ownership_group.clear()
    health_bar_ownership_group.clear()
    for outline_health_bar in outline_health_bar_group:
        outline_health_bar.kill()
    for health_bar in health_bar_group:
        health_bar.kill()
    outline_health_bar_group.empty()
    health_bar_group.empty()
    wizard.sprite.set_wizard_dead(True)


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
button_scale = 3/2

# Settings
# Sounds Button
settings_sounds_button_start_x_pos = center_screen_width
settings_sounds_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
settings_sounds_button_start_pos = (settings_sounds_button_start_x_pos,settings_sounds_button_start_y_pos)
settings_sounds_button_surf = test_font.render("Sounds",False,font_color)
settings_sounds_button_scale = button_scale
settings_sounds_button_surf = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_scale)
settings_sounds_button_rect = settings_sounds_button_surf.get_rect(center = (settings_sounds_button_start_pos))
mouse_on_settings_sounds_button = False
settings_sounds_button_big_scale = button_when_big_scale
settings_sounds_button_surf_big = pygame.transform.scale_by(settings_sounds_button_surf,settings_sounds_button_big_scale)
settings_sounds_button_rect_big = settings_sounds_button_surf_big.get_rect(center = (settings_sounds_button_start_pos))
# Controls Button
settings_controls_button_start_x_pos = center_screen_width
settings_controls_button_start_y_pos = settings_sounds_button_rect_big.bottom + ((32/400) * window_height)
settings_controls_button_start_pos = (settings_controls_button_start_x_pos,settings_controls_button_start_y_pos)
settings_controls_button_surf = test_font.render("Controls",False,font_color)
settings_controls_button_scale = button_scale
settings_controls_button_surf = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_scale)
settings_controls_button_rect = settings_controls_button_surf.get_rect(center = (settings_controls_button_start_pos))
mouse_on_settings_controls_button = False
settings_controls_button_big_scale = button_when_big_scale
settings_controls_button_surf_big = pygame.transform.scale_by(settings_controls_button_surf,settings_controls_button_big_scale)
settings_controls_button_rect_big = settings_controls_button_surf_big.get_rect(center = (settings_controls_button_start_pos))
# Display Button
settings_display_button_start_x_pos = center_screen_width
settings_display_button_start_y_pos = settings_controls_button_rect_big.bottom + ((32/400) * window_height)
settings_display_button_start_pos = (settings_display_button_start_x_pos,settings_display_button_start_y_pos)
settings_display_button_surf = test_font.render("Display",False,font_color)
settings_display_button_scale = button_scale
settings_display_button_surf = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_scale)
settings_display_button_rect = settings_display_button_surf.get_rect(center = (settings_display_button_start_pos))
mouse_on_settings_display_button = False
settings_display_button_big_scale = button_when_big_scale
settings_display_button_surf_big = pygame.transform.scale_by(settings_display_button_surf,settings_display_button_big_scale)
settings_display_button_rect_big = settings_display_button_surf_big.get_rect(center = (settings_display_button_start_pos))
# Back Button
settings_back_button_start_x_pos = center_screen_width
settings_back_button_start_y_pos = settings_display_button_rect_big.bottom + ((32/400) * window_height)
settings_back_button_start_pos = (settings_back_button_start_x_pos,settings_back_button_start_y_pos)
settings_back_button_surf = test_font.render("Main Menu",False,font_color)
settings_back_button_scale = button_scale
settings_back_button_surf = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_scale)
settings_back_button_rect = settings_back_button_surf.get_rect(center = (settings_back_button_start_pos))
mouse_on_settings_back_button = False
settings_back_button_big_scale = button_when_big_scale
settings_back_button_surf_big = pygame.transform.scale_by(settings_back_button_surf,settings_back_button_big_scale)
settings_back_button_rect_big = settings_back_button_surf_big.get_rect(center = (settings_back_button_start_pos))

# Sounds Menu
# Back Button
sounds_back_button_start_x_pos = center_screen_width
sounds_back_button_start_y_pos = 0  # main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
sounds_back_button_start_pos = (sounds_back_button_start_x_pos,sounds_back_button_start_y_pos)
sounds_back_button_surf = test_font.render("Back to Settings",False,font_color)
sounds_back_button_scale = button_scale
sounds_back_button_surf = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_scale)
sounds_back_button_rect = sounds_back_button_surf.get_rect(center = (sounds_back_button_start_pos))
mouse_on_sounds_back_button = False
sounds_back_button_big_scale = button_when_big_scale
sounds_back_button_surf_big = pygame.transform.scale_by(sounds_back_button_surf,sounds_back_button_big_scale)
sounds_back_button_rect_big = sounds_back_button_surf_big.get_rect(center = (sounds_back_button_start_pos))

# Controls Buttons
controls_first_button_start_x_pos = center_screen_width
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
    controls_button_scale = button_scale * controls_button_scalar
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
controls_reset_button_start_x_pos = center_screen_width
controls_reset_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height) + (controls_buttons_y_pos_offset * (len(default_controls_pygame_constants_names_dict)))
controls_reset_button_start_pos = (controls_reset_button_start_x_pos,controls_reset_button_start_y_pos)
controls_reset_button_surf = test_font.render("Reset Controls to Default",False,font_color)
controls_reset_button_scale = button_scale * controls_button_scalar
controls_reset_button_surf = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_scale)
controls_reset_button_rect = controls_reset_button_surf.get_rect(center = (controls_reset_button_start_pos))
mouse_on_controls_reset_button = False
controls_reset_button_big_scale = button_when_big_scale
controls_reset_button_surf_big = pygame.transform.scale_by(controls_reset_button_surf,controls_reset_button_big_scale)
controls_reset_button_rect_big = controls_reset_button_surf_big.get_rect(center = (controls_reset_button_start_pos))
# Back Button
controls_back_button_start_x_pos = center_screen_width
controls_back_button_start_y_pos = 0  # main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
controls_back_button_start_pos = (controls_back_button_start_x_pos,controls_back_button_start_y_pos)
controls_back_button_surf = test_font.render("Back to Settings",False,font_color)
controls_back_button_scale = button_scale
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
display_show_controls_button_start_x_pos = center_screen_width
display_show_controls_button_start_y_pos = main_menu_wizard_rect.bottom + ((32/400) * window_height)
display_show_controls_button_start_pos = (display_show_controls_button_start_x_pos,display_show_controls_button_start_y_pos)
display_show_controls_button_surf = test_font.render(f"Display Controls: {controls_displayed}",False,font_color)
display_show_controls_button_scale = button_scale * display_button_scalar
display_show_controls_button_surf = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_scale)
display_show_controls_button_rect = display_show_controls_button_surf.get_rect(center = (display_show_controls_button_start_pos))
mouse_on_display_show_controls_button = False
display_show_controls_button_big_scale = button_when_big_scale
display_show_controls_button_surf_big = pygame.transform.scale_by(display_show_controls_button_surf,display_show_controls_button_big_scale)
display_show_controls_button_rect_big = display_show_controls_button_surf_big.get_rect(center = (display_show_controls_button_start_pos))
# Show In Game Stats Button
in_game_stats_displayed = get_edited_options_file_dict()["edited_display_in_game_stats"]
display_show_in_game_stats_button_start_x_pos = center_screen_width
display_show_in_game_stats_button_start_y_pos = display_show_controls_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_stats_button_start_pos = (display_show_in_game_stats_button_start_x_pos,display_show_in_game_stats_button_start_y_pos)
display_show_in_game_stats_button_surf = test_font.render(f"Display Stats: {in_game_stats_displayed}",False,font_color)
display_show_in_game_stats_button_scale = button_scale * display_button_scalar
display_show_in_game_stats_button_surf = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_scale)
display_show_in_game_stats_button_rect = display_show_in_game_stats_button_surf.get_rect(center = (display_show_in_game_stats_button_start_pos))
mouse_on_display_show_in_game_stats_button = False
display_show_in_game_stats_button_big_scale = button_when_big_scale
display_show_in_game_stats_button_surf_big = pygame.transform.scale_by(display_show_in_game_stats_button_surf,display_show_in_game_stats_button_big_scale)
display_show_in_game_stats_button_rect_big = display_show_in_game_stats_button_surf_big.get_rect(center = (display_show_in_game_stats_button_start_pos))
# Show In Game Health Button
in_game_health_displayed = get_edited_options_file_dict()["edited_display_in_game_health"]
display_show_in_game_health_button_start_x_pos = center_screen_width
display_show_in_game_health_button_start_y_pos = display_show_in_game_stats_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_health_button_start_pos = (display_show_in_game_health_button_start_x_pos,display_show_in_game_health_button_start_y_pos)
display_show_in_game_health_button_surf = test_font.render(f"Display Health: {in_game_health_displayed}",False,font_color)
display_show_in_game_health_button_scale = button_scale * display_button_scalar
display_show_in_game_health_button_surf = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_scale)
display_show_in_game_health_button_rect = display_show_in_game_health_button_surf.get_rect(center = (display_show_in_game_health_button_start_pos))
mouse_on_display_show_in_game_health_button = False
display_show_in_game_health_button_big_scale = button_when_big_scale
display_show_in_game_health_button_surf_big = pygame.transform.scale_by(display_show_in_game_health_button_surf,display_show_in_game_health_button_big_scale)
display_show_in_game_health_button_rect_big = display_show_in_game_health_button_surf_big.get_rect(center = (display_show_in_game_health_button_start_pos))
# Show In Game Buffs Button
in_game_buffs_displayed = get_edited_options_file_dict()["edited_display_in_game_buffs"]
display_show_in_game_buffs_button_start_x_pos = center_screen_width
display_show_in_game_buffs_button_start_y_pos = display_show_in_game_health_button_rect_big.bottom + display_buttons_y_pos_offset
display_show_in_game_buffs_button_start_pos = (display_show_in_game_buffs_button_start_x_pos,display_show_in_game_buffs_button_start_y_pos)
display_show_in_game_buffs_button_surf = test_font.render(f"Display Buffs: {in_game_buffs_displayed}",False,font_color)
display_show_in_game_buffs_button_scale = button_scale * display_button_scalar
display_show_in_game_buffs_button_surf = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_scale)
display_show_in_game_buffs_button_rect = display_show_in_game_buffs_button_surf.get_rect(center = (display_show_in_game_buffs_button_start_pos))
mouse_on_display_show_in_game_buffs_button = False
display_show_in_game_buffs_button_big_scale = button_when_big_scale
display_show_in_game_buffs_button_surf_big = pygame.transform.scale_by(display_show_in_game_buffs_button_surf,display_show_in_game_buffs_button_big_scale)
display_show_in_game_buffs_button_rect_big = display_show_in_game_buffs_button_surf_big.get_rect(center = (display_show_in_game_buffs_button_start_pos))
# Reset Button
display_reset_button_start_x_pos = center_screen_width
display_reset_button_start_y_pos = display_show_in_game_buffs_button_rect_big.bottom + display_buttons_y_pos_offset
display_reset_button_start_pos = (display_reset_button_start_x_pos,display_reset_button_start_y_pos)
display_reset_button_surf = test_font.render("Reset Display Options to Default",False,font_color)
display_reset_button_scale = button_scale * display_button_scalar
display_reset_button_surf = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_scale)
display_reset_button_rect = display_reset_button_surf.get_rect(center = (display_reset_button_start_pos))
mouse_on_display_reset_button = False
display_reset_button_big_scale = button_when_big_scale
display_reset_button_surf_big = pygame.transform.scale_by(display_reset_button_surf,display_reset_button_big_scale)
display_reset_button_rect_big = display_reset_button_surf_big.get_rect(center = (display_reset_button_start_pos))
# Back Button
display_back_button_start_x_pos = center_screen_width
display_back_button_start_y_pos = 0  # main_menu_settings_button_rect_big.bottom + ((32/400) * window_height)
display_back_button_start_pos = (display_back_button_start_x_pos,display_back_button_start_y_pos)
display_back_button_surf = test_font.render("Back to Settings",False,font_color)
display_back_button_scale = button_scale
display_back_button_surf = pygame.transform.scale_by(display_back_button_surf,display_back_button_scale)
display_back_button_rect = display_back_button_surf.get_rect(center = (display_back_button_start_pos))
mouse_on_display_back_button = False
display_back_button_big_scale = button_when_big_scale
display_back_button_surf_big = pygame.transform.scale_by(display_back_button_surf,display_back_button_big_scale)
display_back_button_rect_big = display_back_button_surf_big.get_rect(center = (display_back_button_start_pos))
