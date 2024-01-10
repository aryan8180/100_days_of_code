#Calculator

def add(n1,n2):
    return n1 + n2 

def subtract(n1,n2):
    return n1 - n2 

def multiply(n1,n2):
    return n1 * n2 

def divide(n1,n2):
    return n1 / n2 

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for i in operations:
    print(i)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
ans = calculation_function(num1,num2)
print(ans)

choice = input(f"Type 'y' to continue calculating with {ans}, or n to exit.: ")
while choice == 'y':
    operation_symbol = input("Pick an operation: ")
    calculation_function = operations[operation_symbol]
    new_num = int(input("What's the number?: "))
    ans = calculation_function(ans,new_num)
    print(ans)
    choice = input(f"Type 'y' to continue calculating with {ans}, or n to exit.: ")
print("End.")