# Eindopdracht Mert Gunes
# Opdracht: Hangman
# Klas ID1G3

import random
from words import word_list
from hangman import display_hangman


def get_word():  # Gets random words from module
    return random.choice(word_list).upper()


def play_game(word):
    print(word)
    # creates underscore for each letter in word
    word_completion = "_" * len(word)
    right_guessed = False  # checker for right answer
    guessed_letters = []  # List of guessed letters
    guessed_words = []  # List of guessed words
    tries = 6  # Total tries before game over

    print("Let's play Hangman!")  # prints start game text
    print(display_hangman(tries))  # Prints the hangman status 6

    while not right_guessed and tries > 0:  # Checks out of tries and guessed word is set to true
        # Get te user input and make it capital letter/word
        guess = input("Please guess a letter or word: ").upper()

        # Validation check for words and letter.
        if (not len(guess) == 1 or not len(guess) == len(word)) and not guess.isalpha():
            # Shows hangman in terminal
            hangman_attempt(tries, word_completion)
            print("Not a valid guess.")
            continue

        # Checks word if same length as user answer
        if len(guess) == len(word):
            if guess != word:
                tries -= 1
                # Shows hangman in terminal
                hangman_attempt(tries, word_completion)
                print(guess, "is not the word.")
                guessed_words.append(guess)
                continue
            # Print if the word is correct and end the game
            print("You already guessed the word", guess)
            right_guessed = True
            word_completion = word

        # Checks if it is already guessed from list
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
            continue

        # If the letter in not in the word
        if guess not in word:
            print(guess, "is not in the word.")
            # Remove a chance
            tries -= 1
            # put guessed letter in a list
            guessed_letters.append(guess)
            # Shows hangman in terminal
            hangman_attempt(tries, word_completion)
            continue

        # Letter is found in the word print it:
        print("Good job,", guess, "is in the word!")
        # put guessed letter in a list
        guessed_letters.append(guess)
        # Creates new list with the previous word completion
        word_as_list = list(word_completion)
        # Finds location for the guessed letter and returns list of number for position
        letter_location_list = [
            i for i, letter in enumerate(word) if letter == guess]
        # Replace the wordlist underscore with the guessed input for all locations
        for position in letter_location_list:
            word_as_list[position] = guess
        # Replace and join into a string the word
        word_completion = "".join(word_as_list)
        # Checks word_completion if the underscore are all gone
        if "_" not in word_completion:
            right_guessed = True
        # Final hangman status
        hangman_attempt(tries, word_completion)
    # Final print lose/win text
    results(right_guessed, word)


def hangman_attempt(tried, wordcom):
    # Gets tries and word_completion and displays it
    print(display_hangman(tried))
    print(wordcom)
    print("\n")


def results(guess, the_word):
    # Checks if won or lost. returns print statement when won or lost
    if guess:
        return print("Congrats, you guessed the word! You win!")
    return print("Sorry, you ran out of tries. The word was " +
                 the_word + ". Maybe next time!")


def main():
    # Everytime a game ands this loop wil ask if you want to play again
    while input("Start a new game? (Y/N) ").upper() == "Y":
        # Sends the random generated word to play_game and starts the play_game function
        play_game(get_word())


# Start of code. unspoken python rule that this file should run
if __name__ == "__main__":
    main()
