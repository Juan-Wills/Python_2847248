"""
Crea un sistema de inventario usando diccionarios. Implementa funciones para:
· Agregar un producto con su cantidad y precio
· Actualizar la cantidad de un producto existente
· Calcular el valor total del inventario
· Encontrar el producto más caro
"""


def main():
    products = []

    data = [3, "RPM-012", 60, 5000]
    create_product(products, data)

    data = [0, "AK-47", 500, 8000]
    creation = create_product(products, data)

    update = update_amount_by_index(products, 120, 3)

    total = total_price(products)

    expensive = most_expensive(products)

    # print(products)


keys = ["id", "nombre", "cantidad", "precio_unitario"]


def create_product(to_fill: list, values: list):
    new_dict = {key: value for key, value in zip(keys, values)}
    to_fill.append(new_dict)
    return print("Dictionary succefully created\n")


def update_amount_by_index(product_list: list, cantidad: list, index: int):
    for items in product_list:
        if items["id"] == index:
            items["cantidad"] = cantidad
            return "Update succefully applied\n"
    return "ID not found\n"


def total_price(product_list: list):
    result = int()
    for products in product_list:
        result += products["precio_unitario"] * products["cantidad"]
    return f"Total inventory price: {result}\n"


def most_expensive(product_list: list):
    precios = []

    for product in product_list:
        precios.append(product["precio_unitario"])

    price = max(precios)
    index = precios.index(price)
    nombre = product_list[index]

    return f"The most expensive item is {nombre["nombre"]} with {price}\n"


if __name__ == "__main__":
    main()
