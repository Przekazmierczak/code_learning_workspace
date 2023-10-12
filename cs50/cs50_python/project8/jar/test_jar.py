from jar import Jar
import pytest

def test__init__():
    jar = Jar()

    assert jar.size == 0
    assert jar.capacity == 12
    jar = Jar(13)
    assert jar.capacity == 13

def test__str__():
    jar = Jar()
    jar.size = 3
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()

    jar.deposit(3)
    assert jar.size == 3
    jar.size = 3
    jar.deposit(5)
    assert jar.size == 8

def test_withdraw():
    jar = Jar()

    jar.size = 5
    jar.withdraw(3)
    assert jar.size == 2

    jar.size = 12
    jar.withdraw(11)
    assert jar.size == 1

def test_deposit_over_capacity():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw_over_size():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)

def test_capacity_less_one():
    with pytest.raises(ValueError):
        Jar(0)