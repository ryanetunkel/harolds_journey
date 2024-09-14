"""Controls"""
import csv

import pygame
import yaml

from strings_constants_dict import *


default_controls_path = "harolds_journey/saved_files/controls/default_controls.yaml"
edited_controls_path = "harolds_journey/saved_files/controls/edited_controls.yaml"
display_names_path = "harolds_journey/display_names.csv"
# display_names_path layout:
# pygame_constant_name: display_name (based on one chosen)

default_options_path = "harolds_journey/saved_files/options/default_options.yaml"
edited_options_path = "harolds_journey/saved_files/options/edited_options.yaml"

held_control_name = ""
held_control_display_name = "Unbound"

# Pygame Constant Interpretation - pygame_constants.csv
def get_display_names_path() -> str:
    return display_names_path


def get_display_name_based_on_constant(constant:str, field:str) -> str:
    with open(get_display_names_path(), "r") as csvfile:
        display_names_dict = csv.DictReader(csvfile)
        for row in display_names_dict:
            if row["constant"] == constant:
                return row[field]


def get_display_name(constant: str) -> str:
    if (custom:=(get_display_name_based_on_constant(constant,"custom_description"))) != "":
        return custom
    elif (ascii:=(get_display_name_based_on_constant(constant,"ascii"))) != "":
        return ascii
    elif (description:=(get_display_name_based_on_constant(constant,"description"))) != "":
        return description
    else:
        return ""

# Yaml Read/Write w/ Dict - default_controls.yaml & edited_controls.yaml
def read_yaml_to_dict(yaml_file: str) -> dict:
    with open(yaml_file, "r") as file:
        yaml_dict = yaml.safe_load(file)
    file.close()
    return yaml_dict


def write_dict_to_yaml(yaml_dict: dict, yaml_file: str):
    with open(yaml_file, "w") as file:
        yaml.dump(yaml_dict,file)
    file.close()

# Options Functions
# Default Options Functions
def get_default_options_path() -> str:
    return default_options_path


def get_default_options_file_dict() -> dict:
    return read_yaml_to_dict(get_default_options_path())


# Edited Options Functions
def get_edited_options_path() -> str:
    return edited_options_path


def get_edited_options_file_dict() -> dict:
    return read_yaml_to_dict(get_edited_options_path())


def set_edited_options_file_dict(yaml_dict: dict):
    write_dict_to_yaml(yaml_dict,get_edited_options_path())


# Default Controls Functions
def get_default_controls_path() -> str:
    return default_controls_path


def get_default_controls_file_dict() -> dict:
    return read_yaml_to_dict(get_default_controls_path())


# Edited Controls Functions
def get_edited_controls_path() -> str:
    return edited_controls_path


def get_edited_controls_file_dict() -> dict:
    return read_yaml_to_dict(get_edited_controls_path())


def set_edited_controls_file_dict(yaml_dict: dict):
    write_dict_to_yaml(yaml_dict,get_edited_controls_path())


# Pygame Constants Functions
def get_control(control_name: str) -> tuple[int,bool]:
    edited_controls_file_dict = get_edited_controls_file_dict()
    edited_controls_pygame_constants_names_dict = edited_controls_file_dict.get("edited_controls_pygame_constants_names_dict")
    edited_controls_pygame_constant_name = edited_controls_pygame_constants_names_dict.get(control_name)
    edited_controls_are_mouse_buttons_dict = edited_controls_file_dict.get("edited_controls_are_mouse_buttons")
    edited_control_is_mouse = edited_controls_are_mouse_buttons_dict.get(control_name)
    if not edited_control_is_mouse and edited_controls_pygame_constant_name in keyboard_strings_constants_dict.keys():
        pygame_constant = keyboard_strings_constants_dict.get(edited_controls_pygame_constant_name)
    elif edited_control_is_mouse and edited_controls_pygame_constant_name in mouse_strings_constants_dict.keys():
        pygame_constant = mouse_strings_constants_dict.get(edited_controls_pygame_constant_name)
    else:
        pygame_constant = list(unbound_constants_dict.values())[0]
    return (pygame_constant, edited_control_is_mouse)


