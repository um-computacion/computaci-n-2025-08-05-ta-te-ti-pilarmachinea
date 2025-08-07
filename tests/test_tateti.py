import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tateti import Tateti
from exceptions import PosOcupadaException, JuegoTerminadoException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti("Ana", "Luis")

    def test_jugadores_creados_correctamente(self):
        self.assertEqual(self.juego.jugador1.obtener_nombre(), "Ana")
        self.assertEqual(self.juego.jugador2.obtener_nombre(), "Luis")

    def test_turno_inicial_es_jugador1(self):
        self.assertEqual(self.juego.obtener_jugador_turno(), self.juego.jugador1)

    def test_ocupar_casilla_valida_y_cambiar_turno(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
        self.assertEqual(self.juego.obtener_jugador_turno(), self.juego.jugador2)

    def test_no_permite_repetir_casilla(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_juego_terminado_lanza_excepcion(self):
        # Simular que el jugador 1 gana en la primera fila
        self.juego.tablero.contenedor = [
            ["X", "X", ""],
            ["0", "0", ""],
            ["", "", ""]
        ]
        self.juego.obtener_jugador_turno = self.juego.jugador1
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X completa la fila y gana

        with self.assertRaises(JuegoTerminadoException):
            self.juego.ocupar_una_de_las_casillas(1, 2)

        self.assertTrue(self.juego.juego_terminado)
    def test_empate(self):
        jugadas = [
            (0, 0),  # X
            (0, 1),  # 0
            (0, 2),  # X
            (1, 1),  # 0
            (1, 0),  # X
            (1, 2),  # 0
            (2, 1),  # X
            (2, 0),  # 0
            (2, 2),  # X
        ]
        for fila, col in jugadas:
            self.juego.ocupar_una_de_las_casillas(fila, col)

        self.assertTrue(self.juego.juego_terminado, "El juego debería estar marcado como terminado.")
        with self.assertRaises(Exception): 
            self.juego.ocupar_una_de_las_casillas(0, 0)

if __name__ == '__main__':
    unittest.main()
