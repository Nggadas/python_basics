import sys

MASTER_PASSWORD = "secret"

password = input("Enter the secret password: ")
attempts = 1

while password != MASTER_PASSWORD:
    if attempts > 3:
        sys.exit("Too many invalid attempts")

    password = input("Wrong password, try again: ")
    attempts += 1


print("Welcome aboard!")
