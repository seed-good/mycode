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
    good_input = True
    while good_input:
        op1 = input(crayons.red("Please enter the first integer operand: "))
        if op1.isdigit():
            op1 = int(op1)
            good_input = False 

    while True:
        oper = input(crayons.red("Please enter the operator (+, -, *, /, **, %): "))
        if oper in ["+", "-", "*", "/", "**", "%"]:
            break

    while True:
        op2 = input(crayons.red("Please enter the second integer operand: "))
        if op2.isdigit() or op2.isdecimal():
            op2 = int(op2)
            if (oper == "/" or oper == "%") and op2 == 0:
                print(crayons.red("Cannot divide by zero!", bold=True))
            else:
                break

    ## run
    result = calculator(op1, op2, oper) # call function to calc
    print(f"The result is {result}")

# call our main function
main()

