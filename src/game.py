"""this is the main py file and entry point for this program.

It contains the text parser functions (command_prompt and run_command) as well
as the game's start function.
"""


import os
import pyfiglet
import player
from verbs import verbs
from one_word_commands import *
from scenes import (
    bedroom,
    street,
    staircase
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
    print(command_list)
    run_command(command_list, scene_name)


def run_command(command, scene_name):
    """take in command list and current scene name. handle various commands
    and errors. If no errors, execute the verb's function from verbs.py. 
    Call the command_prompt func again."""

    print(colors["green"])

    # if no words matched known words
    if command == []:
        print("does not compute.")

    #navigation commands
    elif command[0] == "go" and len(command) == 1:
        print("\nGo where?")
    elif command[0] == "go" and command[1] in str(scene_name.scene["next_scene"]):
        next_scene = scene_name.scene["next_scene"]
        print(next_scene.scene["nouns"][command[1]]["description"])
        print(f"\n{colors['bold']}Current Scene: {colors['green']}{command[1]}")
        print(colors["cyan"])
        command_prompt(next_scene)
    elif command[0] == "go" and command[1] not in str(scene_name.scene["next_scene"]):
        print("\nYou can't go there.")

    #if item is inside another item
    for i in scene_name.scene["nouns"].values():
        if command[0] in verbs.keys() and command[1] in i["contents"]:
            output = verbs[command[0]]["func"](scene_name, command[1])
            print(output)

    # if no noun
    if command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]}...?")

    # if item is in inventory, not scene
    elif command[0] in verbs.keys() and command[1] not in scene_name.scene["nouns"].keys() and command[1] in player.stats["inventory"]:
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)

    # if either verb or noun missing
    elif command[0] not in verbs.keys() or command[1] not in scene_name.scene["nouns"].keys():
        print("\ntry saying that another way.")

    # both verb and noun match
    if command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys():
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)

    #loop back into the prompt
    print(colors['cyan'])
    command_prompt(scene_name)


# start of gameplay
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def start():
    """display welcome message. Call command_prompt func with first scene."""


    game_logo = pyfiglet.figlet_format("MAITREYA's QUEST", font="smkeyboard")
    print(colors["cyan"])
    print(game_logo)
    print(
    f"""{colors['green']}Welcome to {colors['light_green']}MAITREYA'S QUEST! {colors['green']}This game is played by typing two word commands,
a verb followed by a noun. i.e. look sky, get rock, exit door, use hammer,
talk man. To navigate, type 'go' followed by a location. Items that can be
interacted with will appear in [brackets].

You wake up in your [bedroom] which is dimly lit by artificial light coming
through the [window]. In the room is your [computer] sitting on a [desk].
There is one [door] to get out.{colors['cyan']} """)

if __name__ == "__main__":
    clear_terminal()
    start()


#initial call
command_prompt(bedroom)
