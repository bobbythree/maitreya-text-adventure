from nouns import *

def describe(noun):
    print(nouns[noun]["description"])

verbs = {
    "look": {
        "func": describe
    }
}
