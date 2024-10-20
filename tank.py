import pygame
import logging
from settings import *

class Tank:
    
    def __init__(self, x, y, width=40, height=20, speed=0.5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def draw(self, screen):
        # Desenhar o corpo do tanque
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])
        # Desenhar o canhão
        # pygame.draw.rect(screen, (0, 0, 0), [self.x + 10, self.y - 10, 20, 10])

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def fire(self):
        print(f"Atirou da posição: {self.x},{self.y}")