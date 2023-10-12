import datetime
import inflect
import sys


def main():
    birth_day = get_date(input("Birthday: "))
    if birth_day == "ValueError":
        sys.exit("Invalid date")
    else:
        today = datetime.date.today()

        minutes = get_minutes(today, birth_day)
        minutes_text = change_into_text(minutes)

        print(f"You are {minutes_text} minutes old.")

def get_date(birth_day):
    try:
        year, month, day = birth_day.split("-")
        date = datetime.date(int(year), int(month), int(day))
    except ValueError:
        return "ValueError"
    else:
        return date

def get_minutes(today, birth_day):
    days = today - birth_day
    return int(days.total_seconds() / 60)

def change_into_text(number):
    return inflect.engine().number_to_words(number)


if __name__ == "__main__":
    main()