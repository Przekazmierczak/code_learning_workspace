months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        date = input("Date: ")
        try:
            standard_date = mm_dd_yyyy_format(date)
        except ValueError:
            try:
                standard_date = monthname_dd_yyyy_format(date)
            except ValueError:
                pass
            else:
                break
        else:
            break
    print(standard_date)


def mm_dd_yyyy_format(date):

    # Check if input is in correct format
    [m, d, y] = date.split("/")

    # Check if all input value are integer (if not raising ValueError)
    int_d = int(d)
    int_m = int(m)
    int_y = int(y)

    # Check input values correctness
    if int_d < 0 or int_d > 31:
        raise ValueError
    elif int_m < 1 or int_m > 12:
        raise ValueError
    elif int_y < 0:
        raise ValueError

    # Format to add "0"
    d = d.rjust(2, '0')
    m = m.rjust(2, '0')
    y = y.rjust(4, '0')

    standard_date = f"{y}-{m}-{d}"
    return(standard_date)

def monthname_dd_yyyy_format(date):

    # Check if input is in correct format
    [m, d, y] = date.split(" ")

    d = d.replace(",", "")

    # Check if d and y are integer (if not raising ValueError)
    int_d = int(d)
    int_y = int(y)

    # Check input values correctness
    if int_d < 0 or int_d > 31:
        raise ValueError
    elif int_y < 0:
        raise ValueError

    if m in months:
        i = 1
        for month in months:
            if month == m:
                m = str(i)
                break
            i += 1
    else:
        raise ValueError

    # Format to add "0"
    d = d.rjust(2, '0')
    m = m.rjust(2, '0')
    y = y.rjust(4, '0')

    standard_date = f"{y}-{m}-{d}"
    return(standard_date)

main()