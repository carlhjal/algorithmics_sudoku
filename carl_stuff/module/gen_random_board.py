"""
TODO make a good generator that makes use of a solver to make actually random sudokus
this generator just makes one sudoku
after removing numbers its technically a lot of different sudokus, but they all have the same solution
but nice for testing
"""

import random
import numpy as np
import board_printer as bp

def gen(empty_board, nums_keep):
    """
    Very stupid generator but makes a valid sudoku and numbers can just be removed to make it harder
    nums_keep is how many numbers should remain in the sudoku, has to be at least 17
    """

    assert nums_keep > 16

    num_arr = np.array([1,2,3,4,5,6,7,8,9])
    
    for i in range(9):
        if not i % 3 and i != 0:
            num_arr = np.roll(num_arr, 1)
        empty_board[i] = np.roll(num_arr, 3*i)
    
    num_els = empty_board.shape[0] * empty_board.shape[1]
    indices = list(range(num_els))

    for i in range(num_els - nums_keep):
        zero_ind = random.choice(indices)
        indices.remove(zero_ind)
        empty_board[zero_ind//9][zero_ind%9] = 0

    return empty_board
    
def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen(empty_board, 17)
    bp.print_board(sudoku)

if __name__ == "__main__":
    main()