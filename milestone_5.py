import random

class Hangman:
    def __init__(self):
        self.word_list = ["apple", "grapefruit", "orange", "mango", "passionfruit"]
        self.word = random.choice(self.word_list)
        print("Secret word:", self.word)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5  # Initialize num_lives to 5
        self.list_of_guesses = []

    def check_guess(self, guess):
        lowercase_guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{lowercase_guess}' is in the word.")
            self.update_word_guessed(guess)
        else: 
            print(f"Sorry, '{lowercase_guess}' is not in the word.")
            self.num_lives -= 1  # Decrease num_lives when the guess is incorrect
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

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

def play_game():
    game = Hangman()  # Create an instance of the Hangman class
    
    # Create a while loop and set the condition to True
    while True:
        # Check if the num_lives is 0
        if game.num_lives == 0:
            print('You lost!')
            break
        # Check if all letters have been guessed
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        else:
            game.ask_for_input()  # Call the ask_for_input method

# Call the play_game function to start the game
play_game()
