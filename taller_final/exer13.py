"""
Implementa funciones para:
· Leer un archivo CSV con datos de ventas
· Calcular totales por mes y por producto
· Generar un reporte en formato texto
· Manejar errores de archivo no encontrado
"""
import csv
import sys
from datetime import datetime, date
from tabulate import tabulate

def read(csv_file, new_file):

    exist([csv_file])

    with open(csv_file, newline='') as csvfile:
        reader= csv.reader(csvfile)
        with open(new_file, 'w', newline='') as nf:
            new_file= csv.writer(nf)
            formated= [tabulate(reader, headers='firstrow', tablefmt='github', numalign='left')]
            new_file.writerow(formated)


def total(file: str, search, new_file):

    exist([file])

    cols= ['Order Date', 'Item Type', 'Units Sold', 'Unit Price']

    # Mapping source file
    f= open(file, newline='', encoding= 'utf-8')
    reader= csv.DictReader(f)
    data=[row for row in reader]

    # Filter data modes
    if 1 <= search <= 12: 
        by_date(data, search)
    elif isinstance(search, str):
        by_product(data, search)
    else:
        raise ValueError(f"argument {search} is invalid.")

    # Create new file
    with open(new_file, 'w', newline='') as nf:
        writer= csv.DictWriter(nf, fieldnames= cols, extrasaction= 'ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

    f.close()

def by_date(file, m):
    filtered= []
    for data in file:
        month= datetime.strptime(data['Order Date'], '%m/%d/%Y').month
        if month == m:
            data['Total']= 0
            filtered.append(data)

    return filtered


def by_product(file, p):
    filtered= []
    for data in file:
        pass


def exist(files:list):
    try:
        for file in files:
            open(file).close()
    except FileNotFoundError:
        sys.exit(f"Error: Archivo no encontrado '{file}'")
        

total('ventas.csv', 2, 'total.csv')



