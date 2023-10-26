# Write your code here
import random


def card_number_generator():
    client_id = random.randint(100000000, 999999999)
    card_number = "400000" + str(client_id) + "2"
    print(card_number)


def pin_generator():
    print(random.randint(1000, 9999))


while True:
    print("\n1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    userInput = int(input(">"))
    match userInput:
        case 1:
            print("Your card has been created")
            print("Your card number:")
            card_number_generator()
            print("Your card PIN:")
            pin_generator()

        case 2:
            pass
        case 0:
            print("Bye!")
            break
        case _:
            print("Invalid input! Try again.")
            continue
