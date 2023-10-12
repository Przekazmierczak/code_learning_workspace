from fuel import convert, gauge

def test_convert():
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("0/1") == 0

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(0) == "E"