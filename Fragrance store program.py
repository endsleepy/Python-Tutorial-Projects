# Fragrance store program
from datetime import datetime


perfumes_women = {"Chanel Coco Mademoiselle Eau de Parfum": 135,
                  "Ariana Grande Cloud Eau de Parfum": 65,
                  "Burberry Her Eau de Parfum": 120,}

perfumes_men = {"Dior Sauvage Eau de Toilette": 100,
                "Versace Eros Eau de Toilette": 95,
                "YSL Y Eau de Parfum": 130}

cart = []
total = 0 

def menu(perfume_dict):
        print("------------------MENU------------------  (Prices)")
        for key, value in perfume_dict.items()           :
            print(f"{key:40} : ${value:.2f}")
        print("----------------------------------------")

def select_fragrance(perfume_dict):
    while True:
        fragrance = input("Select an item (q to quit): ").strip()

        if fragrance == "Q" or fragrance == "q":
            break    
        elif perfume_dict.get(fragrance) is not None:
            cart.append(fragrance)
            print(f"{fragrance} added to the cart.")
        else:
            print("Sorry, invalid input. Please try again.")
        
while True:
    print("#############################################")
    print("########## SLEEPY'S FRAGRANCE STORE #########")
    print("#############################################")
    print("")
    gender = input("Are you male or female? (M or F): ").strip().upper()

    if gender == "F":
        print("####################################")
        print("########## WOMEN'S SECTION #########")
        print("####################################")
        print("")
        menu(perfumes_women)
        select_fragrance(perfumes_women)
        break

    elif gender == "M":
        print("##################################")
        print("########## MEN'S SECTION #########")
        print("##################################")
        print("")
        menu(perfumes_men)
        select_fragrance(perfumes_men)
        break

    else:
        print("Invalid input. Please enter M or F.")

current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H-%M:%S")

if not cart:
    print("Your cart is empty")

else:
    for fragrance in cart:
        print("")
        print("###########################")
        print("######### RECEIPT #########")
        print("###########################")
        print("")
        print("--------- YOUR ORDER ---------")
        if fragrance in perfumes_men:        
            total = total + perfumes_men.get(fragrance)
            for perfume in cart:
                print(fragrance)
        elif fragrance in perfumes_women:
            total += perfumes_women.get(fragrance, 0)
            for perfume in cart:
                print(fragrance)

    print("")
    print(f"Date & Time: {formatted_time}")  
    print(f"Total is: ${total:.2f}")

