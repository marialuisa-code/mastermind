import random

colors = ['red', 'green', 'blue', 'yellow', 'purple', "white"]

def menu():
    print("Welcome to Mastermind!")
    print("1. Start a new game")
    print("2. View scores")
    print("3. Settings")
    print("4. Exit")
    choice = input("Please enter your choice (1-4): ")
    return choice


def printAvailableColors():
    print("Available colors:")
    for color in colors:
        print(color)

def createCode(lengthOfCode = 4):
    code = ""
    for i in range (lengthOfCode):
        color = random.choice(colors)
        code += color[0]
    return code

def hideCode(code):
    hiddenCode = ""
    for i in range(len(code)):
        hiddenCode += "*"
    return hiddenCode

def compareLetters(guessedLetter, codeLetter):
    print(f"Guessed letter: {guessedLetter}, Code letter: {codeLetter}")
    if guessedLetter.lower() == codeLetter:
        return True
    return False

def guess():
    guess = input("Enter your guess: ")
    return list(guess)

def main():

    action = menu()
    match action:
        case "1":
            startGame()
        case "2":
            viewScores()
            pass
        case "3":
            settings()
        case "4":
            exit()
        case _:
            print("Invalid choice. Please try again.")

def startGame():

    nbAttempts = 12
    code = createCode()
    printAvailableColors()
    print(hideCode(code))

    while nbAttempts > 0:
        userGuess = guess()
        codeWithFoundLetters = createCodeWithFoundLetters(userGuess, code)
        print(codeWithFoundLetters)
        nbAttempts -= 1
        print(f"You have {nbAttempts} attempts left.")

def createCodeWithFoundLetters(userGuess, code):
    codeWithFoundLetters = ""
    for i in range(len(userGuess)):
        if compareLetters(userGuess[i].lower(), code[i]):
            print("Correct guess!")
            codeWithFoundLetters += userGuess[i]
        else:
            print("Incorrect guess.")
            codeWithFoundLetters += "*"
    return codeWithFoundLetters


def viewScores():
    pass

def settings():
    pass

startGame()