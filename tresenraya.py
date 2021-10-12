import random
from os import system

casillasQueFaltan: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
casillasJugador: list = []
casillasOrdenador: list = []
filasCompletas: tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
turnoJugador: bool = False
ganar: bool = False
perder: bool = False

def tirada():
    global turnoJugador
    while ganar == False and perder == False:
        pintarTablero()
        if turnoJugador:
            turnoJugador = False
        else:
            turnoJugador = True
        if turnoJugador:
            tiraJugador()
        else:
            tiraOrdenador()

def tiraJugador():  
    n = False
    while n == False:
        casilla = input("Selecciona la casilla que quieres marcar: ".rjust(82))
        if casilla not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print()
            print("La celda seleccionada tiene que ser un valor numérico entre 1 y 9.".rjust(106))
            print()
        else:
            n = True
    casilla = int(casilla)
    if casilla not in casillasJugador and casilla not in casillasOrdenador:
        casillasJugador.append(casilla)
        casillasQueFaltan.remove(casilla)
        comprobarTirada(casilla)
    else:
        print()
        print(f"La casilla {casilla} ya está marcada.".rjust(69))
        print()
        tiraJugador()

def buscarFilas(casilla):
    filasSeleccionadas = []
    for fila in filasCompletas:
        if casilla in fila:
            filasSeleccionadas.append(fila)
    return filasSeleccionadas

def comprobarTirada(casilla):
    filasSeleccionadas = buscarFilas(casilla)
    for fila in filasSeleccionadas:
        if turnoJugador == True:
            if (fila[0] in casillasJugador and fila[1] in casillasJugador and fila[2] in casillasJugador):
                ganador()
                break
        else:
            if (fila[0] in casillasOrdenador and fila[1] in casillasOrdenador and fila[2] in casillasOrdenador):
                perdedor()
                break
    if len(casillasQueFaltan) == 0:
        empate()
    
def pintarTablero():
    a = b = d = e = e = f = g = h = i = " "
    
    a = "x" if 1 in casillasJugador else "O" if 1 in casillasOrdenador else " "
    b = "x" if 2 in casillasJugador else "O" if 2 in casillasOrdenador else " "
    c = "x" if 3 in casillasJugador else "O" if 3 in casillasOrdenador else " "
    d = "x" if 4 in casillasJugador else "O" if 4 in casillasOrdenador else " "
    e = "x" if 5 in casillasJugador else "O" if 5 in casillasOrdenador else " "
    f = "x" if 6 in casillasJugador else "O" if 6 in casillasOrdenador else " "
    g = "x" if 7 in casillasJugador else "O" if 7 in casillasOrdenador else " "
    h = "x" if 8 in casillasJugador else "O" if 8 in casillasOrdenador else " "
    i = "x" if 9 in casillasJugador else "O" if 9 in casillasOrdenador else " "
    
    system("cls")
    print("\n")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗".rjust(130, " "))
    print("║                                                                                            ║".rjust(130, " "))
    print("║                                        TRES EN RAYA                                        ║".rjust(130, " "))
    print("║                                                                                            ║".rjust(130, " "))
    print("╚════════════════════════════════════════════════════════════════════════════════════════════╝".rjust(130, " "))
    print("\n")
    print("╔═══════╦═══════╦═══════╗".rjust(95))
    print("║       ║       ║       ║".rjust(95))
    print(f"║   {a}   ║   {b}   ║   {c}   ║".rjust(95)) 
    print("║       ║       ║       ║".rjust(95))
    print("╠═══════╬═══════╬═══════╣".rjust(95))
    print("║       ║       ║       ║".rjust(95))
    print(f"║   {d}   ║   {e}   ║   {f}   ║".rjust(95))
    print("║       ║       ║       ║".rjust(95))
    print("╠═══════╬═══════╬═══════╣".rjust(95))
    print("║       ║       ║       ║".rjust(95))
    print(f"║   {g}   ║   {h}   ║   {i}   ║".rjust(95))
    print("║       ║       ║       ║".rjust(95))
    print("╚═══════╩═══════╩═══════╝".rjust(95))
    print("\n")


