"""
Nombre de la función: divisores(num)
Entradas: Números enteros positivos.
Salidas: Los divisores de un número entero.
Restricciones: Solo se puede imprimir los números de manera descendente.
"""
def divisores(num):
    if isinstance(num,int):
        if (num >= 0):
            return divisores_aux(num)
        else:
            print("Error: Solo se permite valores positivos")
    else:
        print("Error: El parámetro num no cumple que sea un número entero positivo")

def divisores_aux(num):
    if (num == 0):
        return 0
    else:
        return num + divisores_aux(num // 10)
"""
Nombre de la función: multiplicarRecursivo(num, factor)
Entradas: Números enteros positivos.
Salidas: El resultado de una multiplicación.
Restricciones: Realizar la operación sin utilizar el operador de multiplicación.
"""
def multiplicarRecursivo(num, factor):
    if isinstance(num,int) and isinstance (factor,int):
        if (num > 0) and (factor > 0):
            return multiplicarRecursivo_aux(num, factor)
        else:
            print("Error: Solo se permite valores positivos")
    else:
        print("Error: El parámetro num no cumple con que sea un número entero positivo")

def multiplicarRecursivo_aux(num, factor):
    if (num == 0):
        return 0
    else:
        return num + multiplicarRecursivo_aux(num, factor)
"""
Nombre de la función: divisionRecursivo(divisor, dividendo)
Entradas: Números enteros positivos.
Salidas: El resultado de divisor y dividendo.
Restricciones: No se puede utilizar el operador de la división.
"""

def divisionRecursivo(divisor, dividendo):
    if isinstance(divisor, int) and isinstance(dividendo, int):
        if (divisor < 0):
            print ("Error")
        else:
            return divisionRecursivo_aux(divisor, dividendo)

def divisionRecursivo_aux(divisor, dividendo):
    if(divisor == 0):
        return 0
    else:
        return divisionRecursivo_aux(divisor, dividendo) + dividendo - divisor
"""
Nombre de la función: corrimientoAEntero(num)
Entradas: Números con decimal que sean positivos.
Salidas: Pasar un número de decimal a entero.
Restricciones: Los números deben ser pasados a enteros.
"""

def corrimientoAEntero(num):
    if isinstance(num, float):
        if (num > 0):
            corrimientoAEntero_aux(num)
        else:
            print("Error")
    else:
        print("Error: el parámetro num no es válido")
def corrimientoAEntero_aux(num):
    if(num == 1):
        return 1
    else:
        if num // 10:
            return num * corrimientoAEntero_aux(num) + num
        else:
            return corrimientoAEntero_aux(num) + num
"""
Nombre de la función: contarDigitosFlotante(num)
Entradas: Números con decimal que sean positivos.
Salidas: Contar la cantidad de dígitos flotantes.
Restricciones: Los números deben ser flotantes.
"""

def contarDigitosFlotante(num):
    if isinstance(num, float) == False:
        return print ("Error")
    elif (num == 0):
        return 0
    else:
        return 1 + contarDigitosFlotante(num // 10) * 10
"""
Nombre de la función: indiceNumero(num, i)
Entradas: Números enteros.
Salidas: Determinar el lugar donde está situado cualquier número según el
         índice solicitado.
Restricciones: Números enteros.
"""

def indiceNumero(num, indice):
    if isinstance(num,int):
        if (num >= 0):
            return indiceNumero_aux(num, indice)
        else:
            print("Error: Solo se permite valores enteros")
    else:
        print("Error: El parámetro no es reconocido")
def indiceNumero_aux(num, indice):
    if(indice > num):
        if((num %2) == 0):
            return indice + indiceNumero_aux(indice + 1 // 10, num)
        else:
            return indiceNumero_aux(indice + 1 // 10, num)
def contarDigitos(num):
    if isinstance(num,int):
        if( n >= 0):
            if(num == 0):
                return 0
            else:
                return 1+contarDigitos(num // 10)
        else:
            print("Error: Solo se permite valores positivos")
    else:
        print("Error: el parámetro nun no cumple que se un número entero")
"""
Nombre de la función: cortarNumero(num, i)
Entradas: Números enteros positivos.
Salidas: Determinar los números solicitados por medio del indice.
Restricciones: Números enteros positivos.
"""

def cortarNumero(num, indice):
    if isinstance(num,int):
        if (num >= 0):
            return cortarNumero_aux(num, indice)
        else:
            print("Error: Solo se permite valores enteros")
    else:
        print("Error: El parámetro no es reconocido")
def cortarNumero_aux(num, indice):
    if(indice > num):
        return 0
    else:
        return 10 * cortarNumero_aux(indice + num +1 // 10)

