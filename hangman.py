# hangman.py
import random
from hangman_art import HANGMAN_PICS

def load_words(filename):
    """Load words from file and return as list."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return [word.strip().upper() for word in words if 4 <= len(word.strip()) <= 12]

def choose_random_word(word_list):
    """Select random word from list."""
    return random.choice(word_list)

def display_hangman(wrong_count):
    """Display ASCII hangman based on wrong guess count."""
    print(HANGMAN_PICS[wrong_count])

def display_game_state(word, guessed_letters, wrong_letters, wrong_count):
    """Display current game state to user."""
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print("\n=== HANGMAN GAME ===")
    print(f"\nWord: {display_word}")
    print(f"Wrong letters: {' '.join(wrong_letters)}")
    print(f"Attempts remaining: {6 - wrong_count}\n")
    display_hangman(wrong_count)

def get_player_guess(guessed_letters):
    """Get and validate player's letter guess."""
    while True:
        guess = input("Enter a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def check_game_over(word, guessed_letters, wrong_count, max_wrong):
    """Check if game is won or lost."""
    if all(letter in guessed_letters for letter in word):
        print(f"\nCongratulations! You guessed the word: {word}")
        return True
    elif wrong_count >= max_wrong:
        print(f"\nGame Over! The word was: {word}")
        return True
    return False

def play_hangman():
    """Main game function."""
    word_list = load_words("words.txt")
    word = choose_random_word(word_list)
    guessed_letters = set()
    wrong_letters = []
    wrong_count = 0
    max_wrong = 6

    while True:
        display_game_state(word, guessed_letters, wrong_letters, wrong_count)
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("\nGood guess!")
        else:
            print("\nWrong letter!")
            wrong_letters.append(guess)
            wrong_count += 1

        if check_game_over(word, guessed_letters, wrong_count, max_wrong):
            break

def main():
    """Main program entry point."""
    play_hangman()
    while input("\nPlay again? (y/n): ").strip().lower() == 'y':
        play_hangman()

if __name__ == "__main__":
    main()
