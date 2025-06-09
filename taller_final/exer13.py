"""
Implementa funciones para:
· Leer un archivo CSV con datos de ventas
· Calcular totales por mes y por producto
· Generar un reporte en formato texto
· Manejar errores de archivo no encontrado
"""
import csv
from tabulate import tabulate

def read(csv_file, new_file):
    with open(csv_file, newline='') as csvfile:
        reader= csv.DictReader(csvfile)
        with open(new_file, newline='', mode='w') as nf:
            new_file= csv.writer(nf)
            formated= [tabulate(reader, headers='firstrow', tablefmt='github')]
            new_file.writerow(formated)

read('ventas.csv', 'sales.csv')

