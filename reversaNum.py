"""
Nombre: reversaNumero
Entradas:: Un número entero positivo mayor o igual a cero.
Salidas: Entero mayor a cero, que el número en orden de inversa sea su representación original.
Restricciones: Entero positivo mayor o igual a cero.
"""
def contarDigitos_V3(num):
    if(isinstance(num, int) == False):
        return print("Error tipo de dato, no es entero")
    elif (num == 0):
        return 1
    else:
        return contarDigitos_aux(num)

def contarDigitos_aux(n):
    if(n == 0):
        return 0
    else:
        return 1 + contarDigitos_aux(n // 10)

def reversaNum(num):
    if isinstance (num, int):
        if (num >=0 ):
            if (num <= 10):
                return num
            else:
                return reversaNum_aux(num, contarDigitos_V3(num))
        else:
            print("El número debe ser ser positivo")
    else:
        print ("Error: el número no es entero")

def reversaNum_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num % 10) * (10 ** (largo - 1)) + reversaNum_aux(num // 10, largo - 1)

