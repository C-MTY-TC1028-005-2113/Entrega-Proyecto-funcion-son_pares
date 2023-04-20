# Nombre -
# Matricula -
# Carrera -
figura = "?"


def  despliega_tablero(opcion, matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    print(matriz)

def son_pares(opcion, tablero, escondidas, r1, c1, r2, c2):
    # destapar las cartas en el tablero
    # desplegar_tablero resaltando las cartas seleccionadas
    # verificar si son pares
    # si si son pares asignar a la variable puntos = 1
    #     desplegar "Par"
    # si no son pares asignar a  puntos = 0
    #     desplegar "Impar"
    #     volver a tapar las cartas en el tablero
    pass

def main() :
    # 1º Leer los datos de entrada
    caso = int(input())
    if caso == 1:
        pares_jugador1 = 0
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = 0,0,3,0
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print("Pares Jugador1:",pares_jugador1)
    elif caso == 2:
        pares_jugador1 = 10
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['a', 'b', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = 4,1,1,1
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print("Pares Jugador2:",pares_jugador1)
    elif caso == 3:
        pares_jugador1 = 5
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = 1, 2, 5, 5
        pares_jugador1 += son_pares(1,tablero, escondidas,r1,c1,r2,c2)
        print("Pares Jugador23:",pares_jugador1)
    


if __name__=='__main__':
    main()
