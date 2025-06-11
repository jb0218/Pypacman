import pygame
from game.settings import TILE_SIZE, YELLOW

class Pacman:
    def __init__(self, x, y):
        self.image = pygame.image.load(r"C:\Users\jatin\OneDrive\Desktop\python\pypacman\assets\pacman.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 4

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1, 0)
        elif keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 1)

    def update(self, walls):
        self.handle_keys()
        next_rect = self.rect.move(self.direction * self.speed)
        if not any(next_rect.colliderect(wall) for wall in walls):
            self.rect = next_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)
