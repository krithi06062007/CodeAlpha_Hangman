import random

# 5 predefined words
words = ["python", "computer", "school", "flower", "program"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Wrong guess count
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses.")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check whether the complete word is guessed
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)
