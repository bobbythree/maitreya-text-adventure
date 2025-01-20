"""
Utility functions
"""

import os
import player

def clear_terminal():
    """This function lears the terminal."""

    os.system("cls" if os.name == "nt" else "clear")


def displayInventory():
   return [x for x in player.stats["inventory"]]
    