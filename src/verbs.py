from scenes import bedroom
import player

def describe(scene_name, noun):
    return scene_name.scene["nouns"][noun]["description"]

def get(scene_name, item):
    player.stats["inventory"].append(item)
    scene_name.scene["nouns"].pop(item)
    print(scene_name.scene["nouns"].keys())
    print(player.stats["inventory"])

verbs = {
    "look": {
        "func": describe
    },
    "get": {
        "func": get
    }
}

