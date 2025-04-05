# Python Compound Interest Calculator
import time

principle = 0
rate = 0
timee = 0


print("************************")
print("PYTHON COMPOUND INTEREST CALCULATOR")
print("************************\n")
time.sleep(2)

# Validates principle amount
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than 0")
    else:
        break

# Validates intereset rate
while True:
    rate = float(input("Enter the Interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than 0")
    else:
        break

# Validates input of years
while True:
    timee = int(input("Enter the time in years: "))
    if timee < 0:
        print("Time cannot be less than 0")
    else:
        break

# Calculates money after interest and years
total = principle * pow(1 + rate / 100, timee)
print(f"Balance afer {timee} year/s is ${total:.2f}")
time.sleep(5)
print("(get yo money up frr)")

