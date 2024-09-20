from funcs import *

#start of gameplay
def main():
    print("welcome to @%#& quest! What is your name?")
    name = input('>')
    print(f"Hello {name}!!")
    print("""Select your character's class:
        fighter
        mage
        rogue
        (type your selection)
        """)

    chooseClass()


if __name__ == "__main__":
    main()
            
