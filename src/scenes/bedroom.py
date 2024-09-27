import player

scene = {
    "nouns": {
        "bedroom": {
            "description": """**describe bedroom""",
            "can_open": False
        },
        "window": {
            "description": "Out the window you see....",
            "can_open": True
        },
        "desk": {
            "description": "The desk has one drawer",
            "can_open": False
        },
        "drawer": {
            "description": "Well...it's a drawer...",
            "can_open": True,
            "is_open": False,
            "opened": "Inside the drawer is a small thumbdrive.",
            "contents": "Inside the drawer you see a small thumbdrive"
        },
        "thumbdrive": {
            "description": "**describe thumbdrive",
            "can_get": True,
            "can_open": False
        },
        "computer": {
            "description": "You look at the computer screen..."
        },
        "door": {
            "description": "It's the door that leads out of your bedroom",
            "can_open": True,
            "is_open": False,
            "contents": "out the door is a staircase down to another door."
        },
        "bed": {
            "description": "A small matress on the floor.",
            "can_open": False
        },
        "inventory": {
            "description": player.stats["inventory"]
        }
    }
}
