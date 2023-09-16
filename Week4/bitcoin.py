import json
import requests
import sys
try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    s=float(sys.argv[1])
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    o = response.json()
    USD_value = o['bpi']['USD']["rate_float"]
    print(f"${USD_value*s:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number ")

except requests.RequestException:
    pass