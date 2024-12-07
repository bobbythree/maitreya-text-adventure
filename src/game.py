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
        print("Go where?")

    elif command[0] == "go" and command[1] in str(scene_name.scene["next_scene"]):
        for s in scene_name.scene["next_scene"]:
            print(s.scene["nouns"][command[1]]["description"])
            print(f"\n{colors['bold']}Current Scene: {colors['green']}{command[1]}")
            print(colors["cyan"])
            command_prompt(s)

    elif command[0] == "go" and command[1] not in str(scene_name.scene["next_scene"]):
        print("You can't go there.")

    # if no noun
    elif command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]}...?")
    elif command[0] in scene_name.scene["nouns"] and len(command) == 1:
        print("wha??")

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


# start of gameplay
def clear_terminal():
    """Clear the terminal"""

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
