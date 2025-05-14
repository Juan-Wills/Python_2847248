# import matematica # Definición Global de Librería

from matematica import suma # Definición local de librería
from matematica import division

gastos_enero = int(input("Ingrese los gastos de enero = "))
gastos_febrero = int(input("Ingrese los gastos de febrero = "))

# suma_gastos = matematica.suma(gastos_enero, gastos_febrero)
suma_gastos = suma(gastos_enero, gastos_febrero)
print(f"El total de gastos es: {suma_gastos}")

# # gastos_division = matematica.division(gastos_enero, gastos_febrero)
gastos_division = division(gastos_enero, gastos_febrero)
print(f"la division de gastos es: {gastos_division}")

