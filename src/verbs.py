from scenes import bedroom

def describe(scene_name, noun):
    return scene_name.scene["nouns"][noun]["description"]

verbs = {
    "look": {
        "func": describe
    }
}

