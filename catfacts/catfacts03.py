#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import random

def main():
    facts = [] 
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    for catfact in r.json():
        facts.append(catfact.get("text"))

    try:
        print(f"Here's a fun cat fact for you: {random.choice(facts)}") 
    except IndexError:
        print("Sorry, you're out of luck today!")


main()

