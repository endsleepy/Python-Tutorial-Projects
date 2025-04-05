
# Takes number from user and operator 
symbol = input("Enter an symbol (+, -, /, *)"  )
num1 = float(input("Enter the first number"  ))
num2 = float(input("Enter the second number"  ))

if symbol == "+":
    print(num1 + num2)
elif symbol == "-":
    print(num1 - num2)
elif symbol == "*":
    print(num1 * num2)
elif symbol == "/":
    print(round(num1 / num2), 2)
else:
    print(f"{symbol} is not an symbol pal")