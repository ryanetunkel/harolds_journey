"""Contains all menu-related items"""
import pygame_menu
import pygame_menu.locals
import pygame_menu.widgets
import pygame_menu.widgets.widget

from controls import *
from harold import *
from player import *
from menu_vars import *


# Text Vars
font_color = "#FCDC4D"
font_name = pygame_menu.font.FONT_MUNRO
title_font_size = int(window_height/16)
default_font_size = int(title_font_size*3/4)
stat_font_size = int(title_font_size/2)
title_padding = int(window_height/64)
title_y_pos_center_offset = -center_screen_height+title_font_size
submenu_widget_y_offset = int(center_screen_height/2)
no_padding = 0
default_padding = 2
default_margin_padding = int(window_height/16)

# Stats Vars
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

# Settings Menu Vars
# Controls Vars
controls_update = False

# Gameplay Vars
display_controls_bool = False
display_in_game_stats_bool = False
display_in_game_health_bool = False
display_in_game_buffs_bool = False


# Statistics Vars Functions
def increase_fireballs_shot():
    global fireballs_shot
    fireballs_shot += 1


def set_score(new_score:int):
    global score
    score = new_score


# Display Vars Functions
# Resolution Vars Functions
def update_pixel_size(new_pixel_size:int):
    global pixel_size
    global global_scalar
    global wizard_width
    global wizard_height
    global wizard_pixel_size
    global grass_top_y

    pixel_size = new_pixel_size
    global_scalar = pixel_size/4
    wizard_width = 32 * pixel_size
    wizard_height = 32 * pixel_size
    wizard_pixel_size = (wizard_height,wizard_width)
    grass_top_y = int((628/640) * window_height)
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"pixel_size":new_pixel_size})
    set_edited_options_file_dict(edited_options_file_dict)


def update_zoom(new_zoom:int):
    global zoom
    zoom = new_zoom
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"zoom":new_zoom})
    set_edited_options_file_dict(edited_options_file_dict)


def update_fps(new_fps:int):
    global fps
    fps = new_fps
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"fps":new_fps})
    set_edited_options_file_dict(edited_options_file_dict)


def check_max_window(window_size:tuple[int,int])->tuple[int,int]:
    global min_window_width, max_window_width
    global min_window_height, max_window_height
    return (max(min_window_width,min(window_size[0],max_window_width)), max(min_window_height,min(window_size[1],max_window_height)))


def update_window_width(new_window_width:int):
    global window_width
    window_width = new_window_width
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"window_width":new_window_width})
    set_edited_options_file_dict(edited_options_file_dict)


def update_window_height(new_window_height:int):
    global window_height
    window_height = new_window_height
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"window_height":new_window_height})
    set_edited_options_file_dict(edited_options_file_dict)


def update_window_size(value: tuple, window_size: bool,**kwargs):
    new_window_size = check_max_window(window_size)
    update_window_width(new_window_size[0])
    update_window_height(new_window_size[1])


# Gameplay Vars Functions
def update_display_controls_bool(value: tuple, enabled: bool,**kwargs):
    edited_options_file_dict = get_edited_options_file_dict()
    edited_display_controls = edited_options_file_dict.get("display_controls")
    edited_options_file_dict.update({"display_controls":(not edited_display_controls)})
    set_edited_options_file_dict(edited_options_file_dict)


def update_display_in_game_stats_bool(value: tuple, enabled: bool,**kwargs):
    edited_options_file_dict = get_edited_options_file_dict()
    edited_display_in_game_stats = edited_options_file_dict.get("display_in_game_stats")
    edited_options_file_dict.update({"display_in_game_stats":(not edited_display_in_game_stats)})
    set_edited_options_file_dict(edited_options_file_dict)


def update_display_in_game_health_bool(value: tuple, enabled: bool,**kwargs):
    edited_options_file_dict = get_edited_options_file_dict()
    edited_display_in_game_health = edited_options_file_dict.get("display_in_game_health")
    edited_options_file_dict.update({"display_in_game_health":(not edited_display_in_game_health)})
    set_edited_options_file_dict(edited_options_file_dict)


