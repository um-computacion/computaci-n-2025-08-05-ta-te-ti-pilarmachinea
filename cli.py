from tateti import Tateti

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("Tablero: ")
        print(juego.tablero.contenedor)
        print("Turno: ")
        print(juego.turno)
        try:
            fil = int(input("Ingrese fila"))
            col = int(input("Ingrese col"))
            juego.ocupar_una_de_las_casillas(fil, col)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()