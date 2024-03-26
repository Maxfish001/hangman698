import random

# List of words for guessing
WORD_LIST = ["apple", "grapefruit", "orange", "mango", "passionfruit"]

def select_random_word():
    """Selects a random word from the list of words."""
    return random.choice(WORD_LIST)

def check_guess(word, guess):
    """Checks if the guess is in the word and prints a corresponding message."""
    lowercase_guess = guess.lower()
    if guess in word:
        print(f"Good guess! '{lowercase_guess}' is in the word.")
    else:
        print(f"Sorry, '{lowercase_guess}' is not in the word. Try again.")

def ask_for_letter():
    """Prompts the user to guess a letter."""
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return guess

def play_hangman():
    """Main function to play the Hangman game."""
    secret_word = select_random_word()
    print("Secret word:", secret_word)
    guess = ask_for_letter()
    check_guess(secret_word, guess)

play_hangman()
