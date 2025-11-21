from sudoku_generator import SudokuGenerator

def main():
    generator = SudokuGenerator(9, 30)

    # For now, maybe just print the empty board (or later: generate, remove, etc.)
    board = generator.print_board()
if __name__ == "__main__":
    main()

