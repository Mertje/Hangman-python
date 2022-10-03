import random
from words import word_list
from hangman import display_hangman


def get_word():
    # Gets random words 
    return random.choice(word_list).upper()

def play_game(word):
    print(word) 
    word_completion = "_" * len(word) # creates underscore for each letter in word
    right_guessed = False # checker for right answer
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print("Let's play Hangman!")  # prints start game text
    print(display_hangman(tries)) # Prints the hangman status 6

    while not right_guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper() # Get te user input and make it capital letter/word

        if len(guess) == len(word) and guess.isalpha():
            if guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                continue
            
            print("You already guessed the word", guess)
            right_guessed = True
            word_completion = word

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
                right_guessed = True

            attempt(tries, word_completion)
            continue


        print("Not a valid guess.")
        attempt(tries, word_completion)

    res(right_guessed, word)




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
