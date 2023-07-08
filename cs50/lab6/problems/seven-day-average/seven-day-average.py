import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)
    print(new_cases.keys())

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    previous_cases = {}
    new_cases = {}
    for covid in reader:
        if covid["state"] not in previous_cases:
            previous_cases[covid["state"]] = [int(covid["cases"])]
            new_cases[covid["state"]] = [int(covid["cases"])]
        else:
            if len(previous_cases[covid["state"]]) < 14:
                previous_cases[covid["state"]].append(int(covid["cases"]))
                new_cases[covid["state"]].append(int(covid["cases"]) - previous_cases[covid["state"]][-2])
            else:
                previous_cases[covid["state"]].pop(0)
                new_cases[covid["state"]].pop(0)
                previous_cases[covid["state"]].append(int(covid["cases"]))
                new_cases[covid["state"]].append(int(covid["cases"]) - previous_cases[covid["state"]][-2])

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        previous_week = round(sum(new_cases[state][0:7]) / 7)
        last_week = round(sum(new_cases[state][7:15]) / 7)
        try:
            average = (previous_week - last_week) / last_week
        except ZeroDivisionError:
            average = 0

        if average >= 0:
            print(f'{state} had a 7-day average of {round(last_week)} and an increase of {round(average * 100)}%.')
        else:
            print(f'{state} had a 7-day average of {round(last_week)} and a decrease of {-(round(average * 100))}%.')

main()
