"""this is the main py file and entry point for this program.

It contains the text parser functions (command_prompt and run_command) as well
as the game's start function.
"""


import pyfiglet
import player
from verbs import *
from one_word_commands import *
from scenes import (
    bedroom,
    street,
    staircase
)

print(street)
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
    
    run_command(command_list, scene_name)


def run_command(command, scene_name):
    """take in command list and current scene name. handle various commands
    and errors. If no errors, execute the verb's function from verbs.py. Call the 
    command_prompt func again."""


    # if no words matched known words
    if command == []: 
        print("does not compute.")

    #navigation commands
    elif command[0] == "go" and len(command) == 1:
        print("Go where?")
    elif command[0] == "go" and command[1] in str(scene_name.scene["next_scene"]):
        print(f"Current Scene: {command[1]}")
        next_scene = scene_name.scene["next_scene"]
        command_prompt(next_scene)
    elif command[0] == "go" and command[1] not in str(scene_name.scene["next_scene"]):
        print("You can't go there.")
           
    # if no noun
    elif command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]}...?")

    # if item is in inventory, not scene
    elif command[0] in verbs.keys() and command[1] not in scene_name.scene["nouns"].keys() and command[1] in player.stats["inventory"].values(): 
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)

    # if either verb or noun missing
    elif command[0] not in verbs.keys() or command[1] not in scene_name.scene["nouns"].keys(): 
        print("try saying that another way.")    

    # both verb and noun match
    elif command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys(): 
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)    
    
    #loop back into the prompt
    command_prompt(scene_name)


# start of gameplay
def start():
    """display welcome message. Call command_prompt func with first scene."""

    
    game_logo = pyfiglet.figlet_format("Q U E S T", font="colossal")
    print(game_logo)
    print(
    """Welcome to QUEST! You wake up in your [bedroom] which is dimly lit by
artificial light coming through the [window]. In the room is your [computer]
sitting on a [desk]. There is one [door] to get out.

This game is played by typing two word commands, a verb followed by a noun.
i.e. look sky, get rock, exit door, use hammer, talk man.
Items that can be interacted with will appear in [brackets].""")            
    
if __name__ == "__main__":
    start()


#initial call 
command_prompt(bedroom)  
