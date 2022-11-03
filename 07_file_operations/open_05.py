# 5. Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.


def get_words():
    filename = "book.txt"
    with open(filename, encoding="utf-8") as file:
        content = file.read().split()
    return content


def get_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def main():
    word_list = get_words()
    print(get_longest_word(word_list))


main()
