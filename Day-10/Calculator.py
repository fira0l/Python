from art import logo
import os
print(logo)

def clear():
    os.system('cls')

def add(n1,n2):
    """Returns the Sum of Two Numbers provided in the parameters"""
    return n1+n2
def subtract(n1,n2):
    """Returns the difference of the two numbers provided in the parameters"""
    return n1 - n2
def multiply(n1,n2):
    """Returns the product of the two numbers provided in the parameters"""
    return n1*n2
def division(n1,n2):
    """Returns the Division of the two numbers provided in the parameters"""
    if n2 == 0:
        return "Are u Dumb u cant divide a number with 0 change it!"
    else:
        return n1/n2
    
operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':division
}

def calculator():
    """THis function is used to calculate and handle the calculation logic"""

    num1 = float(input("What is the first Number?: "))
    for keys in operations:
        print(keys)
    end_of_calculation = False

        

    while not end_of_calculation: 
        operation_symbol = input("Pick an operaton from the line above: ")
        num2 = float(input("What is the other Number?: "))
        first_answer = operations[operation_symbol](num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        
        if input(f"Type 'y to continue calculating with {first_answer}, or Type 'n' to start a new calculation : ")=='y':
            num1 = first_answer
        else:
            end_of_calculation = True
            clear()
            calculator()

calculator()