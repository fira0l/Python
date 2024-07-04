from art import logo
print(logo)

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

num1 = int(input("What is the first Number?: "))
for keys in operations:
    print(keys)
operation_symbol = input("Pick an operaton from the line above: ")
num2 = int(input("What is the second Number?: "))

first_answer = operations[operation_symbol](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next Number?: "))
calculation_function= operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2),num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
