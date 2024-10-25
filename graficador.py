import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import pygame

class Graficador:
    @staticmethod
    def crear_grafico(peso, theta1, theta2, T11, T22):
        plt.switch_backend('Agg')
        fig = plt.figure(figsize=(300/100, 300/100), dpi=100)
        ax = fig.add_subplot(111)

        theta1_rad = math.radians(theta1)
        theta2_rad = math.radians(theta2)
        ancla1_x, ancla2_x = 0, 10
        ancla_y = 10
        cuerpo_x = (ancla1_x + ancla2_x) / 2
        cuerpo_y = ancla_y - 5

        ax.plot([cuerpo_x], [cuerpo_y], 'ro', markersize=10)
        ax.quiver(cuerpo_x, cuerpo_y, 0, -1, scale=3, color='g', width=0.005, label=f'Peso: {peso:.2f}N')
        ax.quiver(cuerpo_x, cuerpo_y, math.cos(theta1_rad), math.sin(theta1_rad), scale=2, color='b', width=0.005, label=f'Angulo 1: {theta1}')
        ax.quiver(cuerpo_x, cuerpo_y, -math.cos(theta2_rad), math.sin(theta2_rad), scale=2, color='r', width=0.005, label=f'Angulo 2: {theta2}')
        
        ax.set_xlim(-2, 12)
        ax.set_ylim(0, 12)
        ax.set_aspect('equal')
        ax.legend(fontsize='x-small')
        ax.set_title('Diagrama de Equilibrio', fontsize='small')
        ax.grid(True)
        plt.tight_layout()

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        plt.close(fig)

        return pygame.image.fromstring(raw_data, size, "RGB")