"""This module contains data for the scene: staircase. It contains the scene
objects (nouns) and their attributes.
"""

from scenes import street as street 


scene = {
    "next_scene": street,
    "nouns": {
        "staircase": {
            "name": "staircase",
            "description": """You are now in the staircase that leads out of
your apartment. It is a shared public staircase that leads down to a heavy
door.""",
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
