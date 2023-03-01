#Ejercicio de la pagina 27 MATEMATICAS FINANCIERAS
from tabulate import tabulate

#solicitamos los datos y los guardamos en variables flotantes
C = float(input("Ingrese el costo del activo: "))
N = float(input("Ingrese el numero de años de vida util: "))

#Se espera que el activo pierda 35,140.02 al final de su vida util. Realizamos la siguiente operacion
B = 35140.02
S = C - B

#calculamos la tasa de depreciacion anual
d = 1 - (S / C)**(1 / N)

dL = [0]
Da = [0]
Dt = [0]
V = [0]
V[0] = C

for i in range(1, int(N+1)):
    V.append(C * (1-d)**i)
    Dt.append((V[i-1]) * d)
    Da.append(Da[i-1] + Dt[i])
    dL.append(d)

#imprimimos la tabla
table = []
for i in range(0, int(N+1)):
    table.append([i, d ,Dt[i], Da[i], V[i]])

print(tabulate(table, headers=["Año", "Tasa", "Depreciacion", "Depreciacion acumulada", "Valor del activo"], tablefmt="fancy_grid"))
print("Datos finales")
print("Costo del activo: ", C)
print("Vida util del activo: ", N)
print("Tasa de depreciacion anual: ", d)
print("Valor de salvamento: ", S)
