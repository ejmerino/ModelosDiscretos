"""
Batalla naval es un juego de estrategia, precision y analisas para saber en que lugar de la matriz esta el barco enemigo y poder atacarlo para ganar

Autores:
Achig Toapanta Steven Jossue

Verisión:
VER.1.2
"""

#importamos la libreria randmos para numeros randomicos
import random
import os

#Declaramos la variable fila y la inicializamos con 5
FILAS = 5
#Declaramos la variable columna y a inicializamos con 5
COLUMNAS = 5
#Declaramos la variable MAR y la inicializamos con un espacio en blanco
MAR = " "
#Declaramos la variable Submarino y la inicializamos con 'S' Ocupa una celda
SUBMARINO = "S" 
#Declaramos la variable Destructor y la inicializamos con 'D' Ocupa dos celdas
DESTRUCTOR = "D"
#Declaramos la variable Destructor vertical y la inicializamos con 'A' Ocupa dos celdas
DESTRUCTOR_VERTICAL = "A" 
#Variable disparo fallido inicializada con un -
DISPARO_FALLADO = "-"
#Variable para el disparo acertado inicializada con un *
DISPARO_ACERTADO = "*"
#numero de oportunidades para disparar
DISPAROS_INICIALES = 10
#Canrtidad de barcos a usar para los dos jugadores
CANTIDAD_BARCOS_INICIALES = 8
#Variables de los jugadores 1 y 2
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"

"""
    Es una funcion para generar la matriz inicial donde se alojaran los barcos en diferentes posiciones
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        Retorna una matriz
"""
def obtener_matriz_inicial():
    #Declaramos un arreglo con nombre matriz
    matriz = []
    #comparamos para un y en un rango tomado el valor de Filas definido antes.
    for y in range(FILAS):
        # Agregamos un arreglo a la matriz, que sería una fila básicamente
        matriz.append([])
        for x in range(COLUMNAS):
            # Y luego agregamos una celda a esa fila. Por defecto lleva "Mar"
            matriz[y].append(MAR)
            #retornamos la matriz
    return matriz


def incrementar_letra(letra):
    return chr(ord(letra)+1)

"""
    Imprimir un renglón dependiendo de las columnas
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna nada
"""
def imprimir_separador_horizontal():
    #vamos imprimiendo los renglones para imprimir la matriz de mejor manera
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")

"""
    Imprimir el separador horizontal para las celdas
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna nada
"""
def imprimir_fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")

"""
    Indica si una coordenada de la matriz está vacía
    Parametros:
    ------------
        Cordenada x
        Cordenada y
        Matriz de ingreso
    
    Retorna:
    ------------
        Retorna MAR
"""
def es_mar(x, y, matriz):
    #retorna si la coordenada esta vacia
    return matriz[y][x] == MAR

"""
    Indica si las coordenadas estan en el rango del tablero
    Parametros:
    ------------
        Cordenada x
        Cordenada y
    
    Retorna:
    ------------
        Retorna las coordenadas "x" y "y" 
"""
def coordenada_en_rango(x, y):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1

"""
    Asigna los barcos a las posiciones y los imprime.
    Parametros:
    ------------
        matriz
        cantidad de barcos
        jugador
    
    Retorna:
    ------------
        Retorna la matriz
"""
def colocar_e_imprimir_barcos(matriz, cantidad_barcos, jugador):
    # Dividimos y redondeamos a entero hacia abajo (ya que no podemos colocar una parte no entera de un barco)
    barcos_una_celda = cantidad_barcos//2
    barcos_dos_celdas_verticales = cantidad_barcos//4
    barcos_dos_celdas_horizontales = cantidad_barcos//4
    if jugador == JUGADOR_1:
        print("Imprimiendo barcos del jugador 1 ")
    else:
        print("Imprimiendo barcos del jugador 2 ")
    print(f"Barcos de una celda: {barcos_una_celda}\nBarcos verticales de dos celdas: {barcos_dos_celdas_verticales}\nBarcos horizontales de dos celdas: {barcos_dos_celdas_horizontales}\nTotal: {barcos_una_celda+barcos_dos_celdas_verticales+barcos_dos_celdas_horizontales}")
    # Primero colocamos los de dos celdas para que se acomoden bien
    matriz = colocar_barcos_de_dos_celdas_horizontal(barcos_dos_celdas_horizontales, DESTRUCTOR, matriz)
    matriz = colocar_barcos_de_dos_celdas_vertical(barcos_dos_celdas_verticales, DESTRUCTOR_VERTICAL, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, SUBMARINO, matriz)
    return matriz

