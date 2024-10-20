import pygame
import sys
from settings import *
from tank import *

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scorched Earth Clone')

# Instanciando o tanque e o projétil
tank = Tank(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 100 - 20)
projectile = {}

# Função para desenhar o cenário
def draw_scenario():
    screen.fill(BLUE)  # Céu
    pygame.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100])  # Terreno

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        tank.move("LEFT")
    if keys[pygame.K_d]:
        tank.move("RIGHT")
    if keys[pygame.K_LEFT]:
        tank.increase_angle()
    if keys[pygame.K_RIGHT]:
        tank.decrease_angle()
    if keys[pygame.K_UP]:
        tank.increase_power()
    if keys[pygame.K_DOWN]:
        tank.decrease_power()
    if keys[pygame.K_SPACE]:
        projectile = tank.fire()

    # Desenhar cenário, tanque e projétil
    draw_scenario()

    tank.draw(screen)

    if projectile:
        projectile.update()
        projectile.draw(screen)

    font = pygame.font.SysFont(None, 30) 
    txt2 = f"power: {tank.power} angle: {tank.angle}"
    text = font.render(txt2, True, WHITE)
    screen.blit(text, (10, 10))  # (50, 100) é a posição do texto

    pygame.display.flip()