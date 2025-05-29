"""
Funciones con Parámetros Variables
Escribe una función que acepte un número variable de argumentos numéricos y:
· Calcule estadísticas básicas (suma, promedio, máximo, mínimo)
· Permita especificar una operación mediante un parámetro keyword
"""

from statistics import mean


def main():
    numbers = [num for num in range(100)]
    result = statistic(numbers, operation="avg")
    print(result)


def statistic(v: list, operation="sum"):
    operation.lower()
    if operation == "sum":
        result = sum(v)
    elif operation == "avg":
        result = mean(v)
    elif operation == "max":
        result = max(v)
    elif operation == "min":
        result = min(v)

    return result


if __name__ == "__main__":
    main()