def update_display_in_game_buffs_bool(value: tuple, enabled: bool,**kwargs):
    edited_options_file_dict = get_edited_options_file_dict()
    edited_display_in_game_buffs = edited_options_file_dict.get("display_in_game_buffs")
    edited_options_file_dict.update({"display_in_game_buffs":(not edited_display_in_game_buffs)})
    set_edited_options_file_dict(edited_options_file_dict)


def update_display_in_game_fps_bool(value: tuple, enabled: bool,**kwargs):
    edited_options_file_dict = get_edited_options_file_dict()
    edited_display_in_game_fps = edited_options_file_dict.get("display_in_game_fps")
    edited_options_file_dict.update({"display_in_game_fps":(not edited_display_in_game_fps)})
    set_edited_options_file_dict(edited_options_file_dict)


# Wizard on Menu Screen
wizard_path = "harolds_journey/graphics/wizard/wizard_idle_animation/wizard_idle_00.png"
main_menu_wizard_surf = pygame.image.load(wizard_path).convert_alpha()
main_menu_wizard_height_by_scale = window_height * (1/8)
main_menu_wizard_width_by_scale = window_height * (1/8)
main_menu_wizard_hat_size = main_menu_wizard_height_by_scale * (6/32) # Needs to stay in menu
main_menu_wizard_size_by_scale = (main_menu_wizard_height_by_scale,main_menu_wizard_width_by_scale)
main_menu_wizard_surf = pygame.transform.scale(main_menu_wizard_surf,main_menu_wizard_size_by_scale)

# Harold on Menu Screen
harold_path = "harolds_journey/graphics/harold/harold_idle_animation/harold_idle_00.png"
main_menu_harold_surf = pygame.image.load(harold_path).convert_alpha()
main_menu_harold_height_by_scale = main_menu_wizard_height_by_scale * 3/8
main_menu_harold_width_by_scale = main_menu_wizard_width_by_scale * 3/8
main_menu_harold_size_by_scale = (main_menu_harold_height_by_scale,main_menu_harold_width_by_scale)
main_menu_harold_surf = pygame.transform.scale(main_menu_harold_surf,main_menu_harold_size_by_scale)

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
    new_w = min(new_w,max_window_width)
    new_h = max(new_h,min_window_height)
    new_h = min(new_h,max_window_height)

    window_width = new_w
    window_height = new_h
    edited_options_file_dict = get_edited_options_file_dict()
    edited_options_file_dict.update({"window_width":new_w})
    edited_options_file_dict.update({"window_height":new_h})
    set_edited_options_file_dict(edited_options_file_dict)

    window_size = (window_width,window_height)
    grass_top_y = int((379 / 400) * window_height)
    menu.resize(new_w, new_h)


# Base Menu Selection
base_menu_selection = pygame_menu.widgets.SimpleSelection()

# Main Menu Background Base Image
main_menu_bg = pygame_menu.BaseImage(
    image_path=bg_image_path,
    image_id="main_menu_bg"
)
main_menu_bg = main_menu_bg.resize(main_menu_bg.get_width()*bg_scalar,main_menu_bg.get_height()*bg_scalar,smooth=False)
main_menu_bg = main_menu_bg.crop_rect((0,bg_surf.get_height()-window_height,window_width,window_height))
# Adjust cropping based on resizing of window - need to snap to the bottomcenter

# Helpful Button Functions
    # onselect is callback when selected
    # action is when "clicked" - unsure exact but that is what happens usually

# Base Menu Theme
base_menu_theme = pygame_menu.Theme(
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    background_color=main_menu_bg,
    widget_offset=(0,0),
    widget_selection_effect=base_menu_selection,
    title_font=font_name,
    title_font_color=font_color,
    title_close_button=False,
    title=False,
    cursor_selection_color="#FFFFFF",
)

