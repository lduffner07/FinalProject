import math,random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        #create 2D board below
        self.board = []
        for r in range(self.row_length):
            row = [] # makes a new row
            for c in range(self.row_length): # 9x9 sudoku board, so row length = column length
                row.append(0)
            self.board.append(row) # add the row to the board
        # result is self.board is a list of 9 rows with each row being a list of 9 numbers (all currently 0)


    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board #board was built in the constructor

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for i in range(len(self.board[row])):
            if self.board[row][i] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for i in range(len(self.board[col])):
            if self.board[col][i] == num: #note to self: self.board is a list in a list
                return False
        return True


    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3): # +3 because we want to include the endpoint row_start + 2
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                # Find the top-left corner of the 3x3 box that (row, col) is in
                # Integer division by 3 gives us what group of 3 the row is in:
                # rows 0-2 --> group 0, rows 3-5 --> group 1, rows 6-8 --> group 2
                # Multiplying by 3 gives us the starting grid index.
                # group 0 --> start row 0, group 1 --> start row 3, group 2 --> start row 6
                row_start = (row // 3) * 3
                col_start = (col // 3) * 3
                if self.valid_in_box(row_start, col_start, num):
                    return True
            return False
        return False
    def unused_in_box(self, row_start, col_start):
        used_numbers = set() # keeps track of the numbers that have already been used
        unused_numbers = []
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                value = self.board[i][j]
                # remember that when we initialized the board, we filled it all with 0s.
                # so the if statement checks if the cell is empty since 0 represents an empty cell
                if value != 0:
                    used_numbers.add(value) # adds all non-zero numbers to the used list
        for number in range(1, 10): # iterates through numbers 1 to 9
            if number not in used_numbers: # checks if not used yet
                unused_numbers.append(number) # adds to unused list
        return unused_numbers
    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                valid_fill_numbers = self.unused_in_box(row_start, col_start)
                fill_number = random.choice(valid_fill_numbers) #picks a valid unused number at random
                self.board[i][j] = fill_number # replaces 0 with the random fill number

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        for index in range(0,9,3):
            self.fill_box(index, index) # will be (0,0), (3,3), (6,6) to fill the 3 3x3 boxes on the diagonal

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col): #did not write this code, was provided to us
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        # This is a counter how many cells are empty
        cells_cleared = 0
        row_max = self.row_length - 1
        col_max = self.row_length - 1

        # Keep going until we have removed the specified number of cells.
        while cells_cleared < self.removed_cells:
            # Randomly select a row and column index.
            row = random.randint(0, row_max)
            col = random.randint(0, col_max)

            # Check if this cell still has a number (is not already cleared, where 0 represents an empty cell).
            if self.board[row][col] != 0:
                # If it's not empty, clear the cell by setting its value to 0.
                self.board[row][col] = 0

                # adds how many sucessful clears.
                cells_cleared += 1

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''



def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board





class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0 #temporary value that the player is guessing/testing
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched_value = value
    def draw(self):
        pass

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty

        if difficulty == "easy":
            removed=30
        if difficulty == "medium":
            removed=40
        if difficulty == "hard":
            removed=50

        self.original_board=generate_sudoku(9, removed)
        self.rows=9
        self.cols=9
        self.cell_width=width//9
        self.cell_height=height//9
        self.selected=None

        self.board=[]
        for r in range(self.rows):
            row_list=[]
            for c in range(self.cols):
                value=self.original_board[r][c]
                row_list.append(Cell(value, r, c, screen))
            self.board.append(row_list)

    def draw(self):
        for row in self.board:
            for cell in row:
                cell.draw()
    #needs to be finished still

    def select(self, row, col):
        self.selected=(row, col)

    def click(self, x, y):
        if x<0 or x>self.width or y<0 or y>self.height:
            return None
        row=y//self.cell_height
        col=x//cell.cell_width
        return (row, col)

    def clear(self):
        if self.selected:
            row, col=self.selected
            if self.original_board[row][col] == 0:
                self.board[row][col].set_cell_value(0)
                self.board[row][col].set_sketched_value()

    def sketch(self, value):
        if self.selected:
            row, col=self.selected
            self.board[row][col].self.sketched_value(value)

    def place_number(self, value):
        if self.selected:
            row, col=self.selected
            if self.original_board[row][col] == 0:
                self.board[row][col].set_cell_value(value)
                self.board[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                self.board[row][col].set_cell_value(self.original_board[r][c])
                self.board[row][col].set_sketched_value(0)

    def is_full(self):
        for r in range(9):
            for c in range(9):
                if self.original_board[r][c] == 0:
                    return False
        return True

    def update_board(self):







