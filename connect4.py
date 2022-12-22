import numpy as np
import sys, random
print('Welcome to connect 4 by Ari')
row_count = 6
column_count = 7

#Creates board using numpy
def create_board():
    board = np.zeros((row_count,column_count))
    return board

#If row[0] is occupied, searches upward for empty spot, 0
def next_open_row(board, col):
    for row in range(row_count):
            if board[row][col] == 0:
                return row

#Prints the board in a regular fashion
def print_board(board):
    print(board[::-1,:])
    
def check_winning_move(board):
    #Check horizontal, update for longer board sizes. (x = 4 - Row_Count) is the number to get len(Rowcount(x))
    for r in range(row_count-3):
        for c in range(column_count-3):
            if (board[r][c] == 1 and board[r][c + 1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1):
                print('Player 1 Wins - horizontal')
                sys.exit()
            elif (board[r][c] == 2 and board[r][c + 1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2):
                print('Player 2 Wins - horizontal')
                sys.exit()
                
    #Check Vertical winning moves
    for r in range(row_count-3):
        for c in range(column_count-3):
            if (board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1):
                print('Player 1 Wins - vertical')
                sys.exit()
            elif (board[r][c] == 2 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 2):
                print('Player 2 Wins - vertical')
                sys.exit()
    #Downwards check but the board is flipped when printed, appears as upward and won as upward
    for r in range(row_count-3):
        for c in range(column_count-3):
            if (board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1):
                print('Player 1 Wins - Upward Diagonal')
                sys.exit()
            elif (board[r][c] == 2 and board[r+1][c + 1] == 2 and board[r+2][c+2] and board[r+3][c+3] == 2):
                print('Player 2 Wins - Upward Diagonal')
                sys.exit()
    #Upwards check but the board is flipped when printed, appears as a downwards check and won as downwards
    for r in range(row_count-3):
        for c in range(column_count-3):
            if (board[r+3][c] and board[r+2][c+1] == 1 and board[r+1][c+2] == 1 and board[r][c+3] == 1):
                print('Player 1 Wins - Downward Diagonal')
                sys.exit()
            elif (board[r+3][c] == 2 and board[r+2][c+1] == 2 and board[r+1][c+2] == 2 and board[r][c+3] == 2):
                print('Player 2 Wins - Downward Diagonal')
                sys.exit()

def main():
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0
    while not game_over:
        if (turn == 0):
            print('Player 1 turn')
            try:
                move = int(input('Make a move on the x-axis: ')) -1
            except:
                print('please enter a valid command')
                move = int(input('Make a move on the x-axis: ')) -1
            row = next_open_row(board,move)
            board[row][move] = 1
            print_board(board)
            check_winning_move(board)
            turn += 1
            
        elif(turn == 1):
            print('Player 2 turn')
            try:
                #move = int(input('Make a move on the x-axis: ')) -1
                move = random.choice((1,6))
            except:
                print('please enter a valid command')
            row = next_open_row(board,move)
            board[row][move] = 2
            print_board(board)
            check_winning_move(board)
            turn += 1
            turn = turn % 2

if(__name__ == "__main__"):
    main()