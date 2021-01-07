import pytest
from pyxkcdpass import XKCDPass

def test_is_readable(dictionary='dictionary', length=4):
    generator = XKCDPass(dictionary, length, True)
    password = generator.generate_random_password()

    words = password.split(" ")
    
    assert(" " in password)
    assert(len(words) == length)

def test_not_readable(dictionary='dictionary', length=4):
    generator = XKCDPass(dictionary, length, False)
    password = generator.generate_random_password()

    assert(" " not in password)