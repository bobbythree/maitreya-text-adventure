"""This module contains data for the scene: street. It contains the scene
objects (nouns) and their attributes.
"""

from scenes import staircase as staircase


scene = {
    "next_scene": {
        "staircase": {
            "name": "staircase",
            "module": staircase
        }
    },
    "nouns": {
        "street": {
            "name": "street",
            "description": """You are on the main street outside your apartment""",             
            "can_get": False,
            "can_open": False,
            "is_open": False,
            "can_exit": False,
            "contents": []
        },
        "staircase": {
            "name": "staircase",
            "description": """It's the staircase back up to your bedroom.""",             
                "can_get": False,
                "can_open": False,
                "is_open": False,
                "can_exit": False,
                "contents": []
        }
    }
}
