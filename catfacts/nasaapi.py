#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    ## create r, which is our request object
    r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY')

    data = r.json()
    print(f"There are {data.get('element_count')} asteroids near Earth")
    num_hazard = 0;

    for date in data["near_earth_objects"]:
        for ast in data["near_earth_objects"][date]:
            if ast.get("is_potentially_hazardous_asteroid"):
                num_hazard += 1
    print(f"Of them, {num_hazard} are potentially hazardous!")         


main()

