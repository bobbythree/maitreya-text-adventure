"""this is the main py file and entry point for this program."""


import os
import pyfiglet
from parser import (command_prompt, run_command)
from scenes import bedroom as bedroom
from colors import colors


# functions
def clear_terminal():
    """This function lears the terminal."""

    os.system("cls" if os.name == "nt" else "clear")


def start():
    """
    Displays the game logo and the opening 
    narration.
    """

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


#clear terminal and call start func
if __name__ == "__main__":
    clear_terminal()
    start()


#pass opening scene to text parser funcs
command_prompt(bedroom)
