

operator = input("Enter an operator (+, -, /, *)"  )
num1 = float(input("Enter the first number"  ))
num2 = float(input("Enter the second number"  ))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(round(num1 / num2), 2)
else:
    print(f"{operator}is not an operator pal")