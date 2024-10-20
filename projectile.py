import pygame
from settings import *

class Projectile:
    
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, self.width, self.height])

    def update(self):
        self.x += self.speed
        self.y -= self.speed
