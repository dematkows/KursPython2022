# Napisz program, który na podstawie numeru karty odpowie czy ma do czynienia z Visą, MasterCard, a może AmericanExpress
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16
# digits. American Express card numbers start with 34 or 37 and have 15 digits.


def check_card_number(number):
    if number.isnumeric() and 12 < len(number) < 17:
        print("Provided card number is valid.")
        return True
    else:
        print("Provided card number is invalid (is not only digits or has less than 13 or more than 16 digits).")
        return False


def is_visa(number):
    return True if number[0] == '4' and len(number) in [13, 16] else False

    # if card_number[0] == '4' and len(card_number) in [13, 16]:
    #     print("This is a Visa card.")
    #     return True
    # else:
    #     return False


def is_mastercard(number):
    return True if len(number) == 16 and (51 <= int(number[0:2]) <= 55
                                               or 2221 <= int(number[0:4]) <= 2720) else False

    # if len(card_number) == 16 and (51 <= int(card_number[0:2]) <= 55 or 2221 <= int(card_number[0:4]) <= 2720):
    #     print("This is a MasterCard card.")
    #     return True
    # else:
    #     return False


def is_american_express(number):
    return True if len(number) == 15 and number[0:2] in ['34', '37'] else False

    # if len(card_number) == 15 and card_number[0:2] in ['34', '37']:
    #     print("This is a American Express card.")
    #     return True
    # else:
    #     print("This is an Unknown card.")
    #     return False


def main():
    card_number = input("Provide a card_number: ")

    if check_card_number(card_number):
        # czy jest Visa
        if is_visa(card_number):
            print("This is a Visa card.")
        # czy jest MasterCard
        elif is_mastercard(card_number):
            print("This is a MasterCard card.")
        # czy jest American Express
        elif is_american_express(card_number):
            print("This is a American Express card.")
        else:
            print("This is an Unknown card.")


# --- main ---
main()
