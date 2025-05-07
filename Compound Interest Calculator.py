# Python Compound Interest Calculator
import time

# Placeholder variables
principle = 0
rate = 0
timee = 0

# ------------------------ START OF CALCULATOR ------------------------
print("************************")
print("PYTHON COMPOUND INTEREST CALCULATOR")
print("************************\n")
time.sleep(2)

# Validates principle amount
while True:
    principle = float(input("Enter the principle amount: ")) # Asks for principle amount
    if principle < 0: # If input is a negative number
        print("Principle cannot be less than 0")
    else: # If input is a positive number
        break

# Validates interest rate
while True:
    rate = float(input("Enter the Interest rate: ")) # Asks for interest amount
    if rate < 0: # If input is a negative number
        print("Interest rate cannot be less than 0") 
    else: # If input is a positive number
        break

# Validates input of years
while True:
    timee = int(input("Enter the time in years: ")) # Asks for time in years
    if timee < 0: # If input is a negative number
        print("Time cannot be less than 0")
    else: #  If input is a positive number
        break

# Display final balance
total = principle * pow(1 + rate / 100, timee)
print(f"Balance afer {timee} year/s is ${total:.2f}")
time.sleep(5)
print("(get yo money up frr)")

