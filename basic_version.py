# Acknowledgement:
# I co-created this code with the help of ChatGPT (OpenAI GPT-5).
# Numly - 3-Digit Number Guessing Game
# this game is inspired by wordle game, however there are some interesting added features.
#main code: simple game ( win or lose, 1 attempt only)

import random  # to generate a random number

class NumlyGame:
    """A simple 3-digit number guessing game."""

    def __init__(self):
        # computer chooses a random 3-digit number between 100 and 999( our set limit)
        self.secret_number = random.randint(100, 999)

    def play(self):
        print("Welcome to Numly – 3-digit Number Guessing Game!")
        print("Try to guess the number between 100 and 999.")
        print("Type 'exit' anytime to quit the game.\n")

        # code keep asking for guesses until player gets it right or exits
        while True:
            guess = input("Enter your guess: ")

            # check if player wants to exit
            if guess.lower() == "exit":
                print("You quit the game. The number was:", self.secret_number)
                break

            # check if input is a number and has 3 digits
            if not guess.isdigit() or len(guess) != 3:
                print("Please enter a valid 3-digit number.\n")
                continue

            # convert guess to integer
            guess = int(guess)

            # check if guess matches the secret number
            if guess == self.secret_number:
                print(" You guessed it right! You win!")
                break
            else:
                print(" Wrong guess! Try again.\n")

# this part runs the game when the file is executed
if __name__ == "__main__":
    game = NumlyGame()
    game.play()