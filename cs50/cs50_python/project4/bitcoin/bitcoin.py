import requests
import sys

if len(sys.argv) == 2:
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument need to be a float number")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        except requests.RequestException:
            sys.exit("There is a server issue")
        else:
            price = response["bpi"]["USD"]["rate_float"] * number
            print(f" ${price:,}")
else:
    sys.exit("Missing command-line argument")