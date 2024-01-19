import numpy as np
import module.board_printer as bp
import module.gen_random_board as gen

def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen.gen(empty_board, 17)
    bp.print_board(sudoku)

if __name__ == "__main__":
    main()