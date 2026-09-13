import random

colors = ['red', 'green', 'blue', 'yellow', 'purple', "white"]
DEFAULT_ATTEMPTS = 12
DEFAULT_CODE_LENGTH = 4
attempts = DEFAULT_ATTEMPTS
codeLength = DEFAULT_CODE_LENGTH


def menu():
    name = input("Please enter your name: ")
    print(f"Hello {name}, Welcome to Mastermind!")
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

def createCode():
    code = ""
    for i in range (codeLength):
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

    nbAttempts = attempts
    code = createCode()
    codeWithFoundLetters = []
    printAvailableColors()
    print(hideCode(code))

    while code != codeWithFoundLetters and nbAttempts > 0:
        userGuess = guess()
        print(f"You have {nbAttempts} attempts left.")
        codeWithFoundLetters = createCodeWithFoundLetters(userGuess, code)
        lettersInsideCode = checkIfLetterisInsideCode(userGuess, code)
        print(f"Letters partially correct: {lettersInsideCode} ")
        print(f"Code with found letters: {codeWithFoundLetters}")
        print(f"Code: {code}, codeWithFoundLetters: {codeWithFoundLetters}")
        nbAttempts -= 1
        
    replay()

def replay():
    gameSessions = 1
    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() == "y":
        gameSessions += 1
        startGame()
        return gameSessions
    else:
        exit() 
        return gameSessions

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

def checkIfLetterisInsideCode(userGuess, code):
    letters = ""
    for i in range(len(userGuess)):
        for j in range(len(code)):
            if userGuess[i] == code[j]:
                if i != j :
                    letters += userGuess[i]
    return letters

def viewScores():
    pass

def settings():
    print("Settings:")
    print("1. Change number of attempts")
    print("2. Change length of code")
    print("3. Add a new color")
    choice = input("Please enter your choice (1-3): ")
    match choice:
        case "1":
            pickNumberOfAttempts()
        case "2":
            pickLengthOfCode()
        case "3":
            addColorsToAvailableColors()
        case _:
            print("Invalid choice. Please try again.")

def pickNumberOfAttempts():
    attempts = int(input("Enter the number of attempts you want (default is 12): "))
    return attempts

def pickLengthOfCode():
    codeLength = int(input("Enter the length of the code you want (default is 4): "))
    return codeLength

def addColorsToAvailableColors():
    newColor = input("Enter a new color to add: ")
    if newColor not in colors:
        colors.append(newColor)
        print(f"{newColor} has been added to the available colors.")
    else:
        print(f"{newColor} is already in the available colors.")

main()