import pygame
import sys
import os
import subprocess

from game_header import *
from game_main import *


def main_menu():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_cursor(*pygame.cursors.ball)
    pygame.display.set_caption('Tic Tac Toe')
    clock = pygame.time.Clock()

    txt_title = pygame.font.Font('freesansbold.ttf', 50).render("TIC TAC TOE", True, red)
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt_singlepl, txt_singlepl_hl = font.render("Single player", True, white), font.render("Single player", True, green)
    txt_twopl, txt_twopl_hl = font.render("1 vs 1", True, white), font.render("1 vs 1", True, green)
    txt_exit, txt_exit_hl = font.render("Exit", True, white), font.render("Exit", True, green)

    rect_title = txt_title.get_rect()
    rect_singlepl, rect_singlepl_hl = txt_singlepl.get_rect(), txt_singlepl_hl.get_rect()
    rect_twopl, rect_twopl_hl = txt_twopl.get_rect(), txt_twopl_hl.get_rect()
    rect_exit, rect_exit_hl = txt_exit.get_rect(), txt_exit_hl.get_rect()

    rect_title.center = (screen_width // 2, screen_height // 2 - 60)
    rect_singlepl.center = (screen_width // 2, screen_height // 2)
    rect_singlepl_hl.center = (screen_width // 2, screen_height // 2 - 1)
    rect_twopl.center = (screen_width // 2, screen_height // 2 + 40)
    rect_twopl_hl.center = (screen_width // 2, screen_height // 2 + 39)
    rect_exit.center = (screen_width // 2, screen_height // 2 + 80)
    rect_exit_hl.center = (screen_width // 2, screen_height // 2 + 79)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_singlepl_hl.collidepoint(pos):
                    singleplayer(screen)  # modalità singleplayer
                elif rect_twopl_hl.collidepoint(pos):
                    versus(screen)  # modalità 1 vs 1
                elif rect_exit_hl.collidepoint(pos):  # esce dal gioco
                    sys.exit()

        screen.fill(black)
        screen.blit(txt_title, rect_title)

        if rect_singlepl.collidepoint(pygame.mouse.get_pos()):
            screen.blit(txt_singlepl_hl, rect_singlepl_hl)
        else:
            screen.blit(txt_singlepl, rect_singlepl)
        if rect_twopl.collidepoint(pygame.mouse.get_pos()):
            screen.blit(txt_twopl_hl, rect_twopl_hl)
        else:
            screen.blit(txt_twopl, rect_twopl)
        if rect_exit.collidepoint(pygame.mouse.get_pos()):
            screen.blit(txt_exit_hl, rect_exit_hl)
        else:
            screen.blit(txt_exit, rect_exit)

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main_menu()