# Menus
# Main Menu
def update_main_menu() -> pygame_menu.Menu:
    global base_menu_theme
    global main_menu_theme
    global main_statistics_menu_theme
    global main_settings_menu_theme
    global main_menu
    global main_statistics_menu
    global main_settings_menu
    global score

    # Main Menu Theme
    main_menu_theme = base_menu_theme.copy()
    main_menu_theme.widget_offset = (0,0) # Already (0,0) but listed for ease of access
    # Main Statistics Menu Theme
    main_statistics_menu_theme = base_menu_theme.copy()
    main_statistics_menu_theme.widget_offset = (0,submenu_widget_y_offset)
    # Main Settings Menu Theme
    main_settings_menu_theme = base_menu_theme.copy()
    main_settings_menu_theme.widget_offset = (0,submenu_widget_y_offset)

    # Menus
    # Main Menu
    main_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_menu_theme,
        center_content=False,
        menu_id="main_menu",
    )

    # Statistics Menu
    main_statistics_menu = pygame_menu.Menu(
        title="Statistics",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_statistics_menu_theme,
        center_content=False,
        columns=3,
        rows=9,
        menu_id="main_statistics_menu",
    )
    main_statistics_menu = update_statistics_menu(main_statistics_menu)

    # Settings Menu
    main_settings_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=main_settings_menu_theme,
        center_content=False,
        menu_id="main_settings_menu",
    )
    main_settings_menu = update_settings_menu(main_settings_menu)

    # Labels
    main_menu_title = (
        "Harold\'s Journey" if score == 0 else f"Score: {score}"
    )
    # Main Menu Label
    main_menu_label = main_menu.add.label(
        title=main_menu_title,
        font_color=font_color,
        font_name=font_name,
        font_size=int(title_font_size*2),
        label_id="main_menu_label",
    )
    edited_stats_file_dict = get_edited_stats_file_dict()
    edited_stats_interactivity_file_dict = edited_stats_file_dict.get("interactivity")
    high_score = edited_stats_interactivity_file_dict.get("high_score")
    # Main Menu High Score Label
    main_menu_high_score_label = main_menu.add.label(
        title=f"High Score: {high_score}",
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        padding=no_padding,
        label_id="main_menu_high_score_label",
    )

    # Extra Draws
    # Extra Main Menu Draws
    half_wizard_width = main_menu_wizard_surf.get_rect().width/2
    main_menu_wizard_y_offset = main_menu_harold_surf.get_rect().height/2
    main_menu_wizard_menu_surf = main_menu.add.surface(
        surface=main_menu_wizard_surf,
        padding=no_padding,
        surface_id="main_menu_wizard_menu_surf",
    ).translate(0,main_menu_wizard_y_offset)
    main_menu_harold_y_offset = -main_menu_wizard_surf.get_rect().height
    main_menu_harold_menu_surf = main_menu.add.surface(
        surface=main_menu_harold_surf,
        padding=no_padding,
        surface_id="main_menu_harold_menu_surf",
    ).translate(0,main_menu_harold_y_offset)

    # Buttons
    # Main Menu Buttons
    main_menu_start_button = main_menu.add.button(
        title="Start Game",
        action=main_menu.disable,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="main_menu_start_button",
    )
    main_menu_statistics_button = main_menu.add.button(
        title="Statistics",
        action=main_statistics_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="main_menu_statistics_button",
    )
    main_menu_settings_button = main_menu.add.button(
        title="Settings",
        action=main_settings_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="main_menu_settings_button",
    )
    main_menu_exit_button = main_menu.add.button(
        title="Exit Game",
        action=pygame_menu.events.EXIT,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="main_menu_exit_button",
    )

    return main_menu


