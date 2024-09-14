import random

characters = {
  "fighter": {
    "id": 1,
    "hp": 50,
    "mp": 0,
    "weapon": "Broadsword(5-15 damage)",
    "damage": random.randint(5, 15)
  },
  "mage": {
    "id": 2,
    "hp": 30,
    "mp": 20,
    "weapon": "staff(10-15 damage)",
    "damage": random.randint(10, 15)
  },
  "rogue": {
    "id": 3,
    "hp": 30,
    "mp": 10,
    "weapon": "daggers(5-15 damage)",
    "damage": random.randint(10, 20)
  }
}