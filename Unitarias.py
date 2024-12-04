import pytest
import math
from Static_Balance import solution, calculate_tensions, calculate_body_position, conversor

# 3.5.1 Probar funciones individuales de cálculo
@pytest.mark.parametrize("weight, theta1, theta2, expected", [
    (100, 45, 45, (70.71, 70.71)),  # Correcto
    (50, 30, 60, (25, 43.3)),      # Corrige el orden
])
def test_solution(weight, theta1, theta2, expected):
    T1, T2 = solution(weight, theta1, theta2)
    assert math.isclose(T1, expected[0], rel_tol=1e-2)
    assert math.isclose(T2, expected[1], rel_tol=1e-2)

# 3.5.2 Verificar conversión de unidades
@pytest.mark.parametrize("Kg, expected", [
    (10, 98.1), (0, 0), (1, 9.81),
])
def test_conversor(Kg, expected):
    assert math.isclose(conversor(Kg), expected, rel_tol=1e-2)

# 3.5.3 Comprobar cálculo de tensiones
@pytest.mark.parametrize("weight, theta1, theta2, expected", [
    (100, 45, 45, (70.71, 70.71)),  # Resultado esperado basado en T1 y T2
    (50, 30, 60, (25, 43.3)),      # Resultado esperado de acuerdo a la lógica de 'calculate_tensions'
])
def test_calculate_tensions(weight, theta1, theta2, expected):
    T1, T2 = calculate_tensions(weight, theta1, theta2)
    assert math.isclose(T1, expected[1], rel_tol=1e-2)
    assert math.isclose(T2, expected[0], rel_tol=1e-2)


# 3.5.4 Validar posicionamiento de objetos
def test_calculate_body_position():
    anchor1_x, anchor2_x, anchor_y = 0, 10, 10
    T1, T2 = 70.71, 70.71
    theta1, theta2 = 45, 45

    body_x, body_y = calculate_body_position(anchor1_x, anchor2_x, anchor_y, T1, T2, theta1, theta2)
    assert body_x > 0
    assert body_y > 0
