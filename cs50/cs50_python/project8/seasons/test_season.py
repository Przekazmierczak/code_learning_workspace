from seasons import get_date, get_minutes, change_into_text
import datetime

def test_get_date_valid():
    assert get_date("1990-10-20") == datetime.date(1990, 10, 20)
    assert get_date("2021-12-30") == datetime.date(2021, 12, 30)
    assert get_date("1998-08-09") == datetime.date(1998, 8, 9)

def test_get_date_invalid():
    assert get_date("cat") == "ValueError"
    assert get_date("cat-dog-pig") == "ValueError"
    assert get_date("1222-14-12") == "ValueError"
    assert get_date("1992-12-60") == "ValueError"
    assert get_date("1662.12.15") == "ValueError"

def test_get_minutes():
    assert get_minutes(datetime.date(2023, 9, 11), datetime.date(2023, 9, 10)) == 1440
    assert get_minutes(datetime.date(2023, 9, 11), datetime.date(2023, 9, 9)) == 2880

def test_change_into_text():
    assert change_into_text(1) == "one"
    assert change_into_text(2) == "two"
    assert change_into_text(55) == "fifty-five"
    assert change_into_text(0) == "zero"
