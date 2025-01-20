"""
Utility functions
"""

import os
import player
from colors import colors


def clear_terminal():
    """This function lears the terminal."""

    os.system("cls" if os.name == "nt" else "clear")


def displayInventory():
    print (f'{colors["bold"]}Your Inventory:{colors["green"]} {[x for x in player.stats["inventory"]]}')
    