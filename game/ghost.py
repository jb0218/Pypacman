import pygame
import random
from game.settings import TILE_SIZE

class Ghost:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load(r"C:\Users\jatin\OneDrive\Desktop\python\pypacman\assets\ghost_red.png"), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.Vector2(1, 0)
        self.speed = 2

    def update(self, walls):
        next_rect = self.rect.move(self.direction * self.speed)
        if any(next_rect.colliderect(wall) for wall in walls):
            self.direction = random.choice([
                pygame.Vector2(1, 0), pygame.Vector2(-1, 0),
                pygame.Vector2(0, 1), pygame.Vector2(0, -1)
            ])
        else:
            self.rect = next_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)
