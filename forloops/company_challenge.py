#!/usr/bin/env python3

fruitcompanies= [{"name":"Zesty","employees":["Ajay","Ashfaq","Bob","Brian","Chad F.", "Chad H."]},
                 {"name":"Ripe.ly","employees":["Eric","Gibran", "Chad","Idris","Juan","Julian"]},
                 {"name":"FruitBee","employees":["Kulwinder","Lalit","Chad","Michael","Milford","Scott"]},
                 {"name":"JuiceGrove","employees":["Chad","Srini","Srinivasa","Vasanti","Vimal"]}]


# problem 1
def prob1():
    for element in fruitcompanies:
        for name in element.get('employees'):
            #print(name)
            if name.strip() == "Vasanti":
                print(f"You work for {element.get('name')}")
                break

# problem 2
def prob2():
    comp_name=input("Enter Company name: ")
    for element in fruitcompanies:
        if comp_name.strip().lower() == element.get('name').lower():
            print(f"Employees working for {comp_name} are:")
            for i in element.get('employees'):
                print(i)

# problem 3
def prob3():
    print("Enter farm name from the following choices:")

def main():
    prob1()
    prob2()

main()    
