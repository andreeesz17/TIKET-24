def calcularCuota(monto, interesAn, Nmeses):
    tasaMensual =  interesAn / 100 / 12
    Cuota = (monto * tasaMensual) / (1 -(1 + tasaMensual) **(-Nmeses))
    return Cuota

from datetime import datetime

def calcularEdad(anNacimiento):
    anActual = datetime.now().year
    
    if anNacimiento < 0 or anNacimiento > anActual:
        return -1
    
    edad = anActual - anNacimiento
    return edad

def encontrarMayor(prim, secu, terc):
    return max(prim, secu, terc)

def encontrarMenor(prim, secu, terc, cuar):
    return min(prim, secu, terc, cuar)
