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
    
    if keys[pygame.K_LEFT]:
        tank.move("LEFT")
    if keys[pygame.K_RIGHT]:
        tank.move("RIGHT")
    if keys[pygame.K_SPACE]:
        tank.fire()

    # Desenhar cenário, tanque e projétil
    draw_scenario()
    tank.draw(screen)

    pygame.display.flip()