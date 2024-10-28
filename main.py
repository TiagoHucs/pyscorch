import pygame
import sys
from settings import *
from tank import *
from sound import *

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scorched Earth Clone')

sound = Sound()

# Instanciando o tanque
tank = Tank(SCREEN_WIDTH // 2 - TANK_WIDTH, SCREEN_HEIGHT - 100 - TANK_HEIGHT)
projectiles = []

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
        if(projectile):
            projectiles.append(projectile)

    # Desenhar cenário
    draw_scenario()

    tank.update()
    tank.draw(screen)

    # remover projeteis que nao aparecem na tela
    for projectile in projectiles:
        if (projectile.x > SCREEN_WIDTH) or (projectile.x < 0) or (projectile.y > SCREEN_HEIGHT) or (projectile.y < 0):
            projectiles.remove(projectile)

    # Desenhar projeteis
    for projectile in projectiles:
        projectile.update()
        projectile.draw(screen)


    # Log de desenvolvimento na tela
    font = pygame.font.SysFont(None, 30) 
    txt2 = f"power: {tank.power} angle: {tank.angle} , projectiles: {len(projectiles)}"
    text = font.render(txt2, True, WHITE)
    screen.blit(text, (10, 10))  # (50, 100) é a posição do texto

    pygame.display.flip()