import pygame
import sys

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Variables del simulador
piston_height = 100  # Altura inicial del pistón
water_level = 0  # Nivel inicial de agua
pressure = 0  # Presión inicial
piston_area = 50  # Área del pistón
max_water_level = 300  # Nivel máximo de agua

# Ciclo principal
running = True
while running:
    screen.fill((255, 255, 255))  # Fondo blanco

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and water_level < max_water_level:
                water_level += 10  # Aumentar agua con flecha arriba
                pressure = (water_level * 9.8) / piston_area  # Ejemplo de cálculo de presión
                piston_height -= pressure  # Elevar pistón según presión

    # Dibujo de elementos en pantalla
    pygame.draw.rect(screen, (0, 0, 255), (100, 400 - water_level, 200, water_level))  # Agua
    pygame.draw.rect(screen, (150, 150, 150), (100, 400 - piston_height, 200, 20))  # Pistón

    # Texto para mostrar valores
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Presión: {pressure:.2f} Pa", True, (0, 0, 0))
    screen.blit(text_surface, (500, 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()