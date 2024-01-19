import numpy as np

def print_board(board):
    """
    Prints the board
    """
    sep = "-"*25

    for i in range(9):
    
        if not i % 3:
            print(sep)

        row = (str(board[i]).strip("[]"))

        print("|" + " " + row[:6] + "|" + " " +  row[6:12] + "|" + " " + row[12:] + " " + "|")

    print(sep)

def main():
    """
    Can be used like this
    """
    empty_board = np.zeros((9,9), dtype=np.uint8)
    print_board(empty_board)
    """
    And does this
    -------------------------
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    -------------------------
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    -------------------------
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    | 0 0 0 | 0 0 0 | 0 0 0 |
    -------------------------
    """

if __name__ == "__main__":
    main()