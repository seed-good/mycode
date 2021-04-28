#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# problem 1
for animal in farms[0].get('agriculture'):
    print(animal)
print()

# problem 2
print("Enter farm name from the following choices:")
print("NE Farm")
print("W Farm")
print("SE Farm")
farm_name = input(">>")
print("You entered: " + farm_name)

for farm in farms:
    if farm["name"].lower() == farm_name.lower():
        for animal in farm["agriculture"]:
            print(animal)
print()

# problem 3
print("Enter farm name from the following choices:")
print("NE Farm")
print("W Farm")
print("SE Farm")
farm_name = input(">>")
print("You entered: " + farm_name)

animal_list = ["sheep", "cows", "pigs", "chickens", "llama", "cats"]
for farm in farms:
    if farm["name"].lower() == farm_name.lower():
        for animal in farm["agriculture"]:
            if animal in animal_list:
                print(animal)

