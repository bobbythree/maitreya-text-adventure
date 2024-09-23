from nouns import *

def describe(noun):
    return nouns[noun]["description"]

verbs = {
    "look": {
        "func": describe
    }
}

