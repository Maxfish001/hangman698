import random

def select_random_word(word_list):
    """Selects a random word from the given list."""
    return random.choice(word_list)

def prompt_user_for_guess():
    """Prompts the user to enter a single letter."""
    return input("Enter a single letter: ")

def validate_guess(guess):
    """Validates the user's guess."""
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

# List of words for guessing
word_list = ["apple", "grapefruit", "orange", "mango", "passionfruit"]

# Select a random word from the list
word = select_random_word(word_list)
print(word)

# Prompt user to enter a single letter
guess = prompt_user_for_guess()

# Validate the user's guess
validate_guess(guess)
