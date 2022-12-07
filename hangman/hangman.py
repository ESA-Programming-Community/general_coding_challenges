"""
# Hangman

You have a list of words and select one for each round. You provide dashes like this (_ _ _ _ _ _).

The number of dashes should equal the number of letters in the selected word.

Allow the user to guess the word letter by letter.

The user has 6 opportunities. When a user enters a letter from the word, you display the location in the word where the character can be located (e.g. If the word is banana and the user typed "a," the output should be something like this _ a _ a _ a).

But if it isn't in the word, you reduce the user's chances by 1 until the user has no chances left.

## Recommendations
- Employ the concepts of functions
- Use Python language
"""
from random import choice


def generateWord():
    words = {
        "Ghana": "It is a country",
        "Pineapple": "It is a fruit",
        "Cucumber": "It is a vegetable",
        "Banana": "It is a fruit",
        "Hangman": "It is the name of the game"
    }
    return choice(list(words.items()))


def validateGuess(userGuess, generatedWord, consoleDisplay):
    if userGuess in generatedWord:
        consoleDisplay = consoleDisplay.split()
        for index in range(len(generatedWord)):
            if generatedWord[index] == userGuess:
                consoleDisplay[index] = userGuess
        return " ".join(consoleDisplay), True
    else:
        return consoleDisplay, False


def askUser(generatedWord, consoleDisplay):
    print(f"Hint: \n{hint}", f"\n{consoleDisplay}")
    userInput = input("Enter your guess: ")
    return validateGuess(userInput.lower(), generatedWord.lower(), consoleDisplay)


if __name__ == "__main__":

    print("=========================")
    print("\tHangman Game")
    print("Guess the right word and\nsave the man from being\n\t\thanged")
    print("=========================")

    chances = 6
    word, hint = generateWord()
    display = "".join(["_ " for _ in range(len(word))]).rstrip()

    while chances != 0:

        display, isCorrectGuess = askUser(word, display)
        if isCorrectGuess:
            if "_" not in display:
                print("Hurray!!! You guessed the word")
                print(f"The word is {word}")
                break
        else:
            print("Wrong guess! Try again!")
            chances -= 1
            print(f"You have {chances} left")

    if chances == 0:
        print(f"You couldn't guess the word\nThe word was {word}")
