# main.py
import sys
import pygame
from sudoku_generator import Board   # change this if your file name is different

WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
BOARD_SIZE = 540  # top 540x540 area is the Sudoku board


def draw_start_screen(screen, font):
    screen.fill((255, 255, 255))  # white background

    # Title and subtitle text
    # both are essentially images with the text on it
    title_text = font.render("Welcome to Sudoku", True, (0, 0, 0))  # black font
    mode_text = font.render("Select Game Mode:", True, (0, 0, 0))   # black font

    # copies the images from title_text and mode_text onto the screen
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 80))
    screen.blit(mode_text, (WINDOW_WIDTH // 2 - mode_text.get_width() // 2, 150))

    # Three buttons: EASY, MEDIUM, HARD
    button_width = 120
    button_height = 50
    gap = 20  # gap between buttons
    total_width = 3 * button_width + 2 * gap # width spanning between the 3 buttons
    start_x = WINDOW_WIDTH // 2 - total_width // 2
    y = 250

    easy_rect = pygame.Rect(start_x, y, button_width, button_height)
    med_rect = pygame.Rect(start_x + button_width + gap, y, button_width, button_height)
    hard_rect = pygame.Rect(start_x + 2 * (button_width + gap), y, button_width, button_height)

    for rect, label in [(easy_rect, "EASY"), (med_rect, "MEDIUM"), (hard_rect, "HARD")]:
        pygame.draw.rect(screen, (210, 140, 80), rect)      # brownish button
        text = font.render(label, True, (0, 0, 0))          # black font
        screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

    pygame.display.flip() # draws everything you see on the screen
    return easy_rect, med_rect, hard_rect



