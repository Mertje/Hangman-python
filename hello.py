import random
from words import word_list
from hangman import display_hangman


def get_word():
    # Gets random words 
    return random.choice(word_list).upper()

def play_game(word):
    print(word)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion + "\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                continue

            if guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                attempt(tries, word_completion)
                continue

            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(
                word) if letter == guess]
            
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True

            attempt(tries, word_completion)
            continue

        if len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            if guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                continue
            guessed = True
            word_completion = word

        print("Not a valid guess.")
        attempt(tries, word_completion)

    res(guessed, word)


def attempt(tried, wordcom):
    print(display_hangman(tried))
    print(wordcom)
    print("\n")


def res(guess, the_word):
    if guess:
        return print("Congrats, you guessed the word! You win!")
    print("Sorry, you ran out of tries. The word was " +
          the_word + ". Maybe next time!")


def main():
    while input("Start a new game? (Y/N) ").upper() == "Y":
        play_game(get_word())


if __name__ == "__main__":
    main()
