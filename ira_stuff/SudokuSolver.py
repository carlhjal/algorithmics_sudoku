import numpy as np
import cv2
import time

class SudokuSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.unassigned = -1

        self.showSudokuInit()
        
        start = time.time()
        self.findPossible()
        self.assignValue()
        while self.unassigned != 0:
            prev_matrix = self.matrix.copy()
            self.updatePossible()
            self.assignValue()

            if np.array_equal(self.matrix, prev_matrix):
                self.updatePossible()
                self.resolveRow()
                self.updatePossible()
                self.resolveCol()
                self.assignValue()
                # print(type(self.matrix))
                # print(type(prev_matrix))
                # print(self.matrix == prev_matrix)

            end = time.time()-start
            grid_copy = self.grid.copy()
            cv2.putText(grid_copy, f"Time taken: {round(end*1000)} ms", (10, grid_copy.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            
            cv2.imshow("Sudoku", grid_copy)
            if np.array_equal(self.matrix, prev_matrix):
                break
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def getBox(self, i, j):
        box = list()
        startRow = i - i % 3
        startCol = j - j % 3
        for i in range(3):
            for j in range(3):
                box.append(self.matrix[i + startRow][j + startCol])
        return box
    
    def findPossible(self):
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val == 0:
                    possible_val = list()
                    box = self.getBox(i, j)
                    for number in range(1, 10):
                        if number not in row and number not in self.matrix[:, j] and number not in box:
                            possible_val.append(number)
                    self.matrix[i][j] = possible_val
                    
    def updatePossible(self):
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if isinstance(val, list):
                    possible_val = list()
                    box = self.getBox(i, j)
                    for number in range(1, 10):
                        if number not in row and number not in self.matrix[:, j] and number not in box:
                            possible_val.append(number)
                    self.matrix[i][j] = possible_val
                    
    def assignValue(self):
        self.unassigned = 0
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if isinstance(val, list):
                    if len(val) == 1:
                        self.matrix[i][j] = val[0]
                        px1 = int(self.cell/2+self.cell*i+8)
                        px2 = int(self.cell/2+self.cell*j)
                        cv2.putText(self.grid, str(self.matrix[i][j]), (px2, px1), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 40, 200), 2)
                    else:
                        self.unassigned += 1

    def resolveRow(self, trans=False):
        for i, row in enumerate(self.matrix):
            positions = list()
            numbers = list()
            for j, val in enumerate(row):
                if isinstance(val, list):
                    for _ in range(len(val)):
                        positions.append((i,j))
                    numbers += val
            numbers = np.array(numbers)
            unique, counts = np.unique(numbers, return_counts=True)
            for idx, count in enumerate(counts):
                if count == 1:
                    coords = positions[int(np.where(numbers==unique[idx])[0])]
                    self.matrix[coords[0]][coords[1]] = unique[idx]
                    if trans:
                        px1 = int(self.cell/2+self.cell*coords[1]+8)
                        px2 = int(self.cell/2+self.cell*coords[0])
                        cv2.putText(self.grid, str(self.matrix[coords[0]][coords[1]]), (px2, px1), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 40, 200), 2)
                    else:
                        px1 = int(self.cell/2+self.cell*coords[0]+8)
                        px2 = int(self.cell/2+self.cell*coords[1])
                        cv2.putText(self.grid, str(self.matrix[coords[0]][coords[1]]), (px2, px1), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 40, 200), 2)

    def resolveCol(self):
        self.matrix = self.matrix.transpose()
        self.resolveRow(True)
        self.matrix = self.matrix.transpose()


                        
    def showSudokuInit(self):
        self.grid = cv2.imread('./ira_stuff/res/sudoku_blankgrid.png')
        
        cv2.namedWindow("Sudoku", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Sudoku", 435, 435)
        
        height, width, color = self.grid.shape
        self.cell = int((height-45)/8)

        self.grid = cv2.copyMakeBorder(self.grid, 0, 50, 0, 0, cv2.BORDER_CONSTANT, value=(255,255,255))
        
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val != 0:
                    self.matrix[i][j] = val
                    px1 = int(self.cell/2+self.cell*i+8)
                    px2 = int(self.cell/2+self.cell*j)
                    cv2.putText(self.grid, str(self.matrix[i][j]), (px2, px1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("Sudoku", self.grid)

if __name__ == "__main__":
    matrix = np.array([
        [0,5,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0],
        [0,0,8,0,0,0,7,9,0],
        [8,0,0,0,1,5,0,0,2],
        [0,0,6,8,0,4,0,0,0],
        [2,0,0,0,6,0,4,0,1],
        [0,0,0,0,0,7,0,0,9],
        [0,1,9,0,0,0,0,5,0],
        [6,4,7,0,0,0,0,0,0]
    ], dtype=object)
    ss = SudokuSolver(matrix)