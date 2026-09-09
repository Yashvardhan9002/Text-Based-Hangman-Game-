"""A simple text-based Hangman game."""

import random


WORDS = ["python", "planet", "garden", "puzzle", "window","banana","rocket","circus","silver","orange"]
MAX_INCORRECT_GUESSES = 6


def get_guess(guessed_letters):
    """Ask the player for one new alphabetic letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    """Play one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("\nWelcome to Hangman!")
    print(f"You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters) or "None")
        print("Incorrect guesses left:", MAX_INCORRECT_GUESSES - incorrect_guesses)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("That letter is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won! The word was '{word}'.")
            return

    print(f"\nGame over! The word was '{word}'.")


def main():
    """Run games until the player chooses to stop."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
