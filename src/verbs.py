from scenes import bedroom, street
import player
import verbs

def describe(scene_name, noun):
    """describes item (if not open) or item's contents(if open)"""
    if noun in scene_name.scene["nouns"]: #if item is in scene/    
        if scene_name.scene["nouns"][noun]["is_open"]:
            return scene_name.scene["nouns"][noun]["contents"]
        else: 
            return scene_name.scene["nouns"][noun]["description"]
    elif noun == player.stats["inventory"]["name"]: # if item is in inv
        if player.stats["inventory"]["is_open"]:
            return player.stats["inventory"]["contents"]
        else: 
            return player.stats["inventory"]["description"]

def get_item(scene_name, item):
    """moves item (dict) from scene to player inv."""
         
    if item in scene_name.scene["nouns"] and scene_name.scene["nouns"][item]["can_get"]:
        removed_item = scene_name.scene["nouns"].pop(item)
        player.stats["inventory"].update(removed_item)
        player.stats["inventory"]["can_get"] = False
        print(f"You pick up the {item}") 
        return f"Your Inventory: {player.stats["inventory"]["name"]}"
    else: return "You cannot get that"
    
        

def open_item(scene_name, item):
    current_item = scene_name.scene["nouns"][item]
    if current_item["can_open"] and not current_item["is_open"]:
        current_item["is_open"] = True
        return f"You open the {item}."        
    elif current_item["can_open"] and current_item["is_open"]:
        return "It's already open!" 
    else: return f"You cannot open {item}"

def exit_scene(scene_name, exit):    
    
    return f"you exit the {exit}"
    


#verb dict
verbs = {
    "look": {
        "func": describe
    },
    "get": {
        "func": get_item
    },
    "open": {
        "func": open_item
    },
    "exit": {
        
    }
}

