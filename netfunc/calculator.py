#!/usr/bin/env python3
"""Stellantis || Author: vasanti.seed@stellantis.com"""

import crayons

# function to calculate
def calculator(first_operand, second_operand, operator): 
    print('Attempting to calculate --> ' + crayons.blue(first_operand)  + 
                   " " +  crayons.blue(operator) + 
                   " " +  crayons.blue(second_operand))  
    if operator == "+":
        return first_operand + second_operand
    elif operator == "-":
        return first_operand - second_operand
    elif operator == "*":
        return first_operand * second_operand
    elif operator == "/":
        if second_operand != 0:
            return first_operand / second_operand
        else:
            return "ERROR!"
    elif operator == "**":
        return first_operand ** second_operand
    elif operator == "%":
        return first_operand % second_operand


# start our main script
def main():

    ## get data set
    print(crayons.red("WELCOME TO THE PYTHON CALCULATOR!", bold=True))
    print()
    while True:
        op1 = input(crayons.red("Please enter the first operand: "))
        try:
            op1 = float(op1)
            break
        except ValueError:
            print(crayons.red("That's not a number! Try again!", bold-True))

    while True:
        oper = input(crayons.red("Please enter the operator (+, -, *, /, **, %): "))
        if oper in ["+", "-", "*", "/", "**", "%"]:
            break

    while True:
        op2 = input(crayons.red("Please enter the second operand: "))
        try:
            op2 = float(op2)
            if (oper == "/" or oper == "%") and op2 == 0:
                print(crayons.red("Cannot divide by zero!", bold=True))
            else:
                break
        except ValueError:
            print(crayons.red("That is not a number! Try again!", bold= True))

    ## run
    result = calculator(op1, op2, oper) # call function to calc
    print(f"The result is {result}")

# call our main function
main()

