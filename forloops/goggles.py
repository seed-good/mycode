#!/ust/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

quote = "My {eyes}! the {goggles} do {nothing)!"

for item in challenge:
    if type(item) == str:
        if item == "nothing":
##            print("found the nothing in challenge")
            nothing = item
    if type(item) == list:
        for i in item:
            if i == "eyes":
#                print("found the eyes in challenge")
                eyes = i
            elif i == "goggles":
#                print("found the goggles in challenge")
                goggles = i
print(f"My {eyes}! the {goggles} do {nothing}!")

# second 
for item in trial:
    if type(item) == str:
        if item == "nothing":
            nothing = item
    if type(item) == dict:
        goggles = item["eyes"]
        eyes = item["goggles"]

print(f"My {eyes}! the {goggles} do {nothing}!")

eyes= nightmare[0]['user']['name']['first']
goggles= nightmare[0]['kumquat']
nothing= nightmare[0]['d']
print(f'My {nightmare[0]["user"]["name"]["first"]}! The {nightmare[0]["kumquat"]} do {nightmare[0]["d"]}!')