"""
    Obtenemos una coordenada x aleatoria
    Parametros:
    ------------
        No tiene parametros
    
    Retorna:
    ------------
        Retorna la coordenada en X aleatoria
"""
def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS-1)

"""
    Obtenemos una coordenada y aleatoria
    Parametros:
    ------------
        No tiene parametros
    
    Retorna:
    ------------
        Retorna la coordenada en y aleatoria
"""
def obtener_y_aleatoria():
    return random.randint(0, FILAS-1)

"""
    ES una funcion que coloca los barcos que solo ocupan una celda
    Parametros:
    ------------
        cantidad de de los barcos
        tipo de barco
        la matriz donde se jugara
    
    Retorna:
    ------------
        Retorna la matriz llena
"""
def colocar_barcos_de_una_celda(cantidad, tipo_barco, matriz):
    #Definimos la variable de barcos colocados
    barcos_colocados = 0
    while True:
        #Obtenemos nuestras coordenadas x, y para colocar los barcos y hacemos el llamado a nuestras funciones anteriores
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        #Analizamos si la celda esta vacia con la funcion es mar
        if es_mar(x, y, matriz):
            #colocamos el barco en las coordenadas obtenidas anteriormente de la matriz 
            matriz[y][x] = tipo_barco
            #aumentamos el contador de barcos colocados para no colocar de mas
            barcos_colocados += 1
        #si el numero de barcos colocados es mayor a la cantidad aceptada entonces se rompe el while 
        if barcos_colocados >= cantidad:
            break
    #retornamos la matriz
    return matriz

"""
    ES una funcion que coloca los barcos que ocupan dos celdas horizontales analizando si la celda esta llena o no y si esta en el rango
    Parametros:
    ------------
        cantidad
        tipo de barco
        la matriz donde se jugara
    
    Retorna:
    ------------
        Retorna la matriz llena
"""
def colocar_barcos_de_dos_celdas_horizontal(cantidad, tipo_barco, matriz):
    #Definimos la variable de barcos colocados
    barcos_colocados = 0
    while True:
        #Obtenemos nuestras coordenadas x, y para colocar los barcos y hacemos el llamado a nuestras funciones anteriores
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        #definimos X2 como x+1 ya que este barco sera de dos celdas y horizontal por eso se incrementa el valor de x y no de "y"
        x2 = x+1
        #analizamos si las coordenadas ambas de x y x2 estan en el ranfo de la tabla y si esta vacia o no
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz):
            #si se cumple entonces asignamos llenamos la matriz en las coordenadas obtenidas
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            #aumentamos el contador de barcos colocados
            barcos_colocados += 1
        #si el numero de barcos colocados es mayor a la cantidad entonces se rompe el while y sale
        if barcos_colocados >= cantidad:
            break
        #retorna la matriz llena.
    return matriz

