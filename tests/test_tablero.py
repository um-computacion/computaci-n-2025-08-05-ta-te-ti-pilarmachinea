import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tablero import Tablero
from exceptions import PosOcupadaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_arranca_vacio(self):
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")

    def test_poner_ficha_en_posicion_valida(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        self.assertEqual(self.tablero.contenedor[1][1], "X")

    def test_poner_ficha_en_posicion_ocupada_lanza_excepcion(self):
        self.tablero.poner_la_ficha(2, 2, "0")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(2, 2, "X")

if __name__ == '__main__':
    unittest.main()
