import random

words = ["ayesha", "computer", "codealpha", "hangman", "coding"]

def display_word(word, guessed_letters):
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)

def hangman():
    word = random.choice(words)
    guessed_letters = []  # LIST use ho raha hai
    wrong_guesses = []    # LIST for wrong ones
    max_wrong = 6

    print("=== HANGMAN GAME ===")

    while len(wrong_guesses) < max_wrong:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}")
        print(f"Remaining chances: {max_wrong - len(wrong_guesses)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter only!")
            continue

        if guess in guessed_letters:
            print("Already tried this letter!")
            continue

        guessed_letters.append(guess)  # list.append()

        if guess in word:
            print("Correct!")
            # Check win condition
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 YOU WIN! The word was: {word}")
                return
        else:
            wrong_guesses.append(guess)  # list.append()
            print(f"Wrong! {len(wrong_guesses)}/{max_wrong}")

    print(f"\nGAME OVER! The word was: {word}")

hangman()
