import numpy as np
import module.board_printer as bp
import module.gen_random_board as gen

# quite like this logic
# https://medium.com/codex/building-a-simple-sudoku-solver-in-python-with-numpy-1a8ea6f5bff5

get get_quadrant(board, row, column):


def get_possible(board, row, column):
    

def solver(board):
    
    for row in board:
        for column in row:
            possible_val = get_possible(board, row, column)
            board[row, column]
    

    

def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen.gen(empty_board, 17)
    bp.print_board(sudoku)
    print(sudoku[0, 0])
    #solved_sudoku = solver(sudoku)
    bp.print_board(solved_sudoku)

if __name__ == "__main__":
    main()