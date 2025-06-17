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


# 1. Read CSV and print in console
def read(file):

    exist([file])

    with open(file, newline="") as f:
        for row in f:
            print(row, end="")


# 2. Group by month and product
def total(file: str, search, new_file="new_total.csv"):

    exist([file])

    cols = ["Order Date", "Item Type", "Units Sold", "Unit Price", "Total"]

    # Mapping source file
    f = open(file, newline="", encoding="utf-8")
    reader = csv.DictReader(f)
    data = [row for row in reader]

    # Filter by modes
    try:
        if 1 <= search <= 12:
            new_data = by_date(data, search)
    except TypeError:
        if isinstance(search, str):
            new_data = by_product(data, search)
        else:
            raise ValueError(f"ValueError: Invalid argument '{search}'.")

    # Create new file
    with open(new_file, "w", newline="") as nf:
        writer = csv.DictWriter(nf, fieldnames=cols, extrasaction="ignore")
        writer.writeheader()
        for row in new_data:
            writer.writerow(row)

    f.close()


# 3. Generate report CSV
def report(csv_file, new_file="report.csv"):

    exist([csv_file])

    with open(csv_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        with open(new_file, "w", newline="") as nf:
            new_file = csv.writer(nf)
            formated = [
                tabulate(reader, headers="firstrow", tablefmt="github", numalign="left")
            ]
            new_file.writerow(formated)


# EXTRA FUNCTIONS
def by_date(file, m):
    filtered = []
    for data in file:
        month = datetime.strptime(data["Order Date"], "%m/%d/%Y").month
        if month == m:
            data["Total"] = float(data["Units Sold"]) * float(data["Unit Price"])
            filtered.append(data)

    if len(filtered) == 0:
        raise ValueError(f"There is no records in month {m}")

    return filtered


def by_product(file, p: str):
    filtered = []
    for data in file:
        if data["Item Type"] == p.title():
            data["Total"] = float(data["Units Sold"]) * float(data["Unit Price"])
            filtered.append(data)

    if len(filtered) == 0:
        raise ValueError(f"There is no records with product {p.title()}")

    return filtered


def exist(files: list):
    try:
        for file in files:
            open(file).close()
    except FileNotFoundError:
        sys.exit(f"Error: Archivo no encontrado '{file}'")
