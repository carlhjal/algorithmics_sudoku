import numpy as np
import module.board_printer as bp
import module.gen_random_board as gen

# https://medium.com/codex/building-a-simple-sudoku-solver-in-python-with-numpy-1a8ea6f5bff5

def get_quadrant():
    pass

def solver(board):

    

def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen.gen(empty_board, 17)
    bp.print_board(sudoku)
    solved_sudoku = solver(sudoku)
    bp.print_board(solved_sudoku)

if __name__ == "__main__":
    main()