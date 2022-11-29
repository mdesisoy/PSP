# Ejercicio 1: Implementa un programa Python que PREGUNTE al 
#   usuario por dos números enteros (x, y) y muestre por 
#   pantalla la suma, resta, multiplicación, división y resto 
#   de ambos, con el siguiente formato:
#       x + y = …
#       x – y = …
#       x * y = …
#       x / y = …
#       x % y = …
def ejercicio_1():
    a = input("Primer numero: ")
    b = input("Segundo numero: ")
    x = int(a)
    y = int(b)
    print("%d + %d = %d" % (x,y,x+y))
    print("%d - %d = %d" % (x,y,x-y))
    print("%d * %d = %d" % (x,y,x*y))
    print("%d / %d = %d" % (x,y,x/y))
    print("%d %% %d = %d" % (x,y,x%y))


# Ejercicio 2:  Escribe un programa Python que pregunte al 
#   usuario por 10 números enteros y muestre por pantalla el 
#   número total de veces que el usuario ha introducido el 
#   0, el número total de enteros mayores que 0 introducidos 
#   y el número total de enteros menores que 0 introducidos.
def ejercicio_2():
    num_ceros = 0
    num_mayores = 0
    num_menores = 0
    for num in range(10):
        x = input("numero %d : " % (num+1))
        a = int(x)
        if (a == 0):
            num_ceros += 1
        elif (a > 0):
            num_mayores += 1
        else:
            num_menores += 1
    print("Numero de ceros: %d" % num_ceros)
    print("Numero de mayores que cero: %d" % num_mayores)
    print("Numero de menores que cero: %d" % num_menores)



# Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un 
#   programa Python que adivine el número. El programa 
#   generará un número aleatorio entre 0 y 20 y luego irá 
#   pidiendo números al usuario indicando “mayor” o “menor” 
#   según sea mayor o menor con respecto al número generado 
#   aleatoriamente. El proceso termina cuando el usuario 
#   acierta, y deberá mostrar un mensaje de felicitaciones 
#   junto al número de intentos que ha necesitado el usuario.
import random

def ejercicio_3():
    encontrado = False
    print("Adivina un numero entre 0 y 20.")
    num_aleatorio = random.randint(0,20)
    while (not encontrado):
        aux = input("Numero: ")
        x = int(aux)
        if (x < 0 or x > 20):
            print("En el rango por favor")
        elif (x > num_aleatorio):
            print("Menor")
        elif (x < num_aleatorio):
            print("Mayor")
        else:
            encontrado = True
            print("¡Ese es el numero!")



# Ejercicio 4:  Implementa un programa Python que solicite al
#   usuario una cadena de caracteres (String) y muestre por 
#   pantalla la longitud de esta.
def ejercicio_4():
    cadena = input("Introduzca una cadena de caracteres: ")
    print("La longitud de la cadena es de %d caracteres" % len(cadena))



# Ejercicio 5:  Implementa un programa Python que solicite al 
#   usuario una cadena de caracteres (String) y muestre por 
#   pantalla el número de veces que aparece la sub-cadena 
#   “aaa” dentro de dicho String.
def ejercicio_5():
    cadena = input("Introduzca una cadena de caracteres: ")
    if (len(cadena) < 3):
        print("La cadena introducida no contiene la secuencia 'aaa'")
    else:
        veces = 0
        for a in range(len(cadena)-2):
            if (cadena[a:a+3] == "aaa"):
                veces += 1
        if (veces != 0):
            print("La cadena introducida contiene la cadena 'aaa' %d veces" % veces)
        else:
            print("La cadena introducida no contiene la cadena 'aaa'")



# Ejercicio 6:  Implementa un programa Python que solicite al 
#   usuario una cadena de caracteres (String) y muestre por 
#   pantalla dicha cadena, pero con el primer y último carácter 
#   cambiados de posición.
def ejercicio_6():
    cadena = input("Introduzca una cadena de caracteres: ")
    aux = cadena[0]
    aux2 = cadena[len(cadena)-1]
    cadena = aux2 + cadena[1:int(len(cadena)-1)] + aux
    print(cadena)



# Ejercicio 7:  Implementa un programa Python que solicite al 
#   usuario una cadena de caracteres y devuelva dicha cadena, 
#   pero al revés.
def ejercicio_7():
    cadena = input("Introduzca una cadena de caracteres: ")
    print(cadena[::-1])



# Ejercicio 8:  Implementa un programa Python con un método 
#   llamado sum(int [] tabla) que muestre por pantalla el 
#   resultado de sumar todos los elementos de la tabla pasada 
#   como parámetro.
def sum(tabla):
    total = 0
    for a in range(len(tabla)):
        for b in range(len(tabla[a])):
            total += tabla[a][b]
    print(total)

