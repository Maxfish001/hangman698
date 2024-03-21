import random

# List of words for guessing
word_list = ["apple", "grapefruit", "orange", "mango", "passionfruit"]

# Select a random word from the list
word = random.choice(word_list)
print("Secret word:", word)


def check_guess(guess):
    lowercase_guess = guess.lower()

    # Check if the guess is in the word
    if guess in word:
        # Step 2: Print a message if the guess is in the word
        print(f"Good guess! '{lowercase_guess}' is in the word.")
    else:
        # Step 3: Print a message if the guess is not in the word
        print(f"Sorry, '{lowercase_guess}' is not in the word. Try again.")


def ask_for_input():
    # Step 1: Create a while loop
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Step 3: Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 4: If the guess passes the checks, break out of the loop
            break
        else:
            # Step 5: If the guess does not pass the checks, print a message
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)


ask_for_input()