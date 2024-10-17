import pytest
import src.verbs as verbs
from src.scenes import bedroom as bedroom


def test_describe_success():
    assert verbs.describe(bedroom, "bed") == "A small matress on the floor."
    

def test_get_success():
    assert verbs.get_item(bedroom, "thumbdrive") == "You pick up the thumbdrive\n""Your Inventory: thumbdrive"


def test_get_fail():
    assert verbs.get_item(bedroom, "bed") == "You cannot get that"

    
def test_open_success():
    assert verbs.open_item(bedroom, "door") == "You open the door."


def test_open_fail():
    assert verbs.open_item(bedroom, "bed") == "You cannot open bed."


def test_already_open():
    if bedroom.scene["nouns"]["door"]["is_open"]:
        assert verbs.open_item(bedroom, "door") == "It's already open!"
