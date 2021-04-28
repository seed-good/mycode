#!/usr/bin/env python3

quiz = [{"Pick a Movie": ["The Parent Trap", "The Silence of the Lambs", "Mean Girls", "The Wolf of Wall Street", "Eternal Sunshine of the Spotless Mind", "The King's Speach"]},
        {"Which Object do you most desire?": ["The Elder Wand", "The Philosopher's Stone", "The Mirror of Erised", "A Firebolt", "The Marauder's Map", "A Deluminator"]},
        {"What is your favorite food?": ["Shepherd's Pie", "Chicken Wings", "Chocolate Eclair", "Steak Tartare", "Salad", "Cheese"]},
        {"Pick a Drink": ["Gin and Tonic", "Tea", "Pimm's", "Beer", "Bloody Mary", "Milk"]},
        {"Pick a Song": ["Get Lucky - Daft Punk", "Flawless - Beyonce", "Stairway to Heaven - Led Zeppelin", "Mr Tambourine Man - Bob Dylan", "Slim Shady - Eminem", "I Will Always Love You - W. Houston"]},
        {"Where would you like to hang out?": ["The Three Broomsticks", "Madam Puddifoot's Tea Shop", "Borgin and Burkes", "Quality Quidditch Supplies", "Weasley's Wizard Wheezes", "Shrieking Shack"]}
        ]

characters = ["Harry Potter", "Hermione", "Ron Weasley", "Luna Lovegood", "Lord Voldemort", "Sirius Black", "Neville Longbottom"]

hp = 0
herm = 0
ron = 0
luna = 0
vold = 0
sirius = 0
neville = 0

def calc_score(q_num, ans_choice):
    global hp 
    global herm 
    global ron 
    global luna
    global vold 
    global sirius
    global neville 
    if q_num == 1:
       if ans_choice == 1:
           hp = hp + 1
       elif ans_choice == 2:
           herm = herm + 1
       elif ans_choice == 3:
           ron = ron + 1
       elif ans_choice == 4:
           luna = luna + 1
       elif ans_choice == 5:
           sirius = sirius + 1
       else:
           neville = neville + 1
    if q_num == 2:
       if ans_choice == 6:
           hp = hp + 1
       elif ans_choice == 5:
           herm = herm + 1
       elif ans_choice == 2:
           ron = ron + 1
       elif ans_choice == 1:
           luna = luna + 1
       elif ans_choice == 4:
           sirius = sirius + 1
       else:
           neville = neville + 1
    if q_num == 3:
       if ans_choice == 2:
           hp = hp + 1
       elif ans_choice == 3:
           herm = herm + 1
       elif ans_choice == 6:
           ron = ron + 1
       elif ans_choice == 5:
           luna = luna + 1
       elif ans_choice == 1:
           sirius = sirius + 1
       else:
           neville = neville + 1           
    if q_num == 4:
       if ans_choice == 1:
           hp = hp + 1
       elif ans_choice == 6:
           herm = herm + 1
       elif ans_choice == 5:
           ron = ron + 1
       elif ans_choice == 2:
           luna = luna + 1
       elif ans_choice == 4:
           sirius = sirius + 1
       else:
           neville = neville + 1   
    if q_num == 5:
       if ans_choice == 6:
           hp = hp + 1
       elif ans_choice == 1:
           herm = herm + 1
       elif ans_choice == 2:
           ron = ron + 1
       elif ans_choice == 5:
           luna = luna + 1
       elif ans_choice == 4:
           sirius = sirius + 1
       else:
           neville = neville + 1
    if q_num == 6:
       if ans_choice == 2:
           hp = hp + 1
       elif ans_choice == 6:
           herm = herm + 1
       elif ans_choice == 3:
           ron = ron + 1
       elif ans_choice == 5:
           luna = luna + 1
       elif ans_choice == 1:
           sirius = sirius + 1
       else:
           neville = neville + 1

print("Want to know which Harry Potter character you are?")
print("Pick an answer choice for each of the following questions:\n")

for i, element in enumerate(quiz):
    for question in element.keys():
        print("   ")
        print(question)
        print("  ")
        for item in element.values():
            num = 0
            for choices in item:
                num = num + 1
                print(f"{num}: {choices}")
            answer = "0" 
            while int(answer) > num or int(answer) < 1:
                answer = input(">>")
                if not answer.isdigit():
                    answer = 0
            answer_choice = int(answer) 
            calc_score(i, answer_choice)

# Find out which character has the highest score
scores = [hp, herm, ron, luna, sirius, neville]
#print(scores)
max = scores[0]
character_index = 0
for i, character_score in enumerate(scores):
    if character_score > max:
        max = character_score
        character_index = i
print(f"\n\nYou are {characters[character_index]}!!!")

