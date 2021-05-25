#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

#3import urllib.request
#import json
import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""

    helmetson = requests.get(MAJORTOM).json()


    # this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRST astro in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

    # Challange #1
    print(f"Number of people currently in Space: {helmetson['number']}")
    for astro in helmetson["people"]:
        print(f"{astro['name']} on the {astro['craft']}")

if __name__ == "__main__":
    main()