# Pause Menu
def update_pause_menu(new_background_color=(50,50,50,50)) -> pygame_menu.Menu:
    global base_menu_theme
    global pause_menu_theme
    global pause_menu
    global pause_statistics_menu
    global pause_settings_menu

    # Pause Menu Theme
    pause_menu_theme = base_menu_theme.copy()
    pause_menu_theme.widget_offset = (0,submenu_widget_y_offset*2)
    if new_background_color:
        pause_menu_theme.background_color = new_background_color
    # Main Statistics Menu Theme
    pause_statistics_menu_theme = pause_menu_theme.copy()
    pause_statistics_menu_theme.widget_offset = (0,submenu_widget_y_offset)
    # Main Settings Menu Theme
    pause_settings_menu_theme = pause_menu_theme.copy()
    pause_settings_menu_theme.widget_offset = (0,submenu_widget_y_offset)

    # Menus
    # Pause Menu
    pause_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_menu_theme,
        center_content=False,
        menu_id="pause_menu",
    )

    # Pause Statistics Menu
    pause_statistics_menu = pygame_menu.Menu(
        title="Statistics",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_statistics_menu_theme,
        center_content=False,
        columns=3,
        rows=9,
        menu_id="pause_statistics_menu",
    )
    pause_statistics_menu = update_statistics_menu(pause_statistics_menu)

    # Pause Settings Menu
    pause_settings_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=pause_settings_menu_theme,
        center_content=False,
        menu_id="pause_settings_menu",
    )
    pause_settings_menu = update_settings_menu(pause_settings_menu)

    # Labels
    # Pause Menu Label
    pause_menu_label = pause_menu.add.label(
        title="GAME PAUSED",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="pause_menu_label",
    ).translate(0,title_y_pos_center_offset)

    # Pause Menu Buttons
    pause_menu_back_button = pause_menu.add.button(
        title="Back to Game",
        action=pause_menu.disable,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="pause_menu_back_button",
    ).translate(0,title_y_pos_center_offset/2)
    pause_menu_statistics_button = pause_menu.add.button(
        title="Statistics",
        action=pause_statistics_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="pause_menu_statistics_button",
    ).translate(0,title_y_pos_center_offset/2)
    pause_menu_settings_button = pause_menu.add.button(
        title="Settings",
        action=pause_settings_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="pause_menu_settings_button",
    ).translate(0,title_y_pos_center_offset/2)
    pause_menu_padding = pause_menu.add.vertical_margin(default_margin_padding)
    pause_menu_end_game_button = pause_menu.add.button(
        title="End Current Game",
        action=end_game,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="pause_menu_end_game_button",
    ).translate(0,title_y_pos_center_offset/2)

    return pause_menu


# Sub Menus
# Statistics Menu
def update_statistics_menu(menu:pygame_menu.Menu):
    global fireballs_shot
    global jumps_made
    global distance_traveled

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

    if score > high_score:
        edited_stats_interactivity_file_dict.update({"high_score":score})
        set_edited_stats_file_dict(edited_stats_file_dict)
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

    # Statistics Menu Sublabels
    statistics_menu_left_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Left Side
    left_side_x_offset = int(center_screen_width*5/12)
    # Kills
    # Skeletons Killed
    statistics_menu_skeletons_killed_label = menu.add.label(
        title=f"Skeletons Killed: {skeletons_killed_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_skeletons_killed_label",
    ).translate(left_side_x_offset,0)
    # Birds Killed
    statistics_menu_birds_killed_label = menu.add.label(
        title=f"Skeleton Birds Killed: {skeleton_birds_killed_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_birds_killed_label",
    ).translate(left_side_x_offset,0)
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
    statistics_menu_time_played_label = menu.add.label(
        title=f"Time Played: {final_displayed_time.strip()}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_time_played_label",
    ).translate(left_side_x_offset,0)
    # High Score
    statistics_menu_high_score_label = menu.add.label(
        title=f"High Score: {high_score}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_high_score_label",
    ).translate(left_side_x_offset,0)
    # Fireballs Shot
    statistics_menu_fireballs_shot_label = menu.add.label(
        title=f"Fireballs Shot: {fireballs_shot_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_fireballs_shot_label",
    ).translate(left_side_x_offset,0)
    # Jumps
    statistics_menu_jumps_label = menu.add.label(
        title=f"Jumps: {jumps_total}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_jumps_label",
    ).translate(left_side_x_offset,0)
    # Distance Traveled
    statistics_menu_distance_traveled_label = menu.add.label(
        title=f"Distance Traveled: {int(distance_traveled_total/wizard_width)}m",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_distance_traveled_label",
    ).translate(left_side_x_offset,0)
    statistics_menu_left_padding_2 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_left_padding_3 = menu.add.vertical_margin(default_margin_padding)

    # Statistics Menu Label
    statistics_menu_label = menu.add.label(
        title="Statistics",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="statistics_menu_label",
    )#.translate(center_screen_width/2,-title_font_size)
    statistics_menu_center_padding_1 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_2 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_3 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_4 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_5 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_6 = menu.add.vertical_margin(default_margin_padding)
    statistics_menu_center_padding_7 = menu.add.vertical_margin(default_margin_padding)
    # Statistics Menu Buttons
    statistics_menu_back_button = menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="statistics_menu_back_button",
    ).translate(0,-int(title_font_size*3/2))


    # Right Side
    statistics_menu_center_right_padding_1 = menu.add.vertical_margin(default_margin_padding)
    right_side_x_offset = -int(center_screen_width*5/12)
    # In-Game Stat Records
    # Highest Speed
    statistics_menu_highest_speed_label = menu.add.label(
        title=f"Highest Speed: {round((highest_speed/wizard_width)*60,2)}m/s",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_highest_speed_label",
    ).translate(right_side_x_offset,0)
    # Highest Damage
    main_statistics_menu_highest_damage_label = menu.add.label(
        title=f"Highest Damage: {highest_damage}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="main_statistics_menu_highest_damage_label",
    ).translate(right_side_x_offset,0)
    # Highest Piercing
    statistics_menu_highest_piercing_label = menu.add.label(
        title=f"Highest Piercing: {highest_piercing - 1}",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_highest_piercing_label",
    ).translate(right_side_x_offset,0)
    # Lowest Cooldown
    statistics_menu_lowest_cooldown_label = menu.add.label(
        title=f"Lowest Cooldown: {round(lowest_cooldown/60, 2)}s",
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_lowest_cooldown_label",
    ).translate(right_side_x_offset,0)
    # Buffs
    # Double Jump Buff
    double_jump_buff_string = "???: Not Yet Found" if not double_jump_buff_found else "Double Jump Buff: Found"
    statistics_menu_double_jump_buff_label = menu.add.label(
        title=double_jump_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_double_jump_buff_label",
    ).translate(right_side_x_offset,0)
    # Knockback Buff
    knockback_buff_string = "???: Not Yet Found" if not knockback_buff_found else "Knockback Buff: Found"
    statistics_menu_knockback_buff_label = menu.add.label(
        title=knockback_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_knockback_buff_label",
    ).translate(right_side_x_offset,0)
    # Shield Buff
    shield_buff_string = "???: Not Yet Found" if not shield_buff_found else "Magic Shield Buff: Found"
    statistics_menu_shield_buff_label = menu.add.label(
        title=shield_buff_string,
        font_color=font_color,
        font_name=font_name,
        font_size=stat_font_size,
        padding=default_padding,
        label_id="statistics_menu_shield_buff_label",
    ).translate(right_side_x_offset,0)
    statistics_menu_center_right_padding_2 = menu.add.vertical_margin(default_margin_padding)

    return menu


