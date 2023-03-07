"""This project is a fun game that generates a random number in a certain specified range and the user must guess the number
after receiving hints, Every time a user`s guess is wrong they are prompted with more hints to make it easier at the cost of
reducing the score"""

userInput, score = 0, 5
import random

for i in range(1):
    value = random.randint(1,10)
    
    if(value % 2 == 0):
        print("First hint: The number is an even number between 1 and 10 inclusive")
        
    elif(value % 2 == 1):
        print("First hint: The number is an odd number between 1 and 10 inclusive")
        
    userInput = int(input("Guess the number: "))
    
    if(userInput == value):
        print(f"Wow! You are a Genius!!!, you guessed the number correctly. Hurray!!!\n The number is {value} and your score is {score}")
        break
        
    elif(userInput != value and value % 2 == 0):
        hint2 = value/2
        print(f"Second hint: {hint2} is the outcome of the number divided by another number")
        
        userInput = int(input("Guess the number: "))
        
        if(userInput == value):
            score -= 2
            print(f"Wow! You are good, you guessed the number correctly on the second attempt.\n The number is {value} and your score is {score}")
        else:
            score -= 4
            print(f"Guesses aren`t your thing. Better luck next time and your score is {score}")
            
    elif(userInput != value and value % 2 == 1):
        hint2 = 10 % value
        print(f"Second hint: {hint2} is the remainder of the number divided by another number")
        
        userInput = int(input("Guess the number: "))
        
        if(userInput == value):
            score -= 2
            print(f"Wow! You are good, you guessed the number correctly on the second attempt.\n The number is {value} and your score is {score}")
        else:
            score -= 4
            print(f"Guesses aren`t your thing. Better luck next time and your score is {score}\nThe number is{value}")
            break


