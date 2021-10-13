from replit import clear
from art import logo

# Add
def add(n1, n2):
    return n1 + n2
# Substract
def substract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbols in operations:
        print(symbols)
    operation = True
    while operation:
        operation_symbols = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculate = operations[operation_symbols]
        result = calculate(num1, num2)
        print(f"{num1}{operation_symbols}{num2} = {result}")
        again = input("Want to calculate the answer? Type 'y' or 'n' to restart the calculation: ").lower()
        if again == "n":
            operation = False
            clear()
            calculator()
        num1 = result

calculator()