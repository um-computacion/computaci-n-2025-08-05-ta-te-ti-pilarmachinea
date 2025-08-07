from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        self.jugador1 = Jugador(nombre_jugador1, "X")
        self.jugador2 = Jugador(nombre_jugador2, "0")
        self.turno = self.jugador1
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fila, columna):
        ficha = self.turno.obtener_ficha()
        self.tablero.poner_la_ficha(fila, columna, ficha)
        self.cambiar_turno()

    def cambiar_turno(self):
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1

    def obtener_jugador_turno(self):
        return self.turno
    
    def obtener_nombre_jugador_turno(self):
        return self.turno.obtener_nombre()
    
    def obtener_ficha_jugador_turno(self):
        return self.turno.obtener_ficha()
