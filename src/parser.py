"""
This module contains the text-parser functions (command_prompt and run_command).
"""


import player
from one_word_commands import one_word_commands
from verbs import verbs
from utils import displayInventory, clear_terminal
from scenes import (
    bedroom as bedroom,
    street as street,
    staircase as staircase
)
from colors import colors


# text-parser funcs
def command_prompt(scene_name):
    """display the command prompt in the current scene. tokenize user input.
    loop over tokens. put verbs, nouns etc into command_list. Call 
    run_command func, passing it the commands.
    """

    command = input("> ")
    tokens = command.lower().split()
    command_list = []
    for x in tokens:
        if x in verbs.keys() and x not in command_list:
            command_list.append(x)
        elif x in scene_name.scene["nouns"].keys() and x not in command_list:
            command_list.append(x)
        elif x in player.stats["inventory"] and x not in command_list:
            command_list.append(x)
        for i in scene_name.scene["nouns"].values():
            if x in i["contents"]:
                command_list.append(x)

    run_command(command_list, scene_name)


def run_command(command, scene_name):
    """take in command list and current scene name. handle various commands
    and errors. If no errors, execute the verb's function from verbs.py. 
    Call the command_prompt func again."""


    print(colors["green"])

    # if no words matched known words
    if command == []:
        print("does not compute.")

    #one word commands ('look', 'inventory', 'save', 'restore', 'quit')
    elif command[0] in one_word_commands and len(command) == 1:
        output = one_word_commands[command[0]]["func"](scene_name)
        print(output)

    #navigation commands
    elif command[0] == "go" and len(command) == 1:
        print("Go where?")

    elif command[0] == "go" and command[1] in scene_name.scene["next_scene"]:
        clear_terminal()
        print(f'{colors["bold"]}Current Scene: {scene_name.scene["next_scene"][command[1]]["name"]}{colors["green"]}')
        print(scene_name.scene["next_scene"][command[1]]["module"].scene["nouns"][command[1]]["description"])
        print(colors["cyan"])
        command_prompt(scene_name.scene["next_scene"][command[1]]["module"])

    elif command[0] == "go" and command[1] not in str(scene_name.scene["next_scene"]):
        print("You can't go there.")

    # if no noun
    elif command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]}...?")
    elif command[0] in scene_name.scene["nouns"] and len(command) == 1:
        print("wha??")

    # to look at inventory
    elif command[0] == "look" and command[1] == "inventory":
        displayInventory()

    # if item is in inventory
    elif command[0] in verbs.keys() and command[1] not in scene_name.scene["nouns"].keys() and command[1] in player.stats["inventory"]:
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)

    # both verb and noun match
    elif command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys():
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)

    # get or describe item inside something
    elif [output := verbs[command[0]]["func"] (scene_name, command[1]) for i in scene_name.scene["nouns"].values() if command[1] in i["contents"] and i ["is_open"]]:
        print(output)

    elif [output := verbs[command[0]]["func"] (scene_name, command[1]) for i in scene_name.scene["nouns"].values() if command[1] in i["contents"] and not i ["is_open"]]:
        print("You do not see such an item.")

    

    #loop back into the prompt
    print(colors['cyan'])
    command_prompt(scene_name)