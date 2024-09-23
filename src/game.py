import pyfiglet
from verbs import *
from nouns import *

def run_command(command):
    if command[0] in verbs.keys() and command[1] in nouns.keys():
        output = verbs[command[0]]["func"](nouns[command[1]]["description"])
        print(output)
    

def start():
    game_logo = pyfiglet.figlet_format("Q U E S T", font="colossal")
    print(game_logo)
    print("""Welcome to QUEST! You wake up in your bedroom which is dimly lit by artificial light coming through the [window]. In the room is your [computer] sitting on a [desk]. There is one [door] to get out.""")       
    command = input("> ")
    tokens = command.lower().split()
    command_list = []
    for x in tokens:
        if x in verbs.keys():
            command_list.append(x)
        if x in nouns.keys():
            command_list.append(x)
    run_command(command_list)
    
            


start()

            
