import random

def hangman():
    words = ['india', 'germany', 'america', 'england', 'itaily']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word:")

    while attempts > 0 and '_' in guessed:
        print(" ".join(guessed))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if '_' not in guessed:
        print(f"Congratulations! You guessed it: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()
