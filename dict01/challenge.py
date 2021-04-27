#!/usr/bin/env python3

#create dict
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

char_name=input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ").lower()

char_stat=input("What statistic do you want to know about? (real name, powers, archenemy) ").lower()

print(f"{char_name.title()}'s {char_stat} is {heroes[char_name].get(char_stat,'Sorry, that is not a valid stat name!')}")

