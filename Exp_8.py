import numpy as np
import random

def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    r = int(input("\nEnter row entry: "))
    c = int(input("Enter column entry: "))
    if (r, c) in selection:
        board[r][c] = player
        return board
    else:
        print("\nSpace already occupied!!\nRetry\n")
        return random_place(board, player)

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win:
            return True
    return False

def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return True
    return False

def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return True

    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("\nBoard after " + str(counter) + " move")
            print(board)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

out = str(play_game())
if out == "-1":
    print("Match Draw!")
else:
    print("\nWinner is: " + out)
