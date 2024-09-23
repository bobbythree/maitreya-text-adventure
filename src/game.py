import pyfiglet
from verbs import *
from scenes import bedroom



# display command prompt, tokenize user input, get verb and noun
def command_prompt(scene_name):
    command = input("> ")
    tokens = command.lower().split()
    command_list = []
    for x in tokens:
        if x in verbs.keys():
            command_list.append(x)
        if x in scene_name.scene["nouns"].keys():
            command_list.append(x)
    run_command(command_list, scene_name)


def run_command(command, scene_name):
    if command[0] in verbs.keys() and len(command) == 1:
        print(f"{command[0]} what?")
    elif command[0] in verbs.keys() and command[1] in scene_name.scene["nouns"].keys():
        output = verbs[command[0]]["func"](scene_name, command[1])
        print(output)
    else: print("Does not compute.")
    command_prompt(scene_name)

def start():
    game_logo = pyfiglet.figlet_format("Q U E S T", font="colossal")
    print(game_logo)
    print("""Welcome to QUEST! You wake up in your bedroom which is dimly lit by artificial light coming through the [window]. In the room is your [computer] sitting on a [desk]. There is one [door] to get out.""")            

if __name__ == "__main__":
    start()

command_prompt(bedroom)  


