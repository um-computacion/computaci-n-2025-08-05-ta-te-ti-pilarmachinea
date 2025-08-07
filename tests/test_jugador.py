import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jugador import Jugador
from exceptions import FichaInvalidaException

class TestJugador(unittest.TestCase):

    def test_creacion_valida(self):
        j1 = Jugador("Pilar", "X")
        self.assertEqual(j1.obtener_nombre(), "Pilar")
        self.assertEqual(j1.obtener_ficha(), "X")

    def test_creacion_con_ficha_invalida(self):
        with self.assertRaises(FichaInvalidaException):
            Jugador("Joaquín", "Z")

    def test_creacion_con_ficha_0(self):
        j2 = Jugador("Mario", "0")
        self.assertEqual(j2.obtener_ficha(), "0")

if __name__ == '__main__':
    unittest.main()
