"""
TODO make a good generator that makes use of a solver to make actually random sudokus
this generator just makes one sudoku (theoretically up to 9)
but nice for testing
"""

import numpy as np
import print_board

def gen(empty_board):
    """
    Very stupid generator but makes a valid sudoku and numbers can just be removed to make it harder
    """
    num_arr = np.array([1,2,3,4,5,6,7,8,9])
    
    for i in range(9):
        if not i % 3 and i != 0:
            num_arr = np.roll(num_arr, 1)
        empty_board[i] = np.roll(num_arr, 3*i)
    
    return empty_board
    


def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen(empty_board)
    print_board.print_board(sudoku)

if __name__ == "__main__":
    main()