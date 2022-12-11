"""
# Guess The Number
This is a fun game that generates a random number within a given range. After obtaining hints, the user must guess the number. 

When a user's guess is incorrect, they are given more hints to help them out at the expense of their score.

## Recommendations
- Employ the concepts of functions
- Use Python language

"""
from random import randint

points = [10, 7, 4, 1]
scores = 0


def generateNumber():
    return randint(10, 20)


def generateHint(secretNumber, userGuess, rounds):
    if rounds == 0:
        hint = "The number is between 10 and 20"
    elif rounds == 1:
        hint = "The number is a even number" if secretNumber % 2 == 0 else "The number is an odd number"
    else:
        hint = "The number is lesser" if userGuess > secretNumber else "The number is greater"
    return hint


def guessNumber():
    secretNumber = generateNumber()

    for eachRound in range(0, 4):
        userInput = int(input("Enter your guess: "))
        if userInput == secretNumber:
            print("Hurray! You have guessed the secret number!")
            return points[eachRound]
        elif userInput != secretNumber and eachRound != 3:
            print("Wrong guess! Try again")
            print(generateHint(secretNumber, userInput, eachRound))
        elif userInput != secretNumber and eachRound == 3:
            print("Sorry wrong guess.... Better luck next time.")
            return 0


def countScores(point):
    score = scores + point
    return score


if __name__ == "__main__":
    while 1:
        print("=====================================")
        print("||\t\t\t\t\t\t\t\t   ||")
        print("||\t\tGuess The Number 😊\t\t   ||")
        print("||\t\t\t\t\t\t\t\t   ||")
        print("=====================================")

        scores = countScores(guessNumber())
        print(f"Your score is {scores} points")
