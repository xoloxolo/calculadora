# Importamos unittest para crear los tests
from unittest import TestCase
# Importamos las funciones del programa
from src.utils import area_of_circle, area_of_triangle, perimeter_of_triangle, calculate

# Creamos una clase para los tests
class TestUtils(TestCase):

    # Test para la función area_of_circle
    def test_area_of_circle(self):
        self.assertEqual(area_of_circle(2.0), 125.066)

    # Test para la función area_of_triangle
    def test_area_of_triangle(self):
        self.assertEqual(area_of_triangle(10, 5), 25)
    
    # Test para la función perimeter_of_triangle
    def test_perimeter_of_triangle(self):
        self.assertEqual(perimeter_of_triangle(3, 4, 5), 12)
    
    # Test para la función calculate
    def test_calculate(self):
        self.assertEqual(calculate("2+3"), 5.0)
        