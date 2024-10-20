import pygame
import math
from settings import *

class Projectile:
    
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.initial_angle = angle
        self.power = power

        # Converter ângulo para radianos
        angulo_rad = math.radians(angle)
        
        # Calcular velocidades
        self.speed_x = power * math.cos(angulo_rad)
        self.speed_y = power * math.sin(angulo_rad)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, self.width, self.height])

    def update(self):
        self.speed_y = self.speed_y - GRAVITY
        self.x += self.speed_x 
        self.y -= self.speed_y