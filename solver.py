"""
solve sudoku
"""


def valid_move(board, pos, num):
    """
    check if the attempted move is valid
    :param board: 2D array
    :param pos: (row, col) postion in 2array
    :param num: int
    :return: bool
    """
    # check the same row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check the same column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # check box
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    """
    find an empty index
    :param board: 2D array
    :return: (int, int)
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j

    return None


def solve(board):
    """
    solve sudoku using backtracking
    :param board: 2D array
    :return: 2D solution
    """
    empty_pos = find_empty(board)
    if empty_pos is None:
        return True
    else:
        row, col = empty_pos

    for try_val in range(1, 10):
        if valid_move(board, empty_pos, try_val):
            board[row][col] = try_val

            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    """
    print sudoku board
    :param board: 2D array
    :return: None
    """
    for row in board:
        for num in row:
            print(num, end = " ")
        print()


test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


