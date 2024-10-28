import pygame
import math
from settings import *
from projectile import *
from sound import *

class Tank:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = TANK_WIDTH
        self.height = TANK_HEIGHT
        self.speed = 0.5
        self.angle = 0
        self.power = TANK_MIN_POWER
        self.reload_time = TANK_RELOAD_TIME
        self.sound = Sound()

    def draw(self, screen):
        # Desenhar o corpo do tanque
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height])
        
        # Tamanho da linha e ângulo (em graus)
        canon_size = TANK_WIDTH / 2
        canon_diam = 2

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

    def update(self):
        if self.reload_time < TANK_RELOAD_TIME:
            self.reload_time += 1

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def increase_angle(self):
        self.angle += TANK_ANGLE_STEP
        if self.angle > 180:
            self.angle = 180

    def decrease_angle(self):
        self.angle -= TANK_ANGLE_STEP
        if self.angle < 0:
            self.angle = 0

    def increase_power(self):
        self.power += TANK_POWER_STEP
        if self.power > TANK_MAX_POWER:
            self.power = TANK_MAX_POWER

    def decrease_power(self):
        self.power -= TANK_POWER_STEP
        if self.power < TANK_MIN_POWER:
            self.power = TANK_MIN_POWER

    def fire(self):
        if (self.reload_time == TANK_RELOAD_TIME) and (self.power > 0):
            self.reload_time = 0
            self.sound.shotgun.play()
            return Projectile(self.x + self.width // 2 ,self.y, self.angle, self.power)
