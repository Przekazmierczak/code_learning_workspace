from response import validation

def test_validation():
    assert validation("harry@gmail.com") == "Valid"
    assert validation("harry@o2.pl") == "Valid"
    assert validation("harry.potter@gmail.com") == "Valid"
    assert validation("harry potter") == "Invalid"
    assert validation("harry@potter") == "Invalid"