def ejercicio_8():
    t1 = [[1,1],[1,1],[1,1]]
    sum(t1)



# Ejercicio 9:  Implementa un programa Python con un método 
#   llamado indexContains(String[] tabla, String cadena) que 
#   devuelva el índice de la tabla cuyo valor es igual al 
#   valor de “cadena”. En caso de no haber ningún valor igual, 
#   devuelve -1.
def indexContains(tabla, cadena):
    for a in range(len(tabla)):
        if (tabla[a] == cadena):
            return a
    return -1

def ejercicio_9():
    tabla = ["aa","ab"]
    cadena = "aa"
    print("La tabla contiene la cadena en la posicion con el indice %d " % indexContains(tabla,cadena))



# Ejercicio 10:  Implementa un método Python llamado 
#   mayorYmenor, el cual recibe como parámetro una tabla de 
#   Strings y muestra por pantalla el String con mayor longitud 
#   y el String con menor longitud.
def mayorYmenor(tabla):
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    for a in range(len(tabla)):
        for b in range(len(tabla[a])):
            if (len(tabla[a][b]) > len(tabla[maxX][maxY])):
                maxX = a
                maxY = b
            if (len(tabla[a][b]) < len(tabla[minX][minY])):
                minX = a
                minY = b
    print("El String con mayor longitud de la tabla es %s" % tabla[maxX][maxY])
    print("El String con menor longitud de la tabla es %s" % tabla[minX][minY])

def ejercicio_10():
    tabla = [["murcielago","casa","gatos","sol"],["rafael","ñu"]]
    mayorYmenor(tabla)



# Ejercicio 11: Tenemos la siguiente tabla multidimensional, la 
#   cual almacena por cada una de sus filas el salario 
#   trimestral de cada uno de los empleados de la empresa.
#       int salarios[][] = { {700, 900, 1300} , {1000, 950, 
#                               1080}, {1300, 930, 1200} }
#   A su vez, disponemos también de una tabla empleados, con 
#       los nombres de los trabajadores:
#       String empleados[] = {Javier María, Antonio Muñoz, 
#                               Isabel Allende}
#   Implementa un programa Python que muestre por pantalla lo 
#       siguiente:
#           Javier Marías -> 700 + 900 + 1300 = 2900€
#           Antonio Muñoz -> 1000 + 950 + 1080 = 3030€
#           Isabel Allende -> 1300 + 930 + 1200 = 3430€
def ejercicio_11():
    salarios = [[700,900,1300],[1000,950,1080],[1300,930,1200]]
    empleados = ["Javier María","Antonio Muñoz","Isabel Allende"]
    for a in range(len(salarios)):
        print("%s -> %d + %d + %d = %d€" % (empleados[a],salarios[a][0],salarios[a][1],salarios[a][2],salarios[a][0]+salarios[a][1]+salarios[a][2]))



# Ejercicio 12: Crea una clase llamada Cuenta que tendrá los 
#   siguientes atributos: titular y cantidad (puede tener 
#   decimales). El titular será obligatorio y la cantidad es 
#   opcional. Crea sus métodos get, set y toString. Tendrá 
#   dos métodos especiales:
#       - ingresar(double cantidad): se ingresa una cantidad 
#           a la cuenta si la cantidad introducida es negativa, 
#           no se hará nada.
#       - retirar(double cantidad): se retira una cantidad a 
#           la cuenta, si restando la cantidad actual a la 
#           que nos pasan es negativa, la cantidad de la cuenta 
#           pasa a ser 0.
class Cuenta:
    def __init__(self,cantidad,titular):
        self.cantidad = cantidad
        self.titular = titular
    def getTitular(self):
        return self.titular
    def setTitular(self,titular):
        self.titular = titular
    def getCantidad(self):
        return self.cantidad
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def toString(self):
        print("La cuenta de %s tiene: %.2f" % (self.titular,self.cantidad))
    def ingresar(self,cantidadIngresada):
        if (cantidadIngresada >= 0):
            self.cantidad += cantidadIngresada
    def retirar(self,cantidadRetirada):
        if ((self.cantidad - cantidadRetirada) < 0):
            self.cantidad = 0
        else:
            self.cantidad -= cantidadRetirada

def ejercicio_12():
    account = Cuenta(0.0,"Maria Lozano")
    print(account.getCantidad())
    print(account.getTitular())
    account.setTitular("Marión")
    account.setCantidad(3000)
    account.toString()
    account.ingresar(287.5)
    account.toString()
    account.retirar(287.5)
    account.toString()
    account.retirar(4000)
    account.getCantidad()
    account.toString()



