import pygame
import sys
from game.settings import *
from game.pacman import Pacman
from game.ghost import Ghost
from game.board import Board

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Py-Pacman")

board = Board(LEVEL_FILE)
pacman = Pacman(*board.pacman_pos)
ghosts = [Ghost(*pos) for pos in board.ghost_pos]
score = 0
font = pygame.font.SysFont(None, 36)

def draw_score():
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pacman.update(board.walls)
    for ghost in ghosts:
        ghost.update(board.walls)

    for dot in board.dots[:]:
        if pacman.rect.colliderect(dot):
            board.dots.remove(dot)
            score += 10

    for ghost in ghosts:
        if pacman.rect.colliderect(ghost.rect):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    board.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)
