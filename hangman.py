import random

WORDS = ["python", "computer", "program", "developer", "algorithm"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word. You can make up to {MAX_WRONG_GUESSES} wrong guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print("\nWord:", display)
        print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