# Ejercicio 13: Implementa la clase “Matriz” con los atributos 
#   int rows, int columns e int[rows][columns] matrix, que 
#   contenga los siguientes métodos: 
#       - getNumberRows(): devuelve el número de filas de la 
#           matriz.
#       - getNumberColumns(): devuelve el número de columnas de 
#           la matriz.
#       - setElement(int x, int j, int element): cambia el 
#           valor de la matriz en [x][j] por el valor de 
#           [element].
#       - addMatrix(int[][] matrix): suma todos los elementos 
#           de la matriz actual a los elementos de [matrix], 
#           y el resultado se almacena en la matriz inicial. 
#           Si [matrix] no tiene el mismo número de filas y 
#           columnas que la matriz inicial, la operación no se 
#           puede realizar (notificalo).
#       - multMatrix(int[][] matrix]: multiplica todos los 
#           elementos de la matriz actual a los elementos de 
#           [matrix], y el resultado se almacena en la matriz 
#           inicial. Si [matrix] no tiene el mismo número de 
#           filas y columnas que la matriz inicial, la 
#           operación no se puede realizar (notificalo).
class Matriz:
    def __init__(self,rows,columns):
        self.matrix = [[0] * columns for _ in range(rows)]
        self.rows = rows
        self.columns = columns
    def getNumberRows(self):
        return self.rows
    def getNumberColumns(self):
        return self.columns
    def setElement(self,x,j,element):
        self.matrix[x][j] = element
    def addMatrix(self, matrix2):
        if (self.rows != matrix2.getNumberRows() or self.columns != matrix2.getNumberColumns()):
            print("No se puede sumar matrices con distinto numero de filas y/o columnas")
        else:
            for x in range(self.rows):
                for y in range(self.columns):
                    self.matrix[x][y] += matrix2.matrix[x][y]
    def multMatrix(self, matrix2):
        if (self.rows != matrix2.getNumberRows() or self.columns != matrix2.getNumberColumns()):
            print("No se puede sumar matrices con distinto numero de filas y/o columnas")
        else:
            for x in range(self.rows):
                for y in range(matrix2.getNumberColumns()):
                    aux2 = 0
                    for z in range(self.columns):
                        aux2 += self.matrix[x][z] * matrix2.matrix[z][y]
                    self.setElement(x, y, aux2)

def ejercicio_13():
    matrix1 = Matriz(2,2)
    print(matrix1.getNumberRows())
    print(matrix1.getNumberColumns())
    matrix1.setElement(0,0,1)
    # 
    matrix2 = Matriz(2,2)
    matrix2.setElement(0,0,2)
    # 
    matrix1.addMatrix(matrix2)
    print(matrix1.matrix)
    #
    print(matrix2.matrix)
    matrix1.multMatrix(matrix2)
    print(matrix1.matrix)
    print()
    #
    matrix1.setElement(1,0,6)
    print(matrix1.matrix)
    matrix3 = Matriz(2, 2)
    matrix3.setElement(0,0,1)
    matrix3.setElement(0,1,1)
    matrix3.setElement(1,0,1)
    matrix3.setElement(1,1,1)
    print(matrix3.matrix)
    matrix1.multMatrix(matrix3)
    print(matrix1.matrix)
    


# Ejercicio 14: Realiza un programa en Python en el que 
#   muestres un menú que te permita 3 opciones:
#       - 1. Volcado (escritura) de una lista con todos los 
#               números pares comprendidos entre 0 y 100.
#       - 2. Mostrar (lectura) por pantalla el contenido del 
#               fichero de texto creado.
#       - 3. Salir del Programa.
def ejercicio_14():
    terminado = False
    while (not terminado):
        print("1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.")
        print("2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.")
        print("3. Salir del Programa.")
        aux = input()
        opcion = int(aux)
        if (opcion == 1):
            for x in range(100):
                if (x % 2 == 0):
                    print(x)
        elif (opcion == 2):
            print("Mostrando contenido del fichero: 'Ejercicio15.txt'")
            file = open("Ejercicio15.txt")
            print(file.read())
            file.close()
        else:
            terminado = True



# Ejercicio 15: Crea un fichero de texto con el nombre y 
#   contenido que tú desees. Por ejemplo, Ejercicio15.txt. 
#   Realiza un programa en Python que lea el fichero 
#   <<Ejercicio15.txt>> y muestre su contenido por pantalla 
#   sin espacios. Por ejemplo, si el fichero contiene el 
#   siguiente texto “Hola que haces”, deberá mostrar 
#   “Holaquehaces”.
def ejercicio_15():
    print("Mostrando contenido del fichero: 'Ejercicio15.txt' sin espacios")
    for line in open("Ejercicio15.txt"):
        aux = line.replace(" ", "")
        print(aux)
    # file.close()

ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_8()
ejercicio_9()
ejercicio_10()
ejercicio_11()
ejercicio_12()
ejercicio_13()
ejercicio_14()
ejercicio_15()