# Settings Menu
def update_settings_menu(menu:pygame_menu.Menu):
    # Themes
    # Sounds Menu Theme
    sounds_menu_theme = menu.get_theme().copy()
    # Controls Menu Theme
    controls_menu_theme = menu.get_theme().copy()
    # Display Menu Theme
    display_menu_theme = menu.get_theme().copy()

    # Menus
    # Sounds Menu
    sounds_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=sounds_menu_theme,
        center_content=False,
        menu_id="sounds_menu",
    )
    sounds_menu = update_sounds_menu(sounds_menu)

    # Controls Menu
    controls_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=controls_menu_theme,
        center_content=False,
        menu_id="controls_menu",
    )
    controls_menu = update_controls_menu(controls_menu)

    # Display Menu
    display_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=display_menu_theme,
        center_content=False,
        menu_id="display_menu",
    )
    display_menu = update_display_menu(display_menu)

    # Settings Menu Label
    settings_menu_label = menu.add.label(
        title="Settings",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="settings_menu_label",
    ).translate(0,-title_font_size)

    settings_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Settings Menu Buttons
    settings_menu_sounds_button = menu.add.button(
        title="Sounds",
        action=sounds_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="settings_menu_sounds_button",
    )
    settings_menu_controls_button = menu.add.button(
        title="Controls",
        action=controls_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="settings_menu_controls_button",
    )
    settings_menu_display_button = menu.add.button(
        title="Display",
        action=display_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="settings_menu_display_button",
    )
    settings_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    settings_menu_back_button = menu.add.button(
        title="Back to Main Menu",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="settings_menu_back_button",
    )

    return menu


# Settings Menus
# Sounds Menu
def update_sounds_menu(menu:pygame_menu.Menu):
    # Sounds Menu Label
    sounds_menu_label = menu.add.label(
        title="Sounds",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="sounds_menu_label",
    ).translate(0,-title_font_size)

    sounds_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Sounds Menu Buttons
    sounds_menu_placeholder_button = menu.add.button(
        title="Placeholder",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="sounds_menu_placeholder_button",
    )
    sounds_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    sounds_menu_back_button = menu.add.button(
        title="Back to Settings",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="sounds_menu_back_button",
    )

    return menu


