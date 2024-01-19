import numpy as np
from modules import print_board

def main():
    empty_board = np.zeros((9,9), dtype=np.uint8)
    print_board.print_board(empty_board)

if __name__ == "__main__":
    main()