"""
    ES una funcion que coloca los barcos que ocupan dos celdas verticales analizando si la celda esta llena o no y si esta en el rango
    Parametros:
    ------------
        cantidad
        tipo de barco
        la matriz donde se jugara
    
    Retorna:
    ------------
        Retorna la matriz llena
"""
def colocar_barcos_de_dos_celdas_vertical(cantidad, tipo_barco, matriz):
    #Definimos la variable de barcos colocados
    barcos_colocados = 0
    while True:
        #Obtenemos nuestras coordenadas x, y para colocar los barcos y hacemos el llamado a nuestras funciones anteriores
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        #definimos y2 como y+1 ya que este barco sera de dos celdas y vertical por eso se incrementa el valor de y y no de "x"
        y2 = y+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_mar(x, y, matriz) and es_mar(x, y2, matriz):
            #si se cumple entonces asignamos llenamos la matriz en las coordenadas obtenidas
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            #aumentamos el contador de barcos colocados
            barcos_colocados += 1
        #si el numero de barcos colocados es mayor a la cantidad entonces se rompe el while y sale
        if barcos_colocados >= cantidad:
            break
    #retorna la matriz llena.
    return matriz

"""
    ES una funcion que nos imprime cuantos disparos restantes le queda a cada jugaor
    Parametros:
    ------------
        disparos restantes
        jugador
    
    Retorna:
    ------------
        No retorna
"""
def imprimir_disparos_restantes(disparos_restantes, jugador):
    print(f"Disparos restantes de {jugador}: {disparos_restantes}")

"""
    ES una funcion que nos imprime la celda de cada jugador para visibilizar mejor
    Parametros:
    ------------
        matriz
        si deberia o no mostrar los barcos
        jugador
    
    Retorna:
    ------------
        No retorna
"""
def imprimir_matriz(matriz, deberia_mostrar_barcos, jugador):
    #imprimimos de que jugador es el mar
    print(f"Este es el mar del jugador {jugador}: ")
    #variable para imprimir el tablero
    letra = "A"
    #para un y en el rango del numero de filas
    for y in range(FILAS):
        #imprimimos los separadores horizontales necesarios
        imprimir_separador_horizontal()
        #imprimimos la letra y el separador horizontal
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if not deberia_mostrar_barcos and valor_real != MAR and valor_real != DISPARO_FALLADO and valor_real != DISPARO_ACERTADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    imprimir_separador_horizontal()
    imprimir_fila_de_numeros()
    imprimir_separador_horizontal()

"""
    ES una funcion que nos pide que ingresen las coordenadas
    Parametros:
    ------------
    jugador
    Retorna:
    ------------
        la coordenada en x
        la coordenada en y
"""
def solicitar_coordenadas(jugador):
    print(f"Solicitando coordenadas de disparo al jugador {jugador}")
    # Ciclo infinito. Se rompe cuando ingresan una fila correcta
    y = None
    x = None
    while True:
        letra_fila = input(
            "Ingresa la letra de la fila tal y como aparece en el tablero: ")
        # Necesitamos una letra de 1 carácter. Si no es de 1 carácter usamos continue para repetir este ciclo
        if len(letra_fila) != 1:
            print("Debes ingresar únicamente una letra")
            continue
        # Convertir la letra a un índice para acceder a la matriz
        # La A equivale al ASCII 65, la B al 66, etcétera. Para convertir la letra a índice
        # convertimos la letra a su ASCII y le restamos 65 (el 65 es el ASCII de la A, por lo que A es 0)
        y = ord(letra_fila) - 65
        # Verificar si es válida. En caso de que sí, rompemos el ciclo
        if coordenada_en_rango(0, y):
            break
        else:
            print("Fila inválida")
    # Hacemos lo mismo pero para la columna
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1  # Queremos el índice, así que restamos un 1 siempre
                break
            else:
                print("Columna inválida")
        except:
            print("Ingresa un número válido")

    return x, y

"""
    ES una funcion que nos permite disparar o si el disaparo es acertado o fallido 
    Parametros:
    ------------
    x
    y
    matriz
    Retorna:
    ------------
        true o false
"""
def disparar(x, y, matriz) -> bool:
    if es_mar(x, y, matriz):
        matriz[y][x] = DISPARO_FALLADO
        return False
    # Si ya había disparado antes, se le cuenta como falla igualmente
    elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
        return False
    else:
        matriz[y][x] = DISPARO_ACERTADO
        return True

