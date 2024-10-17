"""This module contains data for the scene: 'bedroom'. It contains all game
objects (nouns) for this scene and their attributes.
"""


import player
import pyfiglet
from scenes import street as street


scene = {
    "nouns": {
        "bedroom": {
            "name": "bedroom",
            "description": """Your bedroom is small and cluttered.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "window": {
            "name": "window",
            "description": """Looking out the window you can see many video screens up on tall poles that are broadcasting advertisements for various corporate interests such as Pear, MacroFirm, MVideo and Booble.""",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": False,
            "can_exit": False,
            "description_open": """Looking out the window you can see many video screens up on tall poles that are broadcasting advertisements for various corporate interests such as Pear, MacroFirm, MVideo and Booble.""",
            "contents": []
        },
        "desk": {
            "name": "desk",
            "description": "The desk has one drawer",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "drawer": {
            "name": "drawer",
            "description": "Well...it's a drawer...",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": True,
            "can_exit": False,
            "contents": ["thumbdrive"]
        },
        "thumbdrive": {
            "name": "thumbdrive",
            "description": """A mostly obsolete piece of technology that stores files and data. You'd be hard pressed to even find a computer that has a port for it. Yours sure doesn't.""",
            "can_get": True,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "computer": {
            "name": "computer",
            "description": """Your small black laptop sits open on the desk. It is covered in stickers from games and bands you like. The [screen] glows with light blue text""",
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "screen": {
            "name": "screen",
            "description": pyfiglet.figlet_format("""
            ---
            HTP !
            ---""", font="alligator2"),
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "door": {
            "name": "door",
            "description": "It's the door that leads out of your bedroom",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": False,
            "can_exit": True,
            "description_open": "out the door is a staircase down to another door.",
            "next_scene": street,
            "contents": []
        },
        "bed": {
            "name": "bed",
            "description": "A small matress on the floor.",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "inventory": {
            "name": "inventory",
            "description": player.stats["inventory"],
            "can_get": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        }
    }
}
