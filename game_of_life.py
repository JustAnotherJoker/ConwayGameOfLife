# File:         game_of_life.py
# Author:       Abbey Moran
# Date:         11/16/15
# E-mail:       moran3@umbc.edu
# Description:  This program will create a version of "Conway's Game of Life".
#               The user will input how big the board is, which cells of 
#               the board will be on, and how many times the game runs.
#               Rules of the Game: 
#               1) If a live cell has two or three neighbors, it lives on to
#                  the next generation.
#               2) If a live cell has less than two or more than three
#                  neighbors, the cell dies in the next generation.
#               3) If a dead cell has exactly three neighbors, it becomes a 
#                  live cell in the next generation.
#               Enable python 3: /usr/bin/scl enable python33 bash

DEADCELL = "."
LIVECELL = "A"

# startingBoard() creates the first "board" which is a 2-D list
# Input: number of rows, columns, live cells, and iterations
# Output: returns the user input for other definitions
def startingBoard():

    # creates a board full of deadcells
    cellRow = ""
    cellCol = 1
    board = []
    rows = int(input("Please enter number of rows: "))
    while rows <= 1:
        print("\t""That is not a valid value; please enter a number""\n"
              "\t""greater than or equal to 1")
        rows = int(input("Please enter number of rows: "))
    columns = int(input("Please enter number of columns: "))
    while columns <= 1:
        print("\t""That is not a valid value; please enter a number""\n"
              "\t""greater than or equal to 1")
        columns = int(input("Please enter number of columns: "))
    print()
    for i in range(rows):
        board.append([DEADCELL]* columns)

    # now asks user what cells they want alive and changes board
    while cellRow != "q":
        cellRow = input("Please enter the row of a cell to turn on (or q to exit): ")
        if cellRow != "q":
            cellRow = int(cellRow)
            if cellRow < 0 or cellRow > rows - 1:
                print("\t""That is not a valid value. Please enter a number""\n"
                      "\t""between 0 and", rows - 1, "inclusive...""\n")
            else:    
                cellCol = int(input("Please enter a column for that cell: "))
                while cellCol < 0 or cellCol > columns - 1:
                    print("\t""That is not a valid value. Please enter a number""\n"
                          "\t""between 0 and", columns - 1, "inclusive...""\n")
                    cellCol = int(input("Please enter a column for that cell: "))
                print()
                board[int(cellRow)][cellCol] = LIVECELL
    print()

    # asks the user how many times the game should run
    iterations = int(input("How many iterations should I run? "))
    while iterations < 0:
        print("\t""That is not a valid value; please enter a number"
              "\n""\t""greater than or equal to 0")
        iterations = int(input("How many iterations should I run? ")) 
    
    return rows, columns, board, iterations

# printBoard() prints out the board in a neat manner for the user to see
def printBoard(rows, columns, board):
    for i in range(rows):
        printRow = ""
        for j in range(columns):
            if board[i][j] == LIVECELL:
                printRow = printRow + LIVECELL
            elif board[i][j] == DEADCELL:
                printRow = printRow + DEADCELL
        print(printRow)
    print()

# nextIteration() changes the cell based on the number of neighbors they have
def nextIteration(rows, columns, board):
    # this creates a copied board 'nextBoard' to help check for neighbors 
    nextBoard = []
    for row in board:
        nextBoard.append(list(row))

    # this area checks for any neighbors
    for r in range(rows):
        for c in range(columns):
            neighbors = 0
            top = r - 1
            bottom = r + 1
            left = c - 1
            right = c + 1
            # 1) checks the up left corner neighbor 
            if top >= 0 and left >= 0:
                if nextBoard[top][left] == LIVECELL:
                    neighbors += 1
            # 2) checks the neighbor to the left
            if left >= 0:
                if nextBoard[r][left] == LIVECELL:
                    neighbors += 1
            # 3) checks the bottom right corner neighbor
            if bottom < rows and right < rows:
                if nextBoard[bottom][right] == LIVECELL:
                    neighbors += 1
            # 4) checks the neighbor above it
            if top >= 0:
                if nextBoard[top][c] == LIVECELL:
                    neighbors += 1
            # 5) checks the neighbor below it
            if bottom < rows:  
                if nextBoard[bottom][c] == LIVECELL:
                    neighbors += 1
            # 6) checks top right neighbor
            if top >=0 and right < rows:
                if nextBoard[top][right] == LIVECELL:
                    neighbors += 1
            # 7) checks the neighbor to the right
            if right < rows:
                if nextBoard[r][right] == LIVECELL:
                    neighbors += 1
            # 8) checks the bottom left corner neighbor
            if bottom < rows and left >= 0:
                if nextBoard[bottom][left] == LIVECELL:
                    neighbors += 1

            # this checks which cells live and die for the next generation
            # check description for detailed rules
            if nextBoard[r][c] == LIVECELL:
                if neighbors < 2 or neighbors > 3:
                    board[r][c] = DEADCELL
            elif nextBoard[r][c] == DEADCELL:
                if neighbors == 3:
                    board[r][c] = LIVECELL
    return board

def main():

    # finds the starting board and prints it out
    rows, columns, board, iterations = startingBoard()
    print("\n""Starting Board: ")
    print()
    printBoard(rows, columns, board)

    # finds the next iteration of the board and prints out the next board for the user
    for i in range(iterations):
        print("Iteration", i + 1, ":""\n")
        board = nextIteration(rows, columns, board)
        printBoard(rows, columns, board)

main()
