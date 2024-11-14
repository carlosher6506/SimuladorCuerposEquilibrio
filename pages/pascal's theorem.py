import pygame
import sys

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Cargar imágenes
fondo_img = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrio/img/cuerpo2.png")  # Fondo de la interfaz
contenedor_img = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrio/img/Impulsador.jpg")  # Contenedor del agua
cargamento_img = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrio/img/cargamento.jpg")  # Imagen del objeto que se eleva

# Variables del simulador
water_level = 0  # Nivel inicial de agua
pressure = 0     # Presión inicial
piston_area = 50 # Área del pistón (para cálculo de presión)
max_water_level = 300  # Nivel máximo de agua
adding_water = False   # Indicador para activar la animación de llenado automático

# Ajustar el tamaño de las imágenes si es necesario
fondo_img = pygame.transform.scale(fondo_img, (800, 600))
contenedor_img = pygame.transform.scale(contenedor_img, (200, 300))
cargamento_img = pygame.transform.scale(cargamento_img, (150, 100))  # Ajusta el tamaño del objeto

# Ciclo principal
running = True
while running:
    screen.blit(fondo_img, (0, 0))  # Dibuja el fondo

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and water_level < max_water_level:
                adding_water = True  # Activar animación de llenado

    # Actualización de la animación de agua
    if adding_water:
        if water_level < max_water_level:
            water_level += 1  # Incremento gradual en el nivel de agua
            pressure = (water_level * 9.8) / piston_area  # Cálculo de presión
        else:
            adding_water = False  # Detener llenado al alcanzar el nivel máximo

    # Dibujo de elementos visuales
    screen.blit(contenedor_img, (100, 100))  # Dibuja el contenedor
    pygame.draw.rect(screen, (0, 0, 255), (100, 400 - water_level, 200, water_level))  # Agua como rectángulo azul
    screen.blit(cargamento_img, (130, 400 - water_level - cargamento_img.get_height()))  # Coloca el objeto encima del agua

    # Texto para mostrar valores de presión
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Presión: {pressure:.2f} Pa", True, (0, 0, 0))
    print(pressure)
    screen.blit(text_surface, (500, 50))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS para una animación suave

pygame.quit()
sys.exit()
