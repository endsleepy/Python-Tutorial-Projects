# Fragrance store program

perfumes_women = {"Chanel Coco Mademoiselle Eau de Parfum": 135,
                  "Ariana Grande Cloud Eau de Parfum": 65,
                  "Burberry Her Eau de Parfum": 120,}

perfumes_men = {"Dior Sauvage Eau de Toilette": 100,
                "Versace Eros Eau de Toilette": 95,
                "YSL Y Eau de Parfum": 130}

cart = []
total = 0 

while True:

    gender = input("Are you male or female? (M or F): ").capitalize()

    if gender == "F":
        
        print("----------MENU----------        (Prices)")
        for key, value in perfumes_women.items():
            print(f"{key:30} : ${value:.2f}")
        print("------------------------------")

        while True:
            fragrance = input("Select an item (q to quit): ")

            if fragrance == "Q" or fragrance == "q":
                break    
            elif perfumes_women.get(fragrance) is not None:
                cart.append(fragrance)
            else:
                print("a")
                continue

    elif gender == "M":

        print("----------MENU----------        (Prices)")
        for key, value in perfumes_men.items():
            print(f"{key:30} : ${value:.2f}")
        print("------------------------------")

        while True:
            fragrance = input("Select an item (q to quit): ")

            if fragrance == "Q" or fragrance == "q":
                break    
            elif perfumes_men.get(fragrance) is not None:
                cart.append(fragrance)
            else:
                print("a")
                continue
        
        for fragrance in cart:
            total = total + perfumes_men.get(fragrance)
            print(fragrance, end=" ")
        
        print()
        print(f"Total is: ${total:.2f}")

