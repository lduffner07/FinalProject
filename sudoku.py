from sudoku_generator import SudokuGenerator
import pygame
#all of the following code is just to test if my functions are working
def main():
    generator = SudokuGenerator(9, 30)


    board = generator.fill_box(0,0)
    board = generator.print_board()
    pygame.init()
    screen = pygame.display.set_mode(size = (500,500))

if __name__ == "__main__":
    main()
    while True:
        pygame.display.update()

