"""
Crea un módulo utilidades.py con funciones matemáticas útiles:
· Verificar si un número es primo
· Calcular el máximo común divisor
· Convertir entre diferentes bases numéricas
"""

import re


def isprimo(num: int):
    if not isinstance(num, int):
        raise ValueError("Argument must be an integer")

    for div in range(2, num + 1):
        if num % div == 0 and div != num:
            return False

    return True


def mcd(num1, num2):
    if not isinstance(num1, int) and isinstance(num2, int):
        raise ValueError("Elements must be integers")

    if num2 > num1:
        num1, num2 = num2, num1

    while num2:
        num1, num2 = num2, num1 % num2

    return num1


def numbases(num, base):
    if not isinstance(num, int) and isinstance(base, int):
        raise ValueError("Elements must be integers")

    reminder = ""
    while num:
        reminder += str(num % base)
        num //= base

    result = reminder[::-1]

    if base == 16:
        hex = {"01": "A", "11": "B", "21": "C", "31": "D", "41": "E", "51": "F"}
        for keys in hex:
            if keys in reminder[::-1]:
                result = re.sub(keys, hex[keys], result)

        return result
