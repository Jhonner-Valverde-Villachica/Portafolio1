"""
Nombre: numeroPar
Entrada: Un número entero mayor o igual a cero.
Salida: La función es determinar si el número indicado es par, si es par determinará 'True', si no 'False'.
Restricción: El número debe ser entero positivo.
"""

def numeroPar(num):
    if(isinstance(num,int)and num>0):
        if(num%2==0):
            print ('True')
        else:
            print ('False')
    else:
        return 'Digite un número entero'
