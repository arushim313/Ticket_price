### Determine the ticket price based on age ###

run_app = "Y"

while run_app == "Y":
    print("Hello and welcome to ticket price generator for the concert!")
    age = int(input("Enter the age: "))
    print(f"Your age is {age}.")

    if age <= 5:
        price = 0
        print("The price for your ticket is $0!")
    elif age >5 and age <=15:
        price = 15
        print("The price of your ticket is $15")
    elif age > 15 and age <=30:
        price = 30
        print("The price of your ticket is $30")
    elif age > 30 and age <= 60:
        price = 100
        print("The price of your ticket is $100")
    else:
        price = 50
        print("The price of your ticket is $50")

    num_tickets = int(input("How many tickets do you want?: "))

    price_f = price*num_tickets
    print(f"Your final price for all tickets is ${price_f}!")

    run_app = input("Do you want to run the price generator again? Y/N: ")
