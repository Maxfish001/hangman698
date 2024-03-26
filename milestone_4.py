import random

class Hangman:
    def __init__(self):
        # List of words for guessing
        self.word_list = ["apple", "grapefruit", "orange", "mango", "passionfruit"]
        # Select a random word from the list
        self.word = random.choice(self.word_list)
        print("Secret word:", self.word)
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(set(self.word))  # Number of unique letters in the word
        self.list_of_guesses = []

    def check_guess(self, guess):
        lowercase_guess = guess.lower()  # Convert the guessed letter to lower case
        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! '{lowercase_guess}' is in the word.")
            # Loop through each letter in the word
            for i in range(len(self.word)):
                # Check if the letter is equal to the guess
                if self.word[i] == guess:
                    # Replace the corresponding "_" in the word_guessed with the guess
                    self.word_guessed[i] = guess
            # Reduce the variable num_letters by 1
            self.num_letters -= 1
        else: 
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            lowercase_guess = guess.lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif lowercase_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(lowercase_guess)
                break

# Testing the code
hangman_game = Hangman()
hangman_game.ask_for_input()