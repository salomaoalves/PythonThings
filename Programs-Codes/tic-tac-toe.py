import numpy as np

def main():
    print("--------------------WELCOME--------------------------")
    print("X for the first player and O for the second player")
    print()
    board = creatBoard()
    jog1, jog2 = 'X','O'
    print(printMat(board))
    while(not end(board)):
        board = play(jog1,board)
        if not end(board):
            board = play(jog2,board)
    if winner(board) == 1:
        print("Player 1 wins!!!!!")
    elif winner(board) == 2:
        print("Player 2 wins!!!!!")
    else:
        print("Anyone win!")
    print("Thanks for play!")

def winner(board):
    #raw for X
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        return 1
    if board[1][0] == board[1][1] == board[1][2] == 'X':
        return 1
    if board[2][0] == board[2][1] == board[2][2] == 'X':
        return 1

    #columns for X
    if board[0][0] == board[1][0] == board[2][0] == 'X':
        return 1
    if board[0][1] == board[1][1] == board[2][1] == 'X':
        return 1
    if board[0][2] == board[1][2] == board[2][2] == 'X':
        return 1

    #raw for O
    if board[0][0] == board[0][1] == board[0][2] == 'O':
        return 2
    if board[1][0] == board[1][1] == board[1][2] == 'O':
        return 2
    if board[2][0] == board[2][1] == board[2][2] == 'O':
        return 2

    #columns for O
    if board[0][0] == board[1][0] == board[2][0] == 'O':
        return 2
    if board[0][1] == board[1][1] == board[2][1] == 'O':
        return 2
    if board[0][2] == board[1][2] == board[2][2] == 'O':
        return 2

    #dig princ
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return 2

    #dig secS
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return 2
    
    #no winner
    else:
        return 0

def end(board):
    if winner(board) == 1 or winner(board) == 2:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == '1':
                return False
    return True

def creatBoard():
    board = np.ones((3,3),dtype=str)
    return board
        
def printMat(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=' ')
        print()

def play(jog, board):
    while(1):
        print()
        raw = int(input("What raw u want: "))
        column = int(input("What column u want: "))
        if jog == 'X' and board[raw][column] == '1':
            board[raw][column] = 'X'
            printMat(board)
            return board
        if jog == 'O' and board[raw][column] == '1':
            board[raw][column] = 'O'
            printMat(board)
            return board
        print("Move invalid! Try again!")

main()
        
