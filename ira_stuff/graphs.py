import module.gen_random_board as gen
import numpy as np
from SudokuSolver import SudokuSolver
import time
import matplotlib.pyplot as plt

def addlabels(x,y,z):
    for i in range(len(x)):
        plt.text(x[i], y[i]+0.2, z[i], ha = 'center')

numbers = list()
times = list()
matrixes = list()
tries = list()
empty_board = np.zeros((9,9), dtype=np.uint8)
for number in range(60, 19, -1):
    n_try = -1
    solved = False
    while not solved and n_try<10:
        n_try+=1
        matrix = np.array(gen.gen(empty_board, number), dtype=object)
        start = time.time()
        ss = SudokuSolver(matrix, 0, False)
        end = time.time()
        if ss.solved:
            numbers.append(number)
            times.append(round((end-start)*1000))
            tries.append(n_try)
            matrixes.append(ss.matrix)
            solved = True

plt.title("Time taken to solve sudoku")
plt.xlabel("Number of initial values")
plt.ylabel("Time, ms")
plt.bar(numbers, times)
addlabels(numbers, times, tries)
plt.savefig("./ira_stuff/res/graph3.png")
plt.show()




