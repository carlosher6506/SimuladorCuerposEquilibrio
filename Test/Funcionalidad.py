import pygame
import pytest
from Static_Balance import draw_scene, conversor, crear_grafico

# Prueba de inicialización de Pygame
def test_pygame_initialization():
    pygame.init()
    screen = pygame.display.set_mode((1350, 840))
    assert screen is not None, "No se pudo inicializar la ventana de Pygame"
    pygame.quit()

# Prueba de renderizado de escena
def test_scene_render():
    pygame.init()
    screen = pygame.Surface((1350, 840))  # Superficie para pruebas
    draw_scene(screen, weight=100, theta1=45, theta2=45, result_conversion=0, conversor_visible=False)
    # Actualizar el color esperado
    assert screen.get_at((10, 10)) == (0, 71, 125, 255), "El fondo no se renderizó correctamente"
    pygame.quit()


# Prueba del conversor
def test_conversion_kg_to_n():
    result = conversor(10)  # Convertir 10 kg a N
    assert result == pytest.approx(98.1, rel=1e-3), f"Conversión incorrecta, esperado 98.1, obtenido {result}"


def test_graph_generation():
    peso = 100
    theta1 = 45
    theta2 = 45
    T11, T22 = 70.71, 70.71  # Valores esperados para estas condiciones
    grafico = crear_grafico(peso, theta1, theta2, T11, T22)
    
    assert grafico.get_width() > 0 and grafico.get_height() > 0, "El gráfico no se generó correctamente"