import player
import pyfiglet

scene = {
    "nouns": {
        "bedroom": {
            "description": """Your bedroom is small and cluttered.""",
            "can_get": False,
            "can_open": False,
            "is_open": False,
        },
        "window": {
            "description": """Looking out the window you can see many video screens up on tall poles that are broadcasting advertisements for various corporate interests such as Pear, MacroFirm, MVideo and Booble.""",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "contents": """Looking out the window you can see many video screens up on tall poles that are broadcasting advertisements for various corporate interests such as Pear, MacroFirm, MVideo and Booble."""
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
            "description": """A mostly obsolete piece of technology that stores files and data. You'd be hard
pressed to even find a computer that has a port for it. Yours sure doesn't.""",
            "can_get": True,
            "can_open": False,
            "is_open": False
        },
        "computer": {
            "description": """Your small black laptop sits open on the desk. It is covered in stickers from games and bands you like. The [screen] glows with light blue text""",
            "can_open": False,
            "is_open": False,
        },
        "screen": {
            "description": pyfiglet.figlet_format("""
            ---
            HTP !
            ---""", font="alligator2"),
            "can_get": False,
            "can_open": True,
            "is_open": False,
        },
        "door": {
            "description": "It's the door that leads out of your bedroom",
            "can_get": False,
            "can_open": True,
            "is_open": False,
            "contents": "out the door is a staircase down to another door.",
            "next_scene": "street"
        },
        "bed": {
            "description": "A small matress on the floor.",
            "can_get": False,
            "can_open": False,
            "is_open": False,
        },
        "inventory": {
            "description": player.stats["inventory"].values(),
            "can_get": False,
            "is_open": False
        }
    }
}