def tiraOrdenador():
    marca = False
    for celda in casillasOrdenador:
        if perder == False:
            filasSeleccionadas = buscarFilas(celda)
            for fila in filasSeleccionadas:
                if fila[0] in casillasOrdenador and fila[1] in casillasOrdenador and fila[2] in casillasQueFaltan:
                    casillasOrdenador.append(fila[2])
                    perdedor()
                    marca = True
                    break
                elif fila[0] in casillasOrdenador and fila[2] in casillasOrdenador and fila[1] in casillasQueFaltan:
                    casillasOrdenador.append(fila[1])
                    perdedor()
                    marca = True
                    break
                elif fila[1] in casillasOrdenador and fila[2] in casillasOrdenador and fila[0] in casillasQueFaltan:
                    casillasOrdenador.append(fila[0])
                    perdedor()
                    marca = True
                    break
    if perder == False:
        for celda in casillasJugador:
            if marca == True:
                break
            filasSeleccionadas = buscarFilas(celda)
            for fila in filasSeleccionadas:
                if fila[0] in casillasJugador and fila[1] in casillasJugador and fila[2] in casillasQueFaltan:
                    casillasOrdenador.append(fila[2])
                    casillasQueFaltan.remove(fila[2])
                    comprobarTirada(fila[2])
                    marca = True
                    break
                elif fila[0] in casillasJugador and fila[2] in casillasJugador and fila[1] in casillasQueFaltan:
                    casillasOrdenador.append(fila[1])
                    casillasQueFaltan.remove(fila[1])
                    comprobarTirada(fila[1])
                    marca = True
                    break
                elif fila[1] in casillasJugador and fila[2] in casillasJugador and fila[0] in casillasQueFaltan:
                    casillasOrdenador.append(fila[0])
                    casillasQueFaltan.remove(fila[0])
                    comprobarTirada(fila[0])
                    marca = True
                    break

    for celda in casillasOrdenador:
        if marca == True:
            break
        filasSeleccionadas = buscarFilas(celda)
        for fila in filasSeleccionadas:
            if fila[0] in casillasOrdenador and fila[1] in casillasQueFaltan and fila[2] in casillasQueFaltan:
                casilla = random.choice([fila[1], fila[2]])                 
                casillasOrdenador.append(casilla)
                casillasQueFaltan.remove(casilla)
                comprobarTirada(casilla)
                marca = True
                break
            elif fila[0] in casillasQueFaltan and fila[1] in casillasOrdenador and fila[2] in casillasQueFaltan:
                casilla = random.choice([fila[0], fila[2]])
                casillasOrdenador.append(casilla)
                casillasQueFaltan.remove(casilla)
                comprobarTirada(casilla)
                marca = True
                break
            elif fila[0] in casillasQueFaltan and fila[1] in casillasQueFaltan and fila[2] in casillasOrdenador:
                casilla = random.choice([fila[0], fila[1]])
                casillasOrdenador.append(casilla)
                casillasQueFaltan.remove(casilla)
                comprobarTirada(casilla)
                marca = True
                break
    if marca == False:    
        casilla = random.choice(casillasQueFaltan)
        casillasOrdenador.append(casilla)
        casillasQueFaltan.remove(casilla)

def reiniciar():
    global casillasQueFaltan 
    global casillasJugador
    global casillasOrdenador
    global turnoJugador
    global ganar
    global perder
    seguir = input("¿Quieres seguir jugando? (S/N): ".rjust(72))
    if seguir.upper() == "N":
        system("cls")
        system("exit")
    elif seguir.upper() == "S":
        system("cls")
        casillasQueFaltan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        casillasJugador = []
        casillasOrdenador = []
        turnoJugador = False
        ganar = False
        perder = False
        tirada()
    else:
        reiniciar()

def ganador():
    global ganar
    pintarTablero()
    print()
    print("Has ganado.".rjust(51))
    print()
    ganar = True
    reiniciar()
    
def perdedor():
    global perder
    pintarTablero()
    print()
    print("Has perdido.".rjust(52))
    print()
    perder = True
    reiniciar()
    
def empate():
    global ganar, perder
    pintarTablero()
    print()
    print("La partida ha terminado en empate.".rjust(74))
    print()
    ganar = True
    perder = True
    reiniciar()

system("cls")
tirada()