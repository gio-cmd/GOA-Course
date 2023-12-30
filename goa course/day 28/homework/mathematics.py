import math 
x = int(input("Choose a number: "))
y = int(input("Choose 2nd number: "))
symbol = input("Choose one of the operations: (/,+,-,*)")
if symbol == "+":
    print(x + y) 
elif symbol == "-":
    print(x - y)
elif symbol == "*":
    print(x * y) 
elif symbol == "/":
    print(x / y)
else:
    print("Invalid operation selected")  