# weight converter
import time

weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds (K or L): ")

unit = unit.lower()

# Converts KG to Pounds
if unit == "kilograms" or unit == "k": 
    weight = weight * 2.20462
    if weight > 263:
        print(f"DAMN!, You weigh {round(weight)} Lbs?!\nyou reallyy need to loose some weight ngl...")
        print("LIKE FASTTT!!")
    elif weight < 67:
        print(f"Oh...you REALLY need to gain some weight ngl...you weigh {round(weight)} Lbs 🪶🪶🪶")
        time.sleep(2)
        print("Like seriously..")
    else:
        print(f"You weigh {round(weight)} Lbs")

# Converts Pounds to KG
elif unit == "pounds" or unit == "l":
    weight = weight / 2.20462
    if weight > 119:
        print(f"DAMN!, You weigh {round(weight)} Kgs?!\nyou reallyy need to loose some weight ngl...")
        print("LIKE FASST!!")
    elif weight < 31:
        print(f"Oh...you REALLY need to gain some weight ngl...you weigh {round(weight)} Kg 🪶🪶🪶")
        time.sleep(2)
        print("Like seriously..")
    else:
        print(f"You weigh {round(weight)} Kgs")
else:
    print(f"{unit} is invalid I legit just saidd K OR L, not hard.")