from bank import value

def test_value_0():
    assert value("hello") == "0"
    assert value("hello, newman") == "0"

def test_value_20():
    assert value("how you doing?") == "20"

def test_value_100():
    assert value("what's happening?") == "100"