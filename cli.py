from tateti import Tateti

class PosicionInvalidaException(Exception):
    pass

def pedir_coordenada(nombre_jugador, tipo):
    try:
        valor = int(input(f"{nombre_jugador}, ingrese la {tipo} (1 a 3): "))
        if valor < 1 or valor > 3:
            raise PosicionInvalidaException("La coordenada debe estar entre 1 y 3.")
        return valor - 1
    except ValueError:
        raise PosicionInvalidaException("Debes ingresar un número entero válido.")

def mostrar_tablero(tablero):
    print("\nTablero:")
    for i, fila in enumerate(tablero.contenedor):
        linea = " | ".join(casilla if casilla != "" else " " for casilla in fila)
        print(" " + linea)
        if i < 2:
            print("---+---+---")

def main():
    print("Bienvenidos al Tateti")
    nombre1=input("Ingrese el nombre de jugador 1 (X): ")
    nombre2=input("Ingrese el nombre de jugador 2 (O): ")
    juego = Tateti(nombre1, nombre2)

    while True:
        mostrar_tablero(juego.tablero)

        if juego.juego_terminado:
            print("El juego ha terminado.")
            break

        jugador_actual = juego.obtener_jugador_turno()
        print(f"El jugador actual es {jugador_actual.obtener_nombre()} ({jugador_actual.obtener_ficha()})")

        try:
            fila = pedir_coordenada(jugador_actual.obtener_nombre(), "fila")
            columna = pedir_coordenada(jugador_actual.obtener_nombre(), "columna")
            juego.ocupar_una_de_las_casillas(fila, columna)
        except Exception as e:
            print(e)
    
if __name__ == '__main__':
    main()