# Write your code here
import random
import sys


def card_number_generator():
    client_id = random.randint(100000000, 999999999)
    card_number = "400000" + str(client_id) + "2"
    print(card_number)
    return card_number


def pin_generator():
    card_pin_number = []
    for i in range(4):
        card_pin_number.append(random.randint(0, 9))
    card_pin_number = ''.join(map(str, card_pin_number))
    print(card_pin_number)
    return card_pin_number


bank_accounts = {}

while True:
    print("\n1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    userInput = int(input(">"))
    match userInput:
        case 1:
            print("Your card has been created")
            print("Your card number:")
            client_card_number = card_number_generator()
            print("Your card PIN:")
            client_card_pin_number = pin_generator()
            bank_accounts[client_card_number] = client_card_pin_number
        case 2:
            print("Enter your card number:")
            login_card_number = input(">")
            print("Enter your PIN:")
            login_card_pin_number = input(">")
            if login_card_number in bank_accounts and bank_accounts[login_card_number] == login_card_pin_number:
                print("You have successfully logged in!")
                while True:
                    print("\n1. Balance")
                    print("2. Log out")
                    print("0. Exit")
                    logged_user_input = int(input(">"))
                    match logged_user_input:
                        case 1:
                            print("Balance: 0")
                        case 2:
                            print("You have successfully logged out!")
                            break
                        case 0:
                            print("Bye!")
                            sys.exit()
                        case _:
                            print("Invalid input! Try again.")
            else:
                print("Wrong card number or PIN!")
        case 0:
            print("Bye!")
            break
        case _:
            print("Invalid input! Try again.")