"""
    esta funcion nos retorna que jugador es el que esta jugando
    Parametros:
    ------------
    jugador
    Retorna:
    ------------
        Jugador
"""
def oponente_de_jugador(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    else:
        return JUGADOR_1

"""
    esta funcion nos dice si es que todos los barcos de un jugador han sido hundidos
    Parametros:
    ------------
        Matriz
    Retorna:
    ------------
        True o False
"""
def todos_los_barcos_hundidos(matriz):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != MAR and celda != DISPARO_ACERTADO and celda != DISPARO_FALLADO:
                return False
    # Acabamos de recorrer toda la matriz y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
    return True

#imprimir la victoria de un jugador
def indicar_victoria(jugador):
    print(f"Fin del juego\nEl jugador {jugador} es el ganador")

#imprimir la derrota de un jugador
def indicar_fracaso(jugador):
    print(
        f"Fin del juego\nEl jugador {jugador} pierde. Se han acabado sus disparos")

"""
    Esta funcion nos permite imprimir la matriz con los espacios ocupados por barcos o vacios
    Parametros:
    ------------
        Matriz
    Retorna:
    ------------
        True o False
"""
def imprimir_matrices_con_barcos(matriz_j1, matriz_j2):
    print("Mostrando ubicación de los barcos de ambos jugadores:")
    imprimir_matriz(matriz_j1, True, JUGADOR_1)
    imprimir_matriz(matriz_j2, True, JUGADOR_2)

"""
    En esta funcion usamos todas las funciones que hemos creado arriba para poder realizar la jugabilidad y la impresion de las matrices de cada jugador.
    Parametros:
    ------------
        No tiene
    Retorna:
    ------------
        No retorna
"""
def jugar():
    disparos_restantes_j1 = DISPAROS_INICIALES
    disparos_restantes_j2 = DISPAROS_INICIALES
    cantidad_barcos = 5
    matriz_j1, matriz_j2 = obtener_matriz_inicial(), obtener_matriz_inicial()
    matriz_j1 = colocar_e_imprimir_barcos(matriz_j1, cantidad_barcos, JUGADOR_1)
    matriz_j2 = colocar_e_imprimir_barcos(matriz_j2, cantidad_barcos, JUGADOR_2)
    turno_actual = JUGADOR_1
    print("===============")
    while True:
        print(f"Turno de {turno_actual}")
        disparos_restantes = disparos_restantes_j2
        if turno_actual == JUGADOR_1:
            disparos_restantes = disparos_restantes_j1
        imprimir_disparos_restantes(disparos_restantes, turno_actual)
        matriz_oponente = matriz_j1
        if turno_actual == JUGADOR_1:
            matriz_oponente = matriz_j2
        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        x, y = solicitar_coordenadas(turno_actual)
        acertado = disparar(x, y, matriz_oponente)
        if turno_actual == JUGADOR_1:
            disparos_restantes_j1 -= 1
        else:
            disparos_restantes_j2 -= 1

        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        if acertado:
            print("Disparo acertado")
            if todos_los_barcos_hundidos(matriz_oponente):
                indicar_victoria(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        else:
            print("Disparo fallado")
            if disparos_restantes-1 <= 0:
                indicar_fracaso(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
            turno_actual = oponente_de_jugador(turno_actual)
"""
    nos muestra un pequeño menu de opciones
    Parametros:
    ------------
        No tiene
    Retorna:
    ------------
        No retorna
"""
def mostrar_menu():
    eleccion = ""
    while eleccion != "3":
        menu = """
1. Jugar
3. Salir
Elige: """
        eleccion = input(menu)
        if eleccion == "1":
            #llamammos a la funcion jugar
            jugar()
#llamamos ala funcion menu ¿
mostrar_menu()