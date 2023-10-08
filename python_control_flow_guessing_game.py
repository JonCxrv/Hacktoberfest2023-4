# Python Control Flow Guessing Game

# Import the random library
import random

# Define a list of control flow structures
control_flow_structures = ["if", "elif", "else", "for", "while", "try", "except", "finally"]

# Start the game
while True:
    # Generate a random control flow structure
    structure = random.choice(control_flow_structures)

    # Ask the player to guess the structure
    guess = input("What is the control flow structure? ")

    # Check if the player guessed correctly
    if guess == structure:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", structure)

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    if play_again != "y":
        break
