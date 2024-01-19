import numpy as np
import module.board_printer as bp
import module.gen_random_board as gen
import random

# quite like this logic
# https://medium.com/codex/building-a-simple-sudoku-solver-in-python-with-numpy-1a8ea6f5bff5

def get_quadrant_corner(row, column):
    """returns upper left corner of quadrant"""
    left = row//3*3
    upper = column//3*3
    return left, upper

def get_possible(board, row, column):
    """returns all possible values of chosen position"""
    left, upper = get_quadrant_corner(row, column)
    quad = board[left:left+3, upper:upper+3]
    quad_unique = np.unique(quad)
    row_unique = np.unique(board[row,:])
    col_unique = np.unique(board[:,column])
    all_unique = np.unique(np.concatenate((quad_unique, row_unique, col_unique)))
    return [num for num in range(1,10) if num not in all_unique]

def fill(board, row, column):
    """Fills 0 with correct value if there is only 1 possible value"""
    possible_vals = get_possible(board, row, column)
    if len(possible_vals) == 1:
        board[row, column] = possible_vals[0]
        #print(f"printing the board\n {board}")
        return board
    return board

def solver(board):
    """Solves the sudoku"""
    # arbitrary stop
    for i in range(100):
        for row in range(9):
            for column in range(9):
                if board[row,column] != 0:
                    continue
                board = fill(board, row, column)
    return board

def main():
    random.seed(123)
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen.gen(empty_board, 40)
    bp.print_board(sudoku)
    solved_sudoku = solver(sudoku)
    bp.print_board(solved_sudoku)

if __name__ == "__main__":
    main()