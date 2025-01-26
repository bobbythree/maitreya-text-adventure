"""
this module contains one word commands
"""


# funcs
def describe_scene(scene_name):
    return scene_name.scene["description"]


# commands
one_word_commands = {
    "look" : {
        "func": describe_scene
    }
}