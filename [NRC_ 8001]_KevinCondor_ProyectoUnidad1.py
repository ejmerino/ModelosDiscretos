"""
El juego consistirá en que primero se generará un numero aleatorio del 1 al 20, será el valor que quede en el centro e inicia el juego,
se generará otro número aleatorio el cual si es mayor irá en la parte de arriba, caso contrario si es menor irá debajo del centro, los
números se pueden repetir, si un número se repite se colocará al lado del mismo número repetido, el objetivo del juego es conseguir 2
números iguales al del centro, es decir, para ganar se necesitará que el número en el caso que se consiga 3 números iguales 

Autor:
Kevin Cóndor

Versión:
VER.1.0
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

if __name__ == '__main__':
    #Inicia el juego
    Equilibrio()