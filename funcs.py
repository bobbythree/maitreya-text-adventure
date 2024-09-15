import time
import random
from characters import characters
from enemies import enemies

#funcs
def chooseClass():    
    characterClass = input('>')

    if characterClass in characters:
        loadPlayer(characterClass)
    else:
        print("Please type a player class from the list")
        chooseClass()


def loadPlayer(characterClass):
    #player variables
    playerHp = characters[characterClass]["hp"]
    playerMp = characters[characterClass]["mp"]
    playerWeapon = characters[characterClass]["weapon"]
    playerDamage = characters[characterClass]["damage"]


    print(f"""You have selected the {characterClass} class. Here are your stats:
    hp: {playerHp}
    mp: {playerMp}
    weapon: {playerWeapon}
    """)
    time.sleep(2)
    initBattle(characterClass)

def initBattle(characterClass):    
    print("Your first battle is against a giant blue blob!\ntype 'attack' or 'run' to continue")
    
    choice = input(">")    
    
    if choice == "attack":
        fight(characterClass)
    elif choice == "run":
        run(characterClass)
    else:
        print("Please enter either 'attack' or 'run'")
        initBattle(characterClass)

def fight(characterClass):
    while characters[characterClass]["hp"] > 0 and enemies["blueBlob"]["hp"] > 0:        
        print("You attack the blob...")
        time.sleep(2)
        
        hitChance = random.randint(0, 1)
        if hitChance == 1:
            print("HIT!")
            enemies["blueBlob"]["hp"] -= characters[characterClass]["damage"]
            print(f"Enemy HP: {enemies["blueBlob"]["hp"]}")
            if enemies["blueBlob"]["hp"] <= 0:
                print("YOU DEFEATED THE BLUE BLOB!!!")
                break
        else:
            print("MISS!")
        
        time.sleep(2)

        print("The blob attack you...")
        hitChance = random.randint(0, 1)
        time.sleep(2)
        if hitChance == 1:
            print("HIT!")
            characters[characterClass]["hp"] -= enemies["blueBlob"]["damage"]
            print(f"Player HP: {characters[characterClass]["hp"]}")
            if characters[characterClass]["hp"] <= 0:
                print("you friggin died.")
                break
        else:
            print("MISS!")

        time.sleep(2)

def run(characterClass):
    runChance = random.randint(0, 1)
    if runChance == 1:
        print("You escaped the battle")
    else:
        print("Not so fast! The battle continues...")
        time.sleep(2)
        fight(characterClass)