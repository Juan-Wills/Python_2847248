"""
Dada una lista de números, crea funciones para
· Encontrar el mayor y menor número
· Calcular la suma y promedio
· Filtrar solo los números pares
· Ordenar la lista de mayor a menor
"""


def main():
    nums = [num for num in range(1, 101)]
    print(ops(nums, "par"))


def ops(seq: list, operation: str):
    if operation == "min/max":
        result = (max(seq), min(seq))
    elif operation == "avg":
        result = sum(seq) // len(seq)
    elif operation == "par":
        result = []
        for nums in seq:
            if nums % 2 == 0:
                result.append(nums)
    elif operation == "desc":
        seq.sort(reverse=True)
        result = seq
    else:
        result = seq
    return result


if __name__ == "__main__":
    main()
