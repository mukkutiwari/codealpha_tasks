import random

# list of 5 simple words
words = ["apple", "tiger", "house", "plant", "chair"]

# choose one random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")
print("You have 6 wrong attempts.")

while wrong_guesses < max_wrong:
    display_word = ""

    # show guessed letters and _ for missing letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # check if player already won
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    # check valid input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1
        print("Remaining attempts:", max_wrong - wrong_guesses)

# if player loses
if wrong_guesses == max_wrong:
    print("\nGame Over! The word was:", word)