def get_pygame_constant_name(event: pygame.event.Event, is_mouse) -> str:
    if not is_mouse and hasattr(event, "key") and event.key in keyboard_strings_constants_dict.values():
        keyboard_strings_constants_dict_keys = list(keyboard_strings_constants_dict.keys())
        keyboard_strings_constants_dict_value_index = list(keyboard_strings_constants_dict.values()).index(event.key)
        pygame_constant_name = keyboard_strings_constants_dict_keys[keyboard_strings_constants_dict_value_index]
    elif is_mouse and hasattr(event, "button") and event.button in mouse_strings_constants_dict.values():
        mouse_strings_constants_dict_keys = list(mouse_strings_constants_dict.keys())
        mouse_strings_constants_dict_value_index = list(mouse_strings_constants_dict.values()).index(event.button)
        pygame_constant_name = mouse_strings_constants_dict_keys[mouse_strings_constants_dict_value_index]
    else:
        pygame_constant_name = list(unbound_constants_dict.keys())[0]
    return pygame_constant_name


# Controls Functions
def interpret_input(control_name: str, event: pygame.event.Event) -> bool:
    is_mouse = event.type == pygame.MOUSEBUTTONDOWN
    key_or_mouse_event = event.type == pygame.KEYDOWN or is_mouse
    if not key_or_mouse_event:
        return False
    pygame_constant_name = get_pygame_constant_name(event, is_mouse)

    if key_or_mouse_event:
        set_control(control_name, pygame_constant_name, is_mouse)
    return key_or_mouse_event


def set_control(control_name: str, pygame_constant_name: str, is_mouse: bool):
    edited_controls_file_dict = get_edited_controls_file_dict()
    edited_controls_are_mouse_buttons = edited_controls_file_dict.get("edited_controls_are_mouse_buttons")
    edited_controls_pygame_constants_names_dict = edited_controls_file_dict.get("edited_controls_pygame_constants_names_dict")
    edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
    edited_controls_are_mouse_buttons[control_name] = is_mouse
    edited_controls_pygame_constants_names_dict[control_name] = pygame_constant_name
    edited_controls_display_names_dict[control_name] = get_display_name(pygame_constant_name)
    edited_controls_file_dict.update({
        "edited_controls_are_mouse_buttons": edited_controls_are_mouse_buttons,
        "edited_controls_pygame_constants_names_dict": edited_controls_pygame_constants_names_dict,
        "edited_controls_display_names_dict": edited_controls_display_names_dict,
    })
    set_edited_controls_file_dict(edited_controls_file_dict)
    # Handle error in future in case edited_controls_display_names_dict.get(control_name) is not in the edited_controls_display_names_dict


def set_control_to_none(control_name: str):
    set_control(control_name, list(unbound_constants_dict.keys())[0], False)


def set_control_display_name_to_other_display_name(control_name: str, new_display_name: str):
    edited_controls_file_dict = get_edited_controls_file_dict()
    edited_controls_display_names_dict = edited_controls_file_dict.get("edited_controls_display_names_dict")
    edited_controls_display_names_dict[control_name] = new_display_name
    edited_controls_file_dict.update({
        "edited_controls_display_names_dict": edited_controls_display_names_dict,
    })
    set_edited_controls_file_dict(edited_controls_file_dict)


def set_control_display_name_to_unbound(control_name: str):
    set_control_display_name_to_other_display_name(control_name, get_display_name(list(unbound_constants_dict.keys())[0]))


# Must be updated whenever add new control
def reset_controls():
    default_controls_file_dict = get_default_controls_file_dict()
    edited_controls_file_dict = get_edited_controls_file_dict()
    for default_controls_section_name, default_controls_section in default_controls_file_dict.items():
        controls_section_name = default_controls_section_name.lstrip("default_")
        edited_controls_section_name = "edited_" + controls_section_name
        edited_controls_file_dict.update({edited_controls_section_name: default_controls_section})
    set_edited_controls_file_dict(edited_controls_file_dict)