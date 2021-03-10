"""
Nombre: cantidadDeNumerosPares
Entrada: Un número mayor o igual a cero.
Salida: Determinar la cantidad de números pares que exista o existan según el valor indicado en la entrada.
Restricción: El número debe ser entero positivo.
"""


def cantidadDeNumerosPares(num):
    if(isinstance(num,int)and num>0):
        if(num==0):
            return 1
        else:
            return cantidadDeNumerosPares_aux(num)
    else:
        return ("Por favor digite un numero entero positivo")

def cantidadDeNumerosPares_aux(num):
    if num==0:
        return 0
    if num%2==0:
        return 1+cantidadDeNumerosPares_aux(num//10)
    else:
        return 0+cantidadDeNumerosPares_aux(num//10)
