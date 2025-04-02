# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be less than 0")
    else:
        break

total = principle * pow(1 + rate / 100, time)
print(f"Balance afer {time} year/s: ${total:.2f}")
