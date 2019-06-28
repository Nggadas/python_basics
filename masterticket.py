TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


def calculate_price(number):
    return (number * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("-" * 50)
    print("There are {} tickets remaining.".format(tickets_remaining))

    name = input("What is your name?: ")

    # Handle potential ValueError
    try:
        number_of_tickets = int(input("Hello {}, how many tickets would you like to purchase?: ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("That's more tickets than what we have available.")
        elif number_of_tickets < 1:
            raise ValueError("You can only purchase at least 1 ticket")
    except ValueError as error:
        print(error)
        print("Invalid input, try again...")
    else:
        cost_of_tickets = calculate_price(number_of_tickets)

        print("{} tickets will cost £{}.".format(number_of_tickets, cost_of_tickets))

        confirm = input("Would you like to proceed? y/n: ")

        if confirm.lower() == "y":
            print("Sold!, thank you for your purchase {}.".format(name))
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you {}, see you next time.".format(name))
            exit()

if tickets_remaining < 1:
    print("Tickets are sold out!")


