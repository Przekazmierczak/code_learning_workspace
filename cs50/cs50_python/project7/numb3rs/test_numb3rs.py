from numb3rs import validate

def test_validate_true():
    assert validate("255.255.255.255") == "True"
    assert validate("0.0.0.0") == "True"
    assert validate("255.0.0.255") == "True"
    assert validate("1.2.3.4") == "True"

def test_validate_false():
    assert validate("1") == "False"
    assert validate("1.2.3") == "False"
    assert validate("cat.dog.bird.fish") == "False"
    assert validate("1.2.3.4.5") == "False"
    assert validate("275.1999.21.3") == "False"
    assert validate("255,255,255,255") == "False"