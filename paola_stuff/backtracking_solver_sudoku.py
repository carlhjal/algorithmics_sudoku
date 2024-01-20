import time
def print_grid(arr):
	for i in range(9):
		for j in range(9):
			print (arr[i][j], end = " "),
		print ()

# finds the entry in the grid that is still not used
# Searches the grid to find an entry that is still unassigned
def find_empty_location(arr, l):
	for row in range(9):
		for col in range(9):
			if(arr[row][col]== 0):
				l[0]= row
				l[1]= col
				return True
	return False

def used_in_row(arr, row, num):
	for i in range(9):
		if(arr[row][i] == num):
			return True
	return False

def used_in_col(arr, col, num):
	for i in range(9):
		if(arr[i][col] == num):
			return True
	return False

def used_in_box(arr, row, col, num):
	for i in range(3):
		for j in range(3):
			if(arr[i + row][j + col] == num):
				return True
	return False

# Checks whether it will be possible to assign num to the given row, col
def check_location_is_safe(arr, row, col, num):
	
	return (not used_in_row(arr, row, num) and
		(not used_in_col(arr, col, num) and
		(not used_in_box(arr, row - row % 3, 
						col - col % 3, num))))

def solve_sudoku(arr):
	l =[0, 0]
	if(not find_empty_location(arr, l)):
		return True
	
	row = l[0]
	col = l[1]
	for num in range(1, 10):
		
		if(check_location_is_safe(arr, 
						row, col, num)):
			
			arr[row][col]= num 
			if(solve_sudoku(arr)):
				return True

			# if it fails, undo it adn try again
			arr[row][col] = 0
			
	# this triggers backtracking	 
	return False

if __name__=="__main__":
	
	grid =[[0 for x in range(9)]for y in range(9)]

	#hard sudoku
	grid =[[0,5,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,1,0,0],
			[0,0,8,0,0,0,7,9,0],
			[8,0,0,0,1,5,0,0,2],
			[0,0,6,8,0,4,0,0,0],
			[2,0,0,0,6,0,4,0,1],
			[0,0,0,0,0,7,0,0,9],
			[0,1,9,0,0,0,0,5,0],
			[6,4,7,0,0,0,0,0,0]]
	
	#easy sudoku
	# grid= [[5,0,0,4,6,7,3,0,9],
    # [9,0,3,8,1,0,4,2,7],
    # [1,7,4,2,0,3,0,0,0],
    # [2,3,1,9,7,6,8,5,4],
    # [8,5,7,1,2,4,0,9,0],
    # [4,9,6,3,0,8,1,7,2],
    # [0,0,0,0,8,9,2,6,0],
    # [7,8,2,6,4,1,0,0,5],
    # [0,1,0,0,0,0,7,0,8]]
	
	start= time.time()
	if(solve_sudoku(grid)):
		end= time.time()
		print_grid(grid)
		print("Time taken: ", end-start,"seconds")
	else:
		print ("No solution was found")
