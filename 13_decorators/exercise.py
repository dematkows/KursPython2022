from random import choice


# Napisz dekorator stars zmieniający sposób wyświetlania cytatu
# na taki: 
# 
# ********************************* 
#             cytat 
# *********************************
def stars_decorator(func_param):
    def print_stars():
        quote = func_param()
        stars = "*" * 50
        text = stars + '\n' + quote.center(len(stars)) + '\n' + stars
        return text

    return print_stars


@stars_decorator
def get_quote():
    quotes = [
        "Be or not to be",
        "Life is a long lesson in humility.",
        "Whatever you are, be a good one",
        "Be yourself; everyone else is already taken.",
        "Happiness depends upon ourselves."
    ]
    return choice(quotes)


def main():
    print(get_quote())


if __name__ == "__main__":
    main()
