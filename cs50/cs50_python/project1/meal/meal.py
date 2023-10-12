def main():
    # User input
    time = input("What time is it? ")
    # Convert time to float
    time = convert(time)
    # Check if its meal time
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")

def convert(time):
    # Check the format
    if time.endswith("p.m."):
        time = time.replace(" p.m.", "")
        format = "p.m."
    elif time.endswith("a.m."):
        time = time.replace(" a.m.", "")
        format = "a.m."
    else:
        format = "24h"
    # Conver time to float
    [h, m] = time.split(":")
    if format == "a.m." or format == "24h":
        h = float(h)
    # Change p.m. into 24h float
    elif format == "p.m.":
        h = float(h) + 12
    m = float(m)
    m = m/60
    time = h + m
    return time

if __name__ == "__main__":
    main()