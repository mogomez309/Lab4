import random 
import math
def make_board():
    board = [
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0
            ]
    for i in range(len(board)):
        new = random.randint(0, 1)
        if new == 1:
            if board[i] == 1:
                board.pop(i)
                board.insert(i, 0)
            elif board[i] == 0:
                board.pop(i)
                board.insert(i, 1)
            row = int(i / 5) 
            above = i - 5
            below = i + 5
            left = i - 1
            right = i + 1
            if left != -1:
                if int(left / 5) == row:
                    if board[left] == 1:
                        board.pop(left)
                        board.insert(left, 0)
                    elif board[left] == 0:
                        board.pop(left)
                        board.insert(left, 1)
            if int(right / 5) == row:
                if board[right] == 1:
                    board.pop(right)
                    board.insert(right, 0)
                elif board[right] == 0:
                    board.pop(right)
                    board.insert(right, 1)
            if above >= 0:
                if int(above / 5) != 4:
                    if board[above] == 1:
                        board.pop(above)
                        board.insert(above, 0)
                    elif board[above] == 0:
                        board.pop(above)
                        board.insert(above, 1)
            if i < 20:
                if int(below / 5) != 0:
                    if board[below] == 1:
                        board.pop(below)
                        board.insert(below, 0)
                    elif board[below] == 0:
                        board.pop(below)
                        board.insert(below, 1)
    print(board)
    return board

def lightsout():
    moves = 0
    solved_board = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    board = make_board()
    while board != solved_board:
        sqrboard = []
        for i in range(len(board)):
            if board[i] == 1:
                sqrboard.append("\N{WHITE SQUARE}")
            elif board[i] == 0:
                sqrboard.append("\N{BLACK SQUARE}")
        print(sqrboard[0], sqrboard[1], sqrboard[2], sqrboard[3], sqrboard[4])
        print(sqrboard[5], sqrboard[6], sqrboard[7], sqrboard[8], sqrboard[9])
        print(sqrboard[10], sqrboard[11], sqrboard[12], sqrboard[13], sqrboard[14])
        print(sqrboard[15], sqrboard[16], sqrboard[17], sqrboard[18], sqrboard[19])
        print(sqrboard[20], sqrboard[21], sqrboard[22], sqrboard[23], sqrboard[24])

        rowselect = int(input("Select a row: "))
        columnselect = int(input("Select a column: "))
        position = (columnselect - 1) + 5 * (rowselect - 1)
        above = position - 5
        below = position + 5
        left = position - 1
        right = position + 1
        row = int(position / 5)

        if board[position] == 1:
                board.pop(position)
                board.insert(position, 0)
        elif board[position] == 0:
                board.pop(position)
                board.insert(position, 1)
        if left != -1:
            if int(left / 5) == row:
                if board[left] == 1:
                    board.pop(left)
                    board.insert(left, 0)
                elif board[left] == 0:
                    board.pop(left)
                    board.insert(left, 1)
        if int(right / 5) == row:
            if board[right] == 1:
                board.pop(right)
                board.insert(right, 0)
            elif board[right] == 0:
                board.pop(right)
                board.insert(right, 1)
        if above >= 0:
            if int(above / 5) != 4:
                if board[above] == 1:
                    board.pop(above)
                    board.insert(above, 0)
                elif board[above] == 0:
                    board.pop(above)
                    board.insert(above, 1)
        if position < 20:
            if int(below / 5) != 0:
                if board[below] == 1:
                    board.pop(below)
                    board.insert(below, 0)
                elif board[below] == 0:
                    board.pop(below)
                    board.insert(below, 1)
    print("Congratulations! You solved it!")






lightsout()
