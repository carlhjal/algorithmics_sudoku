import numpy as np
from modules import gen_random_board
from modules import print_board

def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen_random_board.gen(empty_board, 17)
    print_board.print_board(sudoku)

if __name__ == "__main__":
    main()