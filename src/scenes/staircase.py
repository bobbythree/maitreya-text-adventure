"""This module contains data for the scene: staircase. It contains the scene
objects (nouns) and their attributes.
"""

from scenes import street as street
from scenes import bedroom as bedroom


scene = {
    "next_scene": {
        "bedroom": {
            "name": "bedroom",
            "module": bedroom
        },
        "street": {
            "name": "street",
            "module": street
        }
    },
    "nouns": {
        "staircase": {
            "name": "staircase",
            "description": """You are now in the staircase that leads out of
your apartment. It is a shared public staircase that leads down to a heavy
[door].""",
            "can_get": False,
                "can_open": False,
                "is_open": False,
                "has_contents": False,
                "can_exit": False,
                "contents": []
        },
        "door": {
            "name": "door",
            "description": "I think it leads outside.",
            "can_get": False,
                "can_open": True,
                "is_open": False,
                "has_contents": False,
                "can_exit": True,
                "description_open": "the door leads outside to the [street]",
                "contents": []            
        },
        "bedroom": {
            "name": "bedroom",
            "description":
            """It's your bedroom.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "street": {
            "name": "street",
            "description": """Looking though the door you can see the [street]
outside.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "has_contents": False,
            "can_exit": True,
            "contents": [] 
        }
    }
}
