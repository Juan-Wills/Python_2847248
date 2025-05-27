"""
Crea un sistema de inventario usando diccionarios. Implementa funciones para:
· Agregar un producto con su cantidad y precio
· Actualizar la cantidad de un producto existente
· Calcular el valor total del inventario
· Encontrar el producto más caro
"""

def main():
    products= [{
                'id': 0,
                'nombre': "AK-47",
                'cantidad': 120,
                'precio unitario': 5000
                },
                {                
                'id': 1,
                'nombre': "Glock",
                'cantidad': 500,
                'precio unitario': 600
                }
    ]
    value_test= [3, "RPM-012", 60, 5000]

    create_product(value_test)

def create_product(values):
    key_test= ['id', 'nombre', 'cantidad',  'precio_unitario']
    print(zip(key_test, values))
    
    
def update_amount():

def total_inventory():

def most_expensive():

if __name__== '__main__':
    main()