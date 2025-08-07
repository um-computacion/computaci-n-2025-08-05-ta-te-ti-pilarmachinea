from tateti import Tateti

class PosicionInvalidaException(Exception):
    pass

def pedir_coordenada(nombre_jugador, tipo):
    try:
        valor = int(input(f"{nombre_jugador}, ingrese la {tipo} (0 a 2): "))
        if valor < 0 or valor > 2:
            raise PosicionInvalidaException("La coordenada debe estar entre 0 y 2.")
        return valor
    except ValueError:
        raise PosicionInvalidaException("Debes ingresar un número entero válido.")


def main():
    print("Bienvenidos al Tateti")
    nombre1=input("Ingrese el nombre de jugador 1 (X): ")
    nombre2=input("Ingrese el nombre de jugador 2 (O): ")
    juego = Tateti(nombre1, nombre2)

    while True:
        print("Tablero:")
        for fila in juego.tablero.contenedor:
            print(fila)

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