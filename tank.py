import pygame
import math
from settings import *
from projectile import *

class Tank:
    
    def __init__(self, x, y, width=40, height=20, speed=0.5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.angle = 0
        self.power = 0

    def draw(self, screen):
        # Desenhar o corpo do tanque
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height])
        
        
        # Tamanho da linha e ângulo (em graus)
        canon_size = 20
        canon_diam = 5

        # Converter o ângulo para radianos
        angle_radians = math.radians(self.angle)

        # Calcular as coordenadas finais com base no ângulo e no comprimento da linha
        # Ponto inicial da linha
        start_pos = (self.x + (self.width // 2), self.y)
        
        end_pos = (
            start_pos[0] + canon_size * math.cos(angle_radians), 
            start_pos[1] - canon_size * math.sin(angle_radians)  # O eixo Y cresce para baixo no Pygame
        )
        
        # Desenhar o canhão
        pygame.draw.line(screen, RED, start_pos, end_pos, canon_diam)

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def increase_angle(self):
        self.angle += 1
        if self.angle > 180:
            self.angle = 180

    def decrease_angle(self):
        self.angle -= 1
        if self.angle < 0:
            self.angle = 0

    def increase_power(self):
        self.power += 1
        if self.power > 1000:
            self.power = 1000

    def decrease_power(self):
        self.power -= 1
        if self.power < 0:
            self.power = 0

    def fire(self):
        return Projectile(self.x + self.width // 2 ,self.y,0.5)