# Controls Menu
def update_controls_menu(menu:pygame_menu.Menu):
    # Controls Menu Label
    controls_menu_label = menu.add.label(
        title="Controls",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="controls_menu_label",
    ).translate(0,-title_font_size)

    controls_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Controls Menu Buttons
    controls_menu_placeholder_button = menu.add.button(
        title="Placeholder",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="controls_menu_placeholder_button",
    )
    controls_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    controls_menu_back_button = menu.add.button(
        title="Back to Settings",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="controls_menu_back_buttons",
    )

    return menu


# Display Menu
def update_display_menu(menu:pygame_menu.Menu):
    # Themes
    # Resolution Menu Theme
    resolution_menu_theme = menu.get_theme().copy()
    # Gameplay Menu Theme
    gameplay_menu_theme = menu.get_theme().copy()

    # Menus
    # Resolution Menu
    resolution_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=resolution_menu_theme,
        center_content=False,
        menu_id="resolution_menu",
    )
    resolution_menu = update_resolution_menu(resolution_menu)
    # Gameplay Menu
    gameplay_menu = pygame_menu.Menu(
        title="",
        width=window_width,
        height=window_height,
        surface=screen,
        theme=gameplay_menu_theme,
        center_content=False,
        menu_id="gameplay_menu",
    )
    gameplay_menu = update_gameplay_menu(gameplay_menu)

    # Display Menu Label
    display_menu_label = menu.add.label(
        title="Display",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="display_menu_label",
    ).translate(0,-title_font_size)

    display_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Display Menu Sliders
    # Zoom Slider
    zoom_range_values = list(num for num in range(0,201))
    edited_zoom = get_edited_options_file_dict().get("zoom")
    display_menu_zoom_slider = menu.add.range_slider(
        title="Zoom:",
        default=edited_zoom,
        range_values=zoom_range_values,
        increment=1,
        width=int(center_screen_width/4),
        value_format=lambda x: str(zoom_range_values[x]),
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        range_box_color=font_color,
        range_line_color=font_color,
        range_line_height=2,
        range_text_value_color=font_color,
        range_text_value_enabled=False,
        range_text_value_tick_color=font_color,
        range_text_value_tick_enabled=False,
        slider_color=font_color,
        slider_sel_highlight_color=pygame.Color("#FFFFFF"),
        slider_selected_color=pygame.Color("#FFFFFF"),
        slider_thickness=4,
        slider_text_value_color=font_color,
        slider_text_value_enabled=True,
        padding=default_padding,
        rangeslider_id="display_menu_zoom_slider",
    )
    update_zoom(display_menu_zoom_slider.get_value())
    display_menu_zoom_slider.set_onchange(update_zoom)

    # Framerate Slider
    fps_range_values = list(num for num in range(1,121))
    edited_fps = get_edited_options_file_dict().get("fps")
    display_menu_framerate_slider = menu.add.range_slider(
        title="Framerate Cap:",
        default=edited_fps,
        range_values=fps_range_values,
        increment=1,
        width=int(center_screen_width/4),
        value_format=lambda x: str(fps_range_values[x-1]),
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        repeat_keys=True,
        repeat_keys_interval_ms=5,
        range_box_color=font_color,
        range_line_color=font_color,
        range_line_height=2,
        range_text_value_color=font_color,
        range_text_value_enabled=False,
        range_text_value_tick_enabled=False,
        slider_color=font_color,
        slider_sel_highlight_color=pygame.Color("#FFFFFF"),
        slider_selected_color=pygame.Color("#FFFFFF"),
        slider_thickness=4,
        slider_text_value_color=font_color,
        slider_text_value_enabled=True,
        padding=default_padding,
        rangeslider_id="display_menu_framerate_slider",
    )
    update_fps(display_menu_framerate_slider.get_value())
    display_menu_framerate_slider.set_onchange(update_fps)

    # Display Menu Buttons
    display_menu_resolution_button = menu.add.button(
        title="Resolution",
        action=resolution_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="display_menu_resolution_button",
    )
    display_menu_gameplay_button = menu.add.button(
        title="Gameplay",
        action=gameplay_menu,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="display_menu_gameplay_button",
    )
    display_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    display_menu_back_button = menu.add.button(
        title="Back to Settings",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="display_menu_back_button",
    )

    return menu


