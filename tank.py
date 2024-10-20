import pygame
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
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.height])
        # Desenhar o canhão
        # pygame.draw.rect(screen, (0, 0, 0), [self.x + 10, self.y - 10, 20, 10])

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