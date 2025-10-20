#  Hangman Game
import random
def hangman():
    words = ["apple", "banana", "grape", "mango", "orange"]
    word = random.choice(words)
    guessed = ""
    tries = 6
    print("Welcome to Hangman!")
    print("Guess the word. It has", len(word), "letters.")
    while tries > 0:
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"
        print("Word:", display)

        if display == word:
            print("🎉 You guessed it! The word was:", word)
            break
        guess = input("Enter a letter: ").lower()
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        guessed += guess
        if guess not in word:
            tries -= 1
            print("Wrong! Attempts left:", tries)
    if tries == 0:
        print(" Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()