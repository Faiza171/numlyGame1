# Acknowledgement:
# I co-created this code with the help of ChatGPT (OpenAI GPT-5).
# Numly - 3-Digit Number Guessing Game
# Features included:
# 1. Limited guesses (5 attempts)
# 2. Feedback system (P/M/X)
# 3. Scoring system (100 points - 10 per wrong guess)
# 4. 2 player mode 

import random


class NumlyGame:
    """3-digit number guessing game with limited guesses, feedback, scoring, and optional two-player mode."""

    def __init__(self):
        self.secret_number = random.randint(100, 999)

    def play(self, two_player=False):
        MAX_ATTEMPTS = 5

        # Single-player variables
        attempts = 0
        score = 100

        # Two-player variables
        if two_player:
            attempts_p1 = 0
            attempts_p2 = 0
            score_p1 = 100
            score_p2 = 100

        print("Welcome to Numly – 3-digit Number Guessing Game!")
        print("Try to guess the number between 100 and 999.")
        print("Type 'exit' anytime to quit the game.")
        print("max number of attempts= 5")
        print("P = perfect in position and number, M = correct number but wrong position, X = number not present\n")

        if two_player:
            print("Two-Player Mode Activated! Players alternate turns.\n")

        while True:
            # Determine current player
            if two_player:
                current_player = 1 if (attempts_p1 + attempts_p2) % 2 == 0 else 2
                attempts = attempts_p1 if current_player == 1 else attempts_p2
                score = score_p1 if current_player == 1 else score_p2
                print(f"Player {current_player}'s turn (Attempt {attempts + 1}/{MAX_ATTEMPTS}):")
            else:
                current_player = 1
                # attempts and score already defined

            # Get player input
            guess = input("Enter your guess: ")

            # Exit handling
            if guess.lower() == "exit":
                print("Game ended by player. The number was:", self.secret_number)
                if two_player:
                    print(f"Player 1 score: {score_p1}, Player 2 score: {score_p2}")
                else:
                    print(f"Your final score: {score}")
                break

            # Validate input
            if not guess.isdigit() or len(guess) != 3:
                print("Please enter a valid 3-digit number.\n")
                attempts += 1
            else:
                guess = int(guess)
                attempts += 1
                # Deduct points for wrong guess
                if guess != self.secret_number:
                    score -= 10
                    if score < 0:
                        score = 0

            # Update attempts and score per player
            if two_player:
                if current_player == 1:
                    attempts_p1 = attempts
                    score_p1 = score
                else:
                    attempts_p2 = attempts
                    score_p2 = score
            else:
                # single-player
                pass  # already using attempts and score

            # Correct guess
            if guess == self.secret_number:
                if two_player:
                    print(f" Player {current_player} guessed it right! Wins!")
                    print(f"Final Scores - Player 1: {score_p1}, Player 2: {score_p2}")
                else:
                    print(" You guessed it right! You win!")
                    print(f"Your final score: {score}")
                break

            # Feedback system
            if guess != self.secret_number:
                guess_str = str(guess)
                secret_str = str(self.secret_number)
                feedback = ""
                for i in range(3):
                    if guess_str[i] == secret_str[i]:
                        feedback += "P"
                    elif guess_str[i] in secret_str:
                        feedback += "M"
                    else:
                        feedback += "X"

                print(f"Feedback for Player {current_player}: {feedback}")
                print("❌ Wrong guess! Try again.\n")

            # Check max attempts
            if two_player:
                if attempts_p1 >= MAX_ATTEMPTS and attempts_p2 >= MAX_ATTEMPTS:
                    print("Maximum attempts reached for both players!")
                    print(f"The number was: {self.secret_number}")
                    print(f"Final Scores - Player 1: {score_p1}, Player 2: {score_p2}")
                    if score_p1 > score_p2:
                        print("Player 1 wins!")
                    elif score_p2 > score_p1:
                        print("Player 2 wins!")
                    else:
                        print("It's a tie!")
                    break
            else:
                if attempts >= MAX_ATTEMPTS:
                    print(f"Maximum attempts reached! The number was: {self.secret_number}")
                    print(f"Your final score: {score}")
                    break


# -------------------------------
# START THE GAME
# -------------------------------
mode = input("Enter number of players (1 or 2): ").strip()
if mode == "2":
    game = NumlyGame()
    game.play(two_player=True)
else:
    game = NumlyGame()
    game.play(two_player=False)