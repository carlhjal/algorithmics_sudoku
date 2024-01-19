import numpy as np
import cv2

class SudokuSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.unassigned = -1

        self.showSudokuInit()
        
        self.findPossible()
        self.assignValue()
        while self.unassigned != 0:
            prev_matrix = self.matrix.copy()
            self.updatePossible()
            self.assignValue()
            if (self.matrix == prev_matrix).all():
                break
            cv2.imshow("Sudoku", self.grid)
        
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
                        
    def showSudokuInit(self):
        self.grid = cv2.imread('./ira_stuff/res/sudoku_blankgrid.png')
        
        cv2.namedWindow("Sudoku", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Sudoku", 435, 435)
        
        height, width, color = self.grid.shape
        self.cell = int((height-45)/8)
        
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
        [5,0,0,4,6,7,3,0,9],
        [9,0,3,8,1,0,4,2,7],
        [1,7,4,2,0,3,0,0,0],
        [2,3,1,9,7,6,8,5,4],
        [8,5,7,1,2,4,0,9,0],
        [4,9,6,3,0,8,1,7,2],
        [0,0,0,0,8,9,2,6,0],
        [7,8,2,6,4,1,0,0,5],
        [0,1,0,0,0,0,7,0,8]
    ], dtype=object)
    ss = SudokuSolver(matrix)
