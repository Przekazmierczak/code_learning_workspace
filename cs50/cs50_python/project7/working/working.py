import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-1]|[0-9])(:[0-5][0-9])? (AM|PM) to (1[0-1]|[0-9])(:[0-5][0-9])? (AM|PM)$", s)
    if matches:
        [start_hour, start_min, start_time, end_hour, end_min, end_time] = matches.groups()
        if start_min != None and end_min != None:
            start_min = start_min.replace(":", "")
            end_min = end_min.replace(":", "")
        else:
            start_min = "00"
            end_min = "00"
        if start_time == "PM":
            start_hour = int(start_hour) + 12
        if end_time == "PM":
            end_hour = int(end_hour) + 12
        # Make sure that hour have 2 digits
        start_hour = int(start_hour)
        end_hour = int(end_hour)
        start_hour = f"{start_hour:02d}"
        end_hour = f"{end_hour:02d}"

        time_24h = f"{start_hour}:{start_min} to {end_hour}:{end_min}"
        return time_24h
    else:
        raise ValueError

if __name__ == "__main__":
    main()