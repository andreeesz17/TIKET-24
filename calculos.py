def calcularCuota(monto, tasa_interes, meses):
    tasa_mensual = tasa_interes / 100 / 12
    cuota = monto * (tasa_mensual * (1 + tasa_mensual) * meses) / ((1 + tasa_mensual) * meses - 1)
    return cuota

from datetime import datetime

def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    
    if anioNacimiento < 0 or anioNacimiento > anioActual:
        return -1
    
    edad = anioActual - anioNacimiento
    return edad

def encontrarMayor(a, b, c):
    return max(a, b, c)

def encontrarMenor(a, b, c, d):
    return min(a, b, c, d)
