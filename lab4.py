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

    # this bit of code here goes through at every square on the board,
    # starting at index 0, and determining wherter to turn them off or on

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

            # This code makes it so that whenever it selects a square to turn
            # off or on, it will also turn off/on the nearby left, right,
            # above, and below square

            if left != -1:
                # the reason for this if statement is to make sure that left
                # doesn't go off at index 0 as there are no square to the left
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
                # this code makes sure that the program doesn't try and turn
                # off/on non-existant squares above the indexes in row 1
                if int(above / 5) != 4:
                    if board[above] == 1:
                        board.pop(above)
                        board.insert(above, 0)
                    elif board[above] == 0:
                        board.pop(above)
                        board.insert(above, 1)
            if i < 20:
                # This if statement makes sure it doesn't turn off/on
                # non-existant square below the indexes in row 5
                if int(below / 5) != 0:
                    if board[below] == 1:
                        board.pop(below)
                        board.insert(below, 0)
                    elif board[below] == 0:
                        board.pop(below)
                        board.insert(below, 1)
    return board


def lightsout():
    # this is the portion of code the user interacts with

    moves = 0
    solved_board = [
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            1, 1, 1, 1, 1
            ]
    # the program later creates the board it displays for the user it flips
    # the on and off squares for some reason, so we had to reverse the solved
    # conditon to compensate
    board = make_board()

    while board != solved_board:
        # this little bit of code is the portion that converts the string of
        # 1 and 0's in board into a collection of white and black squares in
        # a 5x5 grid
        moves += 1
        sqrboard = []
        for i in range(len(board)):
            if board[i] == 1:
                sqrboard.append("\N{WHITE SQUARE}")
            elif board[i] == 0:
                sqrboard.append("\N{BLACK SQUARE}")
        print(sqrboard[0], sqrboard[1], sqrboard[2], sqrboard[3], sqrboard[4])
        print(sqrboard[5], sqrboard[6], sqrboard[7], sqrboard[8], sqrboard[9])
        print(sqrboard[10], sqrboard[11], sqrboard[12], sqrboard[13],
              sqrboard[14])
        print(sqrboard[15], sqrboard[16], sqrboard[17], sqrboard[18],
              sqrboard[19])
        print(sqrboard[20], sqrboard[21], sqrboard[22], sqrboard[23],
              sqrboard[24])

        # finally this code here is responsible for letting the iser interact
        # and change the board by selecting square to turn off and on

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

    # this is to sidplay to solved board and congradulate the player
    # we have white squares becuse for some reason it flips white and black
    solsqrboard = [
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}", "\N{WHITE SQUARE}", "\N{WHITE SQUARE}",
        "\N{WHITE SQUARE}",
            ]
    print(solsqrboard[0], solsqrboard[1], solsqrboard[2], solsqrboard[3],
          solsqrboard[4])
    print(solsqrboard[5], solsqrboard[6], solsqrboard[7], solsqrboard[8],
          solsqrboard[9])
    print(solsqrboard[10], solsqrboard[11], solsqrboard[12], solsqrboard[13],
          solsqrboard[14])
    print(solsqrboard[15], solsqrboard[16], solsqrboard[17], solsqrboard[18],
          solsqrboard[19])
    print(solsqrboard[20], solsqrboard[21], solsqrboard[22], solsqrboard[23],
          solsqrboard[24])

    print(f"Congratulations! You solved it in {moves} moves")


lightsout()
