"""
Batalla naval es un juego de estrategia, precision y analisas para saber en que lugar de la matriz esta el barco enemigo y poder atacarlo para ganar
Dilema de las Ocho Reinas en un tablero de ajedrez. Este problema lógico indica que se deben colocar en un tablero de ajedrez 8 reinas, de forma que ninguna amenace a otra. 
Torres de Equilibrio: El juego consistirá en que primero se generará un numero aleatorio del 1 al 20, será el valor que quede en el centro e inicia el juego,
se generará otro número aleatorio el cual si es mayor irá en la parte de arriba, caso contrario si es menor irá debajo del centro, los
números se pueden repetir, si un número se repite se colocará al lado del mismo número repetido, el objetivo del juego es conseguir 2
números iguales al del centro, es decir, para ganar se necesitará que el número en el caso que se consiga 3 números iguales 
Autores:
Achig Toapanta Steven Jossue
Merino Calderón Ednan Josué
Condor Kevin

Verisión:
VER.1.3
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
"""
    Nos funciona como un contadora para cambiar o aumentar la posicion en la que nos encontremos con una letra A, B, C, D, E. Retorna una letra despues de la que se ingreso es decir si ingresa la A entonces retornara B
    Parametros:
    ------------
        La letra que hayamos mandado.
    
    Retorna:
    ------------
        retorna una letra despues de la que se ingreso
"""
def incrementar_letra(letra):
    return chr(ord(letra)+1)

"""
    Imprimir un renglón dependiendo de las columnas para una mejor vista de la matriz
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
    Imprimir la fila de numeros y los separadores verticales
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
    Indica si una coordenada de la matriz está vacía o no
    Parametros:
    ------------
        Cordenada x
        Cordenada y
        Matriz de ingreso
    
    Retorna:
    ------------
        Retorna MAR si esta vacia o no.
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
def colocar_e_imprimir_barcos(matriz, cantidad_barcos):
    # Dividimos y redondeamos a entero hacia abajo (ya que no podemos colocar una parte no entera de un barco)
    barcos_una_celda = cantidad_barcos//2
    barcos_dos_celdas_verticales = cantidad_barcos//4
    barcos_dos_celdas_horizontales = cantidad_barcos//4
    print("Imprimiendo barcos ")
    #imprimimos que barcos son los que se ingresaran
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
    ES una funcion que nos imprime la celda de cada jugador para visibilizar mejor
    Parametros:
    ------------
        matriz a imprimir
        si deberia o no mostrar los barcos
    Retorna:
    ------------
        No retorna
"""
def imprimir_matriz(matriz, deberia_mostrar_barcos):
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
    ES una funcion que nos pide que ingresen las coordenadas, ademas que valida si las coordenadas ingresadas estan dentro del rango de opciones 
    Parametros:
    ------------
    jugador
    Retorna:
    ------------
        la coordenada en x
        la coordenada en y
"""
def solicitar_coordenadas():
    print(f"Solicitando coordenadas de disparo al jugador")
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
            #se rompe ciclo 
            break
        else:
            #inprime fila invalida
            print("Fila inválida")
    # Hacemos lo mismo pero para la columna
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1  # Queremos el índice, así que restamos un 1 siempre
                break
            else:
                #imprime columna no valida
                print("Columna inválida")
        except:
            #imprime numero ingresado no valido
            print("Ingresa un número válido")
    #retorna las variables x y y
    return x, y

"""
    ES una funcion que nos permite disparar o si el disaparo es acertado o fallido comprobando si la celda escogida esta o no vacia.
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
    #analizamos si es mar es decir esta o no vacia la posición
    if es_mar(x, y, matriz):
        #asignamos la posicion de la matriz a Disparo Fallido
        matriz[y][x] = DISPARO_FALLADO
        #retornamos falso
        return False
    # Si ya había disparado antes, se le cuenta como falla igualmente
    elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
        #retornamos falso
        return False
    #si no
    else:
        #asignamos a la posicion de la matriz disparo acertado
        matriz[y][x] = DISPARO_ACERTADO
        #retorna verdadero
        return True

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

"""
    Esta funcion nos permite imprimir la matriz con los espacios ocupados por barcos o vacios
    Parametros:
    ------------
        Matriz
    Retorna:
    ------------
        True o False
