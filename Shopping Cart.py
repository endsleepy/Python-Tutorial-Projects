# Shopping cart program

def book_cart():
    books = []
    prices = []
    total = 0

    while True:
        print("****************************************")
        book = input("Enter the book you would like to buy 📚\n(q to quit) ").lower()
        if book == "q":
            print("****************************************")
            break
        else:
            price = float(input(f"Enter the price of {book}: £"))
            books.append(book)
            prices.append(price)    

    print("\n")
    print("************* YOUR CART 🛒*************")

    for book in books:
        print(book, end=" ")

    for price in prices:
        total += price

    print(f"\nYour total is: £{total:.2f}")

book_cart()