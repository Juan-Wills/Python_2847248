import json

libro_path= 'C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/data/libros.json'

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

with open(libro_path, 'r', encoding='utf-8') as file:
    data= json.load(file)
    data['libros'].append(person)
    print(data)

with open(libro_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent= 2)