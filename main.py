from art import logo
import os


def clear_screen():
    """
    Clears the console screen providing a clean and clear display.

    This function detects the operating system to execute the appropriate command to clear the screen.

    """
    os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    """returns the addition of two numbers"""
    return n1 + n2

def substract(n1, n2):
    """returns the subtraction between two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """returns the multiplication of two numbers"""
    return n1 * n2

def divide(n1, n2):
    """returns the the devision between two numbers"""
    return n1 / n2

operations = {"+": add,
              "-": substract,
              "*" : multiply,
              "/" : divide,
             }

def calculator():
    """
    A simple calculator program that allows users to perform basic arithmetic operations.
    Note: This calculator supports only addition (+), subtraction (-), multiplication (*), and division (/) operations.

    """
    
    print(logo)
    num1 = float(input("what's your first number?: "))
    
    should_continue = True
    while should_continue:
        for operation in operations:
            print(operation)
        
        choice = input("pick an operation: ")
        num2 = float(input("whats the next number?: "))
    
        function = operations[choice]
        result = function(num1, num2)
        print(f"{num1} {choice} {num2} = {result}")
    
        if input(f"type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            should_continue = False
    
    clear_screen()
    calculator()
            
calculator()