# Display Menus
# Resolution Menu
def update_resolution_menu(menu:pygame_menu.Menu):
    # Resolution Menu Label
    resolution_menu_label = menu.add.label(
        title="Resolution",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        label_id="resolution_menu_label",
    ).translate(0,-title_font_size)

    resolution_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Resolution Menu Buttons
    edited_window_sizes = get_edited_options_file_dict().get("window_sizes")
    default_window_width_value = get_edited_options_file_dict().get("window_width")
    default_window_height_value = get_edited_options_file_dict().get("window_height")
    default_window_sizes_list = []
    window_sizes_int_list = []
    default_window_size_idx = -1
    for size in edited_window_sizes:
        if size != "Custom":
            values = size.split("x")
            values_tuple = (int(values[0]),int(values[1]))
            default_window_sizes_list.append((size,values_tuple))
            window_sizes_int_list.append(values_tuple)
        else:
            values_tuple = (default_window_width_value,default_window_height_value)
            default_window_sizes_list.append((
                f"{size}: {values_tuple[0]}x{values_tuple[1]}",
                values_tuple
            ))
            window_sizes_int_list.append(values_tuple)
        default_window_size_idx = window_sizes_int_list.index(values_tuple)
    resolution_menu_window_size_dropselect = menu.add.dropselect(
        title="Window Size",
        items=default_window_sizes_list,
        default=default_window_size_idx,
        onchange=update_window_size,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        placeholder_add_to_selection_box=False,
        scrollbar_color="#22222277",
        scrollbar_slider_color="#66666677",
        scrollbar_slider_hover_color="#BBBBBB66",
        scrollbar_thick=6,
        selection_box_arrow_color="#55555599", # For some reason this affects selection_box_bgcolor - bug in pygame-menu
        selection_effect=base_menu_selection,
        selection_option_padding=4,
        selection_box_height=8,
        selection_box_bgcolor="#22222277",
        selection_box_width=stat_font_size*10,
        selection_option_border_color="#000000",
        selection_option_font_color=font_color,
        selection_option_font_size=stat_font_size,
        selection_option_selected_font_color="#FFFFFF",
        selection_option_selected_bgcolor="#99999966",
        padding=default_padding,
        button_id="resolution_menu_window_size_dropselect",
    )
    resolution_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    resolution_menu_reload_label = menu.add.label(
        title="[Reload required to apply changes]",
        font_color=font_color,
        font_name=font_name,
        font_size=int(default_font_size*3/4),
        padding=default_padding,
        label_id="resolution_menu_reload_label",
    ).translate(0,-title_font_size)
    resolution_menu_padding_3 = menu.add.vertical_margin(default_margin_padding)
    resolution_menu_back_button = menu.add.button(
        title="Back to Settings",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="resolution_menu_back_button",
    )

    return menu


