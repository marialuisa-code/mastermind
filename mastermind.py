import random

colors = ['red', 'green', 'blue', 'yellow', 'purple', "white"]

def menu():
    print("Welcome to Mastermind!")
    print("1. Start a new game")
    print("2. View scores")
    print("4. Settings")
    print("3. Exit")
    choice = input("Please enter your choice (1-4): ")
    return choice

def createCode(lengthOfCode = 4):
    code = []
    for i in range (lengthOfCode):
        color = random.choice(colors)
        code.append(color[0])
    return code




code = createCode(10)
print(code)

