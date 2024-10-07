import pytest
import src.verbs as verbs
from scenes import bedroom as bedroom


def test_describe():
    assert verbs.describe(bedroom, "bed") == "A small matress on the floor."

def test_get_success():
    assert verbs.get_item(bedroom, "thumbdrive") == "You pick up the thumbdrive\n""Your Inventory: thumbdrive"

def test_get_fail():
    assert verbs.get_item(bedroom, "bed") == "You cannot get that"
    