# Gameplay Menu
def update_gameplay_menu(menu:pygame_menu.Menu):
    edited_options_file_dict = get_edited_options_file_dict()
    display_controls = edited_options_file_dict.get("display_controls")
    display_in_game_buffs = edited_options_file_dict.get("display_in_game_buffs")
    display_in_game_fps = edited_options_file_dict.get("display_in_game_fps")
    display_in_game_health = edited_options_file_dict.get("display_in_game_health")
    display_in_game_stats = edited_options_file_dict.get("display_in_game_stats")
    # Gameplay Menu Label
    gameplay_menu_label = menu.add.label(
        title="Gameplay",
        float=True,
        font_color=font_color,
        font_name=font_name,
        font_size=title_font_size,
        padding=default_padding,
        label_id="gameplay_menu_label",
    ).translate(0,-title_font_size)

    gameplay_menu_padding_1 = menu.add.vertical_margin(default_margin_padding)
    # Gameplay Menu Buttons
    gameplay_menu_items = [("True",True),("False",False)]
    default_display_in_game_health = gameplay_menu_items.index((f"{display_in_game_health}",display_in_game_health))
    gameplay_menu_display_health_button = menu.add.selector(
        title="Display Health: ",
        items=gameplay_menu_items,
        default=default_display_in_game_health,
        onchange=update_display_in_game_health_bool,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_display_health_button",
    )
    default_display_in_game_buffs = gameplay_menu_items.index((f"{display_in_game_buffs}",display_in_game_buffs))
    gameplay_menu_display_buffs_button = menu.add.selector(
        title="Display Buffs: ",
        items=gameplay_menu_items,
        default=default_display_in_game_buffs,
        onchange=update_display_in_game_buffs_bool,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_display_buffs_button",
    )
    default_display_in_game_stats = gameplay_menu_items.index((f"{display_in_game_stats}",display_in_game_stats))
    gameplay_menu_display_stats_button = menu.add.selector(
        title="Display Stats: ",
        items=gameplay_menu_items,
        default=default_display_in_game_stats,
        onchange=update_display_in_game_stats_bool,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_display_stats_button",
    )
    default_display_controls = gameplay_menu_items.index((f"{display_controls}",display_controls))
    gameplay_menu_display_controls_button = menu.add.selector(
        title="Display Controls: ",
        items=gameplay_menu_items,
        default=default_display_controls,
        onchange=update_display_controls_bool,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_display_controls_button",
    )
    default_display_in_game_fps = gameplay_menu_items.index((f"{display_in_game_fps}",display_in_game_fps))
    gameplay_menu_display_fps_button = menu.add.selector(
        title="Display FPS: ",
        items=gameplay_menu_items,
        default=default_display_in_game_fps,
        onchange=update_display_in_game_fps_bool,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_display_fps_button",
    )
    gameplay_menu_padding_2 = menu.add.vertical_margin(default_margin_padding)
    gameplay_menu_back_button = menu.add.button(
        title="Back to Settings",
        action=pygame_menu.events.BACK,
        font_color=font_color,
        font_name=font_name,
        font_size=default_font_size,
        padding=default_padding,
        button_id="gameplay_menu_back_button",
    )

    return menu


def end_game():
    global wizard
    global pause_menu
    wizard_death_calls()
    pause_menu.disable()


def wizard_death_calls():
    global main_menu
    global objects_to_be_removed
    global pause_time
    global score
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
    pause_time = 0
    set_score(0)
    main_menu = update_main_menu()
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
main_menu = update_main_menu()
pause_menu = update_pause_menu()

# Enabling Menus
main_menu.enable()
pause_menu.enable()

# Initial Resizing
on_resize(main_menu)
on_resize(pause_menu)



# Old Code
# Main Menu
button_scale = 3/2

# Controls Buttons
controls_first_button_start_x_pos = center_screen_width
controls_first_button_start_y_pos = 0  # main_menu_wizard_rect.bottom + ((32/400) * window_height)
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
    controls_button_start_x_pos = 0  # main_menu_wizard_rect.centerx
    controls_button_start_y_pos = 0  # main_menu_wizard_rect.bottom + ((32/400) * window_height) + controls_buttons_y_pos_offset * controls_button_index
    controls_button_start_pos = (controls_button_start_x_pos,controls_button_start_y_pos)
    control_name_underscore_removed = control_name.replace("_", " ")
    control_name_capitalized = control_name_underscore_removed.title()
    controls_button_surf = base_font.render(f"{control_name_capitalized}: {edited_controls_display_names_dict[control_name]}",False,font_color)
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
controls_reset_button_start_y_pos = 0  # main_menu_wizard_rect.bottom + ((32/400) * window_height) + (controls_buttons_y_pos_offset * (len(default_controls_pygame_constants_names_dict)))
controls_reset_button_start_pos = (controls_reset_button_start_x_pos,controls_reset_button_start_y_pos)
controls_reset_button_surf = base_font.render("Reset Controls to Default",False,font_color)
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
controls_back_button_surf = base_font.render("Back to Settings",False,font_color)
controls_back_button_scale = button_scale
controls_back_button_surf = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_scale)
controls_back_button_rect = controls_back_button_surf.get_rect(center = (controls_back_button_start_pos))
mouse_on_controls_back_button = False
controls_back_button_big_scale = button_when_big_scale
controls_back_button_surf_big = pygame.transform.scale_by(controls_back_button_surf,controls_back_button_big_scale)
controls_back_button_rect_big = controls_back_button_surf_big.get_rect(center = (controls_back_button_start_pos))
