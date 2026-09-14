import random
import json

colors = ['red', 'green', 'blue', 'yellow', 'purple', "white"]
gameSessions = 1


def askName():
    name = input("Please enter your name: ")
    print(f"Hello {name}, Welcome to Mastermind!")
    return name

def menu():
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

def createCode(lengthPreferences):
    code = ""
    for i in range (lengthPreferences):
        color = random.choice(colors)
        code += color[0]
    return code

def hideCode(code):
    hiddenCode = ""
    for i in range(len(code)):
        hiddenCode += "*"
    return hiddenCode

def compareLetters(guessedLetter, codeLetter):
    if guessedLetter.lower() == codeLetter:
        return True
    return False

def guess():
    guess = input("Enter your guess: ")
    return list(guess)

def main():
    name = askName();
    action = menu()
    match action:
        case "1":
            startGame()
        case "2":
            viewScores()
            pass
        case "3":
            settings(name)
        case "4":
            exit()
        case _:
            print("Invalid choice. Please try again.")

def startGame():

    preferences = readFromPreferences()
    nbAttempts = preferences["numberOfAttempts"]
    lengthCode = preferences["lengthOfCode"]
    playAgain = True
    gameSessions = 1
   
    code = createCode(lengthCode)
    codeWithFoundLetters = []
    printAvailableColors()
    print(hideCode(code))

    while code != codeWithFoundLetters and nbAttempts > 0 and playAgain == True:
        userGuess = guess()
        codeWithFoundLetters = createCodeWithFoundLetters(userGuess, code)
        lettersInsideCode = checkIfLetterisInsideCode(userGuess, code)
        print(f"Letters partially correct: {lettersInsideCode} ")
        print(f"Code with found letters: {codeWithFoundLetters}")
        print(f"Code: {code}, codeWithFoundLetters: {codeWithFoundLetters}")
        nbAttempts -= 1
        print(f"You have {nbAttempts} attempts left.")

    gameSessions += 1
    createHiddenStatisticsFile(gameSessions, nbAttempts)
    
    if ((nbAttempts == 0 ) or (code == codeWithFoundLetters)):
        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() == "y":
            playAgain = True
            
            print(f"GAME sessions{gameSessions}")
            startGame()
        else:
            playAgain = False
            exit()         

def replay():
    replay = input("Do you want to play again? (y/n): ")
    if replay.lower() == "y":
        gameSessions += 1
        print(f"gamesessions nb {gameSessions}")
        startGame()
        
        return gameSessions
    else:
        exit() 
        return gameSessions

def createCodeWithFoundLetters(userGuess, code):
    codeWithFoundLetters = ""
    if (len(userGuess) < len(code)):
        print(f"Your guessed code is TOO SHORT, it should be {len(code)} characters long !")
        for i in range(len(userGuess)):
            if compareLetters(userGuess[i].lower(), code[i]):
                codeWithFoundLetters += userGuess[i]
            else:
                codeWithFoundLetters += "*"
        differenceBetweenlength = len(code) - len(userGuess)
        for i in range(differenceBetweenlength):
            codeWithFoundLetters += "*"
    else:
        for i in range(len(code)):
            if compareLetters(userGuess[i].lower(), code[i]):
                codeWithFoundLetters += userGuess[i]
            else:
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

def settings(user):
    print("Settings:")
    print("1. Change number of attempts")
    print("2. Change length of code")
    print("3. Add a new color")
    choice = input("Please enter your choice (1-3): ")
    attempts = 12
    lengthOfCode = 4
    preferencesColors = []
    match choice:
        case "1":
            attempts = pickNumberOfAttempts()
        case "2":
            lengthOfCode = pickLengthOfCode()
        case "3":
            preferencesColors= addColorsToAvailableColors()
            print(preferencesColors)
        case _:
            print("Invalid choice. Please try again.")
    savePreferences(user, preferencesColors, attempts, lengthOfCode)
    main()

def savePreferences(name, addedColors, attempts = 12, lengthOfCode = 4):
   
    settingsPreferences = {
        "name": name,
        "numberOfAttempts": attempts,
        "lengthOfCode": lengthOfCode,
        "colors": addedColors,
    }

    preferences = json.dumps(settingsPreferences, indent=4)
    with open("settings.json", "w") as file:
        file.write(preferences)

def readFromPreferences():
    with open("settings.json", "r") as file:
        preferences = json.load(file)
        return preferences

def pickNumberOfAttempts():
    attempts = int(input("Enter the number of attempts you want (default is 12): "))
    return attempts

def pickLengthOfCode():
    codeLength = int(input("Enter the length of the code you want (default is 4): "))
    return codeLength

def addColorsToAvailableColors():
    continueAddingColors = True
    preferencesColors= []
    while continueAddingColors:
        addNew = input("Do you want to add another color? (y/n): ")
        if (addNew.lower() == "y"):
            newColor = input("Enter a new color to add: ")
            if (newColor not in colors) and (newColor not in colors):
                preferencesColors.append(newColor)
                print(f"{newColor} has been added to the available colors.")
            else:
                print(f"{newColor} is already in the available colors.")
        else:
            continueAddingColors = False
    print(preferencesColors)
    return preferencesColors

def createHiddenStatisticsFile(gameSession, totalScore ):
    statistics = {
        "gameSession": gameSession,
        "totalScore": totalScore,
    }

    stats = json.dumps(statistics, indent=4)
    with open(".hiddenStatistics.json", "w") as file:
        file.write(stats)

main()
