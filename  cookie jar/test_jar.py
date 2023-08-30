from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(capacity = -1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

def test_notEnough():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)