import pygame
from game.settings import TILE_SIZE, BLUE

class Board:
    def __init__(self, level_path):
        self.walls = []
        self.dots = []
        self.pacman_pos = None
        self.ghost_pos = []

        with open(level_path, 'r') as file:
            lines = file.readlines()

        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line.strip()):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
                if char == 'W':
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif char == '.':
                    self.dots.append(pygame.Rect(x+TILE_SIZE//3, y+TILE_SIZE//3, TILE_SIZE//3, TILE_SIZE//3))
                elif char == 'P':
                    self.pacman_pos = (x, y)
                elif char == 'G':
                    self.ghost_pos.append((x, y))

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)
        for dot in self.dots:
            pygame.draw.circle(screen, (255, 255, 255), dot.center, 4)
