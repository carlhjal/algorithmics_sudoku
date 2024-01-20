"""
Can solve boards with about 30 given numbers
"""

import numpy as np
import module.board_printer as bp
import module.gen_random_board as gen
import random
import time

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

"""
------------------------------------
"""

def solver_1(board):
    """Solves the sudoku by placing num where there is only 1 possible"""
    # arbitrary stop
    for i in range(10):
        for row in range(9):
            for column in range(9):
                if board[row,column] != 0:
                    continue
                possible_vals = get_possible(board, row, column)
                if len(possible_vals) == 1:
                    board[row, column] = possible_vals[0]
    return board

def solver_2_helper(board):
    """Helper function for solver 2, this is just to avoid too much indentation"""
    changed = True
    while changed:
        changed = False
        possible_vals_dict = {}
        for row in range(9):
            for column in range(9):
                if board[row,column] != 0:
                    continue
                
                possible_vals = get_possible(board, row, column)
                possible_vals_dict[row*column] = possible_vals

                if len(possible_vals) == 1:
                    board[row, column] = possible_vals[0]
                    changed = True
        
    return board, possible_vals_dict

def shortest_list(val_dict):
    """
    Returns index of where there could be the least possible numbers
    should make guessing way more efficient
    """
    result = [[len(v), k] for k, v in val_dict.items()]
    result = sorted(result)
    return result[0][1]

def check_invalidity(board, row, column):
    """Check if only possible number is 0, meaning the guess is invalid"""
    left, upper = get_quadrant_corner(row, column)
    quad = board[left:left+3, upper:upper+3]
    quad_unique = np.unique(quad)
    row_unique = np.unique(board[row,:])
    col_unique = np.unique(board[:,column])
    all_unique = np.unique(np.concatenate((quad_unique, row_unique, col_unique)))
    zero = [num for num in range(0,10) if num not in all_unique]
    if 0 in zero:
        return True
    return False

def brute_force_solution(board):
    """Im gonna have a meltdown"""
    list_of_dicts = []
    
    board, possible_vals_dict = solver_2_helper(board)
    #shortest_ind = shortest_list(possible_vals_dict)

    changed_ind = []
    excluded_guesses = []
    
    while True:
        board, possible_vals_dict = solver_2_helper(board)

        if 0 not in board:
            return board

        shortest_ind = shortest_list(possible_vals_dict)
        print(f"shortest ind: {shortest_ind}, {possible_vals_dict[shortest_ind]}")
        changed_ind.append(shortest_ind)
        for i in range(len(possible_vals_dict[shortest_ind])):
            guess = possible_vals_dict[shortest_ind][i]
            board[shortest_ind//9][shortest_ind%9] = guess
                
        # check if guess is definitely invalid
        invalid = check_invalidity(board, shortest_ind//9, shortest_ind%9)
        if invalid:
            print("invalid")
            continue

    """
        while True:
        board, possible_vals_dict = solver_2_helper(board)
        shortest_ind = shortest_list(possible_vals_dict)
        for i in range(len(possible_vals_dict[shortest_ind])):
            guess = possible_vals_dict[shortest_ind][i]
            board[shortest_ind//9][shortest_ind%9] = guess
            
            # check if guess is definitely invalid
            invalid = check_invalidity(board, shortest_ind//9, shortest_ind%9)
            if invalid:
                print("invalid")
                continue

            # try to fast solve the whole board
            solved = solver_1(board)
            if 0 not in solved:
                return solved
            
            # try to solve the board as far as possible
            board, possible_vals_dict = solver_2_helper(board)
            bp.print_board(board)
            shortest_ind = shortest_list(possible_vals_dict)
            print(f"shortest ind: {shortest_ind}, {possible_vals_dict[shortest_ind]}")
            
            # return if finished
            if 0 not in board:
                return board

            # finally rule out guess

    """

    
    return old_board

def solver_2(board):
    possible_vals_dict = {}
    #board, possible_vals_dict = solver_2_helper(board)
    old_board = board.copy()
    board = brute_force_solution(board)
    return board


def solver(board, method=1):
    if method == 1:
        return solver_1(board)
    if method == 2:
        return solver_2(board)

def main():
    random.seed(123)
    empty_board = np.zeros((9,9), dtype=np.uint8)
    sudoku = gen.gen(empty_board, 30)
    bp.print_board(sudoku)
    time1 = time.time()
    solved_sudoku = solver(sudoku, 2)
    print(time.time()-time1)
    bp.print_board(solved_sudoku)

if __name__ == "__main__":
    main()