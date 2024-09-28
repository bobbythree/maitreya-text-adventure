import pyfiglet
import player
from verbs import *
from one_word_commands import *
from scenes import bedroom

# display command prompt, tokenize user input, get verb and noun
def command_prompt(scene_name):
    command = input("> ")
    tokens = command.lower().split()
    command_list = []
    for x in tokens:        
        if x in verbs.keys() and x not in command_list:
            command_list.append(x)
        elif x in scene_name.scene["nouns"].keys() and x not in command_list:
            command_list.append(x)
        elif x == player.stats["inventory"]["name"] and x not in command_list:
            command_list.append(x)       
    
    run_command(command_list, scene_name)

def run_command(command, scene_name):
    if command == []:
        print("does not compute.")
    elif command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]}...?")
    elif command[0] in verbs.keys() and command[1] not in scene_name.scene["nouns"].keys() and command[1] == player.stats["inventory"]["name"]:
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)
        print(f"command: {command}")
    elif command[0] not in verbs.keys() or command[1] not in scene_name.scene["nouns"].keys():
        print("try saying that another way.")    
    elif command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys():
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)
    if "exit" in command:
        exit_scene(scene_name, command[1])
    
    #loop back into the prompt
    command_prompt(scene_name)

# start of gameplay
def start():
    game_logo = pyfiglet.figlet_format("Q U E S T", font="colossal")
    print(game_logo)
    print("""Welcome to QUEST! You wake up in your bedroom which is dimly lit by artificial light coming through the [window]. In the room is your [computer] sitting on a [desk]. There is one [door] to get out.""")            

if __name__ == "__main__":
    start()

command_prompt(bedroom)  


