#!/usr/bin/env python3

import json

ali = {"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},"contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},"favorites":{"number":10,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},"drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}} 

ali_fav_drinks = []
ali_num_wins = 0

# get list of nonadult drinks
nonadult_drinks = ali.get("favorites").get("drink").get("nonadult")
for drink in nonadult_drinks:
    ali_fav_drinks.append(drink)

# get number of wins
ali_num_wins = ali.get("favorites").get("number")

# Now advertise his fav drinks
count = 0
while count < ali_num_wins:
    for drink in ali_fav_drinks:
        print(f"Muhammad Ali's favorite drinks were : {drink}", sep=" ")
    count = count + 1    

