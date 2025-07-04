"""
Usa list comprehension para:
· Crear una lista de cuadrados de números pares del 1 al 20
· Filtrar palabras que contengan más de 5 letras de una lista
· Crear una matriz 3x3 con números del 1 al 9
"""


def main():
    fruits_sample = ["banana", "pear", "apple", "pineapple", "watermelon", "grape"]
    pares = [par for par in range(0, 21, 2)]
    filtro = [string for string in fruits_sample if len(string) > 5]
    matrix = [[x for x in range(1, 10)] for _ in range(3)]
    print(pares)
    print(filtro)
    print(matrix)


if __name__ == "__main__":
    main()
