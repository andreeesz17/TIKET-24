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

def determinarResultadosIMC(numero):
    valor=numero
    if valor < 0 :
        return "IMC fuera de rango"
    elif valor < 16:
        return "Delgadez severa"
    elif valor < 17:
        return "Delgadez moderada"
    elif valor < 18.5:
        return "Delgadez leve"
    elif valor < 25:
        return "Peso normal"
    elif valor < 30:
        return "Sobrepeso"
    elif valor < 35:
        return "Obesidad Grado 1"
    elif valor < 40:
        return "Obesidad Grado 2"
    else:
        return "Obesidad Grado 3"  
