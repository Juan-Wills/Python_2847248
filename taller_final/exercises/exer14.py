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


def serialization(obj):
    if isinstance(obj, (dict, list)):
        return json.dumps(obj, indent=2)

    raise ValueError("A parameter is needed, 'url' or 'python sequence'")


def loadJSON(file):
    data = []
    with open(file, encoding="utf-8", newline="") as f:
        for row in f:
            data.append(row.strip())

    return data


def saveJSON(fname="extras/New_json_file.json", data=None, url=None, p=None):
    if not fname.endswith(".json"):
        fname += ".json"

    with open(fname, "x", newline="") as nf:
        text = []
        if data and url:
            raise ValueError(
                "No se ingreso ningun valor, opciones disponibles: data, url"
            )

        if url:
            response = requests.get(url, params=p)
            if response.status_code == 200:
                text = response.json()
            else:
                raise ConnectionError("Respuesta diferente a 200")

        elif isinstance(data, (dict, list)):
            for dicts in data:
                if not isinstance(dicts, dict):
                    raise ValueError("List objects must be dictionaries")

            text = data
        else:
            raise ValueError("El tipo de dato debe ser 'list' o 'dict'")

        json.dump(text, nf, ensure_ascii=False, indent=4, separators=(", ", ": "))
    print("File created successfuly")


def main():
    url = "https://dummyjson.com/users"
    parameter = {"limit": 5, "skip": 5}

    serialization(database)
    saveJSON(fname="extras/API_data", url=url, p=parameter)
    j = loadJSON("extras/API_data.json")

    for text in j:
        print(text)


main()
