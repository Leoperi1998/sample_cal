# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:26:13 2023

@author: STZ
"""

def operator_cal(num1, num2, operator):
    if operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print('The result is undefined')
            return None
        result = num1 / num2
    elif operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "^":
        result = num1 ** num2
    elif operator == "%":
        result = num1 % num2
    else:
        print('Corresponding input operator is wrong')
        return None

    return round(result, 3)


def select_op(choice):
    if choice == '#':
        print('Terminating')
        exit()
    elif choice == '$':
        return -1
    else:
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        result = operator_cal(num1, num2, choice)
        print("Corresponding result:", result)


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    select_op(choice)
