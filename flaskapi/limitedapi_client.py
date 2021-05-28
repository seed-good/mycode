#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

import requests

## Define URL
LIMITED_API = "http://10.3.60.226:2224/fast"

def main():
    """runtime code"""

    ## Call the webservice 200 times

    for i in range(200):
        resp = requests.get(LIMITED_API)
        print(resp)

if __name__ == "__main__":
    main()

