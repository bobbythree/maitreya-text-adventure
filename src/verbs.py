"""This module contains all verbs for the game and their functions."""

from scenes import bedroom, street
import player

def describe(scene_name, noun):
    """check if item is in scene or in inventory. Check if item is open and if item has contents. Decribe item or item contents. If item has no contents and is open(such as a door), call the item's 'description_open' property"""

    #if item is in current scene/
    if noun in scene_name.scene["nouns"]:
        if scene_name.scene["nouns"][noun]["is_open"] and scene_name.scene["nouns"][noun]["has_contents"]:
            return f'Contents: {scene_name.scene["nouns"][noun]["contents"]}'    
        if scene_name.scene["nouns"][noun]["is_open"]:
            return scene_name.scene["nouns"][noun]["description_open"]
        else: 
            return scene_name.scene["nouns"][noun]["description"]
    # if item is in player inventory
    elif noun == player.stats["inventory"]["name"]:
        if player.stats["inventory"]["is_open"] and player.stats["inventory"]["has_contents"]:
            return f'Contents: {scene_name.scene["nouns"][noun]["contents"]}'
        if player.stats["inventory"]["is_open"]:
            return player.stats["inventory"]["description_open"]
        else: 
            return player.stats["inventory"]["description"]


def get_item(scene_name, item):
    """check if item is in scene and is able to be picked up. If both return true, move item (dict) from scene to player inventory. Print inventory"""
         
    if item in scene_name.scene["nouns"] and scene_name.scene["nouns"][item]["can_get"]:
        removed_item = scene_name.scene["nouns"].pop(item)
        player.stats["inventory"].update(removed_item)
        player.stats["inventory"]["can_get"] = False
        for x in scene_name.scene["nouns"]:
            if item in scene_name.scene["nouns"][x]["contents"]:
                scene_name.scene["nouns"][x]["contents"].remove(item)
        return f'You pick up the {item}\n" f"Your Inventory: {player.stats["inventory"]["name"]}'       
            
    else: return "You cannot get that"    
        

def open_item(scene_name, item):
    """Check if item is openable and item is not already open. If both return true, open the item and change item's state to is_open: True."""
    
    current_item = scene_name.scene["nouns"][item]
    if current_item["can_open"] and not current_item["is_open"]:
        current_item["is_open"] = True
        return f"You open the {item}."        
    elif current_item["can_open"] and current_item["is_open"]:
        return "It's already open!" 
    else: return f"You cannot open {item}."


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

