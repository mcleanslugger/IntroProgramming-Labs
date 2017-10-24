##CMPT 120 Intro to Programming
##Lab #7 Lists & Functions
##Author: David Siegel
##Created: 2017-10-24

symbol = [" ", "x", "o"]

def markBoard(board, row, col, player):
    if board[row][col] == 0:
        board[row][col] = player
        player = player % 2 + 1
    else:
        print("This square has already been marked. Please try again.")
    return player
        

def getPlayerMove():
    row = int(input("Please enter what row you would like to mark: "))
    col = int(input("Please enter what column you would like to mark: "))
    print()
    return (row - 1,col - 1)

def hasBlanks(board):
    newBoard = board[0] + board[1] + board[2]
    try:
        newBoard.index(0)
        return True
    except:
        return False

def squareToSymbol(square):
    return symbol[square]

def displayBoard(board):
    print("+-----------+")
    print("| " + squareToSymbol(board[0][0]) + " | " + squareToSymbol(board[0][1]) + " | " + squareToSymbol(board[0][2]) + " |")
    print("+-----------+")
    print("| " + squareToSymbol(board[1][0]) + " | " + squareToSymbol(board[1][1]) + " | " + squareToSymbol(board[1][2]) + " |")
    print("+-----------+")
    print("| " + squareToSymbol(board[2][0]) + " | " + squareToSymbol(board[2][1]) + " | " + squareToSymbol(board[2][2]) + " |")
    print("+-----------+\n")

def main():
    board = [ [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0] ]
    
    player = 1
    while hasBlanks(board):
        displayBoard(board)
        row,col = getPlayerMove()
        player = markBoard(board, row, col, player)
        markBoard(board,row,col,player)
    else:
        print("Game Over. Good Job.")

main()