"""
def imprimir_matrices_con_barcos(matriz):
    print("Mostrando ubicación de los barcos:")
    imprimir_matriz(matriz, True)

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
    #Definimos a los disparos restantes como los inciales que definimos al incio
    disparos_restantes = DISPAROS_INICIALES
    #Ingresamos la cantidad de barcos que se ingresaran en las celdas de la matriz creada
    cantidad_barcos = 5
    #Hacemos al llamado a obtener matriz para crear una matriz vacia con las condiciones establecidas
    matriz = obtener_matriz_inicial()
    print("\n\n") 
    #hacemos el llamado a la funcion que ingresara los barcos en posiciones aleatorias de la matriz, enviamos la matriz y la cantidad de barcos
    matriz = colocar_e_imprimir_barcos(matriz, cantidad_barcos)
    print("===============")
    #mientras sea verdadero
    while True:
        #Asignamos a la matriz con barcos una nueva variable llamada matriz del jugaro ya que en esta no se donde estan los barcos
        matriz_jugador = matriz
        #Imprimimos los disparos restantes en este caso empezara con el numero de disparos inicales que asignemos.
        print(f"Disparos restantes: {disparos_restantes}")
        #Imprimos la matriz ques se imprimira sin barcosa ya que la funcion matriz si se envia un falso este entiende que no debe mostrar los barcos
        imprimir_matriz(matriz_jugador, False)
        #salto de linea
        print("\n\n") 
        #solicitamos las coordenas con la funcion antes creada y ademas los asignamos a las variables x, y
        x, y = solicitar_coordenadas()
        #Usamos una varibable acertado para asignar el valor de verdad de la funcino disparar a la cual enviamos las coordenadas x, y y la matriz del jugador
        acertado = disparar(x, y, matriz_jugador)
        #si acertado es verdadero
        if acertado:
            #se imprime disparo acertado
            print("Disparo acertado")
            #Si todos los barcos ya han sido hundidos
            if todos_los_barcos_hundidos(matriz_jugador):
                #salto de linea
                print("\n\n") 
                #Se indica que es fin del juego y el jugador ha ganado
                print(f"Fin del juego\nEl jugador es el ganador")
                #se imprime las matrices con los barcos
                imprimir_matrices_con_barcos(matriz)
                #se rompe el while
                break
        #si acertado es falso
        else:
            #se imprime disparo fallido
            print("Disparo fallado")
            #Se resta un disparo
            disparos_restantes -= 1
            #Se verifica si los disparos restantes son menores o iguales a cero
            if disparos_restantes-1 < 0:
                #salto de linea
                print("\n\n") 
                #Se indica el fin del juego y que ha perdido porque se le acabaron los turnos
                print(f"Fin del juego\nEl jugador pierde. Se han acabado sus disparos")
                #se imprime la matriz con los barcos
                imprimir_matrices_con_barcos(matriz)
                #se rompe los while
                break





"""
Torres de Equilibrio
"""

import random
import os

def Equilibrio():
    """
        Es un procedimiento que nos muestra el funcionamiento del juego, genera un número aleatorio el cual se asigna al centro,
        genera un número aleatorio el cual irá encima o debajo del centro, muestra como va el ingreso de los números y muestra si
        es que gano o perdio.
        Parametros:
        ------------
            No tiene parametros de entrada
    
        Retorna:
        ------------
            No retorna ningun valor
    """
    #Declaración y asignación de un número aleatorio a la variable centro
    centro=random.randint(1,20)
    #Declaración la variable contador, el cual hará que el programa se repita las veces que sean necesarias
    contador=0
    #Declaración de la variable lista tipo diccionario, el cual contiene las clasves de los números del 1 al 20, y los valores de repetición de los mismos
    Lista={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
    #Imprime el valor del número central
    print("El número central es: ",centro)
    #Añade en 1 al valor de repetición del número central
    Lista[centro]+=1
    #Imprime los datos de la lista
    Imprimir(Lista)
    #Comienza el juego 
    while(contador<=60):
        #Declaración de la variable naleatorio y asignación de un valor aleatorio del 1 al 20
        naleatorio=random.randint(1,20)
        #Imprime el valor del número aleatorio
        print("El número aleatorio es: ",naleatorio)
        #Comparamos si el valor de naleatorio es menor que el valor del centro
        if(naleatorio<centro):
            #Imprime que el valor naleatorio irá debajo del centro
            print("El número aleatorio va abajo del centro: ",centro)
            #Añade el 1 al valor de repetición de naleatorio dentro de la Lista
            Lista[naleatorio]+=1
            #Imprime los datos de la lista
            Imprimir(Lista)
        #Comparamos si el valor de naleatorio es igual que el valor del centro
        elif(naleatorio==centro):
            #Imprime que el valor naleatorio irá al lado del centro
            print("El número aleatorio va al lado del centro: ",centro)
            #Añade el 1 al valor de repetición de naleatorio dentro de la Lista
            Lista[naleatorio]+=1
            #Imprime los datos de la lista
            Imprimir(Lista)
        #En el caso que no sea ninguna de las condiciones anteriores
        else:
            #Imprime que el valor naleatorio irá encima del centro
            print("El número aleatorio va encima del centro: ",centro)
            #Añade el 1 al valor de repetición de naleatorio dentro de la Lista
            Lista[naleatorio]+=1
            #Imprime los datos de la lista
            Imprimir(Lista)
        
        #Compara si el valor de repetición del centro es igual a 3
        if(Lista[centro]==3):
            #Imprime que ha ganado el juego
            print("Ha ganado el juego!!!")
            #Termina el programa
            return
        #Compara si el valor de repetición de naleatorio es igual a 3
        elif(Lista[naleatorio]==3):
            #Imprime que ha perdido el juego
            print("Game over :c")
            #Termina el programa
            return
        #Si no es ninguno de los casos anteriores
        else:
            #Suma en 1 al contador para que se repita el programa
            contador+=1

def Imprimir(Lista):
    """
        Es un procedimiento que nos imprime en consola la lista de los números según van ingresando
        Parametros:
        ------------
            Ingresa un diccionario
    
        Retorna:
        ------------
            No retorna ningun valor
    """
    #Imprime 'Lista del juego'
    print("Lista del juego")
    #Declaración de la variable cont
    cont=1

    while(cont<21):
        #Compara si el valor de repetición de la lista es igual a cero
        if(Lista[cont]==0):
            #Imprime '-' refieriendose a que esta vacia el valor
            print("-")
        #Compara si el valor de repetición de la lista es igual a uno
        elif(Lista[cont]==1):
            #Imprime la clave una vez
            print(cont)
        #Compara si el valor de repetición de la lista es igual a dos
        elif(Lista[cont]==2):
            #Imprime la clave dos veces
            print(cont,"  ",cont)
        #Si no es ninguno de los casos anteriores
        else:
            #Imprime la clave tres veces
            print(cont,"  ",cont,"  ",cont)
        #Suma en uno el valor cont
        cont+=1
    #Da una pausa a la ejecución
    os.system("pause")
    #Limpia la pantalla de la ejecución
    os.system("cls")

def bienvenida():
        """
        Se le da la bienvenida al usuario pidiendole su nombre y su apellido
        ------------
        nombre y apellido
        
        ------------
        Anuncio dando la bienvenida a la persona
        """               
        #Le pide al usuario que ingrese su nombre
        nombre = input("Ingrese su nombre: ")
        #Le pide al usuario que ingrese su apellido
        apellido = input(f"Ingrese su apellido, {nombre}: ")
        #Le da la bienvenida utilizando su nombre y su apellido
        print(f"Buen día, {nombre} {apellido} :)")
        #Le informa al usuario la solución al problema propuesto
        print(f"La solución al problema de las Ocho Reinas es la siguiente: ")

def free(fila, columna):
        """
        Determina si la casilla fila x columna está libre de amenazas.
        ------------
        r: Fila
        c: Columna
        Retorna:
        ------------
        True si la casilla está libre de amenazas por otras reinas.
        """               
        #Se asigna una variable auxiliar i
        #Para la variable auxiliar i, dentro del rango de ocho
        for i in range(8):
            #Si una reina está en la misma fila y columna que otra reina
            if tablero[fila][i] == '♕' or tablero[i][columna] == '♕':
                #Se retorna un tipo de valor booleano falso
                return False
        #Si la fila es menor o igual a la columna
        if fila <= columna:
            #Parámetro columna = N°Columna - N°Fila
            c = columna - fila
            #Fila es igual a cero
            r = 0
        #Si no se cumple el if fila <= columna
        else:
            #Parámtero fila es igual a N°Fila - N°Columna
            r = fila - columna
            #Columna es igual a cero
            c = 0
        #Mientras las columnas y las filas sean menores a 8
        while c < 8 and r < 8:
            #Si en la posición de la columna y la fila está una Reina ♕
            if tablero[r][c] == '♕':
                #Se retorna un tipo de dato booleano falso
                return False
            #Crecimiento en uno de la fila
            r += 1
            #Crecimiento en uno de la columna
            c += 1

        #Si la fila es menor o igual a la columna
        if fila <= columna:
            #La fila es igual a cero
            r = 0
            #El parámetro columna igual a N°Columna + N°Fila
            c = columna + fila
            #Si el parámetro columna es mayor que siete
            if c > 7:
                #El parámetro fila es igual a parámetro columna menos 7
                r = c - 7
                #El parámetro columna es igual a 7
                c = 7
        #Si la fila es mayor a la columna entonces
        else:
            #El parámetro columna es igual a 7
            c = 7
            #El parámetro fila es igual a N°Fila - (7- N°Columna)
            r = fila - (7 - columna)

        #Mientras el parámetro columna es mayor o igual a cero Y el parámetro fila es menor o igual a 8
        while c >= 0 and r < 8:
            #Si en la posición de la matriz tablero, es decir en una casilla hay una reina "♕"
            if tablero[r][c] == '♕':
                #Se retorna un tipo de valor booleano falso
                return False
            #Incremento de la fila en 1
            r += 1
            #Incremento de la columna en 1
            c -= 1
        #Se retorna un tipo de valor booleano verdadero
        return True

def agregar_reina(n):
        """
        Agrega las reinas dentro del tablero de ajedrez.
        Parametros:
        ------------
        n reinas a agregar
    
        Retorna:
        ------------
        No retorna nada
        """
        #Si es que el número de reinas es menor que 1
        if n < 1:
        #Retorna un valor booleano True
            return True
        #Se asigna una variable auxiliar idx_fila
        #Para la variable auxiliar dentro del rango de ocho
        for idx_fila in range(8):
            #Se asigna una variable auxiliar idx_columna
            #Para la variable auxiliar idx_columna dentro del rango de ocho
            for idx_columna in range(8):
                #Se llama a la función free, teniendo esta vez tomando en cuenta los parámetros idx_fila, idx_columna
                if free(idx_fila, idx_columna):
                    #llamada la función free, que hace que las reinas no se amenacen se asigna el caracter "♕"
                    tablero[idx_fila][idx_columna] = '♕'
                    #Se aplica la recursividad, llamando de nuevo a la función, esta vez con un valor menos para que se cumplan las 8 reinas
                    if agregar_reina(n-1):
                        #Retorna un valor booleano True
                        return True
                    #Cuando terminen de asignarse las reinas en el tablero, sin amenazarse cada una
                    else:
                        #En la matruz del tablero en lugar de una reina se imprime el caracter "_" que simula las casillas vacías
                        tablero[idx_fila][idx_columna] = '_'
        return False

        #Para una mejor comprensión gráfica del ejercicio el tablero se imprime de forma matricial
tablero = []
#Se asigna una variable auxiliar i
#Para la variable auxiliar i, dentro del rango de ocho
for i in range(8):
    #Se imprima un caracter que simula una casilla, para dar una mejor comprensión del tablero
    tablero.append(['_'] * 8)

#Funcion menu para hacer el llamado las funciones jugar o salir
def mostrar_menu():
    """
    Llama a la función menú para elegir el juego o salir
    ------------
    El parámetro es la opción a elegir
    
    Retorna:
    ------------
    Retorna el juego elegido
    """
    #Generamos una variable para almacenar la opcion
    opcion = ""
    #mientras la opcion sea diferente de 2
    while opcion != "4":
        #menu se ejcutara
        menu = """
        Bienvenido al Proyecto
            1. Batalla Naval
            2. Torre de equilibrio
            3. Problema 8 reinas
            4. Salir
            Elija su opción: """
        #opcion es igual a la entrada que debemos a menu
        opcion = input(menu)
        #si la opcion es 1
        if opcion == "1":
            #llamammos a la funcion jugar
            jugar()
        if opcion == "2":
            #Inicia el juego
            Equilibrio()
        if opcion == "3":
            bienvenida()
            #Se llama a la función agregar reina y se agregan 8 reinas
            agregar_reina(8)
            #Para cuando la fila se encuentre en el tablero
            for fila in tablero:
                #Se imprime la solución
                    print(*fila)

#llamamos a la funcion menu para inciar el juego.
mostrar_menu()
