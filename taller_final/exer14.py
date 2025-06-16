"""
Ejercicio 14: JSON y Serialización
Crea un sistema que:
· Convierta objetos Python a JSON
· Guarde y cargue configuraciones desde archivos JSON
· Valide la estructura de datos JSON
"""
import json
import requests
import sys

database = [
    {"titular": "Juan David", "numero_cuenta": 123852469, "saldo": 120000},
    {"titular": "Jesus Santiago", "numero_cuenta": 123654789, "saldo": 120000},
    {"titular": "Jhon Freddy", "numero_cuenta": 753159852, "saldo": 120000},
    {"titular": "Miguel Angel", "numero_cuenta": 147852369, "saldo": 120000},
    ]

def serialization(url=None, obj=None):
    if url:
        return json.dumps(requests.get(url= url).json())

    if isinstance(obj, (dict, list)):
        return json.dumps(obj, indent= 2)
    
    raise ValueError("A parameter is needed, 'url' or 'python sequence'")

def loadJSON(file):
    data= []
    with open(file, encoding='utf-8', newline='') as f:
        for row in f:  
            data.append(row)

    return data

def saveJSON(fname, data):
    try:
        fname.split('.')
        with open(fname, "w") as f:
            f.write(data)
    except:
        print('alksdfj')

"""
config= loadJSON('extras/config.json')
jsonformat= """"""
for char in config:
    jsonformat+= char
print(jsonformat)
"""

db= serialization(obj= database)
saveJSON('database', db)
