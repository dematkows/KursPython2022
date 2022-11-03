# Initial variables
hidden_word = "abracadabra"
# Filling our guessed_word list with '_' characters, so later we can assign correctly guessed letters to it's
# appropriate index.
guessed_word = ["_"] * len(hidden_word)
attempts = len(hidden_word)

print(f"The hidden word has {len(hidden_word)} letters.")
print("You can type 'exit' to quit.")

# User has a limited number of attempts - which equals the length of the hidden_word string.
for attempt in range(attempts):
    attempts_left = attempts - attempt

    print(f"Attempts left: {attempts_left}")
    guessed_letter = input("Give a letter or guess the whole word: ").lower()

    # User can provide any type of input, even nothing at all (Enter). Every option (I guess) is handled by below 'if'
    # statements.
    # 1. When user provides a single character:
    if len(guessed_letter) == 1:
        # User's input is checked whether it's alphabetic or not. If it's not alphabetic, then an info message will be
        # printed and user will just lose one attempt.
        if guessed_letter.isalpha():
            # Checking if the letter that user provided is in hidden word.
            if guessed_letter in hidden_word:
                print(f"Letter '{guessed_letter}' appears {hidden_word.count(guessed_letter)} times!")
                i = 0
                # Add correctly guessed letter to it's appropriate index in guessed_word list, so it can be shown after
                # current attempt.
                # Use Enumerate (?)
                for letter in hidden_word:
                    if guessed_letter == letter:
                        guessed_word[i] = guessed_letter
                    else:
                        pass
                    i += 1
            else:
                print(f"Letter '{guessed_letter}' doesn't appear.")
        else:
            print("Hidden word consists of alphabet letters only. Please provide letters only.")
    # 2. When user doesn't provide input ('Enter' key), user will just lose one attempt.
    elif len(guessed_letter) < 1:
        print("You didn't provide any letter.")
    # 3. User can quit the program typing 'exit' word.
    elif guessed_letter == "exit":
        print("You have quit.")
        exit(0)
    # 4. User can type the whole word to guess the hidden word.
    else:
        if guessed_letter == hidden_word:
            print(f"You guessed the hidden word! It's '{hidden_word}'!")
            exit(0)
        else:
            print("You missed - that's not the hidden word. Try again.")

    # Already guessed letters occurrences of the hidden word are shown after every attempt.
    print("[" + "".join(guessed_word) + "]", "\n")
    # If the user guessed the hidden word successfully by providing the last letter, user wins and the program will end.
    if guessed_word == list(hidden_word):
        print(f"You guessed the hidden word! It's '{hidden_word}'!")
        exit(0)
