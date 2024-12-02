"""This module contains data for the scene: bedroom. It contains the scene's
objects (nouns) and their attributes.
"""


import player
import pyfiglet
from scenes import staircase as staircase


scene = {
    "next_scene": [staircase],    
    "nouns": {
        "test": {
            "name": "test",
                "description": 
                """this is a test""",
                "can_get": True,
                "can_open": False,
                "is_open": False,
                "can_exit": False,
                "contents": []
            },
        "bedroom": {
            "name": "bedroom",
            "description": 
            """Your bedroom is small and cluttered.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "window": {
            "name": "window",
            "description": 
"""The [window] is very dirty and difficult to see through. All you see is the
indication of artificial light outside.""",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": False,
            "can_exit": False,
            "description_open":
"""Looking out the open window you can see many video screens up on tall poles
that are broadcasting advertisements for various corporate interests such as
Pear, MacroFirm, MVideo and Booble.""",
            "contents": []
        },
        "desk": {
            "name": "desk",
            "description": 
"""Your small simple desk has your [computer] sitting on it. The desk has one
[drawer]""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "drawer": {
            "name": "drawer",
            "description":
"""Well...it's a drawer...""",
            "description_open": "The drawer is empty",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": True,
            "can_exit": False,
            "contents": {
                "thumbdrive": {
                    "name": "thumbdrive",
                        "description":
"""A mostly obsolete piece of technology that stores files and data. You'd be
hard pressed to even find a computer that has a port for it. Yours sure doesn't.""",
                "can_get": True,
                "can_open": False,
                "is_open": False,
                "can_exit": False,
                "has_contents": False,
                "contents": []
                },    
            }
        },        
        "computer": {
            "name": "computer",
            "description": 
"""Your small black laptop sits open on the desk. It is covered in stickers
from games and bands you like. The [screen] glows with green text""",
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
            "description": 
"""It's the door that leads out of your [bedroom]""",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "has_contents": False,
            "can_exit": True,
            "description_open":
"""Outside the door is a downward [staircase]. Type 'go staircase' to enter.""",
            "contents": []
        },
        "bed": {
            "name": "bed",
            "description": 
"""A small matress on the floor.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
         "staircase": {
            "name": "staircase",
                "description":
"""The stairs lead down to another door.""",
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
            "contents": {}
        }
    }
}
