from tablero import Tablero
from jugador import Jugador
from exceptions import JuegoTerminadoException

class Tateti:
    def __init__(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        self.jugador1 = Jugador(nombre_jugador1, "X")
        self.jugador2 = Jugador(nombre_jugador2, "0")
        self.turno = self.jugador1
        self.tablero = Tablero()
        self.juego_terminado = False

    def ocupar_una_de_las_casillas(self, fila, columna):
        if self.juego_terminado:
            raise JuegoTerminadoException("El juego ya terminó")
        ficha = self.turno.obtener_ficha()
        self.tablero.poner_la_ficha(fila, columna, ficha)

        if self._hay_ganador_():
            self.juego_terminado = True
            print(f"El jugador {self.obtener_nombre_jugador_turno()} ha ganado.")
            return
        
        if self._tablero_lleno_():
            self.juego_terminado = True
            print(f"Empate!")
            return
        
        self.cambiar_turno()

    def cambiar_turno(self):
        self.turno = self.jugador2 if self.turno == self.jugador1 else self.jugador1

    def obtener_jugador_turno(self):
        return self.turno
    
    def obtener_nombre_jugador_turno(self):
        return self.turno.obtener_nombre()
    
    def obtener_ficha_jugador_turno(self):
        return self.turno.obtener_ficha()
    
    def _hay_ganador_(self):
        c = self.tablero.contenedor
        f = self.turno.obtener_ficha()

        for fila in c:
            if fila == [f, f, f]:
                return True
            
        for i in range(3):
            if [c[0][i], c[1][i], c[2][i]] == [f, f, f]:
                return True
        if [c[0][0], c[1][1], c[2][2]] == [f, f, f]:
            return True
        if [c[0][2], c[1][1], c[2][0]] == [f, f, f]:
            return True
        return False

    def _tablero_lleno_(self):
        return all(c != "" for fila in self.tablero.contenedor for c in fila)
