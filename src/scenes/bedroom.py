import player

scene = {
    "nouns": {
        "bedroom": {
            "description": """**describe bedroom""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
        },
        "window": {
            "description": "Out the window you see....",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "contents": "Out the window you see...."
        },
        "desk": {
            "description": "The desk has one drawer",
            "can_get": False,
            "can_open": False,
            "is_open": False,
        },
        "drawer": {
            "description": "Well...it's a drawer...",
            "can_get": False,
            "can_open": True,
            "is_open": False,                        
            "contents": "Inside the drawer you see a small thumbdrive"
        },
        "thumbdrive": {
            "name": "thumbdrive",
            "description": "**describe thumbdrive",
            "can_get": True,
            "can_open": False,
            "is_open": False
        },
        "computer": {
            "description": "You look at the computer screen...",
            "can_open": False,
            "is_open": False,
        },
        "door": {
            "description": "It's the door that leads out of your bedroom",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "contents": "out the door is a staircase down to another door."
        },
        "bed": {
            "description": "A small matress on the floor.",
            "can_get": False,
            "can_open": False,
            "is_open": False,
        },
        "inventory": {
            "description": player.stats["inventory"],
            "can_get": False,
            "is_open": False
        }
    }
}
