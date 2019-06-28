import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than one person is required to split the check")

    return math.ceil(total / number_of_people)


try:
    total_due = float(input("What is the total?: "))
    if total_due <= 0:
        raise ValueError("Total amount due must be more than zero")

    no_of_people = int(input("How many people?: "))
    amount_due = split_check(total_due, no_of_people)
except ValueError as error:
    print("That's not a valid value. Try again...")
    print("Error Message: {}".format(error))
else:
    print("Each person owes £{}".format(amount_due))
