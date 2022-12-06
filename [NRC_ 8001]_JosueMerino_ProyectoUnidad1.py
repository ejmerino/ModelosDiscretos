"""
    Dilema de las Ocho Reinas en un tablero de ajedrez.
    Este problema lógico indica que se deben colocar en un tablero de ajedrez 8 reinas, de forma
    que ninguna amenace a otra. 

    Autor: Ednan Josué Merino Calderón

    Versión: 1.2
"""

def bienvenida():
        """ Determina si la casilla fila x columna está libre de amenazas.
        @param nombre: Nombre
        @param apellido: Apellido
        @return: Anuncio dando la bienvenida a la persona
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
        """ Determina si la casilla fila x columna está libre de amenazas.
        @param r: Fila
        @param c: columna
        @return: True si la casilla está libre de amenazas por otras reinas.
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
        """ Agrega n reinas al tablero.
        @param: n Reinas a Agregar
        @return True si es que ninguna reina se amenaza entre sí
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
#Se llama a la función bienvenida para saludar al usuario y pedirle su nombre
bienvenida()
#Se llama a la función agregar reina y se agregan 8 reinas
agregar_reina(8)
#Para cuando la fila se encuentre en el tablero
for fila in tablero:
    #Se imprime la solución
    print(*fila)
