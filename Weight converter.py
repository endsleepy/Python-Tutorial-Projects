# weight converter

weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds (K or L): ")

unit = unit.lower()

if unit == "kilograms" or unit == "k": 
    weight = weight * 2.20462
    print(f"You weigh {round(weight, 1)} Lbs")
elif unit == "pounds" or unit == "l":
    weight = weight / 2.20462
    print(f"You weigh {round(weight)} Kgs")
else:
    print(f"{unit} is invalid")