"""
Hangman Game
------------
A simple text-based Hangman game.

Key Concepts Used: random, while loop, if-else, strings, lists
"""

import random

WORDS = [
    "python", "hangman", "computer", "keyboard", "science", "world",
    "programming", "algorithm", "function", "variable", "loop", "condition",
    "string", "integer", "boolean", "list", "dictionary", "tuple", "set",
    "exception", "module", "package", "library", "framework", "object",
    "class", "method", "inheritance", "polymorphism", "encapsulation",
    "abstraction", "Claude", "AI", "machine", "learning", "data", "analysis",
    "visualization", "statistics", "probability", "regression",
    "classification", "clustering", "neural", "network", "deep",
    "reinforcement", "natural", "language", "processing", "ChatGPT",
    "Gemini", "Bing", "Google", "OpenAI", "Microsoft", "Apple", "Amazon",
    "Facebook", "Twitter", "Instagram", "Snapchat", "TikTok", "YouTube",
    "Reddit", "LinkedIn", "Pinterest", "WhatsApp", "Telegram", "Signal",
    "Discord", "Slack", "Saad", "Muhammad", "Asad", "Ali", "Hassan",
    "Ahmed", "Khan", "Nawaz", "Rashid", "Farooq", "Javed", "Saeed",
    "Zahid", "Imran", "Shahid", "Faisal", "Bilal", "Usman", "Ahsan",
    "Tariq", "Waseem", "Jarrar", "Hifza",
]
MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


def play_hangman():
    original_word = random.choice(WORDS)
    word = original_word.lower()   # case-insensitive matching for guesses
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("Welcome to Hangman!")
    print(f"You have {attempts_left} incorrect guesses allowed.\n")

    while attempts_left > 0:
        current_display = display_word(word, guessed_letters)
        print(current_display)

        # Win condition
        if "_" not in current_display:
            print("\nCongratulations! You guessed the word:", original_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            attempts_left -= 1
            print(f"Wrong! Attempts left: {attempts_left}\n")

    if attempts_left == 0:
        print(f"\nGame Over! The word was: {original_word}")


if __name__ == "__main__":
    play_hangman()