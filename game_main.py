import time
import random
from game_header import *
import pygame
import sys

from game_menu import *


def draw_grid(screen):
    screen.fill(black)

    pygame.draw.rect(screen, grid_color, oriz_line_1)
    pygame.draw.rect(screen, grid_color, oriz_line_2)
    pygame.draw.rect(screen, grid_color, vert_line_1)
    pygame.draw.rect(screen, grid_color, vert_line_2)
    pygame.draw.rect(screen, grid_color, top_border)
    pygame.draw.rect(screen, grid_color, bottom_border)
    pygame.draw.rect(screen, grid_color, left_border)
    pygame.draw.rect(screen, grid_color, right_border)


def draw_cross(screen, x, y):
    begin_line0x = x - (screen_width / 6 - grid_thickness * 2)
    begin_line0y = y - (screen_height / 6 - grid_thickness * 2)
    end_line0x = x + (screen_width / 6 - grid_thickness * 2)
    end_line0y = y + (screen_height / 6 - grid_thickness * 2)

    begin_line1x = x - (screen_width / 6 - grid_thickness * 2)
    begin_line1y = y + (screen_height / 6 - grid_thickness * 2)
    end_line1x = x + (screen_width / 6 - grid_thickness * 2)
    end_line1y = y - (screen_height / 6 - grid_thickness * 2)

    cross_line0 = [(begin_line0x, begin_line0y), (end_line0x, end_line0y)]
    cross_line1 = [(begin_line1x, begin_line1y), (end_line1x, end_line1y)]

    pygame.draw.lines(screen, blue, False, cross_line0, grid_thickness)
    pygame.draw.lines(screen, blue, False, cross_line1, grid_thickness)


def draw_circle(screen, x, y):
    pygame.draw.circle(screen, red, (int(x), int(y)), int(screen_width / 6 - grid_thickness * 2), grid_thickness)


def get_cell(x, y):
    x_vert_line1 = (screen_width - 2 * grid_thickness) / 3 + grid_thickness
    x_vert_line2 = (screen_width - 2 * grid_thickness) / 3 * 2 + grid_thickness
    y_vert_line1 = (screen_height - 2 * grid_thickness) / 3 + grid_thickness
    y_vert_line2 = (screen_height - 2 * grid_thickness) / 3 * 2 + grid_thickness
    if x < x_vert_line1 and y < y_vert_line1:
        return 0
    elif x_vert_line1 < x < x_vert_line2 and y < y_vert_line1:
        return 1
    elif x > x_vert_line2 and y < y_vert_line1:
        return 2
    elif x < x_vert_line1 and y_vert_line1 < y < y_vert_line2:
        return 3
    elif x_vert_line1 < x < x_vert_line2 and y_vert_line1 < y < y_vert_line2:
        return 4
    elif x > x_vert_line2 and y_vert_line1 < y < y_vert_line2:
        return 5
    elif x < x_vert_line1 and y > y_vert_line2:
        return 6
    elif x_vert_line1 < x < x_vert_line2 and y > y_vert_line2:
        return 7
    else:
        return 8


def check_victory(grid):
    for i in range(0, 3):
        if grid[i] == grid[i + 3] == grid[i + 6]:
            return True, grid[i], cells[i], cells[i + 6]
    for i in range(0, 7, 3):
        if grid[i] == grid[i + 1] == grid[i + 2]:
            return True, grid[i], cells[i], cells[i + 2]
    if grid[0] == grid[4] == grid[8]:
        return True, grid[0], cells[0], cells[8]
    if grid[2] == grid[4] == grid[6]:
        return True, grid[2], cells[2], cells[6]
    occupied = True
    for i in range(0, 9):
        occupied &= grid[i] == 'x' or grid[i] == 'o'
    if occupied:
        return True, "", (0, 0), (0, 0)
    return False, "", (0, 0), (0, 0)


def render_winner(screen, winner, is_singleplayer):
    font = pygame.font.Font('freesansbold.ttf', 32)
    if winner == 'x' and is_singleplayer:
        text = font.render("You win!", True, blue, black)
    elif winner == 'x':
        text = font.render("'X' player wins!", True, blue, black)
    elif winner == 'o' and is_singleplayer:
        text = font.render("CPU wins!", True, red, black)
    elif winner == 'o':
        text = font.render("'O' player wins!", True, red, black)
    else:
        text = font.render("Draw!", True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.fill(black)
    screen.blit(text, text_rect)


def versus(screen):
    clock = pygame.time.Clock()
    grid = list(range(0, len(cells)))
    turn = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cell_index = get_cell(*pygame.mouse.get_pos())
                if 'o' != grid[cell_index] != 'x':
                    turn = (turn + 1) % 2
                    if turn == 0:
                        grid[cell_index] = 'x'
                    else:
                        grid[cell_index] = 'o'

        draw_grid(screen)

        for i in range(0, len(cells)):
            if grid[i] == 'x':
                draw_cross(screen, *cells[i])
            elif grid[i] == 'o':
                draw_circle(screen, *cells[i])

        victory, winner, start, end = check_victory(grid)
        if victory:
            pygame.draw.line(screen, green, start, end, grid_thickness)
            pygame.display.update()
            time.sleep(2)
            render_winner(screen, winner, False)
            pygame.display.update()
            time.sleep(3)
            return  # ritorna al menu

        pygame.display.update()
        clock.tick(10)


def singleplayer(screen):
    clock = pygame.time.Clock()
    grid = list(range(0, len(cells)))
    turn = 0

    draw_grid(screen)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1:
                cell_index = get_cell(*pygame.mouse.get_pos())
                if 'o' != grid[cell_index] != 'x':
                    grid[cell_index] = 'x'
                turn = (turn + 1) % 2

        if turn == 0:
            turn = (turn + 1) % 2
            while 1:
                cpu_cell = random.randint(0, len(grid) - 1)
                if 'o' != grid[cpu_cell] != 'x':
                    grid[cpu_cell] = 'o'
                    break

        draw_grid(screen)

        for i in range(0, len(cells)):
            if grid[i] == 'x':
                draw_cross(screen, *cells[i])
            elif grid[i] == 'o':
                draw_circle(screen, *cells[i])

        victory, winner, start, end = check_victory(grid)
        if victory:
            pygame.draw.line(screen, green, start, end, grid_thickness)
            pygame.display.update()
            time.sleep(2)
            render_winner(screen, winner, True)
            pygame.display.update()
            time.sleep(3)
            return  # ritorna al menu

        pygame.display.update()
        clock.tick(10)
