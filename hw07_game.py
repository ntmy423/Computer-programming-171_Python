# by My Nguyen
# Nov 6, 2024
# Homework 7: Create a single player board placement game
# Program Description: The game starts with a board full of zeros. The board is an n by n square. It is not possible to win on all board sizes. It is possible to win with boards between 3 and 7. We will only use boards of this size.

import math

# First function
def getInteger(question, a, b):
    while True:
        value = input(question)
        if value.isdigit():
            value = int(value)
            if a <= value <= b:
                return value
            else:
                print("Number outside of range")
        else:
            print("You did not enter a number.")

# Second function
def printOptions(n):
    print(" " * 1, end="")  
    for i in range(n):
        rowElements = []
        for j in range(n):
            rowElements.append(f"{i * n + j:>2}")
        row = "  ".join(rowElements)
        print(row)
        if i < n - 1:
            print(" " * 1, end="")

# Third function
def distance(i, j, n):
    x1, y1 = i % n, i // n
    x2, y2 = j % n, j // n
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Fourth function
def checkBoard(board, n):
    positions = []
    for index in range(len(board)):
        if board[index] == 1:
            positions.append(index)
    distances = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            d = distance(positions[i], positions[j], n)
            print(f"The distance from {positions[i]} to {positions[j]} is {d:.3f}")
            existingDistances = []
            for existing in distances:
                existingDistances.append(abs(d - existing) < 0.0001)
            if any(existingDistances):
                return False
            distances.append(d)
    return True

# Main script
if __name__ == "__main__":
    print("Welcome to Placement Game")
    n = getInteger("Enter Size of Board (between 3 and 7): ", 3, 7)

    board = [0] * (n * n)
    print("Rules:")
    print("You must pick", n, "spaces on the board to place ones.")
    print("The distances between all the ones you placed must be different.")
    print("The possibles spaces are shown below.")
    printOptions(n)
    print(f"Pick {n} spaces")
    
    failedAttempts = 0
    for _ in range(n):
        validPick = False
        while not validPick:
            pick = getInteger(f"Pick Space (0-{n*n - 1}): ", 0, n*n - 1)
            if board[pick] == 0:
                board[pick] = 1
                validPick = True
            else:
                failedAttempts += 1
                if failedAttempts == 2:
                    print("You did not pick unique spaces.")
                    exit ()

    print("Your board is shown below")
    for i in range(n):
        rowElements = []
        for j in range(n):
            rowElements.append(str(board[i * n + j]))
        row = " ".join(rowElements)
        print(row)

    print("We will check the distance between all selections")
    if checkBoard(board, n):
        print("You Win: Your Board Passes the Test")
    else:
        print("You Lose: Your board contained multiple placements with the same distance")
