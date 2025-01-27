"""
this module contains one word commands
"""


from colors import colors
from utils import displayInventory
import player


# funcs
def describe_scene(scene_name):
    return scene_name.scene["description"]


def showInventory():
    return f'{colors["bold"]}Your Inventory:{colors["green"]} {[x for x in player.stats["inventory"]]}'


# commands
one_word_commands = {
    "look" : {
        "func": describe_scene
    },
    "inventory": {
        "func": showInventory
    },
    "inv": {
        "func": showInventory
    },
    "i": {
        "func": showInventory
    }
}